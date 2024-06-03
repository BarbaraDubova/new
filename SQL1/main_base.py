import pymysql
import pymysql.cursors

from main_config_base import host, user, password, bd_name

try:
    connection = pymysql.connect(
        host=host,
        port=3306,
        user=user,
        password=password,
        database=bd_name,
        cursorclass=pymysql.cursors.DictCursor
    )
    print('success')
    print('#' * 30)
    
    try:
        with connection.cursor() as cursor:
            # Создаем таблицу team
            table = """
            CREATE TABLE IF NOT EXISTS team (
                id INT AUTO_INCREMENT PRIMARY KEY,
                name_team VARCHAR(100) NOT NULL,
                num_members INT NOT NULL CHECK (num_members <= 10)
            )
            """
            cursor.execute(table)
            print('Таблица `team` создана')

            # Заполняем таблицу 10 командами
            new = """
            INSERT INTO team (team_name, num_members) VALUES
            ('Регата', 8), ('Цветочники', 5), ('Врачи', 2), ('Огни', 8),
            ('Авиаторы', 10), ('Флористы', 7), ('Шаманы', 9), ('Аниматоры', 1),
            ('Водители', 3), ('Слесари', 4)
            """
            cursor.execute(new)
            connection.commit()
            print('Таблица `team` заполнена')

            # Выводим строки с количеством участников больше 5
            cons = "SELECT * FROM team WHERE num_members > 5"
            cursor.execute(cons)
            teams = cursor.fetchall()

            # Проверка по параметру
            if teams:
                print('Команды где больше 5 участников:')
                for team in teams:
                    print(team)
            else:
                print('Нет команды в которой более 5 участников')

            # Создаем представление для таблицы user
            new_pr = """
            CREATE OR REPLACE VIEW user_ab AS
            SELECT * FROM user
            WHERE (name LIKE 'А%' OR name LIKE 'Б%')
            AND YEAR(reg_date) = 2018
            """
            cursor.execute(new_pr)
            print('Представление user_ab создано')

            # Проверяем данные в представлении
            select = "SELECT * FROM user_ab"
            cursor.execute(select)
            users = cursor.fetchall()
            if users:
                print('Есть с A или B в 2018:')
                for user in users:
                    print(user)
            else:
                print('Нет с A или B в 2018')

    except Exception as e:
        print('An error occurred:')
        print(e)

    finally:
        connection.close()
except Exception as ex:
    print('Connection failed')
    print(ex)





    