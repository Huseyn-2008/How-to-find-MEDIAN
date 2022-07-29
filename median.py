from tqdm import tqdm
#pip install tqdm
from time import sleep

num = [5, 7, 2, 6, 4, 9, 8, 11]


sortnum = num.sort()

a = len(num)

if a % 2 == 0:
     for i in tqdm(range(a)):
          sleep(0.1)
     b = int(a / 2)
     c = b - 1
     d = num[c]
     f = num[b]
     summary = (d + f) / 2
     print(f'Sorted', num)
     print(summary)
else:
     for i in tqdm(range(a)):
          sleep(0.1)
     l = int(a / 2)
     print(f'Sorted', num)
     print(num[l])
