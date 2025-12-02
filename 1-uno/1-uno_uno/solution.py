# Das is eine mögliche Lösung für den ersten Teil der ersten Aufgabe in Advent of Code 2025
# https://adventofcode.com/2025/day/1


def solution_uno_uno(file):
  counter = 0
  position = 50

  with open(file, "r") as f:
    for line in f:
      # Parse data from the input file
      line = line.replace("L", "-").replace("R", "").replace("\n", "")
      move = int(line)

      # Get new dial position
      position = (position + move) % 100

      # Check if dial is on zero
      if position == 0:
        counter += 1
      
    return counter

if __name__ == "__main__":
  print(f"Solution: {solution_uno_uno("real-input.txt")}")

