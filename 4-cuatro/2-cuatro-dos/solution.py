# Eine mögliche Lösung für den zweiten Teil der vierten Aufgabe in Adnvent of Code 2025
# https://adventofcode.com/2025/day/4

def solution(file):
  counter = 0
  rolls_positions = set()

  with open(file, "r") as f:
    for y, line in enumerate(f):
      row = line.replace("\n", "")

      for x, r in enumerate(row):
        if r == "@":
          rolls_positions.add((x, y))
    
    finished = False
    while(not finished):
      finished = True
      
      adjacent_counter = 0
      safe_rolls_positions = rolls_positions.copy()
      for roll in safe_rolls_positions:
        for i in range(-1, 2):
          for j in range(-1, 2):
            if not (roll[0]+i < 0 or roll[0]+i == len(row) 
                    or roll[1]+j < 0 or roll[1]+j > y 
                    or (i, j) == (0, 0) or (roll[0]+i, roll[1]+j) not in rolls_positions):
              adjacent_counter += 1
            
        if adjacent_counter < 4:
          finished = False
          rolls_positions.remove(roll)
          counter += 1
        adjacent_counter = 0

  return counter


if "__main__" == __name__:
  print(f"Solution: {solution("real-input.txt")}")