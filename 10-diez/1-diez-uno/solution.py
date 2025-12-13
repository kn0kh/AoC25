# Eine mögliche Lösung für den ersten Teil der zehnten Aufgabe in Adnvent of Code 2025
# https://adventofcode.com/2025/day/10

def solution(file):
  button_presses = []
  with open(file, "r") as f:
    raw_machines = [line.split(" ") for line in f]

  for machine in raw_machines:
    lights = machine[0].replace("[", "").replace("]", "").replace(".", "0").replace("#", "1")
    buttons = [button.replace("(", "").replace(")", "").split(",") for button in machine[1:-1]]
    final_state = lights
    start_state = "".zfill(len(lights))

    # making masks
    masks = []
    for button in buttons:
      mask = 0
      for element in button:
        mask |= 1 << int(element)
      mask = bin(mask)[2:].zfill(len(lights))
      masks.append(mask[::-1])
    

    # BFS search
    queue_s = {'queue': [(start_state, [start_state])], 'visited': set(start_state)}

    found = False
    while queue_s["queue"] and not found:
      current_s, path_s = queue_s['queue'].pop(0)

      for m in masks:
        node_s = ''.join("1" if a!=b else "0" for a, b in zip(current_s, m))
        if node_s in final_state:
            found = len(path_s)
            break
        if node_s not in queue_s["visited"]:
          queue_s["visited"].add(node_s)
          queue_s["queue"].append((node_s, path_s + [node_s]))
    
    if found:
      button_presses.append(found)

  return sum(button_presses)
  

if "__main__" == __name__:
  print(f"Solution: {solution("real-input.txt")}")