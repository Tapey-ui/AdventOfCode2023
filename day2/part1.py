def collect_num(filename):
  fd = open(filename, 'r')
  sum = 0
  for line in fd:
    poss = True
    line = line.strip().split(':')
    index = line[0].split(' ')[-1]
    result = line[-1].split(';')
    for r in result:
      res = r.split(',')
      for n in res:
        sort = n.split(' ')[1:]
        if (sort[1] == 'red' and int(sort[0]) > 12):
          poss = False
        if (sort[1] == 'green' and int(sort[0]) > 13):
          poss = False
        if (sort[1] == 'blue' and int(sort[0]) > 14):
          poss = False
    if poss == True:
      sum += int(index)
  print(sum)


collect_num("input.txt")
