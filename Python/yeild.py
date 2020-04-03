def gen_AB():
    print('start')
    c = yield 'A'
    print('continue', c)
    d = yield 'B'
    print('end.')
    print(c, d)


temp2 = gen_AB()
a = next(temp2)
# temp2.send(112)
b = next(temp2)
c = next(temp2)
temp = iter(gen_AB())
for i in temp:
    print(i)
for c in gen_AB():
    print('-->', c)
