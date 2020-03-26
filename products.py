import os
products = []
# 找尋是否有檔案
if os.path.isfile("products.csv"):
    print("找到檔案")
    # 讀取檔案
    with open("products.csv", "r", encoding="utf-8") as f:
        for line in f:
            if "商品,種類,價格" in line:
                continue
            name, kind, price = line.strip().split(",")
            products.append([name, kind, price])
    # 印出檔案內資料
    print(products)
else:
    print("找不到檔案......")
# 輸入商品
while True:
    name = input("輸入名稱:")
    print("離開輸入:q")
    if name == "q":  # quit
        break
    kind = input("請輸入食品種類:")
    price = int(input("請輸入價格:"))
    products.append([name, kind, price])
# 印出購買紀錄
for p in products:
    print("商品:", p[0], "種類:", p[1], "價格:", p[2])
# 存入檔案
with open("products.csv", "w", encoding='utf-8') as f:
    f.write("商品,種類,價格\n")
    for p in products:
        f.write(p[0]+","+p[1]+","+str(p[2])+"\n")
