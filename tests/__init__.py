"""Add parent directory to help import to find main.py."""
from os.path import abspath, dirname
from sys import path

my_path = dirname(abspath(__file__))
path.insert(0, my_path + '/../')
