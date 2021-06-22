import numpy as np
import pandas as pd
import re
string = "*******"
from tqdm import tqdm
import time
import codecs
import io
pd.set_option('display.max_rows', 1500)
# - - - - - - - - - - - - - - Parsing TS and Velosity - - - - - - - - - - -  -
class myParser(object):

    def inTsFile(self, inTsfile, bar):# вход TS файлов
    #def inTsFile(self, inTsfile, lon_1,bar):# вход TS файлов

        #print(lon_1.text())
        self.bar = bar

        timSerias_dict = {"MarkShort":[],"Mark":[],"Date":[] ,"X_mm":[],"Y_mm":[],"Z_mm":[],"Longit_d":[],"Latit_d":[],"Altit_d":[]}
        file_count_cof=[]
        if inTsfile :
            for filearr in inTsfile:
                print(filearr)# path
                #file_count_cof.append((len(open.readlines(filearr))) / 100)
                file_count_cof.append(len(open(filearr).readlines()))
                #print('cof ',file_count_cof)
                with codecs.open( filearr, "r", "utf_8_sig" ) as f:
                    sum_file = sum(file_count_cof)#39
                    a =(100/int(sum_file))
                    print(sum_file, ' sum')  # 2.56
                    print(a,' cof')#2.56

                    for i, line in enumerate(f):

                        self.bar.show()
                        self.bar.setValue(i*a)
                        dlina = len(line)
                        if dlina == 33:# popadaet nazvanie marki 4 simv    MADR
                            nome = line[16:24] #ACC4_GPS
                            nomeShort = line[16:20]  # ACC4_GPS
                            print(nomeShort)
                        if dlina == 255:# popadaet nazvanie marki 4 simv    MADR
                            (ymd,hms,jjjj,x,y,z,Sx,Sy,Sz,Rxy,Rxz,Ryz,nLat,elong,height,dN,dE,dU,Sn,Se,Su,Rne,Rnu,Reu,Sol) = line.split()
                            timSerias_dict["MarkShort"].append(nomeShort)
                            timSerias_dict["Mark"].append(nome)
                            timSerias_dict["Date"].append(ymd)
                            timSerias_dict["Longit_d"].append(float(elong))
                            timSerias_dict["Latit_d"].append(float(nLat))
                            timSerias_dict["Altit_d"].append(float(height))
                            timSerias_dict["X_mm"].append(float(x))
                            timSerias_dict["Y_mm"].append(float(y))
                            timSerias_dict["Z_mm"].append(float(z))
                self.outPosTS = pd.DataFrame.from_dict(timSerias_dict)

            #______________________ ВПР файла инфо с TS skjdfhtv

            self.bar.hide()
            return self.outPosTS
            #return timSerias_dict


    def inVellFile(self, inVellFile, bar):  # input velosity file

        self.barV = bar

        vellos_dict = {"MarkShort":[],"Mark":[],"Longit_d":[],"Latit_d":[],"e_rate":[],"n_rate":[],"e_err":[],"n_err":[],"h_rate":[],"h_err":[]} #Словарь для манипул
        #outcsv =open('outPosCsv20.csv','w')
        try:
            out = open('parsVellos.csv', 'w')  # filo dlya zapisi
            out.write('Mark'+'\t'+'MarkShort'+'\t'+'Longit_d'+'\t'+'Latit_d'+'\t'+'Altit_d'+'\t'+'e_rate'+'\t'+'n_rate'+'\t'+'h_rate'+'\t'+'e_err'+'\t'+'n_err'+'\t'+'h_err'+'\t'+'\n')
                        #with io.open('./pos/'+i, 'r', encoding='utf-8') as f:
            velLen = len(open(inVellFile).readlines())
            #text = velLen.read()
            #text = text.replace("*******", "0")
            cof = (100 / velLen)
            print('dlina faila', velLen) # 1612
            with codecs.open( inVellFile, "r", "utf_8_sig" ) as f:
            #f = io.open(inVellFile, encoding="utf-8")

            #with open(inVellFile, "r") as f:


                for i, line in enumerate(f):
                    print(line)
                    self.barV.show()
                    self.barV.setValue(i * cof)
                    f = line.rstrip()#udalyaet simvoli v konce
                    dlina = len(line)
                    if dlina == 115:# popadaet nazvanie marki 4 simv    MADR
                        nome = line[-10:-2]#ACC4_GPS
                        nomeShort = line[-10:-6]  # ACC4
                        print(nomeShort)
                    if dlina == 115:# popadaet nazvanie marki 4 simv    MADR
                        (Long,Lat,E_Rate,N_Rate, E_Adj,N_Adj, E_err,N_err, RHO,H_Rate, H_adj, H_err, site) = line.split()
                    #    out.write(nome+'\t'+ymd+'\t'+x+'\t'+y+'\t'+z+'\t'+elong+'\t'+nLat+'\t'+height+'\n')
                    #    #outcsv.write(nome+'\t'+ymd+'\t'+x+'\t'+y+'\t'+z+'\t'+elong+'\t'+nLat+'\t'+height+'\n')
                        vellos_dict["MarkShort"].append(nomeShort)
                        vellos_dict["Mark"].append(nome)
                        vellos_dict["Longit_d"].append(float(Long))
                        vellos_dict["Latit_d"].append(float(Lat))
                        vellos_dict["e_rate"].append(float(E_Rate))
                        vellos_dict["n_rate"].append(float(N_Rate))
                        vellos_dict["e_err"].append(float(E_err))
                        vellos_dict["n_err"].append(float(N_err))
                        vellos_dict["h_rate"].append(float(H_Rate))
                        vellos_dict["h_err"].append(float(H_err))
                    self.outVellosDF = pd.DataFrame.from_dict(vellos_dict)
                    self.barV.hide()

            return self.outVellosDF

        except OSError as e:
            print(e.errno)
        out.close()  
        #outcsv.close()
        #return self.outVellosDF
 
if __name__ == "__main__":# выполняет этот код
    mypars = myParser()
    mypars.inTsFile()
    mypars.inVellFile()
