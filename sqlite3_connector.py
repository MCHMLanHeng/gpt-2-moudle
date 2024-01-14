def sql_add(answer,question):
    import sqlite3
    from datetime import datetime
    import os

    time = str(datetime.now())
    time = time[:-7]

    conn = sqlite3.connect('example.db')

    cursor = conn.cursor()
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = cursor.fetchall()


    create_query = '''CREATE TABLE IF NOT EXISTS answers_list (
                       id INTEGER PRIMARY KEY AUTOINCREMENT,
                       time TEXT,
                       answer TEXT,
                       question TEXT);'''
    cursor.execute(create_query)
    conn.commit()

    insert_query = "INSERT INTO answers_list (time, answer, question) VALUES ('"+time+"', '"+answer+"','"+question+"')"
    cursor.execute(insert_query)
    conn.commit()

    table_name = 'answers_list'
    # 编写SQL语句进行查询
    query = f"SELECT * FROM {table_name}"
    cursor.execute(query)
    result = cursor.fetchall()
    row_num = 1
    for row in result:
        str_row = str(row)
        print(str_row)
        #row_num = str_row[1]
        row_str = str_row[5:-1]
        row_str_time = row_str[:19]
        row_str_ans = row_str[-4:-1]

        try:
            if int(row_num) >= 5:
                del_ans_time = str(result[0])[5:-9]
                delete_query = "DELETE FROM answers_list WHERE time='" + del_ans_time + "'"
                cursor.execute(delete_query)
                conn.commit()
        except sqlite3.OperationalError:
            conn.close()
            os.remove('example.db')

        row_num += 1
    try:
        conn.close()

    except sqlite3.ProgrammingError:
        pass
