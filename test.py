# 16.请将字符 `name = "wupeiqi"` 翻转。
# name = "wupeiqi"
# name_new = []
# result = ""
# for index in range(len(name)):
#     name_new.insert(0, name[index])
# result = str(name_new)
# print(result)

# 17.bin()
# 18.break是终止循环，continue是跳到下一次循环
# 19. v1 = (1,2,3), v2 = {"k1":"v1"}
# 20.
# info = [
#     {'k1': (1), 'k2': {'k9': 'luffy', 'k10': '武沛齐'}},
#     (11, 22, 33, 44),
#     {199, 2, 3, 4, 5},
#     True,
#     ['李杰', 'alex', {'extra': ("alex", [18, 20], 'eric')}]
# ]
# print(info[0]["k2"]["k9"])
# print(info[1][3])
# del info[0]["k2"]["k10"]
# print(info)
# info[4][2]["name"] = "wupeiqi"
# info[2].add("北京")
# print(info)
# info[3] = "真"
# print(info)
# info[4][2]['extra'][1].insert(0,666)
# print(info)

# 25 写代码实现，循环提示用户输入内容（Q或q终止），并将内容用 "_" 连接起来。
# text = ""
# while True:
#     text_input = input("请输入内容（按Q终止）：")
#     if text_input.upper() == "Q":
#         break
#     text = text + "_" + text_input
# print(text[1:])

# 26

# 27 # 根据以上代码获取各省车牌数量，例如：info = {"沪":2,"京":2 ...}
# car_list = ['鲁A32444', '沪B12333', '京B8989M', '京C49678', '黑C46555', '晋B25041', '沪C34567']
# result = {}
# data_list = []
# num = 1
# for index in range(len(car_list)):
#     data_list.append(car_list[index][0])
# print(data_list)
# for index_list in range(len(data_list)):
#     result[data_list[index_list]] = data_list.count(data_list[index_list])
# print(result)

# 28
# text = """id,name,age,phone,job
# 1,alex,22,13651054608,IT
# 2,wusir,23,13304320533,Tearcher
# 3,老男孩,18,1333235322,IT"""

# 29
# content = input("请输入内容：")
# result = 1
# num_list = content.split("*")
# for num in num_list:
#     result = result * int(num)
# print(result)


# # # 30
# for i in range(1, 10):
#     for j in range(1, i + 1):
#         text = "{}*{}".format(i,j)
#         print(text, end=" ")
#     print("")


# 31
import random
result = {}
user_list = ["alex", "武沛齐", "李路飞"]
# 生成一副扑克牌
total_poke_list = [("小王", 14),("大王", 15)]
color_list = ["红桃", "黑桃", "方块", "梅花"]
num_list = [1,2,3,4,5,6,7,8,9,10,11,12,13]
for color in color_list:
    for num in num_list:
        item = (color, num,)
        total_poke_list.append(item)

# 发牌前的判断
for user in user_list:
    score = 0
    while True:
        choice = input("是否给{}发牌(Y/N)？".format(user))
        choice = choice.upper()

        if choice not in {"Y", "N"}:
            print("输入错误，请重新输入。")
            continue

        if choice == "N":
            print("{}不要拍了".format(user))
            break

# 具体发牌过程
        index = random.randint(0,len(total_poke_list) -1)
        poke = total_poke_list.pop(index)
        value = poke[1]
        if poke[1] > 10:
            value = 0.5
        score = score + value
        print("给{}发的牌：{}{}，此刻所有牌面值总和:{}".format(user, poke[0], poke[1], score))

        if score > 11:
            print("用户{}爆了".format(user))
            score = 0
            break

    result[user] = score

print(result)

