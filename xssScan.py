import requests
import sys
import random


class bcolors:
    CBLACK = '\33[30m'
    CRED = '\33[31m'
    CGREEN = '\33[32m'
    CYELLOW = '\33[33m'
    CBLUE = '\33[34m'
    CVIOLET = '\33[35m'
    CBEIGE = '\33[36m'
    CWHITE = '\33[37m'


def get_user_agent():
    try:
        lines = [line.rstrip("\n") for line in open("useragent.txt")]
    except IOError as e:
        print("User Agent error: %s" % e.strerror)
        sys.exit(1)
    return lines


def xssFind():
    try:
        print(bcolors.CVIOLET,"e.g target -----> http://target.com/index.php?name=")
        url = input("Please Enter Target Url\t:")
        print(bcolors.CBLUE,"Default Payload List -----> xss-payloads.txt \t")
        y = """
        1)  BASIC PAYLOAD LIST
        2)  DIV PAYLOAD LIST
        3)  IMG PAYLOAD LIST
        4)  BODY PAYLOAD LIST
        5)  SVG PAYLOAD LIST
        6)  MIXED PAYLOAD LIST
        7)  ENTER FILE PATH
        8)  EXIT
        """
        print(y)
        choose = input("---->PLEASE CHOOSE PAYLOAD LIST\t:")
        if choose == '1':
            print("Selected payload:basic.txt\n")
            choose = "basic.txt"
        elif choose == '2':
            print("Selected payload:div.txt\n")
            choose = "div.txt"
        elif choose == '3':
            print("Selected payload:img.txt\n")
            choose = "img.txt"
        elif choose == '4':
            print("Selected payload:body.txt\n")
            choose = "body.txt"
        elif choose == '5':
            print("Selected payload:svg.txt\n")
            choose = "svg.txt"
        elif choose == '6':
            print("Selected payload:xss-payloads.txt\n")
            choose = "xss-payloads.txt"
        elif choose == '7':
            print(bcolors.CBEIGE,"e.g. path -----> /usr/share/wordlists/wfuzz/Injections/XSS.txt")
            choose = input("Path enter\t:")
        elif choose == '8':
            print("Exiting...")
            sys.exit()
        else:
            print("Wrong Choose..!!!")
        choose = choose.replace("\\", "/")
        while True:
            with open(choose, "r", errors="replace") as f:
                for i in f:
                    try:
                        usrr = get_user_agent()
                        header = {"User-Agent": "{}".format(random.choice(usrr))}
                        req = requests.get(url + i, headers=header)
                        if i in req.text:
                            print(bcolors.CRED,"Parameter vulnerable\r\n")
                            print(bcolors.CRED,"Vulneranle Payload Find\t: " + req.url)
                            with open("vulnpayload.txt", "a+") as ss:
                                ss.write(i)

                        else:
                            print(bcolors.CBLUE,"TRYING\t:", req.url)
                    except:
                        pass
                break



    except Exception as err:
        print(err)
