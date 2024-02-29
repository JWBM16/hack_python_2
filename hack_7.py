"""
generic script

["1",2] => type string & type int
[0] => type int

text: ["a","b","c","d","e"] output => ["1",2,"3",4,"5"]
text: [] output => [0] 
"""


def fn_hack_7(s):
    result = s
    print(len(result))
    lista_convertida = []
    indice = 0

    while indice < len(result):
        try:
            
            if (indice) % 2 == 0 and len(result) >1:
                lista_convertida.append(str(indice + 1))
            elif (indice) % 2 != 0 and len(result) > 0:
                numero = int(indice + 1)
                lista_convertida.append(numero)
            if (indice) == 0 and len(result) == 1:
                
                lista_convertida.append(int(0))
                break

        except AssertionError as msg:
            print(msg)

        indice += 1

    result = lista_convertida

    return result


prueba = fn_hack_7([0])
print(prueba)
