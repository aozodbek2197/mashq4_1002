class Talaba:
    def __init__(self, ism, familiya, tyil):
        self.ism = ism
        self.familiya = familiya
        self.tyil = tyil

    def info(self):
        print(f"Talaba data_lari: {self.ism} {self.familiya} {self.tyil}")

talaba1 = Talaba("Alijon", "Valiyev", 2000)
talaba1.info()

talaba2 = Talaba("Olim", "Olimov", 1995)
talaba2.info()

talaba3 = Talaba("Husan", "Akbarov", 2004)
talaba3.info()

talaba4 = Talaba("Hasan", "Akbarov", 2004)
talaba4.info()
