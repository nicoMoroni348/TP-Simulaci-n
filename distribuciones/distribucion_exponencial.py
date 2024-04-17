import math

e = math.e

def distribucion_exponencial(numeros_uniformes_0_1, media): 
    lamb = 1/media

    numeros_distribucion_exponencial_negativa = []

    for rnd in numeros_uniformes_0_1:
        x = round((-1/lamb) * math.log(1-rnd, e), 4)
        numeros_distribucion_exponencial_negativa.append(x)
        
    return numeros_distribucion_exponencial_negativa
