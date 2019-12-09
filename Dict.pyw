import json
from difflib import get_close_matches
import tkinter as tk


def find(word):
    word = word.lower()
    data = json.load(open(r"data.json","r"))
    if word in data:
        return data[word]
    elif len(get_close_matches(word,data.keys()))>0:
        word_n = get_close_matches(word,data.keys())[0]
        t1.delete("1.0",tk.END)
        
        def yes():
            b2.place_forget()
            b3.place_forget()
            ans = find(word_n)
            t1.delete("1.0",tk.END) 
            if type(ans) == list:
                for items in ans:
                    t1.insert(tk.END,"\n"+items)
            else:
                t1.insert(tk.END,ans)


        b2 = tk.Button(window,text="Y",command = yes)
        b2.place(relx=0.4,rely=0.7)

        def no():
            
            t1.delete("1.0",tk.END)
            t1.insert(tk.END,"Word doesnot exists")
            b2.place_forget()
            b3.place_forget()

        b3 = tk.Button(window,text="N",command=no)
        b3.place(relx=0.2, rely=0.7)
        
        return "Did you mean %s instead? " %word_n + " Press Y for yes and N for no: "
        

def Search():
    word = text.get()
    ans = find(word)
    t1.delete("1.0",tk.END) 
    if type(ans) == list:
        for items in ans:
            t1.insert(tk.END,"\n"+items)
    else:
        t1.insert(tk.END,ans)
    
window = tk.Tk()

text = tk.StringVar()
e1 = tk.Entry(window,textvariable=text)
e1.grid(row=0,column =0)

b1 = tk.Button(window,text="Search", command =Search)
b1.grid(row=0,column=1)


t1 = tk.Text(window,width=40,height=10)
t1.grid(row=1,column=0, ipadx=10,ipady=10,columnspan=2)

window.mainloop()
