import mysql.connector

mydb=mysql.connector.connect(host='localhost',user='root',passwd='Mehjabeen1')

if mydb.is_connected:
                print('successfully connected')
mycursor=mydb.cursor()
mycursor.execute('create database if not exists Pharmacy_Management_System')
print("Database Successsfully created!")


mycursor.execute('use Pharmacy_Management_System')

mycursor.execute("create table Pharmacy (Cr_No int(10) primary key,Ph_Name varchar(30), Ph_Add varchar(30),Ph_Telno int(10))")
mycursor.execute("create table Customer (Cust_id int(10) primary key,Cust_Name varchar(30), Cust_Add varchar(30),Cust_Pno int(10),Cust_pres varchar(50))")
mycursor.execute("create table Employee (EMP_id int(10) primary key, EMP_Name varchar(30),EMP_add varchar(30),EMP_mno int(10),EMP_Salary int(10),Emp_job varchar(10),EMP_dob date,Emp_visaexp date)")
mycursor.execute("create table Medicine (Med_id int(10) primary key,Med_price int(4),Med_exp date,Med_comp varchar(20),Med_Name varchar(20),Med_details varchar(30),Med_dist varchar(30),Med_qnt int(4))")
mycursor.execute("create table General (Gen_id int(10) primary key,Gen_price int(4),Gen_exp date,Gen_comp varchar(20),Gen_Name varchar(20),Gen_details varchar(30),Gen_dist varchar(30),Gen_qnt int(4))")
mycursor.execute("create table Transaction (trans_id int(10) primary key,trans_amt int(7),trans_type varchar(10),trans_item varchar(30),trans_qnt int(4),trans_date date)")
print("Tables Successfully created!")





