sequenc_user = input('Sua sequência: ')
entrada = [covert for covert in sequenc_user.split(' , ')]
print(' , '.join(sorted(list(set(entrada)))))
