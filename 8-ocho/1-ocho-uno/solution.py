# Eine mögliche Lösung für den ersten Teil der achten Aufgabe in Adnvent of Code 2025
# https://adventofcode.com/2025/day/8

def solution(file):
  pairs = []
  with open(file, 'r') as f:
    coordinates = []
    for line in f:
      coordinates.append(tuple(map(int, line.replace("\n", "").split(","))))
    
    for i, coordinate in enumerate(coordinates[:-1], start=1):
      for coord in coordinates[i:]:
        distance = ((((coordinate[0]-coord[0])**2)+((coordinate[1]-coord[1])**2)+((coordinate[2]-coord[2])**2))**0.5)
        if len(pairs) < 1000:
          pairs.append({"distance": distance, "from": coord, "to": coordinate})
          pairs.sort(key=lambda item: item["distance"])
        elif pairs[-1]["distance"] > distance:
          pairs[-1] = ({"distance": distance, "from": coord, "to": coordinate})
          pairs.sort(key=lambda item: item["distance"])

    circuit = []
    for pair in pairs:
      there = False
      for i, c in enumerate(circuit):
        if pair["from"] in c and pair["to"] in c:
          there = c
        else:
          if pair["from"] in c:
            if not there:
              circuit.append([pair["to"]]+c)
            else:
              circuit.pop(circuit.index(there))
              c.remove(pair["from"])
              circuit.append(there + c)
            circuit.pop(i)
            there = circuit[-1]
          elif pair["to"] in c:
            if not there:
              circuit.append([pair["from"]]+c)
            else:
              circuit.pop(circuit.index(there))
              c.remove(pair["to"])
              circuit.append(there + c)
            circuit.pop(i)
            there = circuit[-1]
      if not there:
        circuit.append([pair["from"], pair["to"]])

    circuit.sort(key=len, reverse=True)
    solution = 1
    for x in circuit[:3]: solution *= len(x)

    return solution
    
if "__main__" == __name__:
  print(f"Solution: {solution("real-input.txt")}")