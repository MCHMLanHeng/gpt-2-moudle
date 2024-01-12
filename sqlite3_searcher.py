def search(question):
	import sqlite3
	conn = sqlite3.connect('example.db')
	print("成功连接到数据库")
	cursor = conn.cursor()
	cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
	tables = cursor.fetchall()
	table_name = 'answers_list'
# 编写SQL语句进行查询
	query = f"SELECT * FROM {table_name}"
	cursor.execute(query)
	result = cursor.fetchall()
	row_num = 1
	for row in result:
		str_row = str(row)
		if question in str_row:
			str_row_list = str_row.split(',')
			str_row_list_ans = str_row_list[-2]
			return str_row_list_ans
		else:
			return ''

	conn.close()
	print('成功关闭数据库连接')
