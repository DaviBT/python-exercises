a = True
while a == True:
    inputKeyboard = input('write something, if you want to get out, enter -out- : ')
    if inputKeyboard != 'out':
        list = []
        list.append(inputKeyboard)
        listLenth = len(list)
        numListLenth = int(listLenth)
        print(list)
        print(f'The list has {numListLenth} item')
    else:
        print('im in, u are out')