# Eine mögliche Lösung für den ersten Teil der siebten Aufgabe in Adnvent of Code 2025
# https://adventofcode.com/2025/day/7


def solution(file):
  with open(file, 'r') as f:
    counter = 0
    tachyon_pos = set()
    for i, line in enumerate(f):
      if "S" in line:
        tachyon_pos.add((line.index("S"), i))
      else:
        for j, l in enumerate(line):
          if (j, i-1) in tachyon_pos:
            if l == "^":
              counter += 1
              tachyon_pos.add((j-1, i+1))
              tachyon_pos.add((j+1, i+1))
            else:
              tachyon_pos.add((j, i))

    return counter





if "__main__" == __name__:
  print(f"Solution: {solution("real-input.txt")}")