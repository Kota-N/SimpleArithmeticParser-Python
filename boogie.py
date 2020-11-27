import sys
import logging
from booloader import BooLoader

class Boogie:

    def __init__(self, filename):
        self.program = BooLoader(filename)

def main(filename):
    Boogie(filename)

if __name__ == "__main__":
    try:
        main(sys.argv[1])
    except IndexError:
        logging.fatal("no input file provided")