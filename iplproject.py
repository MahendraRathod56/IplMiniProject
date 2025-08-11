import mysql.connector

myconnection=mysql.connector.connect(
    host='localhost',
    user='root',
    password='root',
    database='cricket'
)

mycursor=myconnection.cursor()

def addData():
    q="insert into ipl values (%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    pid=int(input("Enter The Player Id: "))
    Pname=input("Enter The Player name: ")
    Total_run=int(input("Enter The Total run: "))
    Half_century=int(input("How many half century: "))
    Century=int(input("How many Century's: "))
    Matches_played=int(input("How Many Matches played"))
    Total_sixes=int(input("How many Sixes: "))
    Total_fours=int(input("How Many fours: "))
    Type_of_player=input("Which Type of Player: ")
    val=(pid,Pname,Total_run,Half_century,Century,Matches_played,Total_sixes,Total_fours,Type_of_player)
    mycursor.execute(q,val)
    print("Data inserted successfull")

#Update data
def updateData():
    player_id=int(input("Enter player id to update: "))
    field=input("Enter the field to update  (Player_name,Total_run,Half_century,Century,Matches_played,Total_sixes,Total_fours,Types_of_player): ")
    value=input("Enter the new value: ")
    integer_fields = ['Total_run','Half_century','century','Matches_played','Total_sixes','Total_Four']
    if field in integer_fields:
        value=int(value)

    mycursor.execute(f"update ipl set {field}=%s where pid=%s",(value,player_id))
    print("Data inserted successfully")    

#Deleting a particular record
def deleteRecord():
    d1="Delete from ipl where pid=%s"
    delete1=int(input("Enter pid: "))
    val1=(delete1,)
    mycursor.execute(d1,val1)
    print("Record delete successfully")



#Showing all the details of the table

def ShowAll():
    mycursor.execute("select * from ipl")

    for i in mycursor:
       print(i)

#show a particular id    
def ShowId():
    s1="select * from ipl where pid=%s"
    idp=int(input("Enter the player id: "))
    val9=(idp,)
    mycursor.execute(s1,val9)

while True:
    print("\n1.Add data to the table: ")
    print("2.Update data in the table")
    print("3.Delete a particular record")
    print("4.Show all detail of the table")
    print("5.Show a particular id")
    print("6.Exit")
    choice=input("Enter your choice: ")

    if choice=="1":
        addData()
    elif choice=='2':
        updateData()
    elif choice=='3':
        deleteRecord()
    elif choice=='4':
        ShowAll()
    elif choice=='5':
        ShowId()
    elif choice=='6':
        break
    else:
        print("Invalid choice.please choose a valid option.")
        

myconnection.commit()
myconnection.close()
mycursor.close()