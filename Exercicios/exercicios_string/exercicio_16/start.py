def insert_sting_middle(loader, loader2):
    return loader[:2] + loader2 + loader[2:]


print(insert_sting_middle('[[]]', 'Python'))
print(insert_sting_middle('{{}}', 'PHP'))
print(insert_sting_middle('<<>>', 'HTML'))
