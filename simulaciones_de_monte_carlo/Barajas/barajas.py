import random
import collections
from bokeh.plotting import figure, show

PALOS =['espada', 'corazon,', 'rombo', 'trebol']
VALORES=['as','2','3','4','5','6','7','8','9','10','jota','reina','rey']

def crear_baraja():
    barajas=[]
    for palo in PALOS:
        for valor in VALORES:
            barajas.append((palo,valor))
    
    return barajas

def obtener_mano(barajas, tamano_mano):
    mano=random.sample(barajas, tamano_mano)
    return mano

def plot(sim, prob, tam):
    plot = figure(title=f'Probabilidad de obtener un par en una mano de tamaño {tam} / Probability of getting a pair in a hand of size {tam} ',x_axis_label="Intentos/Attempts",y_axis_label='Probabilidad/ Probability')
    plot.line(sim, prob)
    show(plot)

def main(tamano_mano,intentos):
    barajas=crear_baraja()

    manos=[]
    for _ in range(intentos):
        mano= obtener_mano(barajas,tamano_mano)
        manos.append(mano)
    
    pares=0
    for mano in manos:
        valores=[]
        for carta in mano:
            valores.append(carta[1])

        counter=dict(collections.Counter(valores))
        for val in counter.values():
            if val==2:
                pares +=1
                break
    
    probabilidad_par= pares/intentos
    print(f'La probabilidad de obtener un par en una mano de {tamano_mano} barajas es , {probabilidad_par}')
    return probabilidad_par




if __name__=='__main__':
    tamano_mano=int(input('De cuantas barajas, sera la mano: '))
    intentos = int(input('Cuantos intentos para calcular la probabilidad: '))
    simulaciones=[]
    probabilidad=[]
    for i in range(1, intentos):
        simulaciones.append(main(tamano_mano,intentos))
        probabilidad.append(i)
    plot(probabilidad, simulaciones, tamano_mano)