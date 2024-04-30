import mysql.connector as db
conn=db.connect(host='localhost',user='root',password='varneek@6969',database='varneek')
mycursor=conn.cursor()
while True:
    print('press 1. to insert employee')
    print('press 2. to fetch all employees')
    print('press 3. to fetch employee by id')
    print('press 4. to delete data by id')
    print('press 5. to exit')
    c=int(input('enter your choice:-'))
    if c==1:
        id=int(input('enter id:-'))
        name=input('enter name:-')
        salary=float(input('enter salary:-'))
        phone=input('enter phone number:-')
        qry='insert into employee values(%s,%s,%s,%s)'
        data=(id,name,salary,phone)
        mycursor.execute(qry,data)
        conn.commit()
        print('employee inserted')
    elif c==2:
        qry='select * from employee'
        mycursor.execute(qry)
        data=mycursor.fetchall()
        for i in range(0,len(data)):
            print(data[i])
    elif c==3:
        id=int(input('enter id:-'))
        qry='select * from employee where id='+str(id)
        mycursor.execute(qry)
        data=mycursor.fetchone()
        print(data)
    elif c==4:
        id=int(input('enter id to delete:-'))
        qry='delete from employee where id='+str(id)
        mycursor.execute(qry)
        print('data deleted')
    elif c==5:
        print('thankyou for using our application')
        break
    else:
        print('invalid input')