decoded = ["0",  "1",  "2",  "3",  "4",  "5",  "6",  "7",  "8",  "9",  "A",  "B",  "C",  "D",  "E",  "F",  "G",  "H",  "I",  "J",  "K",  "L",  "M",  "N",  "O",  "P",  "Q",  "R",  "S",  "T",  "U",  "V",  "W",  "X",  "Y",  "Z",  "a",  "b",  "c",  "d",  "e",  "f",  "g",  "h",  "i",  "j",  "k",  "l",  "m",  "n",  "o",  "p",  "q",  "r",  "s",  "t",  "u",  "v",  "w",  "x",  "y",  "z",  "=",  "."]
encoded = ["49", "48", "4B", "4A", "4D", "4C", "4F", "4E", "41", "40", "38", "3B", "3A", "3D", "3C", "3F", "3E", "31", "30", "33", "32", "35", "34", "37", "36", "29", "28", "2B", "2A", "2D", "2C", "2F", "2E", "21", "20", "23", "18", "1B", "1A", "1D", "1C", "1F", "1E", "11", "10", "13", "12", "15", "14", "17", "16", "09", "08", "0B", "0A", "0D", "0C", "0F", "0E", "01", "00", "03", "44", "57"]

def decode(value) : 
    out_value = ""
    char = [value[i:i+2] for i in range(0, len(value), 2)]
    for i in range(0, len(char)) :
        out_value += decoded[encoded.index(char[i])]
    return out_value

def encode(char) : 
    out_value = ""
    char = [value[i:i+1] for i in range(0, len(value))]
    for i in range(0, len(char)) :
        out_value += encoded[decoded.index(char[i])]
    return out_value

if __name__ == "__main__" :
    print("By default the program will open UserCustom.ini which should be in the directory as the program.")
    user_input = str(input("Would you like to encode or decode UserCustom.ini ? (encode/decode) "))
    const = "+CVars="
    config = open("UserCustom.ini" , "r")
    out_file = open("UserCustom.ini.out", "w")
    out_value = ""
    lines = config.readlines()
    for i in range(0, len(lines)) :
        if lines[i].startswith(const) :
            value = lines[i].split(const)[-1].split("\n")[0]
            if user_input.lower() == "encode" or user_input.lower() == "e" :
                out_value = encode(value)
            elif user_input.lower() == "decode" or user_input.lower() == "d" :
                out_value = decode(value)
            out_file.write(const + out_value + "\n")
        else : 
            out_file.write(lines[i])             
    out_file.close()
    config.close()
    pass