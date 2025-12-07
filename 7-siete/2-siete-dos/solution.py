# Eine mögliche Lösung für den zweiten Teil der siebten Aufgabe in Adnvent of Code 2025
# https://adventofcode.com/2025/day/7

def solution(file):
  with open(file, 'r') as f:
    tachyon_pos = dict()
    counter = 0

    for i, line in enumerate(f):
      if "S" in line:
        tachyon_pos[(line.index("S"), i)] = 1
      else:
        tmp_counter = 0
        for j, l in enumerate(line):
          if (j, i-1) in tachyon_pos:
            amount = tachyon_pos[(j, i-1)]
            if "^" == l:

              tachyon_pos[(j+1, i)] = tachyon_pos.get((j+1, i), 0) + amount
              tachyon_pos[(j-1, i)] = tachyon_pos.get((j-1, i), 0) + amount

              tmp_counter += 2 * amount
            else:
              tachyon_pos[(j, i)] = tachyon_pos.get((j, i), 0) + amount
              tmp_counter += 1 * amount

        if tmp_counter != 0: 
          counter = tmp_counter
      
    return counter 


if "__main__" == __name__:
  print(f"Solution: {solution("real-input.txt")}")