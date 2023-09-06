import argparse
import random

parser = argparse.ArgumentParser()
parser.add_argument('number', type = int, help = 'Number of...')

args = parser.parse_args()
N = args.number

arr = []
for i in range (0, N):
    arr.append(random.random())

for i in range(0, N):
    for j in range (0, N - i - 1):
        if (arr[j] > arr[j + 1]):
            arr[j], arr[j + 1] = arr[j + 1], arr[j]
            
print(arr)
