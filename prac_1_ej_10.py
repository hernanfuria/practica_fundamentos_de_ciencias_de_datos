import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

class Ej10:
    def __init__(self):
        print(60 * '-')
        pass

    def load_data(self):
        print(60 * '-')
        self.ventas = pd.read_excel('datasets/ventas.xlsx')
        print(self.ventas.head())

        self.clientes_base = pd.read_excel('datasets/clientes_base.xlsx')
        print(self.clientes_base.head())

    def q1(self):
        print(60 * '-')

        self.ventas['total_venta'] = self.ventas['cantidad'] * self.ventas['precio_usd_producto']

        self.ipad = self.ventas[self.ventas['producto'].str.contains('iPad')]
        print(self.ipad['total_venta'].sum())

        self.macbook = self.ventas[self.ventas['producto'].str.contains('MacBook')]
        print(self.macbook['total_venta'].sum())

    def q2(self):
        print(60 * '-')
        join = pd.merge(self.ventas, self.clientes_base, on='nombre_cliente', how='inner')
        print(join)


    def q3(self):
        print(60 * '-')
        join = pd.merge(self.ventas, self.clientes_base, on='nombre_cliente', how='left')
        # print(join.info())
        porc = round(len(join[join['id_cliente'].notnull()]) * 100 / len(join), 2)
        print(f'El porcentaje de ventas con cliente registrado es: {porc}%')

    def q4(self):  # preguntar que onda los fuzzy joins
        print(60 * '-')
        mas_ventas = self.ventas.groupby('nombre_cliente').sum()
        print(mas_ventas)

    def run(self):
        self.load_data()
        self.q1()
        self.q2()
        self.q3()
        self.q4()


ej10 = Ej10()
ej10.run()