# Eine mögliche Lösung für den zweite Teil der achten Aufgabe in Adnvent of Code 2025
# https://adventofcode.com/2025/day/8

def solution(file):
  with open(file, 'r') as f:
    coordinates = []
    pairs = []
    for line in f:
      coordinates.append(tuple(map(int, line.replace("\n", "").split(","))))
    
    for i, coordinate in enumerate(coordinates[:-1], start=1):
      for coord in coordinates[i:]:
        distance = ((((coordinate[0]-coord[0])**2)+((coordinate[1]-coord[1])**2)+((coordinate[2]-coord[2])**2))**0.5)
        pairs.append({"distance": distance, "from": coord, "to": coordinate})
    
    pairs.sort(key=lambda item: item["distance"])
    
    tmp_circuits = []
    big_circuit = set({pairs[0]["from"], pairs[0]["to"]})
    i = 1
    while (len(big_circuit) != len(coordinates)):
      pair = pairs[i]
      last_pair = pair
      there = False

      for tc in tmp_circuits:
        if pair["from"] in tc or pair["to"] in tc:
          pair["carry"] = pair.get("carry", []) + [tmp_circuits.index(tc)]
          tc |= set([pair["from"], pair["to"]])
          there = True
  

      if not(pair["from"] in big_circuit and pair["to"] in big_circuit):
        if pair["from"] in big_circuit or pair["to"] in big_circuit:
          
          carryover = pair.get("carry", None)
          if carryover: 
            for carry in reversed(carryover):
              big_circuit |= tmp_circuits[carry]
              del tmp_circuits[carry]

          elif pair["from"] in big_circuit:
            big_circuit.add(pair["to"])
          else:
            big_circuit.add(pair["from"])
          there = True
      else:
        there = True

      if not there:
        tmp_circuits.append(set([pair["from"], pair["to"]]))

      i += 1

    return last_pair["from"][0] * last_pair["to"][0]

if "__main__" == __name__:
  print(f"Solution: {solution("real-input.txt")}")