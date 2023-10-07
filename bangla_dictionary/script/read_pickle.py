# import modules
import pathlib
import pickle

pickle_path = pathlib.Path(__file__).absolute().parents[1] / "data" / "bangla_dictionary_pkl"


def get_dict() -> dict:
    """
        - Just read the pickle file for this pypi module.
    :Returns:
        - pickle file load kore...
    """
    with open(pickle_path, 'rb') as pickle_dict:
        return pickle.load(pickle_dict)
