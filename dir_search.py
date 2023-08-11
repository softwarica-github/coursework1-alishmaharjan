from queue import Queue
import requests
from colorama import Fore
import threading
import sys

try:
    a1 = sys.argv[1]
    if a1.startswith('http'):
        pass
    else:
        a1 = 'https://' + a1
except IndexError:
    a1 = "https://ldce.ac.in"
url = a1

d1 = []
q = Queue()
s = "directory-list-lowercase-2.3-small"

def fill_lines():
    with open(f"wordlist/{s}.txt") as f1:   
        lines = f1.readlines()
    for line in lines:
        m1_url = url + '/' + line.strip() + "/"
        q.put(m1_url)

def dir_search_check(m_url):
    try:
        r = requests.get(m_url)
        if not 399 < r.status_code < 500:
            d1.append(f'{m_url}       #{r.status_code}')
            print(f'{m_url}       #{r.status_code}')
            return True
        else:
            return False
    except Exception as e:
        pass
def worker():
    try:
        while not q.empty():
            m_url = q.get()
            dir_search_check(m_url)
    except KeyboardInterrupt:
        print(Fore.YELLOW, 'KeyboardInterrupt Exiting...')

def write_dir_results():
    results = open("result/dirs.txt", 'a')
    for i in d1:
        results.write(f'{i} \n')
    results.close()
    print('results save to: dirs.txt')

def dir_search_run():
    print(Fore.YELLOW, f'searching directories for {url}', Fore.GREEN)
    thread_list = []
    for i in range(120):
        thread = threading.Thread(target=worker)
        thread_list.append(thread)

    for thread in thread_list:
        thread.start()

    for thread in thread_list:
        thread.join()
def run():
    fill_lines()
    dir_search_run()
    write_dir_results()
if __name__ == '__main__':
    dir_search_run()
    write_dir_results()