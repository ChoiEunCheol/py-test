import pymysql

# MariaDB 연결 설정
connection = pymysql.connect(
    host='localhost',  # 호스트명
    user='root',     # 사용자명
    password='0000',  # 비밀번호
    database='python',  # 데이터베이스명
    charset='utf8mb4',  # 문자 인코딩
    cursorclass=pymysql.cursors.DictCursor  # 결과를 사전 형태로 받기 위해 DictCursor 사용
)

try:
    with connection.cursor() as cursor:
        # SQL 쿼리 실행
        sql = "SELECT title FROM netflix_titles WHERE country = 'United States'"
        cursor.execute(sql)
        
        # 결과 가져오기
        result = cursor.fetchall()
        
        # 결과 출력
        for row in result:
            print(row['title'])
finally:
    # 연결 종료
    connection.close()
