# Eine mögliche Lösung für den zweiten Teil der driten Aufgabe in Adnvent of Code 2025
# https://adventofcode.com/2025/day/3

def solution(file):
  with open(file, 'r') as f:
    for line in f:
      bank = line.replace("\n", "")

if "__main__" == __name__:
  print(f"Solution: {solution("test-input.txt")}")