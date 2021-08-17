class Warrior:
    damage = 5
    health = 50
    _is_alive = True

    def attack(self, target: 'Warrior') -> None:
        """ Attack another unit """
        target.receive_damage(self.damage)

    def receive_damage(self, damage: int) -> None:
        """ Receive damage from another unit's attack"""
        self.health -= damage
        if self.health <= 0:
            self._is_alive = False

    @property
    def is_alive(self) -> bool:
        """ Get is_alive status"""
        return self._is_alive


class Knight(Warrior):
    damage = 7


def fight(unit_1: Warrior, unit_2: Warrior) -> bool:
    """
    Simulate fight between 2 units. Return True if unit_1 won a fight by killing unit_2
    """
    while unit_1.is_alive:
        unit_1.attack(unit_2)
        if unit_2.is_alive:
            unit_2.attack(unit_1)
        else:
            break
    return unit_1.is_alive


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing

    chuck = Warrior()
    bruce = Warrior()
    carl = Knight()
    dave = Warrior()
    mark = Warrior()

    assert fight(chuck, bruce) == True
    assert fight(dave, carl) == False
    assert chuck.is_alive == True
    assert bruce.is_alive == False
    assert carl.is_alive == True
    assert dave.is_alive == False
    assert fight(carl, mark) == False
    assert carl.is_alive == False

    print("Coding complete? Let's try tests!")
