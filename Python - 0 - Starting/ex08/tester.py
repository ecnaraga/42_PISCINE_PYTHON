from time import sleep
from tqdm import tqdm
from Loading import ft_tqdm

i = 0
for elem in ft_tqdm(range(333)):
    sleep(0.005)
print()
# tqdm(range(333))
# t = tqdm(range(333))
# print(type(t))
for elem in tqdm(range(333)):
    sleep(0.005)
# print()
# sleep(1)
# print()
