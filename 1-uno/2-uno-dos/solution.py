# Das is eine mögliche Lösung für den zweiten Teil der ersten Aufgabe in Advent of Code 2025
# https://adventofcode.com/2025/day/1


def solution_uno_dos(file):
  counter = 0
  position = 50

  with open(file, "r") as f:
    for line in f:
      # Parse data from the input file
      line = line.replace("L", "-").replace("R", "").replace("\n", "")
      move = int(line)

      # Get new position and save old position
      old_position = position
      position = (position + move) % 100

      # Check zero's
      if abs(move) >= 100:
        counter += abs(move) // 100
      if not old_position == 0:
        if position == 0:
          counter += 1
        elif move > 0 and old_position > position:
          counter += 1
        elif move < 0 and old_position < position:
          counter += 1

  return counter


if "__main__" == __name__:
  print(f"Solution: {solution_uno_dos("real-input.txt")}")