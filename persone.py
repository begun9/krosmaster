from xml.dom import minidom
import os.path as OS
import xml.etree.cElementTree as ET

list={'xp': 5, 'damag': 3, 'x': 1, 'y': 1}
def save(xp): 
    data = ET.Element('hero')
    for key in xp:
        XPH = ET.SubElement(data, key)
        XPH.text = str(xp[key])

    # xp1.text = xp
    return ET.tostring(data)

if OS.isfile('‬items2.xml') == False:
    #‭ ‬создаём файловую структуру
    data = ET.Element('hero')
    items = ET.SubElement(data, 'items')
    item1 = ET.SubElement(items, 'item')
    item2 = ET.SubElement(items, 'item')
    item1.set('name', 'item1')
    item2.set('name', 'item2')
    item1.text = 'item1abc'
    item2.text = 'item2abc'

    #‭ ‬создаём новый файл XML с результатами
    mydata = ET.tostring(data)
    print(mydata)
    myfile = open('‬items2.xml', 'w', )
    myfile.write(mydata.decode('utf-8'))
    myfile.close()


mydata = save(list)
print(mydata)
myfile = open('‬items2.xml', 'w', )
myfile.write(mydata.decode('utf-8'))
myfile.close()

mydoc = minidom.parse('‬items2.xml')
items = mydoc.getElementsByTagName('xp')
print(items[0].firstChild.data)
# print(items[0].attributes[)
# print(items)