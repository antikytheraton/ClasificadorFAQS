#Para probar puedes usar estos datos, te tiene que dar un vector de 24

#frase = "Quiero ACCION un SUJETO COLOR"

#acciones = ['comprar', 'vender']
#sujetos = ['auto', 'helicóptero', 'monociclo']
#colores = ['azul', 'rojo', 'verde', 'morado']

#valores = [acciones, sujetos, colores]
#huecos = ['ACCION', 'SUJETO', 'COLOR']

def aumentar_data_set(frase, huecos, valores):
    list_frase = frase.split(' ')
    resultado = []
    list_aux = list(list_frase)
    for i in range(len(huecos)):
        if i == 0:
            try:
                index = list_aux.index(huecos[i])
                for valor in valores[i]:
                    list_aux[index] = valor
                    resultado.append(list(list_aux))
            except:
                resultado.append(list(list_aux))
                continue
        else:
            list_aux = list(resultado)
            resultado.clear()
            for j in range(len(list_aux)):
                try:
                    index = list_aux[j].index(huecos[i])
                    for valor in valores[i]:
                        list_aux[j][index] = valor
                        resultado.append(list(list_aux[j]))
                except:
                    resultado.extend(list(list_aux))
                    break
    return resultado

#print(aumentar_data_set(frase, huecos, valores))
#print(len(aumentar_data_set(frase, huecos, valores)))