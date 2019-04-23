import pymysql
def connectdb():
    print('连接到mysql服务器...')
    db = pymysql.connect(
        host="47.101.39.239",
        user="xieliang",
        passwd="xieliang",
        port=3306,
        db="ssmusic",
        charset='utf8',
        cursorclass=pymysql.cursors.DictCursor)
    print('连接上了!')
    return db
connectdb()
