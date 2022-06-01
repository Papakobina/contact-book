contact_list = {

}


def adder():
    name = input("What is the name of the individual?")
    number = input("What is " + name.upper() + "'s number?")
    contact_list[name] = number


nim = 0
while nim < 7:
    print("You can add only 8 things max")
    replay = input("Do you want to add a number to your contact list?")
    if replay == "yes":
        print(adder())
    elif replay == "no":
        nim += 11
        prompt_contact_list = input("Do you want to see your whole contact "
                                    "list or just an individuals name?\n"
                                    "Type in 1 to see your whole contact name and "
                                    "2 to see just one individuals contact")
        if prompt_contact_list == "1":
            print(contact_list)
        else:
            username = input("Who's number do you want to see?")
            print("Okay. " + username.upper() + "'s number is " + contact_list[username])



