#!/usr/bin/env python3

import pandas as pd

def subsetting_with_loc():
    df = pd.read_csv('src/municipal.tsv', sep='\t', index_col=0)
    pass

def main():
    df = subsetting_with_loc()
    print(df.shape)
    print(df.head())

if __name__ == "__main__":
    main()
