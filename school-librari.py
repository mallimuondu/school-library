print("hello ")
a = {
"malli" : "Malli2010!",
"nesh" : "1234",
"sharon": "sharon2008"
}
b = input("please input your username: ")
c = input("please input your pasword: ")
if b != a.keys():   
    print("no such user exists")
elif c != b.value():
    print("wrong passwored")
else:
    print("welcome")
    def categoris():
        print("these are the categorys we have")
        print(
            '''
            a.science
            b.Gamming   
            ''')
        d = input("chose the caetegories you want:  ")
        def logic():
            if d == "a":
                print("you have chosen science")
                print("these are the books we have:")
                print('''
                1.spotlight science
                2.primary science
                ''')
                e = input("chose the book you want?:")
                print("do you want to borrow another book:  ")
                s = input(" yes(y) or no(n): ")
                if s == "y":
                    categoris()  
                elif s == "n":
                    print("Make shure that you return the book or books in two weeks time.")
                    print("Thank you for visiting my library. good bye")
                    
            elif d == "b":
                print("you have chosen gamming")
                print("choose the book you want")
                print('''
                1.secrents of mincraft
                2.how to win a batle royal in fortnght
                ''')
                v = input ("chose the book you want?: ")
                z = input("do you want to borrow another book:  ")

                if z == "yes":
                    categoris()  
                elif z == "no":
                    print("Make shure that you return the book " 
                    if d == "a" and "b"
                          print("books")
                    elif d == "a" or "b":
                          print("book")
                          "in two weeks time.")
                    print("Thankyou for visiting my library good bye")
        logic()
    categoris()

else:
    print("plese regesta at the school office")
    