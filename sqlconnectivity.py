import mysql.connector as db
# db.connect(host='127.0.0.1') we can write localhost replaceing ip address
conn=db.connect(host='localhost',user='root',password='varneek@6969',database='varneek')
# host:-which server  we are using
#cursor:- to carryquarys and sent it to data base
mycursor=conn.cursor()
qry='create table employee(id int primary key, name varchar(100) not null, salary float default 0, phone varchar(10) unique)'
mycursor.execute(qry)
conn.commit()
#write any quary just like qry