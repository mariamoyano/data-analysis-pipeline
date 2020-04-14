import pandas as pd
import numpy as np
import argparse
import os
import sys
from src.functions import *
from src.pdf import *

def parserKey():
    parser = argparse.ArgumentParser(description='Suicidie rates by gbp per capita in : EUR,USD,GBP,BTC,JPY,CHF')
    parser.add_argument("Country", type=str, nargs=1, help='Insert country: ')
    parser.add_argument("Coin", type=str, nargs=1, help='Insert coin (EUR,USD,GBP,BTC,JPY,CHF)')
    args = parser.parse_args()
    print(args)


    return args
def main():
    args = parserKey()
    print(f"The average suicide rate in {args.Country[0]} is {getSumSuicidesByCountry(args.Country[0])} suicides/year with a gbp per capita = {gbpPerCapitaAverage(args.Coin[0],args.Country[0])} {args.Coin[0]}")
    print(f'The age range with the highest suicide rate in {args.Country[0]} is the range between {ageMaxSuicides(args.Country[0])[0]} with {ageMaxSuicides(args.Country[0])[1]} suicides from 1985 to 2016')
    print(f'The age range with the lowest suicide rate in {args.Country[0]} is the range between {ageMinSuicides(args.Country[0])[0]} with {ageMinSuicides(args.Country[0])[1]} suicides from 1985 to 2016')
    print(f'The country in the world with the most number of suicides per 100k is {suicidesCountry100kMax()[0]} with a {suicidesCountry100kMax()[1]} suicides')
    print(f'The country in the world with the lowest number of suicides per 100k is {suicidesCountry100kMin()} with a {suicidesCountry100kMin()[1]} suicides')  
    pdf(args.Country[0],args.Coin[0])

    return args

if __name__ == '__main__':
    main()