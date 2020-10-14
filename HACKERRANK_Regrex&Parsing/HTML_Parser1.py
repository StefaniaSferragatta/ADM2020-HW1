from html.parser import HTMLParser

html_text = ""
N = int(input())
if N > 0 and N <100:
    for i in range(N):
        html_text += input()

# create a subclass and override the handler methods
class MyHTMLParser(HTMLParser):

    def handle_starttag(self, tag, attrs):
        print ('Start :',tag)
        for attr in attrs:
                print ('->',' > '.join(map(str,attr)))

    def handle_endtag(self, tag):
        print ('End   :',tag)

    def handle_startendtag(self, tag, attrs):
        print ('Empty :',tag)
        for attr in attrs:
                print ('->',' > '.join(map(str,attr)))

# instantiate the parser and fed it some HTML
parser = MyHTMLParser()
parser.feed(html_text)
parser.close()