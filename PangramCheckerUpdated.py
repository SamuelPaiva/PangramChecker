import string


def Pangram(str):
    Buchstaben = "abcdefghijklmnopqrstuvwxyz"
    for B in Buchstaben:
        if B not in str.lower():
            return False
    return True

def Pangram2(str):
    Buchstaben = "abcdefghijklmnopqrstuvwxyz"
    for B in Buchstaben:
        if B not in str.lower():
            print(B, "is missing")

string = input(str("Check for pangram: \n\n"))
if (Pangram(string) == True):
    print("\n\n Yes, this sentence is a pangram")



if (Pangram2(string) == False):
    Pangram2(str)

