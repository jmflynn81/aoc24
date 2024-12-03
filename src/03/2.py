import re


def main(data):
  total = 0
  do = True
  for line in data:
    matches = re.findall(r"(?:(do)\(\)|(don)'t\(\)|mul\((\d{1,3}),(\d{1,3})\))", line)
    for match in matches:
      if match[1]:
        do = False
      elif match[0]:
        do = True
      elif do:
        total += int(match[2])*int(match[3])
  return total