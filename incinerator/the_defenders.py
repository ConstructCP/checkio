# Taken from mission Army Battles


class Warrior:
    def __init__(self, attack: int = 5, health: int = 50):
        self.attack = attack
        self.health = health

    def do_damage(self, target: 'Warrior') -> None:
        """ Attack another unit """
        target.receive_damage(self.attack)

    def receive_damage(self, damage: int) -> None:
        """ Get given amount of damage from another unit """
        self.health -= damage

    @property
    def is_alive(self) -> bool:
        return self.health > 0


class Knight(Warrior):
    def __init__(self, attack: int = 7, health: int = 50):
        super().__init__(attack=7)


class Defender(Warrior):
    def __init__(self, attack: int = 3, health: int = 60, defense: int = 2):
        super().__init__(attack=attack, health=health)
        self.defense = defense

    def receive_damage(self, damage: int) -> None:
        """ Get given amount of damage from another unit minus defense """
        real_damage = damage - self.defense
        if real_damage > 0:
            self.health -= real_damage
            if self.health <= 0:
                self._is_alive = False


class Army:
    def __init__(self):
        self.units = []

    def add_units(self, unit_type: Warrior, quantity: int) -> None:
        self.units.extend([unit_type() for _ in range(quantity)])

    def get_unit(self) -> Warrior:
        return self.units[0]

    def remove_dead_unit(self) -> None:
        if not self.units[0].is_alive:
            self.units.pop(0)

    def __bool__(self):
        return len(self.units) > 0


class Battle:
    def fight(self, army1: Army, army2: Army) -> bool:
        while army1 and army2:
            unit1, unit2 = army1.get_unit(), army2.get_unit()
            if fight(unit1, unit2):
                army2.remove_dead_unit()
            else:
                army1.remove_dead_unit()

        return bool(army1)


def fight(unit_1: Warrior, unit_2: Warrior):
    while unit_1.is_alive:
        unit_1.do_damage(unit_2)
        if unit_2.is_alive:
            unit_2.do_damage(unit_1)
        else:
            break
    return unit_1.is_alive


if __name__ == '__main__':
    # fight tests
    chuck = Warrior()
    bruce = Warrior()
    carl = Knight()
    dave = Warrior()
    mark = Warrior()
    bob = Defender()
    mike = Knight()
    rog = Warrior()
    lancelot = Defender()

    assert fight(chuck, bruce) == True
    assert fight(dave, carl) == False
    assert chuck.is_alive == True
    assert bruce.is_alive == False
    assert carl.is_alive == True
    assert dave.is_alive == False
    assert fight(carl, mark) == False
    assert carl.is_alive == False
    assert fight(bob, mike) == False
    assert fight(lancelot, rog) == True

    # battle tests
    my_army = Army()
    my_army.add_units(Defender, 1)

    enemy_army = Army()
    enemy_army.add_units(Warrior, 2)

    army_3 = Army()
    army_3.add_units(Warrior, 1)
    army_3.add_units(Defender, 1)

    army_4 = Army()
    army_4.add_units(Warrior, 2)

    battle = Battle()

    assert battle.fight(my_army, enemy_army) == False
    assert battle.fight(army_3, army_4) == True
    print("Coding complete? Let's try tests!")
