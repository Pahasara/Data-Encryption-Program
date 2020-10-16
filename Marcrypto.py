import time
print("* DvNET Marcrypto v0.8 Build 1016")
time.sleep(1)
print("* (c) 2020 DvNET Technologies. All rights reserved.")
time.sleep(2)
print()


#MAIN FUNCTION
def Main():
    print()
    print("*** MAIN MENU ***")
    print()
    print("1. Data Encrypt")
    print("2. Data Decrypt")
    print()
    print("*****************")
    print()
    u = input("Enter your choice [1/2]: ")
    if u == "1":
        Encrypt()
    elif u == "2":
        Decrypt()
    Main()


#MAIN ENCRYPT
def Encrypt():
    print()
    print("*** DATA ENCRYPT ***")
    print()
    sin = input("Enter the text to encrypt: ")
    encrypto_dat = Encrypto(sin)
    print(encrypto_dat)
    print()
    u = input("Do you want save that to a textfile [y/n] : ")
    if u == "y":
        try:
            TextWr('data.txt', encrypto_dat, 'w+')
        except IOError:
            print("'data.txt' is doesn't exist!")
        else:
            print("Saved successfully!")
    Main()

#MAIN DECRYPT
def Decrypt():
    print()
    print("*** DATA DECRYPT ***")
    print()
    sim = input("Enter to decrypt the text: ")
    if sim == "":
        try:
            decrypto_dat = Decrypto(TextRd('data.txt'))
        except IOError:
            print("'data.txt' is doesn't exist!")
        else:
            print()
            print(decrypto_dat)
            print()
            u = input("Do you want save that to a textfile [y/n] : ")
            if u == "y":
                try:
                    TextWr('data.txt', decrypto_dat, 'w')
                except IOError:
                    print("'data.txt' is doesn't exist!")
                else:
                    print("Saved successfully!")
            else:   
                print(Decrypto(sim))
    Main()

def Encrypto(src):
    # Character Enrypting
    src = src.replace("0", "(g&4>|ha2")
    src = src.replace("1", "%r/3.5u(")
    src = src.replace("2", ")h7$ed&")
    src = src.replace("3", "*f=!de0")
    src = src.replace("4", "-6p^$x8")
    src = src.replace("5", "+_)q2!&lk")
    src = src.replace("6", "s5>!7v4")
    src = src.replace("7", "=-+%^jn$")
    src = src.replace("8", "s-#t9ip")
    src = src.replace("9", "lk_(2q+=")
    src = src.replace("a", ")#07&46")
    src = src.replace("b", "*4a.92@")
    src = src.replace("c", "^%2b5a7")
    src = src.replace("d", "(4c3&a6")
    src = src.replace("e", "7d%4a/2<a")
    src = src.replace("f", "8?d3c74#2")
    src = src.replace("g", "$a5@1$.^")
    src = src.replace("h", "@<f)0_$")
    src = src.replace("i", ".*0/c1a.^f9")
    src = src.replace("j", "-g%8^b4?")
    src = src.replace("k", "#a5.0)+@")
    src = src.replace("l", ":g$6*0&!_")
    src = src.replace("m", "&ge$=*a3/.7")
    src = src.replace("n", "@!g^8-b?fe")
    src = src.replace("o", "_9.<d/'j(3e")
    src = src.replace("p", "%b./0c^4")
    src = src.replace("q", ")2&l6-n&0")
    src = src.replace("r", "*j#b^(^>")
    src = src.replace("s", "h*%f1km$")
    src = src.replace("t", "m(=9:/7&3.g")
    src = src.replace("u", "f=@m-9(*?r")
    src = src.replace("v", ">n.0*&'bk")
    src = src.replace("w", "(u%=<t*v_")
    src = src.replace("x", "4*.p0+#")
    src = src.replace("y", "8^m./?'5r")
    src = src.replace("z", "=2p^f*/g4")
    # Converting to a List
    encr = list(src.split(" "))
    return encr


def Decrypto(encr):
    decr = str(encr)
    # Convertion to a Text
    decr = decr.replace("[", "")
    decr = decr.replace("]", "")
    decr = decr.replace("\"", "")
    decr = decr.replace(";", " ")
    # Character Decrypting
    decr = decr.replace(")#07&46", "a")
    decr = decr.replace("*4a.92@", "b")
    decr = decr.replace("^%2b5a7", "c")
    decr = decr.replace("(4c3&a6", "d")
    decr = decr.replace("7d%4a/2<a", "e")
    decr = decr.replace("8?d3c74#2", "f")
    decr = decr.replace("$a5@1$.^", "g")
    decr = decr.replace("@<f)0_$", "h")
    decr = decr.replace(".*0/c1a.^f9", "i")
    decr = decr.replace("-g%8^b4?", "j")
    decr = decr.replace("#a5.0)+@", "k")
    decr = decr.replace(":g$6*0&!_", "l")
    decr = decr.replace("&ge$=*a3/.7", "m")
    decr = decr.replace("@!g^8-b?fe", "n")
    decr = decr.replace("_9.<d/'j(3e", "o")
    decr = decr.replace("%b./0c^4", "p")
    decr = decr.replace(")2&l6-n&0", "q")
    decr = decr.replace("*j#b^(^>", "r")
    decr = decr.replace("h*%f1km$", "s")
    decr = decr.replace("m(=9:/7&3.g", "t")
    decr = decr.replace("f=@m-9(*?r", "u")
    decr = decr.replace(">n.0*&'bk", "v")
    decr = decr.replace("(u%=<t*v_", "w")
    decr = decr.replace("4*.p0+#", "x")
    decr = decr.replace("8^m./?'5r", "y")
    decr = decr.replace("=2p^f*/g4", "z")
    decr = decr.replace("(g&4>|ha2", "0")
    decr = decr.replace("%r/3.5u(", "1")
    decr = decr.replace(")h7$ed&", "2")
    decr = decr.replace("*f=!de0", "3")
    decr = decr.replace("-6p^$x8", "4")
    decr = decr.replace("+_)q2!&lk", "5")
    decr = decr.replace("s5>!7v4", "6")
    decr = decr.replace("=-+%^jn$", "7")
    decr = decr.replace("s-#t9ip", "8")
    decr = decr.replace("lk_(2q+=", "9")
    return decr


#data READER
def TextRd(src):
    Opile = open(src, 'r')
    Data = Opile.read()
    Opile.close()
    return Data


#data WRITER
def TextWr(scf, stg, tp):
    try:
        wtext = str(stg)
        wtext = wtext.replace(",", "")
        Opile = open(scf, tp)
    except:
        print("File Error!")
    Opile.write(wtext)
    Opile.close()


Main()
ex = input()
