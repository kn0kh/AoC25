# Eine mögliche Lösung für den ersten Teil der driten Aufgabe in Adnvent of Code 2025
# https://adventofcode.com/2025/day/3

def solution(file):
  joltage = 0

  with open(file, 'r') as f:
    for line in f:
      bank = line.replace("\n", "")

      first_digit = max(bank[:-1])
      second_digit = max(bank[bank.index(first_digit)+1:])

      joltage += int(first_digit + second_digit)

  return joltage

if "__main__" == __name__:
  print(f"Solution: {solution("real-input.txt")}")