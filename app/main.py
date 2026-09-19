from app.battle import Battle
from app.knight_clas import Knight


def battle(knights_config: dict) -> dict:
    lancelot = Knight.from_dict(knights_config["lancelot"])
    mordred = Knight.from_dict(knights_config["mordred"])
    arthur = Knight.from_dict(knights_config["arthur"])
    red_knight = Knight.from_dict(knights_config["red_knight"])

    battle1 = Battle(lancelot, mordred)
    battle1.start()

    battle2 = Battle(arthur, red_knight)
    battle2.start()
    return {
        lancelot.name: lancelot.hp,
        arthur.name: arthur.hp,
        mordred.name: mordred.hp,
        red_knight.name: red_knight.hp,
    }

# print(battle(None))
# print(battle(KNIGHTS))
