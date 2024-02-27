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
        # SQL 쿼리 실행 - 'United States'에 해당하는 데이터의 비율을 구함
        sql = "SELECT COUNT(*) AS total_count FROM netflix_titles"
        cursor.execute(sql)
        total_count_result = cursor.fetchone()
        total_count = total_count_result['total_count']  # 전체 데이터의 수
        
        sql = "SELECT COUNT(*) AS us_count FROM netflix_titles WHERE country = 'United States'"
        cursor.execute(sql)
        us_count_result = cursor.fetchone()
        us_count = us_count_result['us_count']  # 'United States'에 해당하는 데이터의 수
        
        us_percentage = (us_count / total_count) * 100  # 'United States' 데이터의 비율 계산
        
        # 'United States'에 해당하는 데이터 출력
        sql = "SELECT title FROM netflix_titles WHERE country = 'United States'"
        cursor.execute(sql)
        us_titles = cursor.fetchall()
        
        for row in us_titles:
            print(row['title'])
        
        # 비율 출력
        print(f"United States 데이터 비율: {us_percentage:.2f}%")

        sql = "SELECT COUNT(*) AS Movie_count FROM netflix_titles WHERE type = 'Movie'"
        cursor.execute(sql)
        Movie_count_result = cursor.fetchone()
        Movie_count = Movie_count_result['Movie_count']
        print(Movie_count/total_count*100)
finally:
    # 연결 종료
    connection.close()
