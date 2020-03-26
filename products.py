import os
day = input("請輸入年月日星期:")


# 讀取檔案
def read_file(filename):
    products = []
    with open(filename, "r", encoding="utf-8") as f:
        for line in f:
            if "號碼,商品,種類,價格,數量" in line:
                continue  # 號碼,商品,種類,價格,數量跳過
            num, name, kind, price, quantity = line.strip().split(",")
            products.append([num, name, kind, price, quantity])
        # 印出檔案內資料
    print(products)
    return products


# 輸入商品
def user_input(products):
    num = int(input("請輸入順序:"))
    while True:
        name = input("輸入名稱:")
        if name == "q":  # quit
            break
        kind = input("請輸入食品種類:")
        price = int(input("請輸入價格:"))
        quantity = int(input("請輸入數量:"))
        products.append([num, name, kind, price, quantity])
    print(products)
    return products


# 印出購買紀錄
def print_products(products):
    for p in products:
        print("號碼:", p[0], "名稱:", p[1], "種類:", p[2], "價格:", p[3], "數量:", p[4])


# 存入檔案
def write_file(filename, products):
    with open(filename, "w", encoding='utf-8') as f:
        f.write("號碼,商品,種類,價格,數量\n")
        for p in products:
            f.write(str(p[0])+","+p[1]+","+p[2]+","+str(p[3])+","+str(p[4])+"\n")


def main(day):
    filename = "products"+day+".csv"
    if os.path.isfile(filename):
        print("找到檔案")
        products = read_file(filename)
    else:
        products = []
        print("找不到檔案")
    products = user_input(products)
    print_products(products)
    write_file(filename, products)


main(day)