if __name__=="__main__":
    with open('C:/Users/asus/Desktop/NLP纠错/数据集/CGED2017/train.release.xml', 'r', encoding='utf8') as load1:
        loads = load1.readlines()
        load1.close()
    hhh = 0
    fff = 0
    for i in loads:
        fff+=1
        if "ERROR" in i:
            with open('C:/Users/asus/Desktop/NLP纠错/2017data.txt', 'a', encoding='utf8') as fo:
                fo.write(i.split('"')[5]+" "+i.split('"')[1]+" "+i.split('"')[3]+"\n")
        if "</DOC>" in i:
            with open('C:/Users/asus/Desktop/NLP纠错/2017data.txt', 'a', encoding='utf8') as fo:
                hhh+=1
                print(hhh)
                print(fff)
                fo.write("\n")