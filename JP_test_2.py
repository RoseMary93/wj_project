import pandas as pd

class QuizApp:
    def __init__(self, csv_file):
        self.csv_file = csv_file

    def run(self):
        df = pd.read_csv(self.csv_file)

        print("[日文測驗小程式]")
        print("模式說明：\n CH：日文出題，猜想中文意思。\n JP：中文出題，猜想日文單字。")
        mode = input("請選擇模式（CH或JP）：")
        n = int(input("請輸入題目數量(1~100)："))
        print("開始測驗！出題後按Enter會顯示答案。")

        sampled_data = df.sample(n)

        for index, row in sampled_data.iterrows():
            CH = row['中文']
            JP = row['日文']
            if mode == "JP":
                print(f"中文: {CH}")
                x = input()
                print(f"日文:\n{JP}")
                print("==============")
            if mode == "CH":
                print(f"日文:\n{JP}")
                x = input()
                print(f"中文: {CH}")
                print("==============")
        print("\n 測驗結束。")

def main():
    csv_file = "N3words.csv"
    app = QuizApp(csv_file)
    app.run()

if __name__ == "__main__":
    main()