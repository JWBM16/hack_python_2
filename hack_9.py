"""
text: {"foo":"fookziman","bar":"barziman"} output => {"Foo":"Fooziman"}
"""


def fn_hack_9(s):
    result = s

    result.popitem()
    print(type(result))

    result["Foo"] = result["foo"]
    del result["foo"]

    result["Foo"] = 'Fooziman'

    # ...
    return result


text = {"foo": "fookziman", "bar": "barziman"}
prueba = fn_hack_9(text)

print(prueba)
