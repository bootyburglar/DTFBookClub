class Humans:
    def __init__(self, name, sex, country, language) -> None:
        self.name = name
        self.sex = sex
        self.country = country
        self.language = language

    def speak(self):
        print(f"Hello, I am {self.name}")
        print(f"Hello, I am from {self.country}!")
        print(f"I speak {self.language}~")
        print()


class Taiwanese(Humans):
    def __init__(self, name, sex, betel_nuts, stinky_tofu, bubble_tea) -> None:
        self.name = name
        self.betel_nuts = betel_nuts
        self.stinky_tofu = stinky_tofu
        self.bubble_tea = bubble_tea
        self.sex = sex
        super().__init__(name=self.name,
                         sex=self.sex,
                         country="Taiwan",
                         language="幹你娘")

    def __str__(self) -> str:
        return self.name

    def chews_betel_nuts(self):
        if self.betel_nuts:
            print("三小啦 台灣檳榔好呷啦!")
        else:
            print("幼齒的來一包")

    def eats_stinky_tofu(self):
        if self.stinky_tofu:
            print("幹修拉")
        else:
            print("幹嘴巴還是臭 >:( ")

    def drinks_bubble_tea(self):
        if self.bubble_tea:
            print("給我一杯QQ奶奶超好喝到咩噗茶～")
        else:
            print("我是共匪 uwu ")

    def speak(self):
        super().speak()
        self.chews_betel_nuts()
        self.eats_stinky_tofu()
        self.drinks_bubble_tea()
        print()


if __name__ == "__main__":
    frank = Humans("Frank", "M", "America", "America FUCK YEAHHHHH")
    tony = Taiwanese("Tony", "M", False, True, True)
    brian = Taiwanese("Brian", "M", True, True, True)
    jacky = Taiwanese("帥哥味全", "M", False, False, False)
    yo = Taiwanese("阿狗的包莖", "M", False, True, False)
    people = [frank, tony, brian, jacky]
    [person.speak() for person in people]
    print(yo)
