import pymysql

class Stores():
	def get_all():
		conn = pymysql.connect(host='db2-svc', port=3000, db='testdb', user='testus', passwd='testpw', charset='utf8')
		curdic = conn.cursor(pymysql.cursors.DictCursor)
		sql = "SELECT * FROM testtable"
		curdic.execute(sql)
		store_lists = curdic.fetchall()
		return store_lists
