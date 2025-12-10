# Eine mögliche Lösung für den zweiter Teil der neunten Aufgabe in Adnvent of Code 2025
# https://adventofcode.com/2025/day/9

def solution(file):
  red_tiles = []
  green_borders = []
  largest_area = 0
  with open(file, 'r') as f:
    for coordinate in f:
      red_tiles.append(tuple(map(int, coordinate.split(","))))

    for i, red_tile in enumerate(red_tiles, start=1):
      i %= len(red_tiles)
      if red_tile[0] == red_tiles[i][0]:
        borders = [red_tile[1], red_tiles[i][1]]
        borders.sort()
        for y in range(borders[0], borders[1]+1):
          green_borders.append((red_tile[0], y))
      else:
        borders = [red_tile[0], red_tiles[i][0]]
        borders.sort()
        for x in range(borders[0], borders[1]+1):
          green_borders.append((x, red_tile[1]))

    green_borders.sort(key=lambda x: x[0])

    green_ranges = dict()
    for green_tile in green_borders:
          borders = [min([green_tile[1],green_ranges.get(str(green_tile[0]), [green_tile[1]])[0]]),
                      max([green_tile[1], green_ranges.get(str(green_tile[0]), [green_tile[1]])[-1]])]
          green_ranges[str(green_tile[0])] = range(borders[0], borders[1]+1)

    for i, r_tile in enumerate(red_tiles, start=1):
      print(f"{i}/{len(red_tiles)}")
      for rt in red_tiles[i:]:
        area = abs(r_tile[0]-rt[0]+1) * abs(r_tile[1]-rt[1]+1)
        if area > largest_area:
          inside = True
          x_borders = [r_tile[0], rt[0]]
          y_borders = [r_tile[1], rt[1]]
          x_borders.sort()
          y_borders.sort()
          for x in range(x_borders[0]+1, x_borders[1]):
            if r_tile[1] not in green_ranges.get(str(x), []):
              inside = False
              break
            if rt[1] not in green_ranges.get(str(x), []):
              inside = False
              break
          if inside:
            for y in range(y_borders[0]+1, y_borders[1]):
              if y not in green_ranges.get(str(r_tile[0]), []):
                inside = False
                break
              if y not in green_ranges.get(str(rt[0]), []):
                inside = False
                break
          if inside:
            largest_area = area



  return largest_area 

  


if "__main__" == __name__:
  print(f"Solution: {solution("real-input.txt")}")