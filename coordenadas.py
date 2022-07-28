import pandas as pd 

df1 = pd.read_csv("coordenadasVLC.csv", encoding="ISO 8859-15", delimiter=";")
df2 = pd.read_csv("intensitat-dels-punts-de-mesura-de-transit-espires-electromagnetiques.csv", encoding = "ISO 8859-15", delimiter=";")
df2["LATITUD"] = df2["Geo Point"].map(lambda x: float(x.split(",")[0]))
df2["LONGITUD"] = df2["Geo Point"].map(lambda x: float(x.split(",")[1]))
series = []
for i in df1.iterrows():
    dist = []
    for j in df2.iterrows():
        dist.append(((i[1]["LATITUD"] - j[1]["LATITUD"])**2+(i[1]["LONGITUD"] - j[1]["LONGITUD"])**2)**0.5)
    series.append(df2["Geo Point"].iloc[dist.index(min(dist))])

df1["Nearest"] = series
print(df1)
df1.to_csv("peticion.csv", encoding="ISO 8859-15")