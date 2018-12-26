#-*-coding:utf-8-*-
import csv
import sys
reload(sys)
sys.setdefaultencoding('utf8')

def write(words):
    table = open('./data/table.csv','a')
    write = csv.writer(table)
    write.writerow(words)
    table.close()

def searchInTable(keyword):
    print "--- searching in table ---"
    table = open('./data/table.csv','r')
    reader = csv.reader(table)
    for line in reader:
        if reader.line_num == 1:
            continue
        if line[0] == keyword:
            return line[1]
    table.close()
    return False

def searchInBook(keyword):
    book = './data/JourneyToTheWest.txt'
    bookObj = open(book,'r')
    print "--- searching in book ---"
    for line in bookObj:
        if keyword in line:
            return line


def addText(keyword, sentence):
    return '说到 "'+keyword+'" ，我就想起 "'+sentence+'" ，明年年初，中美合拍的西游记即将正式开机，我扮演美猴王孙悟空，我会用美猴王艺术形象努力创造一个正能量的形象，文体两开花，希望大家多多关注。'


        


def generator(keyword):
    print keyword

    try:
        sentence= searchInTable(keyword)
        if sentence:
            return addText(keyword,sentence)
        paragraph = searchInBook(keyword)
        sentences = paragraph.split("。")
        for sentence in sentences:
            if(keyword in sentence):
                write([keyword, sentence])
                return addText(keyword,sentence)
        return addText(keyword,"西游记")
    except e: 
        print e

while True:
    try:
        keyword = raw_input("请输入关键词:")
        print generator(keyword)
    except e: 
        print "出了一点小问题， 换个词试试看吧！"
