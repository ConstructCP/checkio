class Warrior:
    def __init__(self, attack: int = 5, health: int = 50):
        self.attack = attack
        self._health = health

    def do_damage(self, target: 'Warrior') -> None:
        """ Attack another unit """
        target.receive_damage(self.attack)

    def receive_damage(self, damage: int) -> None:
        """ Get given amount of damage from another unit """
        self._health -= damage

    @property
    def is_alive(self) -> bool:
        return self._health > 0

    @property
    def health(self):
        return self._health


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
            self._health -= real_damage


class Vampire(Warrior):
    def __init__(self, attack: int = 4, health: int = 40, vampirism: int = 50):
        super().__init__(attack, health)
        self.vampirism = 50

    def do_damage(self, target: 'Warrior') -> None:
        target_health_before_attack = target._health
        super().do_damage(target)
        damage_dealt = target_health_before_attack - target.health
        heal_received = damage_dealt * (self.vampirism * 100)
        self._health += heal_received


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
    eric = Vampire()
    adam = Vampire()
    richard = Defender()
    ogre = Warrior()

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
    assert fight(eric, richard) == False
    assert fight(ogre, adam) == True

    # battle tests
    my_army = Army()
    my_army.add_units(Defender, 2)
    my_army.add_units(Vampire, 2)
    my_army.add_units(Warrior, 1)

    enemy_army = Army()
    enemy_army.add_units(Warrior, 2)
    enemy_army.add_units(Defender, 2)
    enemy_army.add_units(Vampire, 3)

    army_3 = Army()
    army_3.add_units(Warrior, 1)
    army_3.add_units(Defender, 4)

    army_4 = Army()
    army_4.add_units(Vampire, 3)
    army_4.add_units(Warrior, 2)

    battle = Battle()

    assert battle.fight(my_army, enemy_army) == False
    assert battle.fight(army_3, army_4) == True
    print("Coding complete? Let's try tests!")
