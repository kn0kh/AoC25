# Eine mögliche Lösung für den zweiter Teil der neunten Aufgabe in Adnvent of Code 2025
# https://adventofcode.com/2025/day/9

def solution(file):
  x_red, y_red = [], []
  red_tiles = []
  largest_area = 0
  with open(file, 'r') as f:
    for coordinates in f:
      coordinate = (tuple(map(int, coordinates.split(","))))
      red_tiles.append(coordinate)
      x_red.append(coordinate[0])
      y_red.append(coordinate[1])

  raw_red_tiles = red_tiles.copy()

  x_sorted = list(sorted(set(x_red)))
  y_sorted = list(sorted(set(y_red)))
  x_map = dict()
  y_map = dict()

  new_coord = 0
  for xs in x_sorted:
    x_map[str(xs)] = new_coord
    new_coord += 2

  new_coord = 0
  for ys in y_sorted:
    y_map[str(ys)] = new_coord
    new_coord += 2

  for i, rt in enumerate(red_tiles):
    red_tiles[i] = (x_map[str(rt[0])], y_map[str(rt[1])])

  green_tiles = []
  for i, red_tile in enumerate(red_tiles, start=1):
    print(f"Getting green tiles {i}/{len(green_tiles)}")
    i %= len(red_tiles)
    if red_tile[0] == red_tiles[i][0]:
      ranges = sorted([red_tile[1], red_tiles[i][1]])
      for y in range(ranges[0]+1, ranges[1]):
        green_tiles.append((red_tile[0], y))
    else:
      ranges = sorted([red_tile[0], red_tiles[i][0]])
      for x in range(ranges[0]+1, ranges[1]):
        green_tiles.append((x, red_tile[1]))

  bin_map = []
  for y in range(len(y_map)*2):
    print(f"Making bit map {y}/{range(len(y_map)*2)[-1]}")
    bin_map.append([])
    for x in range(len(x_map)*2):
      if (x,y) in red_tiles or (x,y) in green_tiles:
        bin_map[y].append(bin(1))
      else:
        bin_map[y].append(bin(0))

  last_edge = max(raw_red_tiles, key=lambda item: item[0] + item[1]) 
  print("flooding the shape") 
  floodFill(bin_map, y_map[str(last_edge[1])]-1, x_map[str(last_edge[0])]-1)

  
  for i, r_tile in enumerate(raw_red_tiles, start=1):
    for rt in raw_red_tiles[i:]:
      area = (abs(r_tile[0]-rt[0])+1)*(abs(r_tile[1]-rt[1])+1)
      if area > largest_area:
        x_border = sorted([x_map[str(r_tile[0])], x_map[str(rt[0])]])
        y_border = sorted([y_map[str(r_tile[1])], y_map[str(rt[1])]])
        inside = True
        for y in range(y_border[0], y_border[1]+1):
          for x in range(x_border[0], x_border[1]+1):
            if bin_map[y][x] != bin(1):
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
  
  if start_pixel == bin(1):
    return
  
  stack = [(sr, sc)]
  image[sr][sc] = bin(1)
  count = 0

  while stack:
    count += 1
    print(f"Filled in {count} tiles")
    r, c = stack.pop()
    for dr, dc in [1, 0], [0, 1], [-1, 0], [0, -1]:
      nr, nc = dr + r, dc + c
      if  0 <= nr < rows and 0 <= nc < cols and image[nr][nc] == start_pixel:
        image[nr][nc] = bin(1)
        stack.append((nr, nc))

  return image


if "__main__" == __name__:
  print(f"Solution: {solution("real-input.txt")}")