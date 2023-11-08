from setuptools import setup

setup(
    name='word_dictionary',
    version='0.1',
    description="A Complete Bangla Dictionary",
    author="Biplab, Afrar, Shusmit",
    packages=['word_dictionary'],
    package_data={'word_dictionary': ['data/dictionary.pkl']},
    install_requires=['pandas','openpyxl'],
    zip=False,
)
