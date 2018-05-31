
fo = open("a.txt", "r+", encoding='utf_16_le')# ,encoding='latin-1'
i = 100
while i:
    str_r = fo.readline()[:-1]
    word = ''
    str_len = len(str_r)
    index = 0
    begin = False
    while str_len-index:# '【'
        if str_r[index] == '】'[0]:
            break
        if begin:
            word = word + str_r[index]
        if str_r[index] == '【'[0]:
            begin = True
        index = index +1
    if len(word) > 1:
        print ("读取的字符串是 : ", word)
    i = i -1
fo.close()






    
    # 查找当前位置
    # position = fo.tell()
    # print ("当前文件位置 : ", position)
    # 把指针再次重新定位到文件开头
    # position = fo.seek(0, 0)
    # str_r = fo.read(100)#.decoder('utf_16_le')
    # print ("重新读取字符串 : ", str_r)