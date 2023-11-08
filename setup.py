from setuptools import setup

setup(
    name='bangdict',
    version='0.1',
    description="A Complete Digitized Bangla Dictionary",
    author="Biplab, Afrar, Tanvir, Asif Sushmit",
    packages=['bang_dictionary'],
    package_data={'word_dictionary': ['data/bangla_dictionary_pkl.pkl']},
    install_requires=['pandas', 'openpyxl'],
    zip=False,
)
