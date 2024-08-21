import pickle
import itertools as it


GROUPS = ["r", "c", "rc"]
TYPES = ["1", "2"]
TW_FRACS = [0.25, 0.5, 0.75, 1.0]
SAMPLE_CFG = {"groups": GROUPS, "types": TYPES, "tw_fracs": TW_FRACS}
LPATH = "./solomon_stats.pkl"

with open(LPATH, 'rb') as f:
    dset_cfg = pickle.load(f)

cfgs = []
for grp in SAMPLE_CFG['groups']:
    for typ in SAMPLE_CFG['types']:
        for twf in SAMPLE_CFG['tw_fracs']:
            cfgs.append(dset_cfg[grp][f"{grp}{typ}"][f"tw_frac={twf}"])
cfgs = list(it.chain.from_iterable(cfgs))

print(cfgs)
