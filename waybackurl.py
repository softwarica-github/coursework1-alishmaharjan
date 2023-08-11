import requests
import requests.exceptions
import sys
from colorama import Fore
import json
urls = []
try:
    a1 = sys.argv[1]
    if a1.startswith('http'):
        pass
    else:
        a1 = 'https://' + a1
except IndexError:
    # print(e)
    a1 = 'https://rru.ac.in'
def way_back_url():
    print(Fore.GREEN, "searching on way back url...", Fore.YELLOW)
    global a1
    print("target:", a1)
    url = 'https://web.archive.org/web/*/' + a1
    base_url = 'https://web.archive.org/web/'
    headers = {'Referer': url,
               'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                             'Chrome/92.0.4515.107 Safari/537.36'}

    r1 = requests.get(f'https://web.archive.org/__wb/sparkline?output=json&url={a1}&collection=web',
                      headers=headers)
    x1 = r1.text
    y1 = json.loads(x1)
    s = base_url + str(y1["last_ts"]) + '/http:/' + a1[8:]
    print(s)
    urls.append(s)
    s = base_url + str(y1["first_ts"]) + '/http:/' + a1[8:]
    print(s)
    urls.append(s)

    k = dict(y1["years"])
    years = []
    for i in k.keys():
        years.append(i)

    for j in years:

        r2 = requests.get(f'https://web.archive.org/__wb/calendarcaptures/2?url={a1}&date={j}&groupby=day',
                          headers=headers)
        x2 = r2.text
        y2 = json.loads(x2)
        k1 = list(y2["items"])
        for i in k1:

            if i[0] > 999:
                s = base_url + str(j) + str(i[0]) + '/http:/' + a1[8:]
            else:
                s = base_url + str(j) + '0' + str(i[0]) + '/http:/' + a1[8:]
            print(s)
            urls.append(s)
    with open(f'result/waybackurls.txt', 'w') as f:
        for x in urls:
            f.write(f'{x} \n')
    print(f"results store in: result/waybackurls.txt")
if __name__ == '__main__':
    way_back_url()