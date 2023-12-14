import pathlib


def get_test_data_path():
    return pathlib.Path(__file__).absolute().parents[2] / "data/bangla_dictionary_pkl"
