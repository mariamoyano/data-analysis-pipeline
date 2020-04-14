# importing libraries
from fpdf import FPDF 
import pandas as pd
from functions import *
def pdf(country, coin):
    pdf = FPDF('P','mm','A4')
    pdf.add_page()
    pdf.set_font('Arial', 'B', 16)
    pdf.text(10,10,"WORLD SUICIDE RATES")
    pdf.set_font('Arial', 'B', 12)
    wi=10
    pdf.text(10,10+wi,(f"The average suicide rate in {country} is {getSumSuicidesByCountry(country)} suicides/year with a gbp per capita = {gbpPerCapitaAverage(coin,country)} {coin}"))
    pdf.image("../OUTPUT/GBPPerCapita.jpg",20, 90, w=120, h=200)
    
    pdf.text(10,10+2*wi,(f'The age range with the highest suicide rate in {country} is the range between {ageMaxSuicides(country)[0]}'))
    pdf.text(10,10+3*wi,(f' with {ageMaxSuicides(country)[1]} suicides from 1985 to 2016'))
    pdf.text(10,10+4*wi,(f'The age range with the lowest suicide rate in {country} is the range between {ageMinSuicides(country)[0]} with {ageMinSuicides(country)[1]}'))
    pdf.text(10,10+5*wi,(f'suicides from 1985 to 2016'))
    pdf.text(10,10+6*wi,(f'The country in the world with the most number of suicides per 100k is {suicidesCountry100kMax()[0]} '))
    pdf.text(10,10+7*wi,(f'with a {suicidesCountry100kMax()[1]} suicides'))
    pdf.text(10,10+8*wi,(f'The country in the world with the lowest number of suicides per 100k is '))
    pdf.text(10,10+9*wi,(f' {suicidesCountry100kMin()} with a {suicidesCountry100kMin()[1]} suicides'))
    pdf.add_page()
    pdf.image("../OUTPUT/suicideRateByCountry.jpg",10, 50, h=90)
    return pdf.output('../OUTPUT/PDF.pdf',"F")