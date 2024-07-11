#WAP to create a simple chat bot which wil respond "hi!" to hello and "bye!" to anything else.
bot=input("I can chat with you ....\n")
if bot == "Hi!":
    print("Hello! I am a chatbot used to program some simple things.")
    made =input("Wanna ask more things?\n")
    if made=="Yes! Who made you?":#double == is used to define the conditions neccessary.
     print("I was made by Saksham a python programmer in 2024 at 9:30 PM.")
    elif made== "No!":
        print("OK we can talk later...")
elif bot == "Bye!":#if the users input is no from the begininng it will just end by skipping all the above syntaxes.
    print("Bye! Have a great time.....")
else:
    print("Sorry, I can't understand .")#for invalidation likee if its hi or bye or anything else it will just print i can't understand.