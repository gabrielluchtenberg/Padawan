def troca_posicao(a, b):
  posicao_1 = b[:2] + a[2:]
  posicao_2 = a[:2] + b[2:]

  return posicao_1 + ' ' + posicao_2
print(troca_posicao('abc', 'xyz'))