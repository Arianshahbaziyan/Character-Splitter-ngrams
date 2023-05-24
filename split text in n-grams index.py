import arabic_reshaper
from bidi.algorithm import get_display   
path = "text.txt"
text=list()
n_grams = dict()
o_char = str()
value = int()
mean = float()
banned_list =[".","(",")",",",":","-","_","+","[","]","1","2","3","4","5","6","7","8","9","0","?","!","/"]
n = int(input(get_display(arabic_reshaper.reshape("  : متن به چند گرمی تقسیم شود  "))))
#____________opening the file and read the text___________________
with open(path,"r") as f:
    lines = f.readlines()
    for i in range(len(lines)):
        text.extend(lines[i].split(" "))
    f.close()
#__________spiliting the words in 2 grams_____________________
for j in text:
    if len(j) >= 2:
        for char in j.lower():
            o_char = o_char +  char
            if len(o_char) == n and o_char[0] not in banned_list and o_char[1] not in banned_list and o_char != "\n":
                if o_char not in n_grams:
                    n_grams[o_char] = 1
                else:
                    value = n_grams[o_char]+1
                    n_grams.update({o_char: value})
                    value=0
                o_char = o_char[1]
            else:
                pass
    else:
        pass
    o_char=""

print("\n",get_display(arabic_reshaper.reshape("تمام 2 گرمی های غیر نکراری داخل متن به تفکیک و تعداد هرکدام:")),"\n",n_grams)
print("----------------------------------------------------------------")
value = n_grams.values();mean = sum(value)/len(value)
print(len(lines),get_display(arabic_reshaper.reshape("تعداد خطوط متن ورودی:  ")))
print(len(text),get_display(arabic_reshaper.reshape("تعداد کلمات داخل متن: ")))
print(len(value),get_display(arabic_reshaper.reshape ("تعداد کل دو گرمی های غیر نکراری پیدا شده در متن: ")))
print(mean,get_display(arabic_reshaper.reshape ("میانگین تکرار دو گرمی های پیدا شده در متن:  ")),"\n")
        
        

