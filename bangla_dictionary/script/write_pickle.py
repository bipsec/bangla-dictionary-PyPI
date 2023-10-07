import pickle
import pathlib


def write_to_pickle():
    """
        Eida hudai likhsi, eidar kono kam nai....
    :return:
        - pickle file return kore...
    """
    parent_path = pathlib.Path(__file__).absolute().parents[1] / "data"
    bangla_dict = {}

    with open(parent_path / "dict_pkl", encoding="latin-1") as f:
        lines = f.read().split('\n')
        for line in lines:
            word = line.split(' ')[0]
            bangla_dict[word] = " ".join(line.split(' ')[1:])

    with open(parent_path / "dict.pickle", 'wb') as dict_pickle:
        pickle.dump(bangla_dict, dict_pickle, protocol=pickle.HIGHEST_PROTOCOL)

    return bangla_dict
