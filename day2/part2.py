def collect_num(filename):
  fd = open(filename, 'r')
  sum = 0
  for line in fd:
    red = 0
    green = 0
    blue = 0
    line = line.strip().split(':')
    index = line[0].split(' ')[-1]
    result = line[-1].split(';')
    for r in result:
      res = r.split(',')
      for n in res:
        sort = n.split(' ')[1:]
        if (sort[1] == 'red'):
          red = max(red, int(sort[0]))
        if (sort[1] == 'green'):
          green = max(green, int(sort[0]))
        if (sort[1] == 'blue'):
          blue = max(blue, int(sort[0]))
    mult = red * green * blue
    sum += mult
  print(sum)

collect_num("input.txt")
