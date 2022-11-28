import string
import time

def worstHello(tempString) :
    temp = True
    lst = []
    lst.extend(tempString)
    alphabet = list(string.ascii_letters)
    alphabet.insert(5, "ë")
    helloWorld = ""
    counter = 0

    while temp :
        for elements in alphabet :
            time.sleep(.05)
            if helloWorld == tempString :
                temp = False
                break

            print(helloWorld, elements,sep="")

            if " " == lst[counter] :
                helloWorld += " "
                break
            if elements == lst[counter] :
                helloWorld += elements
                break

        counter += 1

if __name__ == "__main__" :
    temp = input("input a string: ")
    worstHello(temp)
    