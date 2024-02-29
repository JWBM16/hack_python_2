"""
generic script

text: ["a","b","c","d","e"] output => ["e-5","d-4","c-3","b-2","a-1"]
text: ["a","b","c"] output => ["c-3","b-2","a-1"]
text: ["a","b","c","d"] output => ["4","3","2","1"]
text: ["a","b"] output => ["2","1"]
"""


def fn_hack_8(s):
    result = s
    _ls = []
    lista3 = []
    if len(result) % 2 == 0:
        result.reverse()
        for i in range(len(result)):
            _ls.append(str(i + 1))
            
        
    else:
        result.reverse()
        for i in range(len(result)):
            _ls.append(i + 1)
        _ls.reverse()
        for x, y in zip(result, _ls):
            elemento = x + "-" + str(y)
            lista3.append(elemento)
        _ls = lista3
        _ls.reverse()
    _ls.reverse()
    result = _ls
    return result



prueba = fn_hack_8(["a","b","c"])
print(prueba)
