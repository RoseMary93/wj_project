import tkinter as tk

def scroll_text(text, speed):
    window = tk.Tk()              # 建立視窗、設定大小。
    window.geometry("500x150")
    window.title("跑馬燈")
	# 建立label來包裝文字。
    label = tk.Label(window, text=text, font=("Consolas", 24))
    label.pack()
	# 設定文字起始位置
    x = 500    # 設置在GUI邊界，使文字從最右邊跑出來
    y = 50     # 設定文字高度

    def move_text():
        nonlocal x  # 促使function外的x數值能被改變
        label.place(x=x, y=y)
        x -= 5  # 每次向左移動5單位，若加大數字可使移動變快
        if (x+len(text)*1.5*24) < 0:  # 字體大小24(中文字*1.5左右)
            x = 500           # 當所有字都到達最左邊，重新再跑
		# 當經過speed (毫秒)後，label執行move_text()功能
		# 也就是說，每n毫秒label的文字會左移5單位。
        label.after(speed, move_text)

    move_text()
    window.mainloop()

# user_input = input("請輸入要顯示的文字：")
user_input = "您好，我是琬靜！"
scroll_text(user_input, 50)  # 設定50毫秒向左移一次