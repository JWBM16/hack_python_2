"""
generic script

["1","-"] => type string
["0"] => type string

text: ["a","b","c","d","e"] output => ["1","-","3","-","5"]
text: [] output => ["0"] 
"""


def fn_hack_6(s):
    result = s
    _ls = []

    if len(result) == 0:
        result = ["0"]
    else:
        contador = 0
        for txt in range(len(result)):
            contador += 1
            if contador % 2 == 0:
                _ls.append(str("-"))
            else:
                _ls.append(str(contador))

        result = "".join(_ls)

        result = list(result)
    return result


text = ["a", "b", "c", "d", "e"]
prueba = fn_hack_6(text)

print(prueba)
