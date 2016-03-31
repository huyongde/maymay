import pymysql

#print dir(pymysql)
conn = pymysql.connect(host='localhost',user='root',passwd='',db='test',port=3306,charset='utf8')
conn2 = pymysql.connect(host='localhost',user='root',passwd='',db='test',port=3306,charset='utf8')
cur = conn.cursor()
cur2 = conn2.cursor()

cur.execute("select * from t1")
data = cur.fetchone()
while data:
    student_id = data[0]
    print "student_id %s " % student_id
    t2_sql = "select * from t2 where id = %d " % (int(data[0]))
    print t2_sql
    cur2.execute(t2_sql)
    data2 = cur2.fetchall()
    if len(data2):
        print data2
        print "name %s , xxx %s " % (data2[0][1], "test")

    print "#####" 

    data = cur.fetchone()

