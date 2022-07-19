import requests as rq 
import os
tipo = "mh"
for file in os.listdir("./Aux"):
    print(file)
    for year in [i for i in range(2022, 2016,-1)]:
        try:
            nfile = file[:-8] + str(year) + ".txt"
            print(nfile)
            petition = rq.get("https://webcat-web.gva.es/webcat_web/datosHistoricosRvvcca/descargarHistorico?nomFichero="+nfile+"&red=&anyo="+str(year)+"&tipoFich=mh")
            open(f'./Datos/{nfile}', 'wb').write(petition.content)
        except:
            break