# Eine mögliche Lösung für den zweiter Teil der neunten Aufgabe in Adnvent of Code 2025
# https://adventofcode.com/2025/day/9

def solution(file):
  red_tiles = []
  largest_area = 0
  with open(file, 'r') as f:
    red_tiles = [tuple(map(int, coordinates.split(","))) for coordinates in f]

  raw_red_tiles = red_tiles.copy()

  x_sorted = sorted(set([x for x, _ in red_tiles]))
  y_sorted = sorted(set([y for _, y in red_tiles]))
  x_map = dict()
  y_map = dict()

  x_map = {x: i*2 for i, x in enumerate(x_sorted)}
  y_map = {y: i*2 for i, y in enumerate(y_sorted)}

  red_tiles = [(x_map[x], y_map[y]) for x, y in red_tiles]

  green_tiles = []
  for (x1, y1), (x2, y2) in zip(red_tiles, red_tiles[1:] + red_tiles[:1]):
    if x1 == x2:
      y_range = sorted([y1, y2])
      green_tiles.extend([(x1, y) for y in range(y_range[0]+1, y_range[1])])
    else:
      x_range = sorted([x1, x2])
      green_tiles.extend([(x, y1) for x in range(x_range[0]+1, x_range[1])])

  occupied = set(green_tiles) | set(red_tiles)
  bin_map = []
  for y in range(len(y_map)*2):
    bin_map.append([])
    for x in range(len(x_map)*2):
      if (x,y) in occupied:
        bin_map[y].append(True)
      else:
        bin_map[y].append(False)

  last_edge = max(raw_red_tiles, key=lambda item: item[0] + item[1]) 
  floodFill(bin_map, y_map[last_edge[1]]-1, x_map[last_edge[0]]-1)

  
  for i, r_tile in enumerate(raw_red_tiles, start=1):
    for rt in raw_red_tiles[i:]:
      area = (abs(r_tile[0]-rt[0])+1)*(abs(r_tile[1]-rt[1])+1)
      if area > largest_area:
        x_border = sorted([x_map[r_tile[0]], x_map[rt[0]]])
        y_border = sorted([y_map[r_tile[1]], y_map[rt[1]]])
        inside = True
        for y in range(y_border[0], y_border[1]+1):
          for x in range(x_border[0], x_border[1]+1):
            if not bin_map[y][x]:
              inside = False
              break
          if not inside:
            break
        if inside:
          largest_area = area
  
  return largest_area


def floodFill(image, sr, sc):
  rows, cols = len(image), len(image[0])
  start_pixel = image[sr][sc]
  
  if start_pixel:
    return
  
  stack = [(sr, sc)]
  image[sr][sc] = True
  count = 0

  while stack:
    count += 1
    print(f"Filled in {count} tiles")
    r, c = stack.pop()
    for dr, dc in (1, 0), (0, 1), (-1, 0), (0, -1):
      nr, nc = dr + r, dc + c
      if  0 <= nr < rows and 0 <= nc < cols and image[nr][nc] == start_pixel:
        image[nr][nc] = True
        stack.append((nr, nc))

  return image


if "__main__" == __name__:
  print(f"Solution: {solution("real-input.txt")}")