import unicodedata


def elimina_tildes(s):
   return ''.join((c for c in unicodedata.normalize('NFD', s) if unicodedata.category(c) != 'Mn'))


file = open("trainingFAQs.txt", 'r')
for linea in file.readlines():
    frase = linea
    frase = frase.replace('?', '').replace('¿', '').replace('\n', '')
    frase = elimina_tildes(frase)
    numero_intencion = frase[-1]
    frase_sin_numero = frase[0:(len(frase)-1)]
    print('{} {} {}'.format(frase, numero_intencion, frase_sin_numero))
file.close()


