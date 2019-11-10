from bs4 import BeautifulSoup


# soup = BeautifulSoup(html_doc, './example_fox.json')

# print(soup.prettify())

class ParseHtml:
    def __init__(self, data):
        self.html_doc = data
        self.soup = BeautifulSoup(self.html_doc, "lxml")

    def generate(self):
        for p in self.soup.find_all('p'):  # TODO get rid of the [4]

            p = self.modifyContent(p)

    def fileWriter(self, data):
        with open('paragraphExample.txt', 'a') as file:
            file.write(data)

    def modifyContent(self, data):
        contents, color = self.callZach(data.string)

        # new_tag = self.new_soup.new_tag('div', id='file_history')
        attributes = {'class': color}
        mark_tag = self.soup.new_tag('mark', **attributes)
        mark_tag.string = str(contents)

        print(mark_tag)
        # return "<mark class=\""+ color +"\">" + str(data) + "</mark>"

    def callZach(self, data):
        # TODO
        return data, "red"


htmlData = ""
with open('example_nyt.json', 'r') as file:
    htmlData = file.read()

parser = ParseHtml(htmlData)
parser.generate()
