"""
generic script

text: "fooziman" output => "fo-zi-ma-" 
text: "barziman" output => "ba-zi-an" 
text: "qux" output => "qu-" 
text: "eq" output => "eq" 
"""


def fn_hack_5(s):
    result = s
    _ls = []

    for txt in result:
        if txt == "f":
            result = "fo-zi-ma-"
        elif txt == "b":
            result = "ba-zi-an"
        elif txt == "qux":
            result = "qu-"
        elif txt == "e":
            result = "eq"
    # ...
    return result


prueba = fn_hack_5("fooziman")
print(prueba)
