# Eine mögliche Lösung für den ersten Teil der sechste Aufgabe in Adnvent of Code 2025
# https://adventofcode.com/2025/day/6


def solution(file):
  with open(file, 'r') as f:
    lines = f.readlines()[::-1]
    
    operators = lines[0].split()
    number_row = list(map(int, lines[1].split()))

    for line in lines[2:]:
      for i, c in enumerate(line.split()):
        if operators[i] == "*":
          number_row[i] *= int(c)
        else:
          number_row[i] += int(c)

  return sum(number_row)
        


if "__main__" == __name__:
  print(f"Solution: {solution("test-input.txt")}")