contact={}
def new():
    name=input("can you tell me your name plz?")
    number=input("can you tell me your phone number?")
    contact[name]=number
    print(contact)
def delete():
    name=input("can you tell me your name plz?")
    del contact[name]
    print("done")
def change():
    name=input("can you tell me your name plz?")
    number=input("can you tell me your new phone number?")
    contact[name]=number
    print(contact)
def show():
    print(contact)

while True:
    y=input("what kind of help you want?")
    if y=="out":
        print("good bye")
        break
    elif y=="new":
         new()
    elif y=="delete":
         delete()
    elif y=="change":
         change()
    elif y=="show":
         show()
    else:
        print("unvalid")
        
