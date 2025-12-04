# Eine mögliche Lösung für den ersten Teil der driten Aufgabe in Adnvent of Code 2025
# https://adventofcode.com/2025/day/3

def solution(file):
  joltage = 0
  with open(file, 'r') as f:
    for line in f:
      line = line.replace("\n", "")
      first_biggest = max(line[:-1])
      first_biggest_index = line.index(first_biggest)
      second_biggest = max(line[first_biggest_index+1:])
      joltage += int(first_biggest + second_biggest)
  return joltage

if "__main__" == __name__:
  print(f"Solution: {solution("real-input.txt")}")