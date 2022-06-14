import random
import string
import datetime
origin = 10 #対象文字数
lost = 2 #欠損文字数
Max_ans = 5 #間違えられる回数
def main():
    st = datetime.datetime.now()
    SG = String_Generation()
    print("対象文字:")
    print(" ".join(SG[0]))
    print("欠損文字:")
    print(" ".join(SG[1]))
    print("表示文字:")
    print(" ".join(SG[2]))
    print()
    Question1(SG, Max_ans)
    ed = datetime.datetime.now()
    print(f"所要時間:{(ed - st).seconds}秒")
def String_Generation():
    i = random.sample(string.ascii_uppercase, k = origin)
    j = random.sample(i, k = lost)
    k = random.sample([a for a in i if a not in j], k = origin - lost)
    return i, j, k
def Question1(data, count):
    while True:
        if count == 0:
            print("これ以上やり直しできません。")
            break
        else:
            q1 = input("欠損文字はいくつあるでしょうか？: ")
            if q1 == "2":
                print("正解です。それでは具体的に欠損文字を一つずつ入力してください。")
                Question2(data, count)
                break
            else:
                print("不正解です。またチャレンジしてください。")
                count -= 1
                continue
def Question2(data, count):
    for i in range(lost):
        q2 = input(f"{i + 1}つ目の文字を入力してください: ")
        if q2 in data[1]:
            if i == lost - 1:
                print("すべて正解しました。")
        else:
            print("不正解です。またチャレンジしてください。")
            count -= 1
            Question1(data, count)
            break

if __name__ == "__main__":
    main()