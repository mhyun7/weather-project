import psycopg2 # driver 임포트 
conn = psycopg2.connect("host=localhost dbname=dvdrental user=postgres password=3484 port=5432") 

cur = conn.cursor() # 커서를 생성한다

cur.execute("SELECT * FROM address where city_id > 500;")
#(actor_id) = cur.fetchone() 
#print(f"{actor_id}")

rows = cur.fetchall()
for i in rows:
    print(i)
# 커서를 닫고 연걸을 종료한다.
cur.close()
conn.close()



 



