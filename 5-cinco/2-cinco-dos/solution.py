# Eine mögliche Lösung für den zweiten Teil der fünften Aufgabe in Adnvent of Code 2025
# https://adventofcode.com/2025/day/5


def solution(file):
  lefts = []
  rights = []
  count = 0
  with open(file, "r") as f:
    for line in f:
      if "-" in line:
        borders = line.split("-")
        lefts.append(int(borders[0]))
        rights.append(int(borders[1].replace("\n", "")))
  
  lefts.sort()
  rights.sort()

  for i, l in enumerate(lefts):
    if not i+1 == len(lefts):
      if not l == lefts[i+1]:
        if lefts[i+1] <= rights[i]:
          rights[i] = lefts[i+1]-1
        count += rights[i]+1-l
    else:
      count += rights[i]+1-l
  
  return count


if "__main__" == __name__:
  print(f"Solution: {solution("real-input.txt")}")