def collect_num(filename):
  sum = 0
  f = open(filename, 'r')
  for x in f:
    num = ""
    for i in x:
      if i.isdigit():
        num += str(i)
    if len(num) == 1:
      num += num
    elif len(num) > 2:
      num = num[0] + num[-1]
    sum += int(num)
  print(sum)


collect_num("input.txt")