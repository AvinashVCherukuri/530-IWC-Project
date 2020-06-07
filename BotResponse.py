#   Avinash Varma
#   Hardcoded message retrieval!

def launchRA(text,name):

    if "hello" in text or "Hello" in text:
        return ("Hi "+name+"!")

    elif "cool" in text or "Cool" in text:
        return ("Yeah right!\nI know")

    elif "Shit" in text or "shit" in text:
        return ("Yeah, this is some cool shit!")

    elif "Okay" in text or "okay" in text:
        return ("Hmmm!\nTry 'Help' for more!")

    elif "haha" in text or "Haha" in text :
        return ("hehehe!")

    elif "hehe" in text or "Hehe" in text :
        return ("hahaha!")

    elif "Nice" in text or "nice" in text :
        return ("Thanks "+name)

    elif text == "/start":
        return ("Hi " + name+"\nHope you are doing great!\n\n")

    elif "team" in text or "Team" in text :
        return ("Mr. Avinash Varma! Ohh Yeah!!!")

    elif "Great" in text or "great" in text :
        return ("Thanks.\nI can do a lot more! Try 'Help'")

    elif text == "End" or text == "end":
        return ("Bye "+name+"!\nWish to see you back soon. Have a great day.")

    elif "Bye" in text or "bye" in text :
        return ("Good Bye "+name+",Just say 'End', and we will be done for good!")

    elif "Help"  in text or "help" in text:
        return ("Hey "+name+"!\n\nI am not exactly sure what the project is. So lets wait and watch!")

    elif "hi" in text or "Hi" in text :
        return ("Hello " + name + "!")

    else:
        return ("I don't know that, Sorry!\nTry 'Help'")