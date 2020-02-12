def first_three(loader):
    return loader[:3] if len(loader) > 3 else loader


print(first_three('ipy'))
print(first_three('python'))
print(first_three('py'))
