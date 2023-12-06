import subprocess
import sys


subprocess.run([sys.executable, "-m", "nbconvert", "./swiss_federal_elections_2023/*.ipynb", "--to", "asciidoc", "--stdout", "--execute"])
subprocess.run([sys.executable, "./swiss_federal_elections_2023/data_story/build_data_story.py"])
