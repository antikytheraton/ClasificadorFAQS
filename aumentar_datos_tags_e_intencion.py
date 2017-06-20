#Para probar puedes usar estos datos, te tiene que dar un vector de 24

# frase = "Quiero ACCION un SUJETO COLOR"
#
# acciones = ['comprar', 'vender']
# sujetos = ['auto', 'helicóptero', 'monociclo']
# colores = ['azul', 'rojo', 'verde', 'morado']
#
# valores = [acciones, sujetos, colores]
# huecos = ['ACCION', 'SUJETO', 'COLOR']
#
# tags=['acc', 'suj', 'clr']
topicos = ['dinero', 'recibo', 'deposito', 'beneficiario', 'cuenta']
acciones = ['enviar', 'recibir', 'cancelar', 'pagar']
unes = ['un', 'una', 'uno']
valores = [topicos, acciones, unes]

huecos = ['TOPICO', 'ACCION', 'UN']
tags = ['tpc', 'acc', 'uno']

frase = "Cual es la definicion de TOPICO"


def aumentar_data_set(frase, huecos, valores, tags):
    list_frase = frase.split(' ')
    resultado = []
    resultado_tags = []
    list_aux = list(list_frase)
    list_aux_tags = list('*'*len(list_aux))
    for i in range(len(huecos)):
        if i == 0:
            try:
                index = list_aux.index(huecos[i])
                for valor in valores[i]:
                    list_aux[index] = valor
                    resultado.append(list(list_aux))

                    list_aux_tags[index] = tags[i]
                    resultado_tags.append(list(list_aux_tags))
            except:
                resultado.append(list(list_aux))
                resultado_tags.append(list(list_aux_tags))
                continue
        else:
            list_aux = list(resultado)
            resultado.clear()

            list_aux_tags = list(resultado_tags)
            resultado_tags.clear()

            for j in range(len(list_aux)):
                try:
                    index = list_aux[j].index(huecos[i])
                    for valor in valores[i]:
                        list_aux[j][index] = valor
                        resultado.append(list(list_aux[j]))

                        list_aux_tags[j][index] = tags[i]
                        resultado_tags.append(list(list_aux_tags[j]))
                except:
                    resultado.extend(list(list_aux))
                    resultado_tags.extend(list(list_aux_tags))
                    break
    return resultado, resultado_tags

print(aumentar_data_set(frase, huecos, valores, tags)[0])
print(len(aumentar_data_set(frase, huecos, valores, tags)[0]))

print(aumentar_data_set(frase, huecos, valores, tags)[1])
print(len(aumentar_data_set(frase, huecos, valores, tags)[1]))