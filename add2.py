import os
por = "AMD"
mulu = []
fil = []
filename = "0"
extension = "0"
count = ""
cout = 0
print("<h4>"+por+"</h4>")
for pdf in os.listdir("F:\\Users\\18210\\Documents\eAIP\\chartfinder\\OTHER"):
    filename,extension = os.path.splitext(pdf)
    cout = cout + 1
    if cout == 2 :
        print(count+"&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<a href=\""+"./OTHER/"+pdf+"\">"+filename+"</a></p>")
        cout = 0
    else :
        count = "<p class=\"tag\"><a href=\"./OTHER/"+pdf+"\">"+filename+"</a>"
if cout == 1 :
    print(count+"</p>")
