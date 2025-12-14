# Eine mögliche Lösung für den zweiten Teil der ölften Aufgabe in Adnvent of Code 2025
# https://adventofcode.com/2025/day/11

from functools import cache

@cache
def solution(file):
  paths = 0
  with open(file, 'r') as f:
    devices = dict()
    for line in f:
      in_out = line.strip().split(" ")
      device = in_out[0][:-1]
      outputs = in_out[1:]
      devices[device] = outputs

    @cache
    def count_paths(current, target):
      if current == target:
        return 1
      if current not in devices:
        return 0
      
      total = 0
      for neighbor in devices[current]:
          total += count_paths(neighbor, target)
      return total
    
    paths = count_paths("svr", "fft") * count_paths("fft", "dac") * count_paths("dac", "out")

  return paths


if __name__ == "__main__":
  print(f"Solution {solution("real-input.txt")}")