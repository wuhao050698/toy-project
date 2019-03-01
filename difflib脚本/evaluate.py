import difflib


if __name__ == "__main__":
    hd = difflib.HtmlDiff()
    loads = ''
    with open('C:/Users/asus/Desktop/NLP纠错/error.txt', 'r', encoding='gbk') as load1:
        loads = load1.readlines()
        load1.close()
    mem = ''
    with open('C:/Users/asus/Desktop/diff2.txt', 'r', encoding='gbk') as load2:
        mem = load2.readlines()
        load2.close()

    j = 0
    S = [0,0]
    S[0] = 0
    S[1] = 0
    R = [0,0]
    R[0] = 0
    R[1] = 0
    M = [0,0]
    M[0] = 0
    M[1] = 1
    W = [0,0]
    W[0] = 0
    W[1] = 0
    flag = 0
    for i in loads:
        print(i+"1 2"+mem[j]+ str(j))
        if j=="\n":
            if i=="\n":
                j+=1
                continue
            else:
                continue
        if i=="\n":
            while mem[j]!="\n":
                j+=1
            j+=1
            continue
        if i.split(" ")[0] == 'W':
            if i == mem[j]:
                W[0] += 1
                j+=1
                if mem[j]=="\n":
                    continue
            else:
                ppp = 0
                if mem[j].split(' ')[1]>i.split(' ')[1]:
                    W[1] += 1
                else:
                    while mem[j].split(' ')[1]<i.split(' ')[1]:
                        if i==mem[j]:
                            W[0] += 1
                            j+=1
                            if mem[j] == "\n":
                                ppp=1
                                break
                            W[1] -= 1
                            break
                        j += 1
                        if mem[j] == "\n":
                            ppp = 1
                            break
                    if ppp == 1:
                        continue
                    W[1]+=1
        elif i.split(" ")[0]=="S":
            if i == mem[j]:
                S[0] += 1
                j+=1
                if mem[j]=="\n":
                    continue
            else:
                ppp = 0
                if mem[j].split(' ')[1]>i.split(' ')[1]:
                    S[1] += 1
                else:
                    while mem[j].split(' ')[1]<i.split(' ')[1]:
                        if i==mem[j]:
                            S[0] += 1
                            j+=1
                            if mem[j] == "\n":
                                ppp=1
                                break
                            S[1] -= 1
                            break
                        j += 1
                        if mem[j] == "\n":
                            ppp = 1
                            break
                    if ppp == 1:
                        continue
                    S[1]+=1
        elif i.split(" ")[0]=="M":
            if i == mem[j]:
                M[0] += 1
                j+=1
                if mem[j]=="\n":
                    continue
            else:
                ppp = 0
                print(mem[j]+"aaaaa"+i)
                if mem[j].split(' ')[1]>i.split(' ')[1]:
                    M[1] += 1
                else:
                    while mem[j].split(' ')[1]<i.split(' ')[1]:
                        if i==mem[j]:
                            M[0] += 1
                            j+=1
                            if mem[j] == "\n":
                                ppp=1
                                break
                            M[1] -= 1
                            break
                        j += 1
                        if mem[j] == "\n":
                            ppp = 1
                            break
                    if ppp == 1:
                        continue
                    M[1]+=1
        else:
            if i == mem[j]:
                R[0] += 1
                j+=1
                if mem[j]=="\n":
                    continue
            else:
                ppp = 0
                if mem[j].split(' ')[1]>i.split(' ')[1]:
                    R[1] += 1
                else:
                    while mem[j].split(' ')[1]<i.split(' ')[1]:
                        if i==mem[j]:
                            R[0] += 1
                            j+=1
                            if mem[j] == "\n":
                                ppp=1
                                break
                            R[1] -= 1
                            break
                        j += 1
                        if mem[j] == "\n":
                            ppp = 1
                            break
                    if ppp == 1:
                        continue
                    R[1]+=1

