import os
from lib.utils.io_utils import (
    read_tsplib_cvrptw,
    normalize_instance,
    to_rp_instance,
)

LPATH = './data/solomon_txt/r2100/r201.txt'
pth = os.path.join(LPATH)
instance = read_tsplib_cvrptw(pth)
df = instance['features']

xcoord = []
ycoord = []
for x in df['x_coord']:
    xcoord.append(int(x))
for y in df['y_coord']:
    ycoord.append(int(y))

answer = []
for i in range(len(xcoord)):
    answer.append((xcoord[i],ycoord[i]))

tst = []
tend = []
for x in df['tw_start']:
    tst.append(int(x))
for y in df['tw_end']:
    tend.append(int(y))

time = []
answer = []
for i in range(len(tst)):
    time.append((tst[i],tend[i]))

demand = []
for ds in df['demand']:
    print(ds)
    demand.append(int(ds))

print(demand)
