import pandas
import numpy
import xml.etree.cElementTree as etree
def Text(file):
    xmlDoc = open(file, 'r')
    xmlDocData = xmlDoc.read()
    xmlDocTree = etree.XML(xmlDocData)
    paragraph_text=''
    for paragraph in xmlDocTree.iter('PARAGRAPH'):
        paragraph_text +="new_para "+str(paragraph.text.encode('utf-8'))



    import lxml.etree
    root = lxml.etree.fromstring(xmlDocData)
    results = root.findall('SUB_CHAPTER')
    sub_chapter_heading = [r.find('HEADING').text for r in results]


    root = lxml.etree.fromstring(xmlDocData)
    result_s = root.findall('SUB_CHAPTER/SUB_SUB_CHAPTER')
    topic_heading = [r.find('HEADING').text for r in result_s]


    activity_text=''
    for activity in xmlDocTree.iter('ACTIVITY'):
        activity_text +="Activity "+str(activity.text.encode('utf-8'))


    question_text=''
    for question in xmlDocTree.iter('QUESTION'):
        question_text +="Question "+str(question.text.encode('utf-8'))


    solution_text=''
    for solution in xmlDocTree.iter('SOLUTION'):
        solution_text +="solution "+str(question.text.encode('utf-8'))


    heading_text=''
    for heading in xmlDocTree.iter('HEADING'):
        heading_text +="Headings "+str(heading.text.encode('utf-8'))

    table_text=''
    for content in xmlDocTree.iter('CONTENTS'):
        table_text +="table_text "+str(content.text.encode('utf-8'))



    chapter_text=  paragraph_text+activity_text+question_text+heading_text+table_text
    
    #k = topic_heading+sub_chapter_heading
    
    text_file = open("/home/anvesha/Desktop/Nextstep/chapter12_txt.txt", "w")
    text_file.write("Chapter: %s" % chapter_text)
    text_file.close()
    return topic_heading+sub_chapter_heading

ch12=Text('/home/anvesha/Desktop/Nextstep/XML_FILES/CHAPTER 12.xml')
print ch12
ch1=Text('/home/anvesha/Desktop/Nextstep/XML_FILES/CHAPTER 1.xml')
print ch1