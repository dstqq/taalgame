import mysql.connector
# from bot.misc import TgKeys

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="H_wU3LHsNh6rg85wL", # TgKeys.SQL_PASS,
    database="taalgame"
)

mycursor = mydb.cursor()


def check_for_table(table_name: str):
    mycursor.execute("SHOW TABLES")
    for x in mycursor:
        if table_name in x:
            return True
    return False


def drop_table(table_name: str):
    print(table_name)
    sql = f"DROP TABLE IF EXISTS {table_name}"
    mycursor.execute(sql)


def change_user_game(user, game_num):  # изменить в какой игре пользователь(also for 0)
    sql = f"UPDATE users SET user_in_game = '{game_num}' WHERE user_id = '{user}'"
    mycursor.execute(sql)
    mydb.commit()


def check_in_database(table, what_to_search, what_to_use, value):
    if isinstance(what_to_search, str):
        mycursor.execute(f"SELECT {what_to_search} FROM {table} WHERE {what_to_use} = '{value}'")
    else:
        line = ''
        for i in what_to_search:
            line += i
        try:  
            mycursor.execute(f"SELECT {line} FROM {table} WHERE {what_to_use} = '{value}'")
        except:
            print("Something went wrong")
    return mycursor.fetchall()


def edit_in_database(table, field, value, where_field, where_value):
    sql = f"UPDATE {table} SET {field} = '{value}' WHERE {where_field} = '{where_value}'"
    print(sql)
    mycursor.execute(sql)
    mydb.commit()


def insert_in_database(table, fields, values):
    line = ''
    for i in fields:
        line += i + ', '
    sql = f"INSERT INTO {table} ({line[:-2]}) VALUES ({('%s, '*len(fields))[:-2]})"
    val = []
    if len(fields) == len(values):
        for item in values:
            val.append(str(item))
        mycursor.execute(sql, val)
    else:
        line = []
        for item in values:
            line.append(item)
            if len(line) == len(fields):
                val.append(line)
                line = []
        mycursor.executemany(sql, val)
    mydb.commit()


def create_user_table(name, id):
    mycursor.execute(f"CREATE TABLE user_{id} (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(50), status VARCHAR(50), game VARCHAR(50))")


def create_quiz_table(quiz, user):
    game_num = check_in_database(table='settings', what_to_search='value', what_to_use='field', value='Game quantity')
    game_num = game_num[0][0]
    drop_table(f"quiz_{game_num}") # защита от повторного создания одного квеста
    mycursor.execute(f"CREATE TABLE quiz_{game_num} (number INT, rus VARCHAR(50), ned VARCHAR(50), article ENUM('het', 'de', ''), res ENUM('processing', 'right', 'wrong', 'none'))")
    sql = f"INSERT INTO quiz_{game_num} (number, rus, ned, article, res) VALUES (%s, %s, %s, %s, %s)"
    change_user_game(user, game_num)
    val = []
    start = 1
    for i in quiz:
        val.append([start, i[1], i[2], i[4], 'none'])
        start += 1
    mycursor.executemany(sql, val)  # if len > 1, else execute()
    mydb.commit()