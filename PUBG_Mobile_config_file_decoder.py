import sys
from textwrap import wrap
print("enter decode / d if you wish to decode the config")
print("enter encode / e if you wish to encode the config")
print("enter exit / end / close if you whish to exit the script")
user_input = input("enter your option : ")
#encoding loop
while user_input.lower() == "encode" or user_input.lower() == "e" :
    config = input("please enter the config without '+CVars=' : ")
    if config == "exit" or config == "end" or config == "close" :
        sys.exit("exiting the program")
# we check the config if it contains +CVars= 
    while "+CVars=" in config : 
        print("your config contains '+CVars=' please enter it again without it")
        config = input("please enter the config again without '+CVars=' : ")
# here we encode the config
    enlst = wrap(config, 1)
    for i in enlst :
        en = i.replace("1", "48").replace("2", "4B").replace("3", "4A").replace("4", "4D").replace("5", "4C").replace("6", "4F").replace("7", "4E").replace("8", "41").replace("9", "40").replace("0", "49").replace("A", "38").replace("B", "3B").replace("C", "3A").replace("D", "3D").replace("E", "3C").replace("F", "3F").replace("G", "3E").replace("H", "31").replace("I", "30").replace("J", "33").replace("K", "32").replace("L", "35").replace("M", "34").replace("N", "37").replace("O", "36").replace("P", "29").replace("Q", "28").replace("R", "2B").replace("S", "2A").replace("T", "2D").replace("U", "2C").replace("V", "2F").replace("W", "2E").replace("X", "21").replace("Y", "20").replace("Z", "23").replace("a", "18").replace("b", "1B").replace("c", "1A").replace("d", "1D").replace("e", "1C").replace("f", "1F").replace("g", "1E").replace("h", "11").replace("i", "10").replace("j", "13").replace("k", "12").replace("l", "15").replace("m", "14").replace("n", "17").replace("o", "16").replace("p", "09").replace("q", "08").replace("r", "0B").replace("s", "0A").replace("t", "0D").replace("u", "0C").replace("v", "0F").replace("w", "0E").replace("x", "01").replace("y", "00").replace("z", "23").replace("=", "44").replace(".", "57")
        print(en, end="")
    print("")
#decoding loop
while user_input.lower() == "decode" or user_input.lower() == "d" :
    config = input("please enter the config without '+CVars=' : ")
    if config.lower() == "exit" or config.lower() == "end" or config.lower() == "close" :
        sys.exit("exiting the program")
# we check the config if it contains +CVars= 
    while "+CVars=" in config :
        print("your config contains '+CVars=' please enter it again without it")
        config = input("please enter the config again without '+CVars=' : ")
# here we decode the config
    delst = wrap(config, 2)
    for i in delst :
        de = i.replace("48", "1").replace("4B", "2").replace("4A", "3").replace("4D", "4").replace("4C", "5").replace("4F", "6").replace("4E", "7").replace("41", "8").replace("40", "9").replace("49", "0").replace("38", "A").replace("3B", "B").replace("3A", "C").replace("3D", "D").replace("3C", "E").replace("3F", "F").replace("3E", "G").replace("31", "H").replace("30", "I").replace("33", "J").replace("32", "K").replace("35", "L").replace("34", "M").replace("37", "N").replace("36", "O").replace("29", "P").replace("28", "Q").replace("2B", "R").replace("2A", "S").replace("2D", "T").replace("2C", "U").replace("2F", "V").replace("2E", "W").replace("21", "X").replace("20", "Y").replace("23", "Z").replace("18", "a").replace("1B", "b").replace("1A", "c").replace("1D", "d").replace("1C", "e").replace("1F", "f").replace("1E", "g").replace("11", "h").replace("10", "i").replace("13", "j").replace("12", "k").replace("15", "l").replace("14", "m").replace("17", "n").replace("16", "o").replace("09", "p").replace("08", "q").replace("0B", "r").replace("0A", "s").replace("0D", "t").replace("0C", "u").replace("0F", "v").replace("0E", "w").replace("01", "x").replace("00", "y").replace("23", "z").replace("44", "=").replace("57", ".")
        print(de, end="")
    print("")
if user_input.lower() == "exit" or user_input.lower() == "end" or user_input.lower() == "close" :
    sys.exit("exiting the program")
