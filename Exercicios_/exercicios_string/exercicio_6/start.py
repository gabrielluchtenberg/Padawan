def string_ing(string):
  info = len(string)

  if info > 2:
    if string[-3:] == 'ing':
      string += 'ly'
    else:
      string += 'ing'

  return string
print(string_ing('test'))