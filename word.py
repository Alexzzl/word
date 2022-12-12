from math import floor


def gettext():
    txt = open("201207.txt","r",errors='ignore').read()
    txt = txt.lower()
    for ch in '!"#$&()*+,-./:;<=>?@[\\]^_{|}·~‘’':
        txt = txt.replace(ch,"")
    return txt
txt = gettext()
words = txt.split()
counts = {}
all_word_count = 0
i = 0
num1 = len(words)
for word in words:
    # 词组
    # if(i+1<num1):
    #     word_group = words[i] + ' ' + words[i+1]
    #     # print(word_group)
    #     counts[word_group] = counts.get(word_group,0) + 1
    # i = i + 1
    
    # 单词
    counts[word] = counts.get(word,0) + 1
    all_word_count = all_word_count + 1
items = list(counts.items())
items.sort(key=lambda x:x[1],reverse=True)
num = len(items)
print(num,all_word_count,num1)
file = open('result201207.txt','w')
for i in range(num):
    word,count = items[i]
    percent = round(count * 100 / all_word_count, 4) 
    file.write("{0:<10}{1:>5}   {2:>5}%\n".format(word,count,percent))
    # print("{0:<10}{1:>5}   {2:>5}%".format(word,count,percent))