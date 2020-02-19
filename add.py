import os
def match(dir) :
    if dir == "AD" :
        return "机场细则:"
    elif dir == "AOC" :
        return "机场障碍物图:"
    elif dir == "ADC" :
        return "机场图:"
    elif dir == "APDC" :
        return "停机位图:"
    elif dir == "FDA" :
        return "其他:"
    elif dir == "IAC" :
        return "仪表进近图:"
    elif dir == "SID" :
        return "标准仪表离场图:"
    elif dir == "STAR" :
        return "标准仪表进近图:"
    elif dir == "PATC" :
        return "精密进近地形图:"
    else :
        return "其他:"
fir = "ZSHA"
por = "ZSAM"
name = "厦门高崎国际机场"
str = fir+"\\"+por
mulu = []
fil = []
filename = "0"
extension = "0"
print("<h4>"+por+"</h4>")
print("<p class=\"tag\">"+name+"</p>")
for root,dirs,files in os.walk("F:\\Users\\18210\\Documents\\eAIP\\chartfinder\\"+str) : 
    for dirn in dirs :
        print("<p class=\"tag\">"+match(dirn)+"</p>")
        for n,t,pdfs in os.walk("F:\\Users\\18210\\Documents\\eAIP\\chartfinder\\"+str+"\\"+dirn) :
            cout = 0
            for pdf in pdfs :
                filename,extension = os.path.splitext(pdf)
                cout = cout + 1
                if cout == 2 :
                    print(count+"&nbsp;&nbsp;<a href=\""+"./"+por+"/"+dirn+"/"+pdf+"\">"+filename+"</a></p>")
                    cout = 0
                else :
                    count = "<p class=\"tag\"><a href=\""+"./"+por+"/"+dirn+"/"+pdf+"\">"+filename+"</a>"
            if cout == 1 :
                print(count+"</p>")
