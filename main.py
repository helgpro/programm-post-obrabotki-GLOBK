import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon
#from test4 import Ui_MainWindow
from lgpsFace import Ui_MainWindow
from pars_lib import myParser
from dataBase import DataBase
import time
from PyQt5.QtCore import QBasicTimer,QTimer
import pandas as pd
import numpy as np
from PyQt5.QtWidgets import (QWidget, QProgressBar, QPushButton, QFileDialog, QLineEdit, QInputDialog, QApplication, QMenuBar, QMenu)
#from currency_converter import CurrencyConverter
TIME_LIMIT = 100

class CurrencyConv(QtWidgets.QMainWindow):
    parsTs = None
    #try:  # Создание datafrme siteInfo
        #siteInfo = pd.read_csv('siteInfo.txt', sep=';')
        #print(siteInfo.head(5))
    #except Exception as e:
    #    print(e.errno)
    def __init__(self):# конструктор вызываеться при создании экземпляра
        super(CurrencyConv, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.init_UI()
        self.mypars = myParser()# запуск моей библиотеки
        self.statusBar()

        self.timer = QBasicTimer()
        self.step = 0

        #self.timer.timeout.connect(self.handleTimer)
        #self.timer.start()
        #self.btn = QPushButton('Start', self)
        #self.btn.move(40, 180)
        #self.btn.clicked.connect(self.startProgres)

    def init_UI(self):
        self.setWindowTitle('Программа анализа выходных файлов GLOBK') 
        self.setWindowIcon(QIcon('lgps.ico'))
        self.ui.lon_1.setText('65.78') # отображаем в полях
        self.ui.lat_1.setText('36.57')
        self.ui.lon_2.setText('88.84')
        self.ui.lat_2.setText('55.03')
        self.ui.spinBox.setValue(3)
        self.ui.spinBox_2.setValue(3)
        self.ui.spinBox_3.setValue(30)
        self.ui.spinBox_4.setValue(30)
        self.ui.spinBox_5.setValue(15)
        self.ui.spinBox_6.setValue(30)
        # Koll let izmereniy
        self.ui.spinBox_7.setValue(3)
        self.ui.spinBox_8.setValue(2)
        self.inputfile = ''
        self.velfile = ''
        self.ui.progressBar.hide()
   
        self.ui.toolButton.clicked.connect(self.showDialogTS)
        self.ui.toolButton_2.clicked.connect(self.showDialogVell)
        #self.ui.pushButton.clicked.connect(self.converter)#
        self.ui.pushButton.clicked.connect(self.onButtonClick)
        #self.ui.pushButton.clicked.connect(self.ui.progressBar.show())


    def showDialogTS(self):# ADD TS

        try: #          -----------   ПАРСИНГ ВРЕМЕННОГО РЯДА ИЗ ФАЙЛОВ POS    - - - - - - -- -
            #sql = DataBase()
            #sqlDataFrame = sql.getDataBase()
            paths, tsname = QFileDialog.getOpenFileNames(self, "Select one or more files to open","./","Pos files (*.pos)")
            self.parsTs = self.mypars.inTsFile(paths, self.ui.progressBar)  # вызов метода с библиотеки парсит временной ряд    self чтоб вызвать с другого метода

            #dat = self.parsTs["Date"]
            self.parsTs['Date'] = pd.to_datetime(self.parsTs['Date'], format='%Y%m%d')
            print(self.parsTs)
            #self.parsTs = self.mypars.inTsFile(paths, self.ui.lon_1,self.ui.progressBar)# Передаем  пути, координаты? объект прогресбара   OLD

            #print('---------------LOOKUP--------------- ok')

            self.statusBar().showMessage("Парсинг Time serias")
            #self.ui.statusBar().showMessage("Парсинг Time serias")
            self.ui.importfile.setText(tsname)  # отображаем папку
            #-------------------------------  VPR ________________
        except Exception:
            print(" пустой масив")

    def showDialogVell(self):# ADD VELOCITY
        try:#          -----------   ПАРСИНГ ИЗ ФАЙЛА ORG    - - - - - - -- -
            #sql = DataBase()    # загрузка из БД надо перенести
            #sqlDataFrame = sql.getDataBase()
            self.statusBar().showMessage("Парсинг Velocity")
            vellname = QFileDialog.getOpenFileName(self, 'Select one vellosity file', '.')[0]
            self.parsVel = self.mypars.inVellFile(vellname, self.ui.progressBar)  # вызов метода с библиотеки парсит временной ряд    self чтоб вызвать с другого метода
            print('parser Vel \n')
            print(self.parsVel.head(5))

            #vlookupVel = (pd.merge(self.parsVel, sqlDataFrame.loc[:, {'mark', 'site', 'country'}], how='left', left_on=['Mark'],right_on=['mark'], copy=False))
            #print(vlookupVel)
            self.ui.importfile_2.setText(vellname)# отображаемм в поле файл
        except Exception:
            print("не выбран файл")
    #def handleTimer(self):
    #    value = self.ui.progressBar.value()
    #    if value < 100:
    #        value = value + 1
    #        self.pbar.setValue(value)
    #        #self.ui.progressBar.show()
    #        #self.ui.progressBar.setProperty(value)
#        else:
#            self.timer.stop()

    def onButtonClick(self): #      - - - -          START         -  -  -  -


        try:
            self.statusBar().showMessage("Сборка")
            sql = DataBase() #
            sqlDataFrame = sql.getDataBase()#  info Saite Mark Country
            print('SQL \n')
           # print(sqlDataFrame)

            vlookupVel = (pd.merge(self.parsVel, sqlDataFrame.loc[:, {'mark','site', 'country'}], how='left', left_on=['MarkShort'],right_on=['mark'], copy=False))# VeL +Info
            #vlookupTs = (pd.merge(self.parsTs, sqlDataFrame.loc[:, {'mark','site', 'country'}], how='left', left_on=['Mark'],right_on=['mark'], copy=False))#  TS + info
            print('vel  + info \n')
            print(vlookupVel)
            #mark = vlookupTs.mark
            #vlookupTs = vlookupTs.drop(['mark'], axis=1)
            #print(vluokup.head(4))
            count_Vel = vlookupVel.count()# Считает сколько строк
            count_Vel=int(count_Vel.Mark) # Для прогресбара
            # count_Ts = vlookupTs.count()#
            #count_Ts=int(count_Ts.mark)  # Для прогресбара

            print('------------------------ START ---------------------------------------------')
            print('LOOKUP')#   Удалить дубликаты ограничить по координатам слить две табл фильтры и прогресбар
            #tsLooUp = vlookupTs.drop(['mark'],axis=1)# удаление столбца марки из Временных рядов                                 ??
            VlLooUp = vlookupVel.drop(['mark'], axis=1) # Удаление столбца mark из Скоростей из БД
            #print(tsLooUp)
            #------------------ DEl DUPLICATE VEL    E_err, n_err,     ОСТАЕТЬСЯ ОДНА МАРКА   проблема посы нужны всех марок с пункта надо по нескольким параметром скорости и лшибки вместе
            dublicateVel = VlLooUp.drop_duplicates(['e_err','n_err','h_err','e_rate','n_rate','h_rate'], keep='last')#
            #dublicateVel = dublicateVel.drop_duplicates(['n_err'], keep='last')#
            #dublicateVel = dublicateVel.drop_duplicates(['Latit_d'], keep='last')
            print('drop dublicate e_eer n_err')
            print(dublicateVel)
            # - - - -   LOOCKUP  Time Serias - - - -
            tsLookup = (pd.merge(self.parsTs, sqlDataFrame.loc[:, {'mark', 'site', 'country'}], how='left', left_on=['MarkShort'],right_on=['mark'], copy=False))# TS + info
            count_Ts = tsLookup.count()  #
            count_Ts = int(count_Ts.Mark)  # Для прогресбара
            countSumCof = (100 / (count_Vel + count_Ts))  #
            print('stroki s ts+vel', countSumCof)
            #print(tsLookup)
            dropDublTs = tsLookup.drop_duplicates(['MarkShort'],keep='last') # удаляет дубликат оставл последний по дате измерений по столбцу Mark
            #print('not dublikate Mark')
            #print(dropDublTs)#
            TsDdubShort = dropDublTs.drop(['mark'], axis=1)  # Удаление столбца Коротких Марок пришедших из БД
            print(TsDdubShort)
            print(self.ui.lon_1.text())#
            lon = self.ui.lon_1.text()  #
            print(self.ui.lon_2.text())#
            lonB = self.ui.lon_2.text()  #
            print(self.ui.lat_1.text())#
            lat = self.ui.lat_1.text()  #
            print(self.ui.lat_2.text())#
            latB = self.ui.lat_2.text()#

            lon = float(lon)
            lonB = float(lonB)
            lat = float(lat)
            latB = float(latB)
            print(' Ts \n')
            print(TsDdubShort)
            print(' vel \n')
            print(dublicateVel)
            #                                                                                          -   - - -  -      MARGE    -   -  -  -  -
            vlookupTsVel = (pd.merge(TsDdubShort, dublicateVel.loc[:,
                                                 {'site', 'e_rate', 'n_rate', 'h_rate', 'e_err', 'n_err',
                                                  'h_err'}], how='left', left_on=['site'], right_on=['site'],copy=False))
            #vlookupTsVel = (pd.merge(dropDublTs, dublicateVel.loc[:, {'Mark','site','e_rate','n_rate','h_rate','e_err','n_err','h_err'}], how='left', left_on=['site'],right_on=['site'], copy=False)) #OLD
            #vlookupTsVel = (pd.merge(dropDublTs, dublicateVel.loc[:, {'Mark','site','e_rate'}], how='left', left_on=['Mark'],right_on=['Mark'], copy=False))
            #print(vlookupTsVel['mark']) # [X_mm Y_mm Z_mm Longit_d Lalit_d Altit_d mark country site e_rate e_err  n_err h_err  n_rate  h_rate]
            # _     -    -   -  -     -  -  -  -       Щграничение по Координатам   -  -  -  -   PS нужны flaot

            print(vlookupTsVel)
            # -- --  --- --- --  ОБРЕЗКА ПО КООРДИНАТАМ -- -- -- -- -- --
            vlookupTsVel = vlookupTsVel.query(
                'Longit_d > @lon & Longit_d <= @lonB & Latit_d > @lat & Latit_d <= @latB ')
            #vlookupTsVel = vlookupTsVel.query("Longit_d >= '{lon}' & Longit_d <= '{lon2}' & Latit_d >= '{lat}' & Latit_d <= '{lat2}'".format(lon=lon,lon2=lon2,lat=lat,lat2=lat2))

            #                                      -    -     -    -   -    Фильтрация по RATE  ERR   -    -    -    -   -   -
            err_e  = self.ui.spinBox.text()#err e
            err_e = int(err_e)
            err_n = self.ui.spinBox_2.text()
            err_n = int(err_n)
            rate_e = self.ui.spinBox_3.text()#rate e
            rate_e = int(rate_e)
            rate_n = self.ui.spinBox_4.text()#rate n
            rate_n = int(rate_n)
            err_h = self.ui.spinBox_5.text()#h err
            err_h = int(err_h)
            rate_h = self.ui.spinBox_6.text()# rate h
            rate_h = int(rate_h)
            # -- --  --- --- --  ОБРЕЗКА ПО ОШИБКАМ -- -- -- -- -- --
            # Чистый список когда ошибки и скорости по заданным параметрам
            ClearTsVel = vlookupTsVel.query(
                'e_err < @err_e & n_err < @err_n & h_err < @err_h & e_rate < @rate_e & n_rate < @rate_n & h_rate < @rate_h')
            ##  Грязный список ошибки или скорости  WORNING!!!!! есть момент что три марки пункта имеют большие ошибки а одна в норме норм попадает в чистый лист а плохие в грязный
            BadTsVel = vlookupTsVel.query(
                'e_err > @err_e & n_err > @err_n or h_err > @err_h or e_rate > @rate_e or n_rate > @rate_n or h_rate > @rate_h')

            print('bad n rate ',BadTsVel.n_rate,' \n')
            print(BadTsVel.e_rate, '\n ')
            print(BadTsVel.h_rate,'\n')
            print('bad n err ',BadTsVel.n_err, ' \n')
            print(BadTsVel.e_err, '\n ')
            print(BadTsVel.h_err, '\n')
            #
            #    DROP  MARKS one SITE    PS помкнять на BadTsVel
            clearSites = ClearTsVel.drop_duplicates(['site'],keep='first')  # Тут удаляем дублирующие марки пункта так как в хорошем не нужны
            BadTsVel = BadTsVel.drop_duplicates(['site'],keep='first')  # Тут удаляем дублирующие марки пункта так как в плохом списке поиск будет по сайтам всех марок
            #arrDict = {'Mark':[],'Date':[]}       #                       -  -  -  -  -  Проверка количества измерений  -  -  -  -  -
            #arrDict = {}
            #  - - - - - - Словарь с именами плохих марок - - - -
            sortBadDict = {"MarkShort":[]}

            for i, row  in BadTsVel.iterrows():# SITE  нужен один сайт
                print('ID ',i)
                #print(' SITE    ', row["site"])
            #   sortBadDict["MarkShort"].append(site)
            #newBadDf = self.parsTs.loc[self.parsTs.Mark.isin(sortBadDict["MarkShort"])]
                itemBad = (tsLookup.loc[tsLookup["site"]==row["site"]])  # подставляет сайты всех GPS 4ps 5ps 6ps а сайт один
                        #print('minim ',itemBad["Date"].min())
                        #print('max ',itemBad["Date"].max())

                markCount = (itemBad.Date.count())
                dateMin = itemBad.Date.min()
                dateMax = itemBad.Date.max()
                days = dateMax-dateMin
                            #print(itemBad["Mark"])
                            #print(' min data ',dateMin,' max data ',dateMax, '   dney izmereniya ',markCount)
                years = (days/np.timedelta64(1,'Y'))
                #print('scolco let ',years)
                let = self.ui.spinBox_7.text()
                let = int(let)
                dneys = self.ui.spinBox_8.text()
                dneys = int(dneys)

                if(markCount>=dneys and years>=let):
                    print('bolshe',years,' let and ',markCount,'dney')
                    print(row)
                    print(itemBad)
                    # нужно отдать скорости пункта
                else:
                    print('menishe',let,'let i ',dneys, ' dney   vikidivaem --')
                    print(row)

                #Если количество три то смотрим <900 дней
            #self.parsTs['Date'] = pd.to_datetime(self.parsTs['Date'], format='%Y%m%d')
            #BadTsVel[BadTsVel]


            #sortBad = pd.DataFrame.from_dict(sortBadDict)

            #                                                                                       -  -  -  -  -  Запись в CSV  -  -  -  -  -
            clearSites.to_csv('outClear.csv', sep=';', index=False, header=False)
            BadTsVel.to_csv('outBad.csv', sep=';', index=False, header=False)
            #print(vlookupTsVel.loc[vlookupTsVel['Mark_x'] == 'POL3'])

        except Exception as ex:
            print(ex)
        #self.ui.progressBar.show()
        #count = 0
        #while count < TIME_LIMIT:
        #    count += 1
        #    time.sleep(1)
        #    self.ui.progressBar.setValue(count)
        #if count >=TIME_LIMIT: self.ui.progressBar.hide()
        #self.startProgres()


app = QtWidgets.QApplication([])
application = CurrencyConv()
application.show()
 
sys.exit(app.exec())


