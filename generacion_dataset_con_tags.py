"""Clase que te ayuda a 'inflar' tu dataset"""
from aumenta_datos import aumentar_data_set
import unicodedata


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

frases = []
numeros_intencion = []

#En este caso las frases a inflar las sacamos de un archivo txt
#Las frases infladas se guardan en frases y sus número de intencion en numeros_intencion
file = open("trainingFAQs.txt", 'r')
for linea in file.readlines():
    frase = linea
    frase = frase.replace('?', '').replace('¿', '').replace('\n', '')
    frase = elimina_tildes(frase)
    numero_intencion = frase[-1]
    frase_sin_numero = frase[0:(len(frase) - 1)]
    frases.append(list(aumentar_data_set(frase_sin_numero, huecos, valores)))
    numeros_intencion.append(numero_intencion*len(aumentar_data_set(frase_sin_numero, huecos, valores)))
file.close()

#Se ingresa el numero de intencion con la frase inflada correspondiente, y se escribe a otro tx
numeros_intencion = ''.join(numeros_intencion)
file = open("data_final_chido.txt", 'w')
index_numeros_intencion=0
for oraciones in frases:
    for palabra in oraciones:
        oracion = " ".join(str(x) for x in palabra)
        file.write(oracion+numeros_intencion[index_numeros_intencion])
        file.write('\n')
        index_numeros_intencion+=1
file.close()