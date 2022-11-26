import string
import time

def worstHello() :
    temp = True
    helloList = ["h","e", "l", "l", "o", "w", "o","r", "l", "d"]
    alphabet = list(string.ascii_lowercase)
    helloWorld = ""
    counter = 0

    while temp :
        for elements in alphabet :
            time.sleep(.05)
            if helloWorld == "helloworld" :
                temp = False
                break

            print(helloWorld, elements,sep="")

            if elements == helloList[counter] :
                helloWorld += elements
                break

        counter += 1

if __name__ == "__main__" :
    worstHello()
    