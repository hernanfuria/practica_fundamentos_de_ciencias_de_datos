import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

class Ej2:
    def __init__(self):
        pass

    def load_data(self):
        print(60 * '-')
        self.df = pd.read_csv('datasets/incendios-cantidad-causas-provincia_2022.csv', encoding='latin1', skiprows=3)
        self.df['natural'] = self.df['natural'].apply(lambda x: x.replace('-', '0'))
        self.df['natural'] = self.df['natural'].astype(int)

        print(self.df.info())

    def q1(self):
        print(60 * '-')
        print(self.df.groupby('anio').sum().sort_values(by='total', ascending=False)['total'].head(1).reset_index())

    def q2(self):
        print(60 * '-')
        print(self.df[(self.df['provincia'] == 'Córdoba') & (self.df['anio'] >= 1993) & (self.df['anio'] <= 2021)].groupby('anio').sum())

    def q3(self):  # preguntar
        """
        Realice una tabla en la que se muestre, para cada año del periodo 1993-2021, 
        la provincia en la que tuvo lugar el mayor número de incendios intencionales. 
        Sugerencia: explore las funcionalidades del método idxmax() de la librería Pandas.
        """
        print(60 * '-')
        df_filtered = self.df[(self.df['anio'] >= 1993) & (self.df['anio'] <= 2021)]
        
        # Get the index of max intentional fires for each year
        idx_max = df_filtered.groupby('anio')['intencional'].idxmax()
        print(idx_max)
        
        # Get the corresponding rows
        result = self.df.loc[idx_max, ['anio', 'provincia', 'intencional']].reset_index(drop=True)
        print(result)

    def q4(self):
        print(60 * '-')
        filtrado = self.df[(self.df['provincia'] == 'Santa Fe') & (self.df['anio'] >= 2015) & (self.df['anio'] <= 2021)].sum()[['negligencia', 'natural', 'intencional']]
        print(filtrado)
        # print(suma.loc['negligencia'])
        # print(suma.loc['natural'])
        # print(suma.loc['intencional'])

        sns.barplot(data=filtrado)
        plt.show()
                
    def q5(self):
        print(60 * '-')
        filtrado = self.df[(self.df['provincia'] == 'Río Negro') & (self.df['anio'] >= 1993) & (self.df['anio'] <= 2021)][['negligencia', 'natural', 'intencional']].mean()
        print(filtrado)

    def run(self):
        self.load_data()
        self.q1()
        self.q2()
        self.q3()
        self.q4()
        self.q5()

ej2 = Ej2()
ej2.run()