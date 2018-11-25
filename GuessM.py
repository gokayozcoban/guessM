import random as r

rastgelesayı = r.randint(1,50)
print("                                    ")
print("                                    ")
print("                                    ")
print("***************GUESS****************")
print("                                    ")
print("                                    ")
print("                                    ")
print("     guess a number from 1 to 50    ")

while True:
    print("                                    ")
    tahmin = int(input("Give me a number: "))
    if tahmin == rastgelesayı:
        print("                                    ")
        print("                                    ")
        print("*********************")
        for i in range(5):
            print("YOU WIN! :)")
        print("                                    ")
        print("                                    ")
        print("*********************")
        print("coded by Gökay!")
        break
    elif tahmin < rastgelesayı:
        print("                                    ")
        print("Bigger")
    elif tahmin > rastgelesayı:
        print("                                    ")
        print("Smaller")
        
        
        
