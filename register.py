import mysql.connector

vk= mysql.connector.connect(
    host="localhost",
    user="root",
    password="vijaykavi",
    database="online_booking"
    
    
)
mycursor=vk.cursor()

def insert(name,password,mobile_no):
    a="insert into register(name,password,mobile_no) values(%s,%s,%s)"
    b=(name,password,mobile_no)
    mycursor.execute(a,b)
    vk.commit()
    show = mycursor.fetchall()
    print(show)

def bus_ticket(starting,ending,how,name):
    mycursor.execute(f"select starting_point,ending_point from bus where name='{name}'")
    show=mycursor.fetchall()
    result=show[0]
    if starting=="cheyyar" and ending=="vellore":
        # cheyyar_vellore=120
        total=how*120
        print(f"Starting-point ='{starting}'")
        print(f"ending-point ='{ending}'")
        print(f" how many ticket ='{how}'")
        print(f"Total Cast For Ticket ='{total}'")
    elif starting == "cheyyar" and ending=="kanchipuram":
        # cheyyar_kanchipuram=100
        total=how*100
        print(f"Starting-point ='{starting}'")
        print(f"ending-point ='{ending}'")
        print(f" how many ticket ='{how}'")
        print(f"Total Cast For Ticket ='{total}'")
    elif starting == "cheyyar" and ending=="chennai":
        # cheyyar_chennai=150
        total=how*150
        print(f"Starting-point ='{starting}'")
        print(f"ending-point ='{ending}'")
        print(f" how many ticket ='{how}'")
        print(f"Total Cast For Ticket ='{total}'")

    else:
        print("Someting went to wrong")


def bus(starting,ending,how,name):
    a="insert into bus(starting_point,ending_point,how_many,name) values(%s,%s,%s,%s)"
    b=(starting,ending,how,name)
    mycursor.execute(a,b)
    vk.commit()
    bus_ticket(starting,ending,how,name)

def train(starting,ending,how,name):
    a="insert into train(starting_point,ending_point,how_many,name) values(%s,%s,%s,%s)"
    b=(starting,ending,how,name)
    mycursor.execute(a,b)
    vk.commit()
    train_ticket(starting,ending,how,name)

def train_ticket(starting,ending,how,name):
    mycursor.execute(f"select starting_point,ending_point from bus where name='{name}'")
    show=mycursor.fetchall()
    result=show[0]
    if starting=="cheyyar" and ending=="vellore":
        # cheyyar_vellore=60
        total=how*60
        mycursor.execute(f"update train set total_cost='{total}' where name='{name}'")
        vk.commit()
        print(f"Starting-point ='{starting}'")
        print(f"ending-point ='{ending}'")
        print(f" how many ticket ='{how}'")
        print(f"Total Cast For Ticket ='{total}'")
    elif starting == "cheyyar" and ending=="kanchipuram":
        # cheyyar_kanchipuram=50
        total=how*50
        print(f"Starting-point ='{starting}'")
        print(f"ending-point ='{ending}'")
        print(f" how many ticket ='{how}'")
        print(f"Total Cast For Ticket ='{total}'")
    elif starting == "cheyyar" and ending=="chennai":
        # cheyyar_chennai=75
        total=how*150
        print(f"Starting-point ='{starting}'")
        print(f"ending-point ='{ending}'")
        print(f" how many ticket ='{how}'")
        print(f"Total Cast For Ticket ='{total}'")

    else:
        print("Someting went to wrong")   

def login(name,pawwsord):
    mycursor.execute(f"select name,password from register where name='{name}'")
    show = mycursor.fetchall()
    if show !=[]:
        print("Entr Correct Password")
        if name==show[0][0] and password==show[0][1]:
            print("Login Successful\n Now You Can Book Tickets")
            print("1.Bus Ticket")
            print("2.Train Ticket")
            print("3.Flight Ticket")
            user=int(input("Which Ticket You Want: "))
            if user == 1:
               starting=input("Enter Your Starting-point: ")
               ending=input("Enter Your ending-point: ")
               how=int(input("How Many Ticket You Want: "))
               bus(starting,ending,how,name)


            elif user == 2:
               starting=input("Enter Your Starting-point: ")
               ending=input("Enter Your ending-point: ")
               how=int(input("How Many Ticket You Want: "))
               train(starting,ending,how,name)

            elif user == 3:
                 print(user,"selected")

            else:
                 print("Enter Valid option")
    else:
        print("Loginn Failed")

user=int(input("\n press 1 Register \n  press 2 login \n"))
if user == 1:
    name=input("Enter Your Name: ")
    password=input("Enter Your password: ")
    mobile_no=input("Enter Your Mobile: ")
    insert(name,password,mobile_no)
elif user == 2:
    name=input("Enter Your Name: ")
    password=input("Enter Your Password: ")

    login(name,password)
    