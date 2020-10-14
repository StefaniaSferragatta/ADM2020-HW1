import xml.etree.ElementTree as etree

maxdepth = 0
def depth(elem, level):
    global maxdepth
    level += 1 #increase the level because the default value is -1
    if level >= maxdepth: #if the level is greater (or equal) than the maxdepth variable
        maxdepth = level #update maxdepth at level's value
    #For each element, if that element has children, list(elem),
    #use recursion calling the function depth
    for child in elem:
        depth(child, level)

if __name__ == '__main__':
    n = int(input())
    xml = ""
    for i in range(n):
        xml =  xml + input() + "\n"
    tree = etree.ElementTree(etree.fromstring(xml))
    depth(tree.getroot(), -1)
    print(maxdepth)

