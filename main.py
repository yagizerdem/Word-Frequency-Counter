from bs4 import BeautifulSoup
import requests


class Node:

    def __init__(self):
        self.wordend = False
        self.counter = 0
        self.table = {}


class Trie:
    def __init__(self):
        self.root = Node()

    def insert(self, word):
        main = self.root
        for i in range(len(word)):
            char = word[i]
            if (main.table.get(char) == None):
                main.table[char] = Node()
            main = main.table[char]
        main.wordend = True
        main.counter = main.counter + 1

    def search(self, word):
        main = self.root
        for i in range(len(word)):
            char = word[i]
            if (not main.table.get(char)):
                return -1
            main = main.table[char]
        if main.wordend == False:
            return -1
        return main.counter


trie = Trie()
while True:
    url = input("enter url")
    resp = requests.get(url)
    html = resp.text
    soup = BeautifulSoup(html, "html.parser")
    data = soup.encode('utf-8').decode('utf-8')
    data = ''.join(char for char in data if ord(char) <= 255)
    words = data.split()
    for w in words:
        trie.insert(w)
    target = input("enter word to find frequency")
    counter = trie.search(target)
    if counter <= 0:
        print("this word dont exist")
    else:
        print("word frequency counter is %d" % counter)
