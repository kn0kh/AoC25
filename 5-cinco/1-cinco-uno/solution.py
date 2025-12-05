# Eine mögliche Lösung für den ersten Teil der fünften Aufgabe in Adnvent of Code 2025
# https://adventofcode.com/2025/day/5

def solution(file):
  counter = 0
  ranges = set()
  with open(file, 'r') as f:

    for line in f:
      if "-" in line:
        ranges.add(tuple(line.replace("\n", "").split("-")))

      elif not line == "\n":
        ingredient_id = int(line.replace("\n", ""))
        for r in ranges:
          if ingredient_id >= int(r[0]) and ingredient_id <= int(r[1]):
            counter += 1
            break

  return counter


if "__main__" == __name__:
  print(f"Solution: {solution("real-input.txt")}")