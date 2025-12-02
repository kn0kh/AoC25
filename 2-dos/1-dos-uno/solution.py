# Eine mögliche Lösung für den ersten Teil der zweiten Aufgabe in Adnvent of Code 2025
# https://adventofcode.com/2025/day/2

def solution(file):
  counter = 0
  with open(file, "r") as f:

    # Parse the data
    data = f.read()
    raw_ranges = data.split(",")

    # Get the ranges
    for r in raw_ranges:
      ran = r.split("-")
      start,end = ran[0], ran[1]
      
      # Get the ID's
      for i in range(int(start), int(end)+1):
        str_i = str(i)

        # If the length of ID and sum of digits are even
        if len(str_i) % 2 == 0 and sum(map(int, str_i)) % 2 == 0:
          # Split the id in half and check if two halfs are the same
          if str_i[:(len(str_i)//2)] == str_i[(len(str_i)//2):]:
              counter += i

  return counter

        
if "__main__" == __name__:
  print(f"Solution: {solution("real-input.txt")}")