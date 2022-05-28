#Поиск зависимостей и запись их в сокращенном виде
def compress(raw):
    r = ""
    while True:
        if raw == []: break
        a = raw[0:3]

        if len(a) == 1:
            r = r + str(a[0])
            del raw[0]
            break

        elif a[0] == a[1]:
            if len(raw) == 2:
                r = r + str(a[0]) + "*" + str(2)
                del raw[0:2]
            for i in range(2, len(raw)):
                if i == len(raw) - 1 and raw[i] == raw[i - 1]:
                    r = r + str(a[0]) + "*" + str(i + 1)
                    del raw[0:i + 1]
                    break
                if raw[i] != raw[i - 1]:
                    r = r + str(a[0]) + "*" + str(i) + ","
                    del raw[0:i]
                    break

        elif len(a) == 3 and a[1] - a[0] == a[2] - a[1]:
            if len(raw) == 3:
                if abs(raw[1] - raw[0]) == 1:
                    r = r + str(a[0]) + "-" + str(raw[2])
                else:
                    r = r + str(a[0]) + "-" + str(raw[2]) + "/" + str(abs(raw[1] - raw[0]))
                del raw[0:3]
            for i in range(3, len(raw)):
                if raw[i] - raw[i - 1] != raw[i - 1] - raw[i - 2]:
                    if abs(raw[i - 1] - raw[i - 2]) == 1:
                        r = r + str(a[0]) + "-" + str(raw[i - 1]) + ","
                    else:
                        r = r + str(a[0]) + "-" + str(raw[i - 1]) + "/" + str(abs(raw[i - 1] - raw[i - 2])) + ","
                    del raw[0:i]
                    break
                else:
                    if i == len(raw) - 1:
                        if abs(raw[i - 1] - raw[i - 2]) == 1:
                            r = r + str(a[0]) + "-" + str(raw[i])
                        else:
                            r = r + str(a[0]) + "-" + str(raw[i]) + "/" + str(abs(raw[i - 1] - raw[i - 2]))
                        del raw[0:i + 1]

        else:
            r = r + str(a[0]) + ","
            del raw[0]

    return r






print(compress([1, 2, 3, 4, 10, 9, 8, 6, 8, 10]))







exit(0)
if len(a) == 3 and a[0] == a[1] - 1 and a[1] == a[2] - 1:
    if len(raw) == 3:
        r = r + str(a[0]) + "-" + str(raw[2])
        del raw[0:3]
    for i in range(3, len(raw)):
        if raw[i] != raw[i - 1] + 1:
            r = r + str(a[0]) + "-" + str(raw[i - 1]) + ","
            del raw[0:i]
            break
        else:
            if i == len(raw) - 1:
                r = r + str(a[0]) + "-" + str(raw[i])
                del raw[0:i + 1]
                break
















def max_ball(v):
    t = 0
    v = v * 1000 / 3600
    g = 9.81
    b =[]
    a = (0, 0)
    while True:
        h = v * t/10 - 0.5 * g * t * t/100
        if h < a[1]: return t-1
        a = (t, h)
        b.append(a)
        t += 1



print(max_ball(50))

exit(0)
def rot13(message):
    a = "abcdefghijklmnopqrstuvwxyz"

    b = []
    for i in message:
        if i in a or i in a.upper():
            c = a.index(i) + 13
            if c > len(a) - 1:
                c = 12 - (a.index("z") - a.index(i))
            b.append(a[c])
        else: b.append(i)
    return "".join(b)



print(rot13("terrakot"))





exit(0)

# НЕ ДОДЕЛАНО !!!!!!!!!!!!!!
def ant_bridge(ants, terrain):
    a = [i for i in ants]
    b = []
    c = len(a)
    for i in range(0, len(terrain) - 1):
        if terrain[i] == "-" and terrain[i + 1] == ".":
            if len(a) < 1:
                b.append(b[0])
                del b[0]
                continue
            b.append(a[-1])
            del a[-1]
        elif terrain[i] == ".":
            if len(a) < 1:
                b.append(b[0])
                del b[0]
                continue
            b.append(a[-1])
            del a[-1]
        elif terrain[i] == "-" and terrain[i - 1] == ".":
            if len(a) < 1:
                b.append(b[0])
                del b[0]
                continue
            b.append(a[-1])
            del a[-1]
        elif terrain[i] == "-" and terrain[i - 1] == "-" and c > len(a):
            a.insert(0, b[0])
            del b[0]
        print(a)
        print(b)

    return "".join(a)


print(ant_bridge("KJIHGFEDCBA", "----....-----------"))



















exit(0)
def best_match(goals1, goals2):
    b ={}
    c = []
    for i in range(0, len(goals1)):
        a = goals1[i] - goals2[i]
        b[i] = a
        c.append(a)
    print(b)
    d = {}
    for key in b:
        if b[key] == min(c):
            d[key] = b[key]
    print(d)
    f = {}
    c = []
    for key in d:
        f[key] = goals2[key]
        c.append(goals2[key])
    for key in f:
        if f[key] == max(c):
            return key





print(best_match([12, 9, 10, 3, 17, 15, 3, 20, 16, 11, 10, 13, 7, 4], [4, 3, 1, 1, 7, 9, 1, 10, 7, 3, 8, 7, 5, 0]))




exit(0)



def rotate_and_remove(arr):
    f = arr
    x = 0
    while x < len(arr):
        c =[]
        for i in range(0, len(f[0])):
            b = []
            for y in range(0, len(f)):
                a = f[y][-(i +1)]
                b.append(a)
            c.append(b)

        for i in c:
            if len(i) == 1:
                return i[0]
            i.remove(max(i))
            i.remove(min(i))

        f = c
        x += 1

print(rotate_and_remove([[3,5,8,4,2],
                   [1,9,2,3,8],
                   [4,6,7,2,2],
                   [7,5,5,5,5],
                   [6,5,3,8,1]]))








exit(0)









def parts_sums(ls):
    s = []
    s1 = sum(ls)
    s.append(s1)
    for i in ls:
        s1 = s1 - i
        s.append(s1)
    return s





print(parts_sums([1, 2, 3, 4, 5, 6]))