import xml.etree.ElementTree as ET
myTree = ET.parse('movies.xml')
myroot = myTree.getroot()


#print(myroot[3][1].attrib)
#for x in myroot[0]:
#   print(x.tag,x.attrib,x.text)


for x in myroot.findall('movie'):
    item = x.find('type').text
    print(item)    
    
for x in myroot.iter('description'):
    a=str(x.text)+" Description has been added"
    x.text=str(a)
    x.set('updated','yes')
myTree.write('new.xml')

ET.SubElement(myroot[0],'bollywood')
for x in myroot.iter('bollywood'):
    b='comedy'
    x.text=str(b)
myTree.write('new2.xml')
    