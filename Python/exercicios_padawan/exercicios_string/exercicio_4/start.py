def troca_de_char(string):
    lenChar = string[0]
    troca = string.replace(lenChar, '$')
    troca = lenChar + troca[1:]

    return troca

print('Original: restart')
print(troca_de_char('restart'))