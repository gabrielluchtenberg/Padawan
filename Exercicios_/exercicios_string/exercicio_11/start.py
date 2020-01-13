def valores_string(test):
  result = ""
  for i in range(len(test)):
    if i % 2 == 0:
      result = result + test[i]
  return result

print(valores_string('exercicio'))
print(valores_string(('1234')))