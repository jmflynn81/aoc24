def pad(data):
  new_tab = []
  for line in data:
    nline = []
    for i in line:
      nline.append(int(i))
    new_tab.append(nline)
  
  dlen = len(data[0])
  hpad = []
  for i in range(dlen):
    hpad.append(-1)

  new_tab.insert(0, hpad)
  new_tab.append(hpad)

  for line in range(len(new_tab)):
    new_tab[line].insert(0, -1)
    new_tab[line].append(-1)
  return new_tab


def get_true(poss, tick, data):
  new_poss = []
  print(tick, poss)


  
  if tick == 9:
    for i in poss:
      if data[i[0]][i[1]] == tick:
        new_poss.append([i[0],i[1]])
  else:
    for i in poss:
      if data[i[0]][i[1]] == tick:
        new_poss += [[i[0]-1, i[1]], [i[0]+1, i[1]], [i[0], i[1]-1], [i[0], i[1]+1]]
  
  return new_poss



def main(data):
  total = 0
  data = pad(data)
  for y in range(len(data)):
    for x in range(len(data[y])):
      if data[y][x] == 0:
        print(y, x)
        tick = 0
        poss = [[y-1, x], [y+1, x], [y, x-1], [y, x+1]]
        while tick !=9 and len(poss) != 0:
          tick += 1
          poss = get_true(poss, tick, data)
        
        if poss:
          print(set(tuple(i) for i in poss))
          total += len(poss)

  return total