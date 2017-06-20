#from aumenta_datos import aumentar_data_set
from aumenta_datos import aumentar_data_set
import unicodedata


def elimina_tildes(s):
   return ''.join((c for c in unicodedata.normalize('NFD', s) if unicodedata.category(c) != 'Mn'))


topicos = ['dinero', 'dinero sucio', 'recibo', 'deposito', 'beneficiario', 'cuenta', 'cuenta compartida']
acciones = ['enviar', 'recibir', 'obtener exitosamente', 'cancelar', 'pagar']
unes = ['un', 'una', 'uno']
valores = [topicos, acciones, unes]

huecos = ['TOPICO', 'ACCION', 'UN']

frases = []
numeros_intencion = []

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


numeros_intencion = ''.join(numeros_intencion)
file = open("data_final_chido.txt", 'w')
i = 0
for oraciones in frases:
    for palabra in oraciones:
        oracion = " ".join(str(x) for x in palabra)
        file.write(oracion+numeros_intencion[i])
        file.write('\n')
        i+=1
file.close()

#frases = aumentar_data_set(frase, huecos, valores)
#print(frases)