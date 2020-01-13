def frequency(objt):
    dicionario = {}
    for n in objt:
        keys = dicionario.keys()
        if n in keys:
            dicionario[n] += 1
        else:
            dicionario[n] = 1
    return dicionario


print(frequency('google.com'))