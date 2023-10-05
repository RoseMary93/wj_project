import tkinter as tk

def scroll_text(text, speed):
    window = tk.Tk()  
    window.geometry("500x150")
    window.title("跑馬燈")
    label = tk.Label(window, text=text, font=("Consolas", 24))
    label.pack()
    x = 500   
    y = 50    

    def move_text():
        nonlocal x  
        label.place(x=x, y=y)
        x -= 5  
        if (x+len(text)*1.5*24) < 0: 
            x = 500  
        label.after(speed, move_text)

    move_text()
    window.mainloop()

user_input = "您好，我是琬靜！"
scroll_text(user_input, 50)  