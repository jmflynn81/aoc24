def get_data_sets(data):
  rule_map = {}
  while data[0] != "":
    temp = data.pop(0).split("|")
    if temp[0] not in rule_map:
      rule_map[temp[0]] = []
    rule_map[temp[0]].append(temp[1])
  data.pop(0)
  return rule_map, data


def main(data):
  rule_map, update_table = get_data_sets(data)
  total = 0
  for line in update_table:
    update = line.split(',')
    correct = True
    for i in range(1, len(update)):
      if update[i] in rule_map:
        for rule in rule_map[update[i]]:
          if rule in update[:i]:
            correct = False
    if correct:
      total += int(update[int((len(update)-1)/2)])

  return total