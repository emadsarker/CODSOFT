contacts = {}
while True:
    print("1.add contact")
    print("2.view contacts")
    print("3.search contact")
    print("4.update contact")
    print("5.delete contact")
    print("6.exit")
    option=int(input("select your option:"))
    if option=="1":
        name=input("enter contact name:")
        phone=input("enter phone number:")
        email=input("enter email:")
        address=input("enter address:")
        if name and phone:
            contacts[name]={"phone":phone,"email":email,"address":address}
            print(f"contact {name} has been added")
        else:
            print("requiring the number.")
    elif option=="2":
        if contacts:
            print("contact list:")
            for name,info in contacts.items():
                print(f"{name}:{info['phone']}")
        else:
            print("no available contacts.")
    elif option=="3":
        search_term=input("enter name or phone number to search:")
        found=False
        for contact,details in contacts.items():
            if contact==search_term or details['phone']==search_term:
                print(f"contact found: name: {contact}, phone: {details['phone']}, email: {details['email']}, address: {details['address']}")
                found=True
                break
        if not found:
            print("contact not found.")
    elif option=="4":
        name=input("enter the name of the contact to update:")
        if name in contacts:
            phone=input("enter number")
            email=input("enter email")
            address=input("enter address")
            if phone:
                contacts[name]['phone']=phone
            if email:
                contacts[name]['email']=email
            if address:
                contacts[name]['address']=address
            print(f"contact {name} updated")
        else:
            print("contact not found.")
    elif option=="5":
        name=input("enter the name of the contact to delete:")
        if name in contacts:
            del contacts[name]
            print(f"contact {name} deleted")
        else:
            print("contact not found.")
    elif option=="6":
        print("exiting")
        break
    else:
        print("invalid choice.")
