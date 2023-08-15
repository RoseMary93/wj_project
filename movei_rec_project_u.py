from tkinter import *

win = Tk()
win.title("~電影推薦心理程式~")
win.geometry("450x700")
Label(win, text="~電影推薦心理程式~").pack(side="top", anchor="n")

Q1_que = "Q1.若能到世界上的任何一個地方旅遊，你會選擇哪裡？"
Q1_a = [("A. 南極冰原", "A"),("B. 亞馬遜雨林", "B"),("C. 紐約大城市", "C"),("D. 瑞士阿爾卑斯山", "D"),("E. 塔克拉瑪干沙漠", "E"),
         ("F. 法國彩色小鎮", "F"),("G. 古城", "G"),("H. 印度鄉村", "H"),("I. 馬爾地夫海邊", "I"),("J. 義大利的教堂古蹟", "J")]
Q2_que = "Q2.若在旅途的過程中，只能帶一樣東西，你會選擇帶什麼？\n（不用考慮維生需求，不包含錢）"
Q2_a = [("A. 書籍", "A"),("B. 音樂播放機", "B"),("C. 電腦遊戲機", "C"),("D. 心愛的玩偶", "D"),("E. 相機", "E")]
Q3_que = "Q3.到了當地，你最想要的行程安排是什麼？"
Q3_a = [("A. 玩多種極限運動", "A"),("B. 聽歌劇、看電影、欣賞表演", "B"),("C. 參觀展覽與古蹟", "C"),("D. 上山下海盡覽各種美景", "D"),("E. 躺在飯店", "E")]
Q4_que = "Q4.你希望旅程的氛圍怎麼樣？"
Q4_a = [("A. 四處冒險，活力滿滿，探索不同地區的可能性", "A"),("B. 刺激緊張瘋狂，青春就是要不一樣", "B"),
      ("C. 哼著歌、跳著舞，漫步在鄉村田野間", "C"),("D. 帶著自己的另一半與小孩，享受家庭時光", "D"),("E. 一個人坐著火車漂流，緣分便是旅行的最佳註解", "E")]
Q5_que = "Q5.若在路上有人向你招手，你會如何回應？"
Q5_a = [("A. 他看起來神秘且有趣，我要去瞧一瞧", "A"),("B. 和他招手，這個地方的人文風情太友善美麗了", "B"),
      ("C. 注意安全，不隨便回應", "C"),("D. 越壞我越愛哈哈哈哈哈", "D")]
Q6_que = "Q6.若路上有個老人擁有預知能力，並可以告知你一些事情，你希望...？"
Q6_a = [("A. 讓他告訴你未來一年會發生的事", "A"),("B. 讓他告訴你明天會發生的事", "B"),("C. 輕輕的、什麼都不必說", "C")]
Q7_que = "Q7.假如你得知世界末日即將來臨，在最後的日子你想要做什麼？"
Q7_a = [("A. 把握最後的時光和心愛的人待在一起", "A"),("B. 趕快花光所有積蓄，讓自己享受", "B"),("C. 做平常不敢做的犯罪行為", "C"),("D. 不顧一切和世界拼搏，只要不放棄，一定能找到出路", "D")]
Q8_que = "Q8.回到現實，請問你想看線上電影還是院線電影？"
Q8_a = [("A. 線上電影", "線上電影"),("B. 院線電影", "院線電影")]

questions = [{Q1_que:Q1_a, Q2_que:Q2_a, Q3_que:Q3_a},{Q4_que:Q4_a, Q5_que:Q5_a, Q6_que:Q6_a},{Q7_que:Q7_a, Q8_que:Q8_a}]

class Question:
    def __init__(self, question_text, options):
        self.question_text = question_text
        self.options = options
        self.answer_var = StringVar()

def show_next_page(questions):
    for widget in win.winfo_children():
        widget.destroy()
    ans.append([question.answer_var.get() for question in questions])
    show_page(page + 1)
def close_window(xwin):
    xwin.destroy()

