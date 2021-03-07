params = {'название':'', 'цена':'', 'кол-во':'', 'ед изм':''}
analys = {'название':[], 'цена':[], 'кол-во':[], 'ед изм':[]}
tovar = []
i = 0
while True:
    i += 1
    for p in params.keys():
        pr = input(f'Введите параметр {p} : ')
        if (p == 'цена') or p == 'кол-во':
            params[p] = int(pr)
        else:
            params[p] = str(pr)
        analys[p].append(params[p])
    tovar.append((i, params.copy()))
    print(f'Структура товаров - {tovar}')
    print('Аналитика товаров')
    for key, value in analys.items():
        print(key,value)
