from game import game

import numpy as np
import matplotlib.pyplot as plt
import csv

def main():
    ##########################  init controler  ################################
    gm = game(0.008)
    ############################################################################

    gm.run(False)

if __name__ == '__main__':
    print("++++    +++   ++  + start main +  ++   +++    ++++")
    main()
    print("++++    +++   ++  + end main +  ++   +++    ++++")