def show_page(page_num):
    if page_num < len(questions):
        global page
        page = page_num
        for widget in win.winfo_children():
            widget.destroy()
        frame1 = Frame(win)
        frame1.pack(side="top", anchor="w", padx=50)

        question_objs = []  # 用於存儲每個問題的物件
        for que in questions[page]:   # que: Q1_que:Q1_a / Q2_que:Q2_a / Q3_que:Q3_a
            question_obj = Question(que, questions[page][que])  # 把每一題套入Qusetion類別的架構。 # que: self.question_text (問題), questions[page][que]=Qn_a: self.options (答案)
            question_objs.append(question_obj)  # 把每一題Question加進去
            Label(frame1, text="\n" + question_obj.question_text, wraplength=350, justify='left').pack(side="top", anchor="w")
            for num, check in question_obj.options:
                Radiobutton(frame1, text=num, variable=question_obj.answer_var, value=check, wraplength=350).pack(anchor="w")
        if page_num < len(questions)-1:
            Button(win, text="下一頁", command=lambda: show_next_page(question_objs)).pack()
        elif page_num == len(questions)-1:
            Button(win, text="察看結果(將會開新視窗，請耐心等待幾秒~)", command=lambda: (show_next_page(question_objs), close_window(win))).pack()
    # elif page_num >= len(questions):
    #     frame1 = Frame(win)
    #     frame1.pack(side="top", anchor="w", padx=50)
    #     Label(frame1, text="測驗完成，點擊下方按鈕拿看結果。").pack(side="top", anchor="w")
    #     Button(frame1, text="察看結果(需耐心等待幾秒~)", command=lambda: close_window(win)).pack(side="top", anchor="w")

ans = []
page = 0

show_page(page)
win.mainloop()

merge_ans = []
for lst in ans:
    merge_ans.extend(lst)  # 利用.extend(list)拆開多個list，加入物件至新的list中 
print(merge_ans)

冒險,科幻,奇幻,劇情,犯罪,恐怖,懸疑驚悚,喜劇,愛情,溫馨家庭,動畫,戰爭,音樂歌舞,歷史傳記,紀錄片,勵志,武俠,影展=0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0
a1 = merge_ans[0]
if a1 == "A" or a1 =="B":  
    冒險+=1
    奇幻+=1
elif a1 == "C" :
    音樂歌舞+=1
    劇情+=1 
    愛情+=1 
    紀錄片+=1 
    勵志+=1 
    影展+=1
elif a1 =="D":
    音樂歌舞+=1 
    勵志+=1 
    劇情+=1
elif a1 =="E":
    冒險+=1  
    奇幻+=1  
    恐怖+=1 
elif a1 =="F":
    動畫+=10
    喜劇+=1
    奇幻+=1 
    溫馨家庭+=1
    音樂歌舞+=1
elif a1 =="G":
    冒險+=1 
    武俠+=10 
    奇幻+=1
elif a1 =="H":
    冒險+=1  
    劇情+=1  
    紀錄片+=1 
elif a1 == "I":
    愛情+=1
    劇情+=1
    喜劇+=1
elif a1 =="J":
    劇情+=5 
    歷史傳記 +=1
    紀錄片+=1 
    影展+=1
    
a2 = merge_ans[1]
if a2 == "A":
    劇情+=7 
    科幻+=1
    歷史傳記+=1
    動畫+=5
elif a2 == "B" :
    音樂歌舞+=10
    愛情+=3
elif a2 == "C" :
    冒險+=1
    科幻+=1
    奇幻+=1
    犯罪+=1
    恐怖+=1
    懸疑驚悚+=1
elif a2 =="D":
    愛情+=5
    溫馨家庭+=10
elif a2 =="E":
    紀錄片+=10
    影展+=10
    
a3 = merge_ans[2]
if a3 == "A":
    冒險+=5
    恐怖+=5 
    科幻+=2
    奇幻+=3
elif a3 == "B":
    音樂歌舞+=8
    紀錄片+=3
    愛情+=3
    影展+=5
    劇情+=5
elif a3 =="C":
    歷史傳記+=20
    影展+=5
    紀錄片+=5
elif a3 =="D":
    冒險+=3
    喜劇+=3
    愛情+=3
    科幻+=2
elif a3 =="E":
    愛情+=7
    喜劇+=5
    溫馨家庭+=3

a4 = merge_ans[3]
if a4 == "A":
    冒險+=2
    奇幻+=2
    科幻+=3
elif a4 == "B" :
    戰爭+=5
    冒險+=1
    恐怖+= 3
    懸疑驚悚+= 2
elif a4 == "C" :
    音樂歌舞+=10
    喜劇+=5
    劇情+=2 
elif a4 =="D":
    愛情+=5
    喜劇+=5
elif a4 =="E":
    劇情+=5
    影展+=7
    紀錄片+=2

a5 = merge_ans[4]
if a5 == "A":
    冒險+=1 
    奇幻+=1
elif a5 == "B" :
    音樂歌舞+=1
    喜劇+=4
elif a5 == "C" :
    劇情+=3
elif a5 == "D" :
    犯罪+= 5
    恐怖+= 5
    懸疑驚悚+= 5
    
a6 = merge_ans[5]
if a6 == "A":
    冒險+=1 
    奇幻+=1
elif a6 == "B" :
    愛情+=1
elif a6 == "C" :
    喜劇+=1
    音樂歌舞+=1 

a7 = merge_ans[6]
if a7 == "A":
    喜劇+=1 
    愛情+=1
    溫馨家庭+=1
