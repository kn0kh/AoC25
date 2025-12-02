# Eine mögliche Lösung für den ersten Teil der zweiten Aufgabe in Adnvent of Code 2025
# https://adventofcode.com/2025/day/2


def solution(file):
  counter = 0

  # Parse the file
  with open(file, "r") as f:
    data = f.read().split(",")

  # Get the ranges
  for id_range in data:
    r = id_range.split("-")
    start, end = int(r[0]), int(r[1])

    # Get the ID's
    for i in range(start, end+1):
      str_i = str(i)

      # If a sequence repeats in str_i, then .replace(sequence, "") will result in ""
      sequence = ""
      for d in str_i[:len(str_i)//2]:
        sequence += d
        if str_i.replace(sequence, "") == "":
          counter += i
          break

  return counter


if "__main__" == __name__:
  print(f"Solution: {solution("real-input.txt")}")