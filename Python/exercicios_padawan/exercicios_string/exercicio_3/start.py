def string_rever(objt):
    if len(objt) < 2:
        return objt

    return objt[0:2] + objt[-2:]


print(string_rever('w3resource'))
print(string_rever('w3'))
print(string_rever('w'))