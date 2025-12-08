# Eine mögliche Lösung für den ersten Teil der achten Aufgabe in Adnvent of Code 2025
# https://adventofcode.com/2025/day/8

def solution(file):
  shortest = []
  with open(file, 'r') as f:
    coordinates = []
    for line in f:
      coordinates.append(tuple(map(int, line.replace("\n", "").split(","))))
    
    for i, coordinate in enumerate(coordinates[:-1], start=1):
      for coord in coordinates[i:]:
        distance = ((((coordinate[0]-coord[0])**2)+((coordinate[1]-coord[1])**2)+((coordinate[2]-coord[2])**2))**0.5)
        if len(shortest) < 1000:
          shortest.append({"distance": distance, "from": coord, "to": coordinate})
          shortest.sort(key=lambda item: item["distance"])
        elif shortest[-1]["distance"] > distance:
          shortest[-1] = ({"distance": distance, "from": coord, "to": coordinate})
          shortest.sort(key=lambda item: item["distance"])

    circuit = [[shortest[0]["from"], shortest[0]["to"]]]

    for s in shortest[1:]:
      where = False
      for i, c in enumerate(circuit):
        if not(s["from"] in c and s["to"] in c):
          if s["from"] in c:
            if not where:
              circuit.append([s["to"]]+c)
            else:
              circuit.pop(circuit.index(where))
              c.remove(s["from"])
              where += c
              circuit.append(where)
            circuit.pop(i)
            where = circuit[-1]
          elif s["to"] in c:
            if not where:
              circuit.append([s["from"]]+c)
            else:
              circuit.pop(circuit.index(where))
              c.remove(s["to"])
              where += c
              circuit.append(where)
            circuit.pop(i)
            where = circuit[-1]
        else:
          where = c
      if not where:
        circuit.append([s["from"], s["to"]])

    circuit.sort(key=len, reverse=True)
    solution = 1
    for x in circuit[:3]:
      solution *= len(x)

    return solution
    
if "__main__" == __name__:
  print(f"Solution: {solution("real-input.txt")}")