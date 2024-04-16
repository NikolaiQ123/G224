from data_client import Sqlite, Postgres


def show():
    #1
    while True:
        choice_db = input(
''' //// menu 1////
      1. Sqlite
      2. Postgresql
      3. Exite    
      
Your choice:''')

        match choice_db:
            case '1':
                sql = Sqlite()
            case '2':
                sql = Postgres()
            case '3':
                break
            case _:
                print('Такого вариант нет, попробуй еще')

        #2
        while True:
            choice_menu = input(
    ''' 
    //// menu 2 ////
    1. Вывести данные
    2. Добавить данные
    3. Удалить данные
    4. Обновить данные
    5. Выход
      
Your choice:''')

            match choice_menu:
                case '1':
                    sql.select()
                case '2':
                    login = input('login: ')
                    password = input('password: ')
                    sql.insert(login, password)
                case '3':
                    id = input('id: ')
                    sql.delete(id)
                case '4':
                    id = input('id: ')
                    login = input('login: ')
                    password = input('password: ')
                    sql.update(id, login, password)
                case '5':
                    break
                case _:
                    print('Такого вариант нет, попробуй еще')