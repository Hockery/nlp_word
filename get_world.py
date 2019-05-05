
fo = open("dict_ch.txt", "r+", encoding='utf_16_le')# ,encoding='latin-1'
# i = 100
word_num = 0
word_l = []
key_num = 0
key_l = {}
key_lt = []
str_r = fo.readline()
while not (str_r==''):
    word = ''
    str_r = str_r[:-1]
    str_len = len(str_r)
    index = 0
    begin = False
    while str_len-index:# '【'
        if str_r[index] == '】':
            break
        if begin:
            word = word + str_r[index]
        if str_r[index] == '【':
            begin = True
        index = index +1
    if len(word) > 1:
        word_num  += 1
        # print ("[%05d]: "%(word_num), word)
        word_l.append(word)
    elif len(word) == 1 and word not in key_lt:
        key_num += 1
        key_lt.append(word)
        # print ("[%05d]: "%(key_num), word)
    str_r = fo.readline()
    # i = i -1

print(key_lt, word_l)
for ind, w in enumerate(word_l) :
    for wt in w: 
        if wt not in key_l:
            key_l[wt] = [ind]
        else:
            key_l[wt].append(ind)

print(key_l)
fo.close()






    
    # 查找当前位置
    # position = fo.tell()
    # print ("当前文件位置 : ", position)
    # 把指针再次重新定位到文件开头
    # position = fo.seek(0, 0)
    # str_r = fo.read(100)#.decoder('utf_16_le')
    # print ("重新读取字符串 : ", str_r)