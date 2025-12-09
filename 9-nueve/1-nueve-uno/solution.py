# Eine mögliche Lösung für den ersten Teil der neunten Aufgabe in Adnvent of Code 2025
# https://adventofcode.com/2025/day/9

def solution(file):
  areas = []
  coordinates = []
  with open(file, 'r') as f:
    for coordinate in f:
      coordinates.append(list(map(int, coordinate.split(","))))

    for i, coordinate in enumerate(coordinates, start=1):
      for c in coordinates[i:]:
        areas.append(abs(coordinate[0]-c[0]+1)*abs(coordinate[1]-c[1]+1))

  return max(areas)


if "__main__" == __name__:
  print(f"Solution: {solution("real-input.txt")}")