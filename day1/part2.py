word_digit_pairs = [
    ('zero', 'z0o'),
    ('one', 'o1e'),
    ('two', 't2o'),
    ('three', 't3e'),
    ('four', 'f4r'),
    ('five', 'f5e'),
    ('six', 's6x'),
    ('seven', 's7n'),
    ('eight', 'e8t'),
    ('nine', 'n9e')
]

def collect_num(filename):
  sum = 0
  f = open(filename, 'r')
  for x in f:
    num = ""
    for word, digit in word_digit_pairs:
      x = x.replace(word, digit)
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
  
  