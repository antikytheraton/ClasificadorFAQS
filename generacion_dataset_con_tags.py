#from aumenta_datos import aumentar_data_set
from aumenta_datos import aumentar_data_set
import unicodedata


def elimina_tildes(s):
   return ''.join((c for c in unicodedata.normalize('NFD', s) if unicodedata.category(c) != 'Mn'))


topicos = ['dinero', 'recibo', 'deposito', 'beneficiario', 'cuenta']
acciones = ['enviar', 'recibir', 'cancelar', 'pagar']
unes = ['un', 'una', 'uno']
valores = [topicos, acciones, unes]

huecos = ['TOPICO', 'ACCION', 'UN']

frases = []

file = open("trainingFAQs.txt", 'r')
for linea in file.readlines():
    frase = linea
    frase = frase.replace('?', '').replace('¿', '').replace('\n', '')
    frase = elimina_tildes(frase)
    frases.append(list(aumentar_data_set(frase, huecos, valores)))
file.close()

file = open("data_final_chido.txt", 'w')
for oraciones in frases:
    for palabra in oraciones:
        oracion = " ".join(str(x) for x in palabra)
        file.write(oracion)
        file.write('\n')
file.close()

#frases = aumentar_data_set(frase, huecos, valores)
#print(frases)