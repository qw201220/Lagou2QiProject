import yaml


class Animals:
    def __init__(self, name, color, age, gender):
        self.name = name
        self.color = color
        self.age = age
        self.gender = gender

    # 会叫
    def shout(self):
        print("%s会叫" % self.name)

    # 会跑
    def run(self):
        print("%s会跑" % self.name)


class Cat(Animals):
    def __init__(self, name, color, age, gender, hair="短发"):
        super().__init__(name, color, age, gender)
        self.hair = hair

    # 添加一个新的方法， 会捉老鼠
    def ability(self):
        print(f"猫猫的姓名:{self.name}，颜色:{self.color}，年龄:{self.age}，性别:{self.gender}，毛发:{self.hair}，捉到了老鼠")

    # 复写父类的‘【会叫】的方法，改成【喵喵叫】
    def shout(self):
        print("%s会喵喵叫" % self.name)


class Dog(Animals):
    def __init__(self, name, color, age, gender, hair="长毛"):
        super().__init__(name, color, age, gender)
        self.hair = hair

    # 添加一个新的方法， 会看家
    def ability(self):
        print(f"狗狗的姓名:{self.name}，颜色:{self.color}，年龄:{self.age}，性别:{self.gender}，毛发:{self.hair}，会看家")

    # 复写父类的‘【会叫】的方法，改成【汪汪叫】
    def shout(self):
        print("%s会汪汪叫" % self.name)


if __name__ == '__main__':
    file = open('att.yml', encoding='utf-8')
    data = yaml.safe_load(file)
    print(data)
    print(data['cat'])
    Cat(data['cat']['name'], data['cat']['color'], data['cat']['age'], data['cat']['gender'],
        data['cat']['hair']).ability()
    Dog(data['dog']['name'], data['dog']['color'], data['dog']['age'], data['dog']['gender'],
        data['dog']['hair']).ability()
