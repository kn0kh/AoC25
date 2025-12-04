# Eine mögliche Lösung für den zweiten Teil der driten Aufgabe in Adnvent of Code 2025
# https://adventofcode.com/2025/day/3

def solution(file):
  joltage = 0

  with open(file, 'r') as f:
    for line in f:
      bank = line.replace("\n", "")
      bank_joltage = []

      j = -1
      for i in range(-11, 1):

        if i == 0:
          sample_biggest = max(bank[j+1:])
          j += bank[j+1:].index(sample_biggest) + 1
        else:
          sample_biggest = max(bank[j+1:i])
          j += bank[j+1:i].index(sample_biggest) + 1

        bank_joltage.append(sample_biggest)
      joltage += int(''.join(bank_joltage))
       
    return joltage
  

if "__main__" == __name__:
  print(f"Solution: {solution("real-input.txt")}")