# Eine mögliche Lösung für den zweiten Teil der zehnten Aufgabe in Adnvent of Code 2025
# https://adventofcode.com/2025/day/10
from z3 import Optimize, Int, Sum

def solution(file):
  button_presses = []
  with open(file, 'r') as f:
    raw_machines = [line.split(" ") for line in f]

  for machine in raw_machines:
    joltages = machine[-1].replace("{", "").replace("}", "").strip().split(",")
    buttons = [button.replace("(", "").replace(")", "").split(",") for button in machine[1:-1]]

    matrix = []
    for i, joltage in enumerate(joltages):
      matrix.append([])
      for b in buttons:
        if str(i) in b:
          matrix[i].append(1)
        else:
          matrix[i].append(0)
      matrix[i].append(int(joltage))

    n = len(buttons)
    opt = Optimize()
    x = [Int(f"x{i}") for i in range(n)]

    for xi in x:
      opt.add(xi >= 0)

    for m in matrix:
      lhs = Sum([m[i] * x[i] for i in range(n)])
      opt.add(lhs == m[-1])

    opt.minimize(Sum(x))
    model = opt.model()
    button_presses.append(model.evaluate(Sum([model[xi] for xi in x])))

  return model.evaluate(Sum(button_presses))



if __name__ == "__main__":
  print(f"Solution: {solution("real-input.txt")}")