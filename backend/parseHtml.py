from bs4 import BeautifulSoup


# soup = BeautifulSoup(html_doc, './example_fox.json')

# print(soup.prettify())

class ParseHtml:
    def __init__(self, data):
        self.html_doc = data
        self.soup = BeautifulSoup(self.html_doc, "lxml")

    def generate(self):
        for p in self.soup.find_all('p'):
            self.fileWriter(p.get_text() + "\n")
            print("[" + p.get_text() + "]")

    def fileWriter(self, data):
        with open('paragraphExample.txt', 'a') as file:
            file.write(data)






htmlData = ""
with open('example_nyt.json', 'r') as file:
    htmlData = file.read()

parser = ParseHtml(htmlData)
parser.generate()






























