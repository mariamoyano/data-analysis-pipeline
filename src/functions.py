import pandas as pd
import numpy as np
import os
import requests
import json
import re
from dotenv import load_dotenv
load_dotenv()


def dfToEur(df):
    c = []
    for e in df.gdp_for_year:
        e = ''.join(e.split(','))
        c.append(int(e)*0.92)
    c = np.array(c)
    return pd.DataFrame(c)

def usdToEur(df):
    return df*0.92
    
def change(df,coin):
 
    api_Key = os.getenv("FIXER_APIKEY")
    print("APIKEY FOUND!!") if api_Key else print("ERROR: NO APIKEY FOUND")
    res= requests.get(f'http://data.fixer.io/api/latest?access_key={api_Key}')
    print(res)
    data=res.text
    coin_json=json.loads(data)
    return df*coin_json["rates"][coin]
    
def getSumSuicidesByCountry(country):
    df = pd.read_csv("../OUTPUT/analysis.csv", encoding='latin-1')
    dfcount = df.groupby("Country").agg({"suicides_no": "sum"})
    dfcount['suicides_no(float)']=round(dfcount['suicides_no']/31,2)
    return float(dfcount.loc[[country],"suicides_no(float)"])

def gbpPerCapitaAverage(coin,country):
    df = pd.read_csv("../OUTPUT/analysis.csv", encoding='latin-1')
    gbp=0
     
    dfcount= df.groupby("Country").agg({f"gdp_per_capita{coin}": "count"})
    dfsum= df.groupby("Country").agg({f"gdp_per_capita{coin}": "sum"})
    dfsum[f'Average_gdp_per_capita{coin}']=round(dfsum[f"gdp_per_capita{coin}"]/dfcount[f'gdp_per_capita{coin}'],2)
    gbp = float(dfsum.loc[[country],f"Average_gdp_per_capita{coin}"])  
    return gbp
#def imageGbpPerCapita(country,coin):
 #   df = pd.read_csv("../OUTPUT/analysis.csv", encoding='latin-1')
  #  dfsum= df.groupby("Country").agg({f"gdp_per_capita{coin}": "sum"}).plot(kind='bar', stacked=True, figsize=(18,8),title = "GBPPerCapita")
   # return dfsum.figure.savefig("../OUTPUT/GBPPerCapita.jpg")

def ageMaxSuicides(country):
    df = pd.read_csv("../OUTPUT/analysis.csv", encoding='latin-1')
    df2 = df.loc[df["Country"] == country].groupby("age").agg({"suicides_no": "sum"})
    dmax = df2.suicides_no.max()
    d3=df2.loc[df2["suicides_no"] == dmax]
    return [re.match(r"[^[]*\[([^]]*)\]", str(d3.index)).groups()[0], dmax]

def ageMinSuicides(country):
    df = pd.read_csv("../OUTPUT/analysis.csv", encoding='latin-1')
    df2 = df.loc[df["Country"] == country].groupby("age").agg({"suicides_no": "sum"})
    dmin = df2.suicides_no.min()
    d3=df2.loc[df2["suicides_no"] == dmin]
    return [re.match(r"[^[]*\[([^]]*)\]", str(d3.index)).groups()[0], dmin]
def suicidesCountry100kMax():
    df = pd.read_csv("../OUTPUT/analysis.csv", encoding='latin-1')
    dfcount= df.groupby("Country").agg({"suicides/100k pop": "sum"})
    dmax = dfcount["suicides/100k pop"].max()
    daux=dfcount.loc[dfcount["suicides/100k pop"] == dmax]
    return [re.match(r"[^[]*\[([^]]*)\]", str(daux.index)).groups()[0], round(dmax,2)]

def suicidesCountry100kMin():
    df = pd.read_csv("../OUTPUT/analysis.csv", encoding='latin-1')
    dfcount= df.groupby("Country").agg({"suicides/100k pop": "sum"})
    dmin = dfcount["suicides/100k pop"].min()
    daux=dfcount.loc[dfcount["suicides/100k pop"] == dmin]
    return [re.match(r"[^[]*\[([^]]*)\]", str(daux.index)).groups()[0], round(dmin,2)] 