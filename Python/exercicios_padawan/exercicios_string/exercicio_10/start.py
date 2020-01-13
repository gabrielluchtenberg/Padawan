def test(testando):
    return testando[-1:] + testando[1:-1] + testando[:1]


print(test('abcd'))
print(test('12345'))