dict_convert = {
    "1" : "ๅ",
    "2" : "/",
    "3" : "-",
    "4" : "ภ",
    "5" : "ถ",
    "6" : "ุ",
    "7" : "ึ",
    "8" : "ค",
    "9" : "ต",
    "0" : "จ",
    "-" : "ข",
    "=" : "ช",
    "q" : "ๆ",
    "w" : "ไ",
    "e" : "ำ",
    "r" : "พ",
    "t" : "ะ",
    "y" : "ั",
    "u" : "ี",
    "i" : "ร",
    "o" : "น",
    "p" : "ย",
    "[" : "บ",
    "]" : "ล",
    "\\" : "ฃ",
    "a" : "ฟ",
    "s" : "ห",
    "d" : "ก",
    "f" : "ด",
    "g" : "เ",
    "h" : "้้",
    "j" : "่",
    "k" : "า",
    "l" : "ส",
    ";" : "ว",
    "'" : "ง",
    "z" : "ผ",
    "x" : "ป",
    "c" : "แ",
    "v" : "อ",
    "b" : "ิ",
    "n" : "ื",
    "m" : "ท",
    "," : "ม",
    "." : "ใ",
    "/" : "ฝ",
    # Shift
    "!" : "+",
    "@" : "๑",
    "#" : "๒",
    "$" : "๓",
    "%" : "๔",
    "^" : "ู",
    "&" : "฿",
    "*" : "๕",
    "(" : "๖",
    ")" : "๗",
    "_" : "๘",
    "+" : "๙",
    "Q" : "๐",
    "W" : "\"",
    "E" : "ฎ",
    "R" : "ฑ",
    "T" : "ธ",
    "Y" : "ํ",
    "U" : "๊",
    "I" : "ณ",
    "O" : "ฯ",
    "P" : "ญ",
    "{" : "ฐ",
    "}" : ",",
    "|" : "ฅ",
    "A" : "ฤ",
    "S" : "ฆ",
    "D" : "ฏ",
    "F" : "โ",
    "G" : "ฌ",
    "H" : "็",
    "J" : "๋",
    "K" : "ษ",
    "L" : "ศ",
    ":" : "ซ",
    "\"" : ".",
    "Z" : "(",
    "X" : ")",
    "C" : "ฉ",
    "V" : "ฮ",
    "B" : "ฺ",
    "N" : "์",
    "M" : "?",
    "<" : "ฒ",
    ">" : "ฬ",
    "?" : "ฦ",
    " " : " "
}

def decode(code):
    data = ''
    for i in range(len(code)):
        data += dict_convert[code[i]]
    return data

def run():
    while code := input("code : "):
        if code == "-1" :
            break;
        else :
            print(decode(code))

if __name__ == '__main__':
    run()


