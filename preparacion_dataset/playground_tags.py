import unicodedata
from preparacion_dataset.aumentar_datos_tags import aumentar_dataset_con_tags

def elimina_tildes(s):
   return ''.join((c for c in unicodedata.normalize('NFD', s) if unicodedata.category(c) != 'Mn'))

topicos = ['dinero', 'dinero sucio', 'recibo', 'deposito', 'beneficiario', 'cuenta', 'cuenta compartida']
acciones = ['enviar', 'recibir', 'obtener exitosamente', 'cancelar', 'pagar']
unes = ['un', 'una', 'uno']
valores = [topicos, acciones, unes]

huecos = ['TOPICO', 'ACCION', 'UN']

title_tags = ['tpc', 'acc', 'uns']

frasesTags = []

res_frases = []
res_tags = []

file = open("./trainingFAQs.txt", 'r')
for linea in file.readlines():
    frase = linea
    frase = frase.replace('?', '').replace('¿', '').replace('\n', '')
    frase = elimina_tildes(frase)
    numero_intencion = frase[-1]
    frase_sin_numero = frase[0:(len(frase) - 1)]
    frasesTags, tags = aumentar_dataset_con_tags(frase_sin_numero, huecos, valores, title_tags)
    res_frases.append(frasesTags)
    res_tags.append(tags)
file.close()

i = 0
j = 0
k = 0
file = open("./data_final_inflado_tags.txt", 'w')
for oraciones in res_frases:
    j = 0
    for palabrax in oraciones:
        oracion = " ".join(str(x) for x in palabrax)
        k = 0
        for palabra in oracion.split(' '):
            file.write('- -\n- -\n- -')
            file.write(res_tags[i][j][k])
            file.write(' ')
            file.write(palabra)
            file.write('\n- -\n- -\n- -')
            file.write('\n')
            k += 1
        j+=1
    i+=1