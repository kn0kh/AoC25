# Eine mögliche Lösung für den ersten Teil der zwölften Aufgabe in Adnvent of Code 2025
# https://adventofcode.com/2025/day/12

def solution(file):
  present_area = []
  places = []
  count = 0
  with open(file, 'r') as f:
    area = 0
    for line in f:
      if "#" in line:
        area += line.count("#")
      elif line == "\n":
        present_area.append(area)
        area = 0
      elif "x" in line:
        i_colon = line.index(":")
        raw_area = line[:i_colon].replace("x", "*")
        place_data = {"area": eval(raw_area), "presents": line[i_colon+1:].strip().split(" ")}
        places.append(place_data)

  # check areas
  for place in places:
    pure_area = sum([int(pa) * present_area[i] for i, pa in enumerate(place["presents"])])
    has = place["area"]

    if pure_area <= has:
      count += 1

      

  return count

if __name__ == "__main__":
  print(f"Solution: {solution("real-input.txt")}")