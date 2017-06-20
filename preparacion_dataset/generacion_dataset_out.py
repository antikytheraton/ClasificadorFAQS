"""Clase que te ayuda a 'inflar' tu dataset"""
import unicodedata

from preparacion_dataset.aumenta_datos import aumentar_data_set
from preparacion_dataset.aumentar_datos_tags import aumentar_dataset_con_tags


def elimina_tildes(s):
   return ''.join((c for c in unicodedata.normalize('NFD', s) if unicodedata.category(c) != 'Mn'))

#Declaración de los parámetros para inflar nuestro dataset
#Frase: Es la frase base donde los campos que queremos sustituir están en mayúsculas
#Hueco: Es el campo que queremos sustituir, recuerda que debe de ir en mayúscula
#Valores: Son los valores con los que quieres sustituir los huecos
#IMPORTANTE: el orden de arreglo de valores, y de huecos deben de coincidir.

topicos = ['dinero', 'dinero sucio', 'recibo', 'deposito', 'beneficiario', 'cuenta', 'cuenta compartida']
acciones = ['enviar', 'recibir', 'obtener exitosamente', 'cancelar', 'pagar']
unes = ['un', 'una', 'uno']
valores = [topicos, acciones, unes]

huecos = ['TOPICO', 'ACCION', 'UN']

title_tags = ['tpc', 'acc', 'uns']

frases = []
numeros_intencion = []
res_frases = []
res_tags = []
#En este caso las frases a inflar las sacamos de un archivo txt
#Las frases infladas se guardan en 'frases' y sus número de intencion en 'numeros_intencion'
file = open("./preparacion_dataset/trainingFAQs.txt", 'r')
for linea in file.readlines():
    frase = linea
    frase = frase.replace('?', '').replace('¿', '').replace('\n', '')
    frase = elimina_tildes(frase)
    numero_intencion = frase[-1]
    frase_sin_numero = frase[0:(len(frase) - 1)]
    frases.append(list(aumentar_data_set(frase_sin_numero, huecos, valores)))
    numeros_intencion.append(numero_intencion*len(aumentar_data_set(frase_sin_numero, huecos, valores)))

    frasesTags, tags = aumentar_dataset_con_tags(frase_sin_numero, huecos, valores, title_tags)
    res_frases.append(frasesTags)
    res_tags.append(tags)
file.close()

##########----INTENCIONES----##########
#Se ingresa el numero de intencion con la frase inflada correspondiente, y se escribe a otro tx
numeros_intencion = ''.join(numeros_intencion)
file = open("./data_final_inflado_intencion.txt", 'w')
index_numeros_intencion=0
for oraciones in frases:
    for palabra in oraciones:
        oracion = " ".join(str(x) for x in palabra)
        file.write(oracion+numeros_intencion[index_numeros_intencion])
        file.write('\n')
        index_numeros_intencion+=1
file.close()

#########----TAGS----###########
i = 0
j = 0
k = 0
file = open("./data_final_inflado_tags.txt", 'w')
for oraciones in res_frases:
    j = 0
    for palabrax in oraciones:
        oracion = " ".join(str(x) for x in palabrax)
        k = 0
        file.write('- -\n- -\n- -\n')
        for palabra in oracion.split(' '):
            file.write(res_tags[i][j][k])
            file.write(' ')
            file.write(palabra)
            file.write('\n')
            k += 1
        j+=1
        file.write('- -\n- -\n- -\n')
    i+=1



