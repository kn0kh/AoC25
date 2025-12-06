# Eine mögliche Lösung für den zweiten Teil der sechste Aufgabe in Adnvent of Code 2025
# https://adventofcode.com/2025/day/6

def solution(file):
  result = 0
  with open(file, 'r') as f:
    lines = f.readlines()[::-1]
    operators = lines[0].split()
    rotated = []


    for line in lines[1:]:
      for i, c in enumerate(line):
        if i > len(rotated)-1:
          rotated.append([c])
        else:
          rotated[i].append(c)

    operators_index = 0
    problem = []
    for i, __ in enumerate(rotated):
      rotated[i] = ''.join(reversed(rotated[i])).strip()
      if rotated[i] != '':
        problem.append(int(rotated[i]))
      else:
        if operators[operators_index] == "*":
          tmp = 1
          for x in problem: tmp *= x
          result += tmp
        else:
          result += sum(problem)

        problem.clear()
        operators_index += 1

  return result

if "__main__" == __name__:
  print(f"Solution: {solution("real-input.txt")}")