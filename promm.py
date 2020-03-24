import bs4
import requests


class bcolors:
    CBLACK = '\33[30m'
    CRED = '\33[31m'
    CGREEN = '\33[32m'
    CYELLOW = '\33[33m'
    CBLUE = '\33[34m'
    CVIOLET = '\33[35m'
    CBEIGE = '\33[36m'
    CWHITE = '\33[37m'


def proxy_lister():
    global table
    pageeLink = "https://free-proxy-list.net/"
    try:
        pagee = requests.get(pageeLink)
        soup = bs4.BeautifulSoup(pagee.content, "lxml")
        table = soup.find_all('table', attrs={'id': 'proxylisttable'}) and soup.table.find('tbody')
    except Exception as err:
        print("Check Web Sites ", err)

    data = []
    counter = 0
    for row in table:
        findd = row.find_all('td')
        findd = [x.text.strip() for x in findd]
        data.append([x for x in findd if x])
        del data[counter][2:8]
        data[counter] = ['{}:{}'.format(data[counter][0], data[counter][1])]
        counter += 1
    try:
        fileName = "proxy.txt"
        with open(fileName, "w+") as file:
            for i in data:
                i = ''.join(i)
                file.writelines(str(i) + "\n")
        print("{1}Proxyler Saved{3} {2}{0}{3}".format(fileName, bcolors.CVIOLET, bcolors.CBEIGE, bcolors.CRED))


    except Exception as err:
        print(err)
    return data


counter = 0
for i in proxy_lister():
    i = ''.join(i)
    print("{1}Proxy Find\t:{3} {2}{0}{3}".format(i, bcolors.CBLUE, bcolors.CVIOLET, bcolors.CRED))
    counter += 1

print("\nTotaly {1}{0}{2} Proxy Find!".format(counter, bcolors.CBLACK, bcolors.CRED))
print("{0}Proxy Saved!!! {2} {1}proxy.txt{2}".format(bcolors.CBLUE, bcolors.CVIOLET, bcolors.CRED))
