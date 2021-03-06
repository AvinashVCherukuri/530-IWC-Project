import gbmodel

# This definition tells what message we have to reply back to the user
def launchRA(user, name, msg):

    model = gbmodel.get_model()
    entries = [dict(username=row[0], bagcolor=row[1], cellphone=row[2], description=row[3], status=row[4], tagid=row[5]) for row in model.select()]

    # This is where the bot compares the user name to the ones in the Database and gets their status
    if msg == "Status" or msg == "status":
        for lists in entries :
            if  user in lists.values():
                print(lists)
                return(lists["status"], lists["tagid"])  


    elif "hello" in msg or "Hello" in msg:
        return ("Hi "+name+"!")

    elif "cool" in msg or "Cool" in msg:
        return ("Yeah right!\nI know")

    elif "Shit" in msg or "shit" in msg:
        return ("Yeah, this is some cool shit!")

    elif "Okay" in msg or "okay" in msg:
        return ("Hmmm!\nTry 'Help' for more!")

    elif "haha" in msg or "Haha" in msg :
        return ("hehehe!")

    elif "hehe" in msg or "Hehe" in msg :
        return ("hahaha!")

    elif "Nice" in msg or "nice" in msg :
        return ("Thanks "+name)

    elif msg == "/start":
        return ("Hi " + name+"\nHope you are doing great!\n\n")

    elif "team" in msg or "Team" in msg :
        return ("Mr. Avinash Varma! Ohh Yeah!!!")

    elif "Great" in msg or "great" in msg :
        return ("Thanks.\nI can do a lot more! Try 'Help'")

    elif "Bye" in msg or "bye" in msg or msg == "End" or msg == "end":
        return ("Good Bye "+name+", Have a nice day!")

    elif "Help"  in msg or "help" in msg:
        return ("Hey "+name+"!\n\nI am LostMyBag Bot. You can say\n\nstatus - to know the status of your bag")

    elif "hi" in msg or "Hi" in msg :
        return ("Hello " + name + "!")

    else:
        return ("I don't know that, Sorry!\nTry 'Help'")