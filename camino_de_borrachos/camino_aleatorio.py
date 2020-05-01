from Borracho import BorrachoTradicional
from Campo import Campo
from Coordenada import Coordenada
from bokeh.plotting import figure, show

def main(distancia, inicio, borracho):
    campo = Campo()
    campo.anadir_borracho(borracho, inicio) #poner un borracho en origen
    ejecutar_caminata(campo, borracho, distancia)

def ejecutar_caminata(campo, borracho, distancia):
    x_arreglo = []
    y_arreglo = []
    
    for _ in range(distancia):
        campo.mover_borracho(borracho) #se actualiza las coordenadas del borracho
        x_arreglo.append(campo.obtener_coordenada(borracho).x)
        y_arreglo.append(campo.obtener_coordenada(borracho).y)

    graficar(x_arreglo, y_arreglo)

def graficar(x, y):
    figura = figure()
    figura.line(x, y)
    show(figura)

if __name__ == '__main__':
    distancia = 10930
    inicio = Coordenada(0,0)
    borracho = BorrachoTradicional('Angel')
    for i in range(10):

        main(distancia, inicio, borracho)



