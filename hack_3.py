"""
generic script

a = @
e = 3
i = ¡
o = 0
u = v

text: "fooziman" output => "F00z¡m@N" 
text: "barziman" output => "B@rz¡m@N" 
text: "3q" output => "3Q" 
text: "qu" output => "Qv" 
text: "qux" output => "QvX" 
"""


def fn_hack_3(s):
    result = s
    diccionario = {
        "a": "@",
        "e": 3,
        "i": "¡",
        "o": 0,
        "u": "v",
    }
    _str = []
    for txt in result:
        if txt.lower() in diccionario:  # Convertir a minúscula para comparar
            _str.append(str(diccionario[txt.lower()]))
        else:
            _str.append(txt)
    result = "".join(_str)
    if len(result) % 2 != 0:  # Verificar si la longitud es impar
        first_character = result[0].upper()
        other_characters = result[1:-1]
        last_character = result[-1].upper()
        result = first_character + other_characters + last_character
    else:
        if len(result) % 2 == 0:
            if len(result) == 2:
                if result[1] == "q":
                    result = result[0] + result[1].upper()
                else:
                    result = result[0].upper() + result[1]
            else:
                result = result[0].upper() + result[1:-1] + result[-1].upper()

    return result


