#client-segment-client for CU HIN project

import argparse
import numpy as np
import pandas as pd
from scipy.sparse import csr_matrix

def getSubnets(file):
    with open(file, 'r') as subnetData:
        data = pd.read_csv(subnetData, delimiter= '\t',
                           names = ['dns name', 'subnet', 'netmask', 'desc'])

    arr = np.asarray(data[['subnet']], dtype=float)
    subnetArr = arr[np.logical_not(np.isnan(arr))]
    

def main():

    parser = argparse.ArgumentParser()
    parser.add_argument('--inputfile', type=str, required=True,
                        help='The file containing subnet info.')

    flags = parser.parse_args()

    getSubnets(flags.inputfile)


if __name__ == '__main__':
    main()
