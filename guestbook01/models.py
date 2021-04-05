from MySQLdb import connect, OperationalError
from MySQLdb.cursors import DictCursor

def findAll():
    try:
        db = conn()

        # cursor 객체 생성 : 
        cursor = db.cursor(DictCursor)

        # SQL 실행
        sql = 'select no, name, message, date_format(reg_date, "%Y-%m-%d %p %h:%i:%s") as reg_date from guestbook order by reg_date desc;'
        cursor.execute(sql)

        # 결과 받아오기
        results = cursor.fetchall()

        # 자원 정리
        cursor.close()
        db.close()

        # 결과 반환
        return results

    except OperationalError as e:
        print(f"connect is failed. {e}")

def insert(name, password, message):
    try:
        db = conn()

        # cursor 객체 생성 : 
        cursor = db.cursor()

        # SQL 실행
        sql = 'insert into guestbook values(null, %s, %s, %s, now())'
        count = cursor.execute(sql, (name, password, message))

        # commit
        db.commit()

        # 자원 정리
        cursor.close()
        db.close()

        return count == 1

    except OperationalError as e:
        print(f"connect is failed. {e}")

def removeby_no_and_pass(no, password):
    try:
        db = conn()

        # cursor 객체 생성 :
        cursor = db.cursor()

        # SQL 실행
        sql = 'delete from guestbook where no=%s and password=%s'
        cursor.execute(sql, (no, password)) 

        # commit
        db.commit()

        # 자원 정리
        cursor.close()
        db.close()

    except OperationalError as e:
        print(f"connect is failed. {e}")


def conn():
    return connect(
        user='webdb',
        password='webdb',
        host='localhost',
        port=3306,
        db='webdb',
        charset='utf8'
    )