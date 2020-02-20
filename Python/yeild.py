def gen_AB():
    print('start')
    yield 'A'
    print('continue')
    yield 'B'
    print('end.')


temp = iter(gen_AB())
for i in temp:
    print(i)
for c in gen_AB():
    print('-->', c)
