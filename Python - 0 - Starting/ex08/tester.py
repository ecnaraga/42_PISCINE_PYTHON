from time import sleep
from tqdm import tqdm
from Loading import ft_tqdm

i = 0
for elem in ft_tqdm(range(0, 333)):
    sleep(0.005)
print()
for elem in tqdm(range(0, 333)):
    sleep(0.005)
print()
