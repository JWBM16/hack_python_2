"""
generic script

text: "fooziman" output => "oozima" 
text: "barziman" output => "arzima" 
text: "qux" output => "qux" 
"""


def fn_hack_4(s):
    result = s
    
    if len(result) % 2 == 0:
        result = result[0:-1]
        result = result[1:]
    else:
        result = result
    
    
    return result

prueba = fn_hack_4("qux")
print(prueba)