elif a7 == "B" :
    音樂歌舞+=1
    喜劇+=3
elif a7 == "C" :
    犯罪+= 30
    恐怖+= 10
    懸疑驚悚+= 10
elif a7 == "D" :
    勵志+=5
    冒險+=1
    戰爭+=1

type1 = merge_ans[7]

movie_tag0=[冒險,科幻,奇幻,劇情,犯罪,恐怖,懸疑驚悚,喜劇,愛情,溫馨家庭,動畫,戰爭,音樂歌舞,歷史傳記,紀錄片,勵志,武俠,影展]
dict1={"冒險":冒險,"科幻":科幻,"奇幻":奇幻,"劇情":劇情,"犯罪":犯罪,"恐怖":恐怖,"懸疑驚悚":懸疑驚悚,
       "喜劇":喜劇,"愛情":愛情,"溫馨家庭":溫馨家庭,"動畫":動畫,"戰爭":戰爭,
       "音樂歌舞":音樂歌舞,"歷史傳記":歷史傳記,"紀錄片":紀錄片,"勵志":勵志,"武俠":武俠,"影展":影展}
favorite_score1=max(movie_tag0)
favorite_tag1=get_key(dict1,favorite_score1)
dict1[favorite_tag1]=0
movie_tag0.sort()
movie_tag0.pop(-1)  # 把最大的移除
favorite_score2=max(movie_tag0)
favorite_tag2=get_key(dict1,favorite_score2)
dict1[favorite_tag2]=0
movie_tag0.pop(-1)
favorite_score3=max(movie_tag0)
favorite_tag3=get_key(dict1,favorite_score3)
dict1[favorite_tag3]=0

tag1t=favorite_tag1
tag2t=favorite_tag2
tag3t=favorite_tag3
# print("tags:", tag1t, tag2t, tag3t)

from bs4 import BeautifulSoup as bs
import requests
import random
headers={
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36"
}

def movie_tag(x):
    url=x
    headers={
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36"
    }
    res=requests.get(url,headers=headers)
    soup = bs(res.text, 'lxml')
    div_items = soup.find_all('div', '_slickcontent')
    title_list=[]
    for ele in div_items:
        title=ele.h2.text.strip()
        website=ele.select("a")[0]["href"]  
        title_list.append({title:website})
    return title_list

def find_movie_website(taglist,name):
    for i in taglist:
        if name in i:
            return(i.get(name,"not found"))


## 將 same_tag_movie()內容換成包含tag的list。
def same_tag_movie(tag_list):   # 依照排序選
    same_tag_movie_list=[]
    for i in tag_list[0]:
        if i in tag_list[1]:
            if i in tag_list[2]:
                same_tag_movie_list.append(i)  # 0.1.2
            else:
                same_tag_movie_list.append(i)  # 0.1
        if i in tag_list[2]:
            same_tag_movie_list.append(i)    # 0.2
    if same_tag_movie_list==[]:
        for i in tag_list[1]:
            if i in tag_list[2]:
                same_tag_movie_list.append(i)    # 1.2
    if same_tag_movie_list==[]:
        for i in tag_list[0]:
            same_tag_movie_list.append(i)      # 0
    if same_tag_movie_list==[]:
        for i in tag_list[1]:
            same_tag_movie_list.append(i)      # 1
    if same_tag_movie_list==[]:
        for i in tag_list[2]:
            same_tag_movie_list.append(i)      # 2
    return same_tag_movie_list


def choose_movie(same_tag_movie):
    choose=random.choice(same_tag_movie)
    return choose

def movie_details(web):
    url=web
    headers={
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36"
    }
    res=requests.get(url,headers=headers)
    soup = bs(res.text, 'lxml')

    div_items = soup.find_all('div', {"class":"movie_intro_info_r"})

    result=[]
    
    for ele in div_items:
        title=ele.find("h1").text.strip().split("\n")[0]  
        entitle=ele.find("h3").text.strip()
        tag=ele.find_all("div", {"class":"level_name"})
        tag_list=[]
        for elem in tag:
            tags=elem.select("a")[0].text.strip()
            tag_list.append(tags)
        details=ele.find_all("span")
        for i in range(0,5):
            x = details[i].text.strip()
            if "播出日期" in x:
                exp_date=x.replace("播出日期：","")
                break
            elif "上映日期" in x:
                exp_date=x.replace("上映日期：","")
                break
            else: 
                exp_date="未提供"
                i+=1
        for i in range(0,5):
            x = details[i].text.strip()
            if "片" in x:
                movie_duration=x.replace("片　　長：","")
                break
            else: 
                movie_duration="未提供"
                i+=1
        for i in range(0,5):
            x = details[i].text.strip()
            if "發行公司" in x:
                company=x.replace("發行公司：","")
                break
            else: 
                company="未提供"
                i+=1
        for i in range(0,5):
            x = details[i].text.strip()
            if "IMDb" in x:
                IMDb_score=x.replace("IMDb分數：","")
                break
            else: 
                IMDb_score = "未提供"
                i+=1
    div_items2 = soup.find_all('div',{"id":"container"}, {"class":"content_c"})
    for ele in div_items2:    
        platform=ele.find("div",{"class":"evaluate_txt_finish"}).text.strip()
    story= soup.find('div', {"class":"gray_infobox_inner"}).find('span', {"id":"story"}).text.strip()

    result.append({
        "title":title,
        "entitle":entitle,
        "tag_list":tag_list,
        "exp_date":exp_date,
        "movie_duration":movie_duration,
        "company":company,
        "IMDb_score":IMDb_score,
        "platform":platform,
        "story":story
    })
    return(result)

