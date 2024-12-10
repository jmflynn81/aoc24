def main(data):
  line = data[0]
  tick = True
  loc = 0
  newline = []
  for x in line:
    y = int(x)
    if tick:
      for z in range(y):
        newline.append(loc)
      loc +=1
    else:
      for z in range(y):
        newline.append(".")
    tick = not tick
  backloc = -1
  for pos in range(0, len(newline)):
    if newline[pos] == ".":
      if len(set(newline[pos:])) == 1:
        break
      swap = False
      while not swap:
        if newline[backloc] != ".":
          newline[pos] = newline[backloc]
          newline[backloc] = "."
          backloc -= 1
          swap = True
        else:
          backloc -= 1
      # for pos2 in newline:
      #   print(pos2, end="")
      # print()
  
  total = 0

  for i in range(0, len(newline)):
    if newline[i] == ".":
      break
    total += i*newline[i]
  
  a = [1,2,3]
  a.insert(1, 4)
  print(a)
  return total

