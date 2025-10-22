# Создаем словарь с данными о людях
slovar= {
"Sasha":" ул. Александровская д.69",
"Misha":" ул. Ленина д.123",
"Masha":" ул. Дзержинского д.95"} 

while True:  # делаем цикличность, чтобы не заканчивалось.
    print('Выберите действие:')
    print('1 - Показать все данные')
    print('2 - Изменить адрес')
    print('3 - Удалить запись')
    action = input('введите номер: ')  

    #Выбор номера
    if action =='1':
        print('Все адреса:')
        for name, addres in slovar.items():   
            print(f'{name}:{addres}') #f выводит значение того, что в фигурных скобках в принт
    elif action =='2':
        name = input('Введите имя:')
        if name in slovar: #Ecли имя в словоре
            new_addres = input('введите адрес:')
            slovar[name]= new_addres   #изменяем адрес
            print(f'адрес для{name} изменили на {new_addres}')
        else:
            print('Ошибка!')
    elif action == '3':
      name = input('Введите имя человека: ')
      if name in slovar:
          del slovar[name] # Удаляем человека из словаря
          print(f'Человек {name} удален из словаря.')
      else:
        print(f'Человека с именем {name} нет в словаре.')
    
    #цикл бесконечный, для выхода:
    elif action == 'b':
        break
    
    else:
        print('Неверный ввод')
