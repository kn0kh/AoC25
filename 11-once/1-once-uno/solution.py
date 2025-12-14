# Eine mögliche Lösung für den ersten Teil der ölften Aufgabe in Adnvent of Code 2025
# https://adventofcode.com/2025/day/11

def solution(file):
  with open(file, 'r') as f:
    devices = dict()
    for line in f:
      in_out = line.strip().split(" ")
      device = in_out[0][:-1]
      outputs = in_out[1:]
      devices[device] = outputs

    start = "you"
    end = "out"
    paths = 0

    stack = [start]
    while stack:
      current = stack.pop(0)
      if current == end:
        paths +=1
      else:
        stack += devices[current]

    return paths


if __name__ == "__main__":
  print(f"Solution {solution("real-input.txt")}")
