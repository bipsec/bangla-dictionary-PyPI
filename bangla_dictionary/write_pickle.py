# Import Standard Libary Packages
import pickle
import pathlib

parent_path = pathlib.Path(__file__).absolute().parents[1]

bangla_dict = {}
with open(parent_path / 'defs') as f:
    lines = f.read().split('\n')
    for line in lines:
        word = line.split(' ')[0]
        bangla_dict[word] = " ".join(line.split(' ')[1:])

with open('dict.pickle', 'wb') as dict_pickle:
    pickle.dump(bangla_dict, dict_pickle, protocol=pickle.HIGHEST_PROTOCOL)
