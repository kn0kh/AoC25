# Das is eine mögliche Lösung für den ersten Teil der ersten Aufgabe in Advent of Code 2025
# https://adventofcode.com/2025/day/1


def solution_uno_uno(file):
  counter = 0
  moves = []
  dial = 50
  with open(file, "r") as f:
    for line in f:
      rotation = int(line[1:-1])
      if line[0] == "L":
        moves.append(-1*rotation)
      else:
        moves.append(rotation)

  for move in moves:
  
    dial = dial + move
    if abs(dial) >= 100:
      dial = dial % 100
    if dial == 0:
      counter+=1
  return counter

if __name__ == "__main__":
  print(solution_uno_uno("real-input.txt"))

