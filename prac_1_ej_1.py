import pandas as pd

class Ej1:
    def __init__(self):
        pass

    def load_data(self):
        self.df = pd.read_excel('datasets/flete-aereo-vacunas-covid19-al-2021-06-28.xlsx')
        self.df.info()

    def run(self):
        self.load_data()

ej1 = Ej1()
ej1.run()
