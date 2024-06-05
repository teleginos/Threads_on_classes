from threading import Thread


class Knight(Thread):
    def __init__(self, name, skill, army=100, *args, **kwargs):
        super(Knight, self).__init__(*args, **kwargs)
        self.name = name
        self.skill = skill
        self.army = army

    def run(self):
        print(f"{self.name}, на нас напали!", flush=True)
        for day, army_size in enumerate(range(self.army - self.skill, -self.skill, -self.skill), start=1):

            if day % 10 == 1 and day % 100 != 11:
                declination_of_the_day = 'день'
            elif day % 10 in (2, 3, 4) and day not in (12, 13, 14):
                declination_of_the_day = 'дня'
            else:
                declination_of_the_day = 'дней'

            print(f"{self.name}, сражается {day} {declination_of_the_day}..., осталось {army_size} войнов!", flush=True)
        print(f"{self.name} одержал победу, спустя {self.army // self.skill} дней!", flush=True)




