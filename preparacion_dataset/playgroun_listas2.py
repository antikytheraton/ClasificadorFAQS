index = 3
frase = "Quiero comprar un helicoptero blindado armado azul"
list_aux_tags = ['*', '*', '*', '*', '*']
for k in range(3):
    if k == 0:
        list_aux_tags = list_aux_tags[:index]+['suj']+list_aux_tags[index+1:]
    else:
        list_aux_tags = list_aux_tags[:index] + ['suj'] + list_aux_tags[index:]
print(frase)
print(list_aux_tags)