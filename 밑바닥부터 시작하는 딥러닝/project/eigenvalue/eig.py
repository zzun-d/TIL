from msvcrt import kbhit
import numpy as np
import random
from time import time
from tqdm import tqdm
save_input = []
save_output = []

for _ in tqdm(range(10000)):
    mat =[[random.random() * random.randint(-10, 10) for _ in range(3)] for _ in range(3)]
    save_input.append(mat)
    mat = np.array(mat)
    eig_val, eig_vec = np.linalg.eig(mat)
    save_output.append([(eig_val.real**2 + eig_val.imag**2)**0.5])
    

print(save_output[:10])
save_input = np.array(save_input)
save_output = np.array(save_output)
np.save('./input', save_input)
np.save('./output', save_output)





