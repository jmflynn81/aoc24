from copy import deepcopy


def check_reports(reports):
  total = 0
  for report in reports:
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
  if total == 0:
    return False
  else:
    return True


def create_potential_reports(report):
  reports = []
  levels = report.split(' ')
  for level in range(0, len(levels)):
    local_levels = deepcopy(levels)
    local_levels.pop(level)
    reports.append(' '.join(local_levels))
  return reports


def main(data):
  total = 0
  for report in data:
    if check_reports([report]):
      total += 1
    else:
      potential_reports = create_potential_reports(report)   
      if check_reports(potential_reports):
        total += 1
      else:
        total += 0
    
  return total