import psycopg2 
from psycopg2 import OperationalError

def connect_to_do():
    try:
        con = psycopg2.connect(host='127.0.0.1',port=5432,dbname= 'postgres',user= 'postgres',password= 'postgres')
        return con
    except OperationalError as e:
        print(f"The error '{e}' occurred")
connecting = connect_to_do()

choice = input('What you choice craete , read , update , or Delete ? ')

if choice == 'create':
    create = connecting.cursor()
    cart_num = int(input('Enter Cart number: '))
    youre_name = input('Enter youre name: ')
    bal = int(input('Enter youre balance: '))
    add = f"INSERT INTO bank(cart_number, owner, balance) VALUES ('{cart_num}', '{youre_name}', {bal})"
    query = f'select * from bank'
    create.execute(query)
    responese1 = create.fetchall()
    create.execute(add)
    connecting.commit()
    for row1 in responese1:
        print(row1)

elif choice == 'Delete':
    id_del = int(input('what you wante del give his ID ? '))
    delete = connecting.cursor()
    delete.execute(f'DELETE FROM bank WHERE "ID"={id_del}')
    connecting.commit()
 

    delete.execute("SELECT * FROM bank")
    print(delete.fetchall()) 

elif choice == 'update':
    task= input('Ты будешь менять номер карты(1), имя(2), или баланс карты(3)?: ')
    id= int(input('Введи id: '))
    cursor =connecting.cursor()

    
    if task == '1':
        new_card_num = input("Новый номер карты: ")
        query = f"Update bank set card_number='{new_card_num}' "

    if task == '2':
        new_name = input("Новое имя: ")
        query =f"Update bank set onwer='{new_name}' "

    if task == '3':
        new_balance = int(input("Новый баланс: "))
        query =f"Update bank set balance={new_balance} "

    query = query + f' where "ID"={id}'
    cursor.execute(query)
    connecting.commit()
    querystart = f'select * from bank'
    cursor.execute(querystart)
    response = cursor.fetchall()
    for row in response:
        print(row)


elif choice == 'read':
    cursor = connecting.cursor()
    ID_choice= int(input('1) Read all , 2) read from ID ?'))
    if ID_choice == 1:
        query = f'select * from bank'
    elif ID_choice == 2:
        id = int(input('Enter ID  : '))
        query = f'select * from bank where "ID"={id}'
    cursor.execute(query)
    responese = cursor.fetchall()
    for row in responese:
        print(row)



