class Humans:
    def __init__(self, country, sex, language) -> None:
        self.country = country
        self.sex = sex
        self.language = language

    def speak(self):
        print(f"Hello, I am from {self.country}!")
        print(f"I speak {self.language}~")


class Taiwanese(Humans):
    pass


if __name__ == "__main__":
    frank = Humans("Taiwan", "M", "幹你娘")
    frank.speak()