# print(movie_details(c_movie_web))
def outside_net(movie):
    detail=movie_details(movie)[0]
    platform=detail.get("platform")
    plat_dict={"Disney+":"https://www.disneyplus.com/zh-tw",
               "Netflix":"https://www.netflix.com/tw/",
               "Apple TV+":"https://www.apple.com/tw/apple-tv-plus/"}
    if platform in plat_dict:
        return("現在就去："+platform+"\n"+plat_dict.get(platform))

### 開始跑程式

movie_tag_id={"動作":1,"冒險":2,"科幻":3,"奇幻":4,"劇情":5,"犯罪":6,"恐怖":7,"懸疑驚悚":8,"喜劇":9,"愛情":10,
              "溫馨家庭":11,"動畫":12,"戰爭":13,"音樂歌舞":14,"歷史傳記":15,"紀錄片":16,"勵志":17,"武俠":18,"影展":19}
movie_type={"院線電影":0,"線上電影":2}

## 找出符合標籤的電影及其網址
tag_t_list=[tag1t,tag2t,tag3t]
movies_list=[movie_tag("https://movies.yahoo.com.tw/category.html?genre_id={x}&type_id={y}&sort=popular".format(x=movie_tag_id.get(tag1t),y=movie_type.get(type1))),\
         movie_tag("https://movies.yahoo.com.tw/category.html?genre_id={x}&type_id={y}&sort=popular".format(x=movie_tag_id.get(tag2t),y=movie_type.get(type1))),\
         movie_tag("https://movies.yahoo.com.tw/category.html?genre_id={x}&type_id={y}&sort=popular".format(x=movie_tag_id.get(tag3t),y=movie_type.get(type1)))]
same_tag_movie=same_tag_movie(movies_list)

choose=choose_movie(same_tag_movie)
for i in choose:
    c_movie=i   # 推薦的電影名稱
c_movie_web=choose.get(c_movie) # 推薦的電影網址

detail=movie_details(c_movie_web)[0]
# print("電影細節：\n","\n電影名稱： {ch} ({en})".format(ch=detail.get("title"),en=detail.get("entitle")),"\n電影年份：",detail.get("year"),"\n播出日期：",detail.get("exp_date"),"\n電影片長：",detail.get("movie_duration"),"\n發行公司：",detail.get("company"),"\nIMDb分數：",detail.get("IMDb_score"),"\n","\n劇情簡介：",detail.get("story"),"\n")
outside_net(c_movie_web)

win0 = Tk()
win0.title("Movie Recommendation")
win0.geometry('700x700')

# Label(win0, text="Your answer: " + str(favorite_tag1)+ str(favorite_tag2)+ str(favorite_tag3)).pack()
Label(win0, text="  此程式由 闕琬靜、周榆庭、何幸佳 共同製作，感謝您的使用~").pack(side="top",anchor="w",)
Label(win0, text="\n專屬推薦電影：").pack(side="top",anchor="n",)
電影名稱="\n電影名稱： {ch} ({en})".format(ch=detail.get("title"),en=detail.get("entitle"))
播出日期="播出日期："+detail.get("exp_date").replace("播出日期：","")
電影片長="電影片長："+detail.get("movie_duration")
發行公司="發行公司："+detail.get("company")
IMDb分數="IMDb分數："+detail.get("IMDb_score")
劇情簡介="\n劇情簡介：\n"+detail.get("story")

Label(win0, text=電影名稱,wraplength=650).pack()
Label(win0, text=播出日期).pack()
Label(win0, text=電影片長).pack()
Label(win0, text=發行公司).pack()
Label(win0, text=IMDb分數).pack()
Label(win0, text=劇情簡介,wraplength=650, justify='left').pack(side="top")
Label(win0, text=outside_net(c_movie_web)).pack()

win0.mainloop()