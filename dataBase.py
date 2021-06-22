import sqlite3
import pandas as pd

class DataBase(object):
    #def __init__(self,username,password):
    #    self.username = username
    #    self.password = password
    #    """Constructor"""
    #    pass
    def getDataBase(self):
        try:
            dat = sqlite3.connect('firstOut.db')  # connected to database with out error
            print('connect bd firsOut')
            #sql = pd.DataFrame.from_records(dat, index=None, exclude=None, columns=None, coerce_float=False, nrows=None)
            df = pd.read_sql_query("SELECT * FROM siteInfo",dat)
            df = df.drop(['id'], axis=1)
            print(df.head(15))
        except sqlite3.Error as error:
            print("Ошибка при подключении к sqlite", error)
        finally:
            if (dat):
                dat.close()
                print("Соединение с SQLite закрыто")
        return df

if __name__ == "__main__":# выполняет этот код
    base = DataBase()
    base.getDataBase()