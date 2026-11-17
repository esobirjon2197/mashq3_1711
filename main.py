
# 3-m
class Telefon:
    def __init__(self, brend, madel):
        self.brend = brend
        self.madel = madel

    def yoqish(self):
        print(f"Brend: {self.brend}")
        print(f"Madel: {self.madel}")


class Smartfon(Telefon):
    def __init__(self, brend, madel, xotira):
        super().__init__(brend, madel)
        self.xotira = xotira

    def yoqish(self):
        super().yoqish()
        print(f"Xotira: {self.xotira}")


x = Smartfon("samsung", "s 22 ultra", "256GB")
x.yoqish()
