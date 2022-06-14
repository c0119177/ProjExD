import random
import datetime
def quiz():
    print("問題")
    st = datetime.datetime.now()
    i = random.randint(0, 2)
    data = [["サザエの旦那の名前は？: ", "カツオの妹の名前は？: ", "タラオはカツオから見てどんな関係？: "], 
    ["masuo", "ますお", "マスオ"], 
    ["wakame", "わかめ", "ワカメ"], 
    ["oi", "甥", "おい", "甥っ子", "おいっこ"]]
    a = input(data[0][i])
    if a.lower() in data[i + 1]:
        print("正解")
    else:
        print("出直してこい")
    ed = datetime.datetime.now()
    print("所要時間:" + str((ed - st).seconds) + "秒")

if __name__ == "__main__":
    quiz()