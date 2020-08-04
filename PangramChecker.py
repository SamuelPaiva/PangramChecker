import string


def Pangram(str):
    Buchstaben = "abcdefghijklmnopqrstuvwxyz"
    for B in Buchstaben:
        if B not in str.lower():
            return False


    return True


string = input(str("Check for pangram: \n\n"))
if (Pangram(string) == True):
    print("\n\n Yes, this sentence is a pangram")

if (Pangram(string) == False):
    print("\n\nThis is'nt a pangram, because:\n")

if "a" not in string:
    print("a is missing")
if "b" not in string:
    print("b is missing")
if "c" not in string:
    print("c is missing")
if "d" not in string:
    print("d is missing")
if "e" not in string:
    print("e is missing")
if "f" not in string:
    print("f is missing")
if "g" not in string:
    print("g is missing")
if "h" not in string:
    print("h is missing")
if "i" not in string:
    print("i is missing")
if "j" not in string:
    print("j is missing")
if "k" not in string:
    print("k is missing")
if "l" not in string:
    print("l is missing")
if "m" not in string:
    print("m is missing")
if "n" not in string:
    print("n is missing")
if "o" not in string:
    print("o is missing")
if "p" not in string:
    print("p is missing")
if "q" not in string:
    print("q is missing")
if "r" not in string:
    print("r is missing")
if "s" not in string:
    print("s is missing")
if "t" not in string:
    print("t is missing")
if "u" not in string:
    print("u is missing")
if "v" not in string:
    print("v is missing")
if "w" not in string:
    print("w is missing")
if "x" not in string:
    print("x is missing")
if "y" not in string:
    print("y is missing")
if "z" not in string:
    print("z is missing")
