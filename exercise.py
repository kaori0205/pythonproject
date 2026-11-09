def greet(name):
    print("こんにちは、" + name + "さん！")

greet("Taro")

class Dog:
    def __init__(self, name):
        self.name = name

    def bark(self):
        print(self.name + "がワン！")

pochi = Dog("ポチ")
pochi.bark()

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

rectangle1 = Rectangle(5, 10)
print("面積:", rectangle1.area())
print("周囲の長さ:", rectangle1.perimeter())


employee = {
    "employee_1": {
        "name": "Alice",
        "projects": {
            "project_A":{"task_1": "完了", "task_2": "未完了", "task_3": "完了"},
            "project_B":{"task_1": "未完了", "task_2": "未完了"}
        }}
    ,"employee_2": {
        "name": "Bob",
        "projects": {
            "project_C":{"task_1": "完了", "task_2": "完了", "task_2": "完了"},
            "project_D":{"task_1": "未完了", "task_2": "完了"}
        }}
}

print("Updated Employee")
print(employee)


try:
    a = int(input("割られる数を入力してください: "))
    b = int(input("割る数を入力してください: "))
    result = a / b
    print("結果:", result)
except ZeroDivisionError:
    print("0では割り算できません。")

try:
    fruits = ["りんご", "みかん", "バナナ"]
    index = int(input("表示したい果物の番号を入力してください（0～2）: "))
    print("選ばれた果物:", fruits[index])
except IndexError:
    print("その位置の要素は存在しません")