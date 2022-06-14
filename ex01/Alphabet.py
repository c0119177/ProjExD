import random
import string
import datetime
origin = 10 #対象文字数
lost = 2 #欠損文字数
Max_ans = 5 #間違えられる回数
def main():
    st = datetime.datetime.now()
    for i in range(Max_ans):
        SG = String_Generation()
        print("対象文字:")
        print(" ".join(SG[0]))
        print("欠損文字:")
        print(" ".join(SG[1]))
        print("表示文字:")
        print(" ".join(SG[2]))
        print()
        q1 = Question1(SG)
        if q1 == 0:
            print("不正解です。またチャレンジしてください。")
            print("------------------------------------------")
            break
        else:
            q2 = Question2(SG)
            if q2 == 1:
                break
        if i == Max_ans - 1:
            print("これ以上やり直しできません。")
    ed = datetime.datetime.now()
    print(f"所要時間:{(ed - st).seconds}秒")
def String_Generation():
    i = random.sample(string.ascii_uppercase, k = origin)
    j = random.sample(i, k = lost)
    k = random.sample([a for a in i if a not in j], k = origin - lost)
    return i, j, k
def Question1(data):
    q1 = input("欠損文字はいくつあるでしょうか？: ")
    if q1 == "2":
        print("正解です。それでは具体的に欠損文字を一つずつ入力してください。")
    else:
        return 0
def Question2(data):
    for i in range(lost):
        q2 = input(f"{i + 1}つ目の文字を入力してください: ")
        if q2 in data[1]:
            data[1].remove(q2)
            if i == lost - 1:
                print("すべて正解しました。")
                return 1
        else:
            print("不正解です。またチャレンジしてください。")
            print("------------------------------------------")
            break

if __name__ == "__main__":
    main()