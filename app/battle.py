from app.knight_clas import Knight


class Battle:
    def __init__(self, knight1: Knight, knight2: Knight) -> None:
        self.knight1 = knight1
        self.knight2 = knight2

    def prepare(self) -> None:
        self.knight1.before_fight()
        self.knight2.before_fight()

    def fight(self) -> None:
        self.knight1.hp -= self.knight2.power - self.knight1.protection
        if self.knight1.hp <= 0:
            self.knight1.hp = 0

        self.knight2.hp -= self.knight1.power - self.knight2.protection
        if self.knight2.hp <= 0:
            self.knight2.hp = 0

    def start(self) -> None:
        self.prepare()
        self.fight()
