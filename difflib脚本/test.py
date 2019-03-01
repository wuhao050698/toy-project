import difflib
import sys
if __name__=="__main__":
    hd = difflib.HtmlDiff()
    loads = ''
    with open('C:/Users/asus/Desktop/NLP纠错/error.txt', 'r', encoding='gbk') as load1:
        loads = load1.readlines()
        load1.close()
    mem = ''
    with open('C:/Users/asus/Desktop/diff2.txt', 'r', encoding='gbk') as load2:
        mem = load2.readlines()
        load2.close()
    # tex1 = """hhhh
    # 23333
    # 66666
    # """
    # tex1_lines = tex1.split   lines()
    # tex2 = """hhhh
    # 2333
    # 5555
    # """
    # tex2_lines = tex2.splitlines()
    # d = difflib.HtmlDiff()
    # q = d.make_file(tex1_lines, tex2_lines)
    # old_str = 'charset=ISO-8859-1'
    # new_str = 'charset=UTF-8'
    with open('C:/Users/asus/Desktop/diff4.html', 'w' , encoding='utf8') as fo:
        fo.write(hd.make_file(loads,mem))
        print("out!")
        fo.close()