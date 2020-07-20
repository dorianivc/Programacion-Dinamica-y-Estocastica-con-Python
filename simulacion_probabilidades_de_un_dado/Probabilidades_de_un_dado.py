import random
from bokeh.plotting import figure, show


def tirar_dado(numero_de_tiros):
    secuencia_de_tiros = []

    for _ in range(numero_de_tiros):
        tiro = random.choice([1, 2, 3, 4, 5, 6])
        secuencia_de_tiros.append(tiro)
    return secuencia_de_tiros


def plot(sim, prob):
    plot = figure(title='Probabilidad de obtener "1" con un tiro de dado /Probability of getting "1" with a die roll ',x_axis_label="Intentos/Attempts",y_axis_label='Probabilidad/ Probability')
    plot.line(sim, prob)
    show(plot)


def _calculo_de_probabilidad(numero_de_tiros, numero_de_intentos):
    tiros = []
    for _ in range(numero_de_intentos):
        secuencia_de_tiros = tirar_dado(numero_de_tiros)
        tiros.append(secuencia_de_tiros)
    tiros_con_1 = 0
    for tiro in tiros:
        if 1 in tiro:  #Si quiere calcular cuando No haya la probabilidad cambiar por:
        #if 1 not in tiro:
            tiros_con_1 += 1
    probabilidad_tiros_con_1 = float(tiros_con_1 / numero_de_intentos)
    return probabilidad_tiros_con_1

def main(numero_de_tiros, numero_de_intentos):
    probabilidad=[]
    simulaciones=[]
    for n in range(1, numero_de_intentos, 100):
        tiros=[]
        for _ in range(n):
            secuencia_de_tiros=tirar_dado(numero_de_tiros)
            tiros.append(secuencia_de_tiros)
        propabilidad_caer_1= _calculo_de_probabilidad(numero_de_tiros,numero_de_intentos)
        print(f'Probabilidad de que el dado tenga valor de "1" en {numero_de_tiros} tiro(s) = {propabilidad_caer_1}')
        probabilidad.append(propabilidad_caer_1)
        simulaciones.append(n)

    plot(simulaciones,probabilidad)

    
if __name__ == "__main__":
    numero_de_tiros = int(input('Numero de Tiros de dado:'))
    numero_de_intentos= int(input('Numero de simulaciones:'))
    main(numero_de_tiros, numero_de_intentos)
