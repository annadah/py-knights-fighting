from __future__ import annotations


class Knight:
    def __init__(self, name: str, power: int, hp: int, armour: list,
                 weapon: dict, potion: dict,
                 protection: int | None = None) -> None:
        self.name = name
        self.power = power
        self.hp = hp
        self.armour = armour
        self.weapon = weapon
        self.potion = potion
        self.protection = protection

    @classmethod
    def from_dict(cls, config: dict) -> Knight:
        return cls(
            name=config["name"],
            power=config["power"],
            hp=config["hp"],
            armour=config["armour"],
            weapon=config["weapon"],
            potion=config["potion"],
        )

    def apply_weapon(self) -> None:
        self.power += self.weapon["power"]

    def protect(self) -> None:
        self.protection = 0
        for protection_one in self.armour:
            self.protection += protection_one["protection"]

    def before_fight(self) -> None:
        self.protect()
        self.apply_weapon()
        if self.potion is None:
            return
        if "hp" in self.potion["effect"]:
            self.hp += self.potion["effect"]["hp"]
        if "power" in self.potion["effect"]:
            self.power += self.potion["effect"]["power"]
        if "protection" in self.potion["effect"]:
            self.protection += self.potion["effect"]["protection"]

#
# lancelot = Knight("Lancelot", 35, 100, [],
#                       {"name": "Metal Sword", "power": 50}, None)
#
# arthur = Knight("Arthur", 45, 75, [
#                     {
#                         "part": "helmet",
#                         "protection": 15,
#                     },
#                     {
#                         "part": "breastplate",
#                         "protection": 20,
#                     },
#                     {
#                         "part": "boots",
#                         "protection": 10,
#                     }
#                 ],
#                 {
#                     "name": "Two-handed Sword",
#                     "power": 55,
#                 }, None)
#
# mordred = Knight("Mordred", 30, 90,[
#                     {
#                         "part": "breastplate",
#                         "protection": 15,
#                     },
#                     {
#                         "part": "boots",
#                         "protection": 10,
#                     }],
#                   {
#                     "name": "Poisoned Sword",
#                     "power": 60,
#                   },
#                   {
#                               "name": "Berserk",
#                               "effect": {
#                                   "power": +15,
#                                   "hp": -5,
#                                   "protection": +10,
#                               }}
#                   )
#
#
# red_knight = Knight("Red Knight", 40,70, [
#                     {
#                         "part": "breastplate",
#                         "protection": 25,
#                     }
#                 ],{
#                     "name": "Sword",
#                     "power": 45
#                 },
#                     {
#                     "name": "Blessing",
#                     "effect": {
#                         "hp": +10,
#                         "power": +5,
#                     }}
#                 )
#
# # list_knight = [lancelot, arthur, mordred, red_knight]
