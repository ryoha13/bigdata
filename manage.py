import pymysql
from app import create_app


pymysql.install_as_MySQLdb()
app = create_app('dev' or 'default')


if __name__ == '__main__':
    app.run()
