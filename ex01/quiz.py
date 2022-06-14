import random
import datetime
def quiz(i):
    data = [["サザエの旦那の名前は？: ", "カツオの妹の名前は？: ", "タラオはカツオから見てどんな関係？: "], 
    ["masuo", "ますお", "マスオ"], 
    ["wakame", "わかめ", "ワカメ"], 
    ["oi", "甥", "おい", "甥っ子", "おいっこ"]]
    a = input(data[0][i])
    if a.lower() in data[i + 1]:
        return "正解"
    else:
        return "出直してこい"

if __name__ == "__main__":
    print("問題")
    st = datetime.datetime.now()
    print(quiz(random.randint(0, 2)))
    ed = datetime.datetime.now()
    print("所要時間:" + str((ed - st).seconds) + "秒")