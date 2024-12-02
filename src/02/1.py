def main(data):
  total = 0
  for report in data:
    down = False
    up = False
    safe = True
    levels = report.split(' ')
    current = levels[0]
    for next in range(1, len(levels)):
      difference = int(current) - int(levels[next])
      if abs(difference) > 3:
        safe = False
      if difference > 0:
        down = True
      elif difference < 0:
        up = True
      else:
        up = True
        down = True
      current = levels[next]
    if (down and up) or not safe:
      total += 0
    else:
      total += 1
    
  return total