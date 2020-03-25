products = []
price = []
kind = []
while True:
    name = input("輸入名稱:")
    print("離開輸入:q")
    if name == "q":  # quit
        break
    kind = input("請輸入食品種類:")
    price = int(input("請輸入價格:"))
    products.append([name, kind, price])

with open("products.csv", "w", encoding='utf-8') as f:
    f.write("商品,種類,價格\n")
    for p in products:
        f.write(p[0]+","+p[1]+","+str(p[2])+"\n")
        print("商品:", p[0], "種類:", p[1], "價格:", p[2])
