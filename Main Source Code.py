import mysql.connector

mydb=mysql.connector.connect(host='localhost',user='root',passwd='Mehjabeen1',database='pharmacy_management_system')
c1=mydb.cursor()
if mydb.is_connected:
    print("xx----------------------WELCOME TO FAIZA Group of Pharmacies-------------------xx")
    print("1.Login")
    print("2.Exit")
    print()
    option=int(input("Enter your choice:"))
    if option==1:
        print()
        user=input('Employee Name: ')
        c1.execute("select * from employee where Emp_name like '" + user + "'")
        data=c1.fetchall()
        for i in data:
            value_1=i[1]
            value_2=i[0]
        if user==value_1:
            password=int(input('Enter Employee ID:'))
            if password==value_2:
                print()
                print('Login successfull')
                print()
                while True:
                    print("========================================================================================")
                    print("1.Pharmacy Details")
                    print("2.Customer Details")
                    print("3.Medicine Details")
                    print("4.General Item Details")
                    print("5.Employee Details")
                    print("6.Trasnsaction Details")
                    print("7.Exit the current session")
                    print()
                    ch=int(input("Enter your choice:"))
                    print()
                    if ch==1:
                        while True:
                            print("--------------------------------------------------------------------------------")
                            print("Viewing Pharmacy Details")
                            print()
                            print("1.Display details of all Pharmacies")
                            print("2.Add New Pharmacy details")
                            print("3.Update existing Pharmacy details")
                            print("4.Delete existing Pharmacy details")
                            print("5.Exit Pharmacy Details")
                            print()
                            opt=int(input("Enter your choice:"))
                            print()
                            if opt==1:
                                c1.execute('select * from Pharmacy')
                                mydata=c1.fetchall()
                                for i in mydata:
                                    print(i)
                                print()
                            elif opt==2:
                                crno=int(input("Enter the new CR no.:"))
                                phname=input("Enter the Pharmacy Name:")
                                phadd=input("Enter the Pharmacy Address:")
                                phtell=int(input("Enter the Pharmacy Telephone no.:"))
                                print()
                                c1.execute("insert into Pharmacy (Cr_no,Ph_name,Ph_add,Ph_telno) VALUES ('%s',%s,%s,'%s')",(crno,phname,phadd,phtell))
                                print("Record Added!")
                                mydb.commit()
                            elif opt==3:
                                crno=int(input("Enter the CRno. to be updated:"))
                                c1.execute('Select * from Pharmacy where Cr_no=%s'%(crno))
                                mydata=c1.fetchone()
                                if mydata!=None:
                                    crnonew=int(input("Enter the CRno.:"))
                                    phname=input("Enter the Pharmacy Name:")
                                    phadd=input("Enter the Pharmacy Address:")
                                    phtell=int(input("Enter the Pharmacy Telephone no.:"))
                                    
                                    c1.execute("update Pharmacy set Cr_no='{0}',Ph_name='{1}',Ph_add='{2}',Ph_telno='{3}' where Cr_no='{4}'".format(crnonew,phname,phadd,phtell,crno))
                                    c1.execute("Select * from Pharmacy where Cr_no=%s"%(crnonew))
                                    mydata1=c1.fetchone()
                                    print(mydata1)
                                    print()
                                    mydb.commit()
                                else:
                                    print('No such record found with given CR no.')
                                    print()
                            elif opt==4:
                                crno=int(input("Enter the CR no. to be deleted:"))
                                c1.execute('Select * from Pharmacy where Cr_no=%s'%(crno))
                                mydata=c1.fetchone()
                                if mydata!=None:
                                    c1.execute("Delete from Pharmacy where Cr_no=%s"%(crno))
                                    print("Record Deleted!")
                                    mydb.commit()
                                else:
                                    print('No such record found with given CR no.')
                                    print()
                            else:
                                break
                    
                    if ch==2:
                        while True:
                            print("--------------------------------------------------------------------------------")
                            print("Viewing Customer Details")
                            print()
                            print("1.Display details of all Customers")
                            print("2.Add New Customer details")
                            print("3.Update existing Customer details")
                            print("4.Delete existing Customer details")
                            print("5.Exit Customer Details")
                            print()
                            opt=int(input("Enter your choice:"))
                            print()
                            if opt==1:
                                c1.execute('select * from Customer')
                                mydata=c1.fetchall()
                                for i in mydata:
                                    print(i)
                                print()
                            elif opt==2:
                                custid=int(input("Enter the new Customer ID no.:"))
                                custname=input("Enter the Customer Name:")
                                custadd=input("Enter the Customer Address:")
                                custpno=int(input("Enter the Customer Phone no.:"))
                                custpres=input("Enter the Customer priscription:")
                                print()
                                c1.execute("insert into Customer (Cust_id,Cust_Name,Cust_Add,Cust_pno,Cust_pres) VALUES ('%s',%s,%s,'%s',%s)",(custid,custname,custadd,custpno,custpres))
                                print("Record Added!")
                                mydb.commit()
                            elif opt==3:
                                custid=int(input("Enter the Customer ID no. whose details is to be updated:"))
                                c1.execute('Select * from Customer where Cust_id=%s'%(custid))
                                mydata=c1.fetchone()
                                if mydata!=None:
                                    custidnew=int(input("Enter the Custmer ID no.:"))
                                    custname=input("Enter the Customer Name:")
                                    custadd=input("Enter the Customer Address:")
                                    custpno=int(input("Enter the Customer Phone no.:"))
                                    custpres=input("Enter the Customer priscription:")
                                    
                                    c1.execute("update Customer set Cust_id='{0}',Cust_name='{1}',Cust_add='{2}',Cust_pno='{3}',Cust_pres='{4}' where Cust_id='{5}'".format(custidnew,custname,custadd,custpno,custpres,custid))
                                    c1.execute("Select * from Customer where Cust_id=%s"%(custidnew))
                                    mydata1=c1.fetchone()
                                    print(mydata1)
                                    print()
                                    mydb.commit()
                                else:
                                    print('No such record found with given ID no.')
                            elif opt==4:
                                custid=int(input("Enter the Customer ID no. whose details is to be deleted:"))
                                c1.execute('Select * from Customer where Cust_id=%s'%(custid))
                                mydata=c1.fetchone()
                                if mydata!=None:
                                    c1.execute("Delete from customer where Cust_id=%s"%(custid))
                                    print("Record Deleted!")
                                    mydb.commit()
                                else:
                                    print('No such record found with given ID no.')
                                    print()
                            else:
                                break
                            
                    if ch==3:
                        while True:
                            print("--------------------------------------------------------------------------------")
                            print("Viewing Medicine Details")
                            print()
                            print("1.Display details of all Medicines")
                            print("2.Add New Medicine details")
                            print("3.Update existing Medicine details")
                            print("4.Delete existing Medicine details")
                            print("5.Exit Medicine Details")
                            print()
                            opt=int(input("Enter your choice:"))
                            print()
                            if opt==1:
                                c1.execute('select * from Medicine')
                                mydata=c1.fetchall()
                                for i in mydata:
                                    print(i)
                                print()
                            elif opt==2:
                                medid=int(input("Enter the new Medicine ID no.:"))
                                medexp=input("Enter the expiration date of the Medicine(yyyy-mm-dd):")
                                medcomp=input("Enter the name of the company of the Medicine:")
                                medname=input("Enter the name of the Medicine:")
                                meddetails=input("Enter the details of the Medicine:")
                                meddist=input("Enter the distributor of the Medicine:")
                                medqnt=int(input("Enter the quantity of the Medicine:"))
                                medprice=int(input("Enter the price of the Medicine:"))
                                print()
                                c1.execute("insert into Medicine (Med_id,Med_exp,Med_comp,Med_name,Med_details,Med_dist,Med_qnt,Med_price) VALUES ('%s',%s,%s,%s,%s,%s,'%s','%s')",(medid,medexp,medcomp,medname,meddetails,meddist,medqnt,medprice))
                                print("Record Added!")
                                mydb.commit()
                            elif opt==3:
                                medid=int(input("Enter the Medicine ID no. whose details is to be updated:"))
                                c1.execute('Select * from Medicine where Med_id=%s'%(medid))
                                mydata=c1.fetchone()
                                if mydata!=None:
                                    medidnew=int(input("Enter the Medicine ID no.:"))
                                    medexp=input("Enter the expiration date of the Medicine:")
                                    medcomp=input("Enter the name of the company of the Medicine:")
                                    medname=input("Enter the name of the Medicine:")
                                    meddetails=input("Enter the details of the Medicine:")
                                    meddist=input("Enter the distributor of the medicine:")
                                    medqnt=int(input("Enter the quantity of the Medicine:"))
                                    medprice=int(input("Enter the price of the Medicine:"))
                                               
                                    
                                    c1.execute("update Medicine set Med_id='{0}',Med_exp='{1}',Med_comp='{2}',Med_name='{3}',Med_details='{4}',Med_dist='{5}',Med_qnt='{6}',Med_price='{7}' where Med_id='{8}'".format(medidnew,medexp,medcomp,medname,meddetails,meddist,medqnt,medprice,medid))
                                    c1.execute("Select * from Medicine where Med_id=%s"%(medidnew))
                                    mydata1=c1.fetchone()
                                    print(mydata1)
                                    print()
                                    mydb.commit()
                                else:
                                    print('No such record found with given ID no.')
                                    print()
                            elif opt==4:
                                medid=int(input("Enter the Medicine ID no. whose details is to be deleted:"))
                                c1.execute('Select * from Medicine where Med_id=%s'%(medid))
                                mydata=c1.fetchone()
                                if mydata!=None:
                                    c1.execute("Delete from Medicine where Med_id=%s"%(medid))
                                    print("Record Deleted!")
                                    mydb.commit()
                                else:
                                    print('No such record found with given ID no.')
                                    print()
                            
                            else:
                                break
                            
                    if ch==4:
                        while True:
                            print("--------------------------------------------------------------------------------")
                            print("Viewing General Items' Details")
                            print()
                            print("1.Display details of all Genral Items")
                            print("2.Add New General Item details")
                            print("3.Update existing General Item details")
                            print("4.Delete existing General Item details")
                            print("5.Exit General Item Details")
                            print()
                            opt=int(input("Enter your choice:"))
                            print()
                            if opt==1:
                                c1.execute('select * from General')
                                mydata=c1.fetchall()
                                for i in mydata:
                                    print(i)
                                print()
                            elif opt==2:
                                genid=int(input("Enter the new General Item ID no.:"))
                                genexp=input("Enter the expiration date of the General Item(yyyy-mm-dd):")
                                gencomp=input("Enter the name of the company of the General Item:")
                                genname=input("Enter the name of the General Item:")
                                gendetails=input("Enter the details of the General Item:")
                                gendist=input("Enter the distributor of the General Item:")
                                genqnt=int(input("Enter the quantity of the General Item:"))
                                genprice=int(input("Enter the price of the General Item:"))
                                print()
                                c1.execute("insert into General (Gen_id,Gen_exp,Gen_comp,Gen_name,Gen_details,Gen_dist,Gen_qnt,Gen_price) VALUES ('%s',%s,%s,%s,%s,%s,'%s','%s')",(genid,genexp,gencomp,genname,gendetails,gendist,genqnt,genprice))
                                print("Record added!")
                                mydb.commit()
                            elif opt==3:
                                genid=int(input("Enter the General Item ID no. whose details is to be updated:"))
                                c1.execute('Select * from General where Gen_id=%s'%(genid))
                                mydata=c1.fetchone()
                                if mydata!=None:
                                    genidnew=int(input("Enter the General Item ID no.:"))
                                    genexp=input("Enter the expiration date of the General Item(yyyy-mm-dd):")
                                    gencomp=input("Enter the name of the company of the General Item:")
                                    genname=input("Enter the name of the General Item:")
                                    gendetails=input("Enter the details of the General Item:")
                                    gendist=input("Enter the distributor of the General Item:")
                                    genqnt=int(input("Enter the quantity of the General Item:"))
                                    genprice=int(input("Enter the price of the General Item:"))
                                               
                                    
                                    c1.execute("update General set Gen_id='{0}',Gen_exp='{1}',Gen_comp='{2}',Gen_name='{3}',Gen_details='{4}',Gen_dist='{5}',Gen_qnt='{6}',Gen_price='{7}' where Gen_id='{8}'".format(genidnew,genexp,gencomp,genname,gendetails,gendist,genqnt,genprice,genid))
                                    c1.execute("Select * from General where Gen_id=%s"%(genidnew))
                                    mydata1=c1.fetchone()
                                    print(mydata1)
                                    print()
                                    mydb.commit()
                                else:
                                    print('No such record found with given ID no.')
                                    print()
                            elif opt==4:
                                genid=int(input("Enter the General Item ID no. whose details is to be deleted:"))
                                c1.execute('Select * from General Item where Gen_id=%s'%(genid))
                                mydata=c1.fetchone()
                                if mydata!=None:
                                    c1.execute("Delete from General where Gen_id=%s"%(genid))
                                    print("Record Deleted!")
                                    mydb.commit()
                                else:
                                    print('No such record found with given ID no.')
                                    print()
            
                            else:
                                break

                    if ch==5:
                        while True:
                            print("--------------------------------------------------------------------------------")
                            print("Viewing Employee Details")
                            print()
                            print("1.Display details of all Employee")
                            print("2.Add New Employee details")
                            print("3.Update existing Employee details")
                            print("4.Delete existing Employee details")
                            print("5.Exit Employee Details")
                            print()
                            opt=int(input("Enter your choice:"))
                            print()
                            if opt==1:
                                c1.execute('select * from Employee')
                                mydata=c1.fetchall()
                                for i in mydata:
                                    print(i)
                                print()
                            elif opt==2:
                                empid=int(input("Enter the new Employee ID no.:"))
                                empname=input("Enter the Employee Name:")
                                empadd=input("Enter the Employee Address:")
                                empmno=int(input("Enter the Employee Mobile no.:"))
                                empsalary=int(input("Enter the Employee Salary:"))
                                empjob=input("Enter the job of the Employee:")
                                empdob=input("Enter the DOB of the Employee(yyyy-mm-dd):")
                                empvisaexp=input("Enter the visa expiration date of the Employee(yyyy-mm-dd):")
                                print()
                                c1.execute("insert into Employee (Emp_id,Emp_Name,Emp_Add,Emp_mno,Emp_salary,Emp_job,Emp_dob,Emp_visaexp) VALUES ('%s',%s,%s,'%s','%s',%s,%s,%s)",(empid,empname,empadd,empmno,empsalary,empjob,empdob,empvisaexp))
                                print("Record Added!")
                                mydb.commit()
                            elif opt==3:
                                empid=int(input("Enter the Employee ID no. whose details is to be updated:"))
                                c1.execute('Select * from Employee where Emp_id=%s'%(empid))
                                mydata=c1.fetchone()
                                if mydata!=None:
                                    empidnew=int(input("Enter the Employee ID no.:"))
                                    empname=input("Enter the Employee Name:")
                                    empadd=input("Enter the Employee Address:")
                                    empmno=int(input("Enter the Employee Mobile no.:"))
                                    empsalary=int(input("Enter the Employee Salary:"))
                                    empjob=input("Enter the job of the Employee:")
                                    empdob=input("Enter the DOB of the Employee(yyyy-mm-dd):")

                                    
                                    c1.execute("update Employee set Emp_id='{0}',Emp_name='{1}',Emp_add='{2}',Emp_mno='{3}',Emp_salary='{4}',Emp_job='{5}',Emp_dob='{6}',Emp_visaexp='{7}' where Emp_id='{8}'".format(empidnew,empname,empadd,empmno,empsalary,empjob,empdob,empvisaexp,empid))
                                    c1.execute("Select * from Employee where Emp_id=%s"%(empidnew))
                                    mydata1=c1.fetchone()
                                    print(mydata1)
                                    print()
                                    mydb.commit()
                                else:
                                    print('No such record found with given ID no.')
                            elif opt==4:
                                empid=int(input("Enter the Employee ID no. whose details is to be deleted:"))
                                c1.execute('Select * from Employee where Emp_id=%s'%(empid))
                                mydata=c1.fetchone()
                                if mydata!=None:
                                    c1.execute("Delete from Employee where Emp_id=%s"%(empid))
                                    print("Record Deleted!")
                                    mydb.commit()
                                else:
                                    print('No such record found with given ID no.')
                                    print()
                            else:
                                break

                    if ch==6:
                        while True:
                            print("--------------------------------------------------------------------------------")
                            print("Viewing Transaction Details")
                            print()
                            print("1.Display details of all Transactions")
                            print("2.Add New Transactionmdetails")
                            print("3.Update existing Transaction details")
                            print("4.Delete existing Transaction details")
                            print("5.Exit Transaction Details")
                            print()
                            opt=int(input("Enter your choice:"))
                            print()
                            if opt==1:
                                c1.execute('select * from Transaction ')
                                mydata=c1.fetchall()
                                for i in mydata:
                                    print(i)
                                print()
                            elif opt==2:
                                transid=int(input("Enter the new Transaction  ID no.:"))
                                transprice=int(input("Enter the Transaction amount:"))
                                transtype=input("Enter the type of Transaction:")
                                transitem=input("Enter the item:")
                                transqnt=int(input("Enter the quantity of items in Transaction:"))
                                transdate=input("Enter the date of the Transaction(yyyy-mm-dd):")
                                print()
                                c1.execute("insert into Transaction (Trans_id,Trans_amt,Trans_type,Trans_item,Trans_qnt,Trans_date) VALUES ('%s','%s',%s,%s,'%s',%s)",(transid,transprice,transtype,transitem,transqnt,transdate))
                                print("Record Added!")
                                mydb.commit()
                            elif opt==3:
                                transid=int(input("Enter the Transaction ID no. whose details is to be updated:"))
                                c1.execute('Select * from Transaction where Trans_id=%s'%(transid))
                                print()
                                mydata=c1.fetchone()
                                if mydata!=None:
                                    transidnew=int(input("Enter the new Transaction  ID no.:"))
                                    transprice=int(input("Enter the Transaction amount:"))
                                    transtype=input("Enter the type of Transaction:")
                                    transitem=input("Enter the item:")
                                    transqnt=int(input("Enter the quantity of items in Transaction:"))
                                    transdate=input("Enter the date of the Transaction(yyyy-mm-dd):")
                                    print()           
                                    
                                    c1.execute("update General set Trans_id='{0}',Trans_amt='{1}',Trans_type='{2}',Trans_item='{3}',Trans_qnt='{4}',Trans_date='{5}' where Trans_id='{6}'".format(transidnew,transprice,transtype,transitem,transqnt,transdate,transid))
                                    c1.execute("Select * from Transaction where Tans_id=%s"%(transidnew))
                                    mydata1=c1.fetchone()
                                    print(mydata1)
                                    print()
                                    mydb.commit()
                                else:
                                    print('No such record found with given ID no.')
                                    print()
                            elif opt==4:
                                transid=int(input("Enter the Transaction ID no. whose details is to be deleted:"))
                                c1.execute('Select * from Transaction where Trans_id=%s'%(transid))
                                mydata=c1.fetchone()
                                if mydata!=None:
                                    c1.execute("Delete from Transaction where trans_id=%s"%(transid))
                                    print("Record Deleted")
                                    mydb.commit()
                                else:
                                    print('No such record found with given ID no.')
                                    print()
                            else:
                                break
                    if ch==7:
                        print("Exiting this session!")
                        break

    if option==2:
        print("Exiting this session!")
        
                            
                                                        
                                                    
                                                    
                                        
