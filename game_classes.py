class Player:
    def __init__(self, name):
        self._name = name
        self._health = 100
        self._damage = 10
        self._tag = "O"
        self._alive = True

    def __str__(self):
        return self._tag

    @property
    def name(self):
        return self._name

    @property
    def health(self):
        return self._health

    @property
    def damage(self):
        return self._damage

    @property
    def alive(self):
        return self._alive


class Enemy:
    def __init__(self, name, health, damage):
        self._name = name
        self._health = health
        self._damage = damage
        self._tag = "X"

    def __str__(self):
        return self._tag

    @property
    def name(self):
        return self._name

    @property
    def health(self):
        return self._health

    @property
    def damage(self):
        return self._damage


class Zombie(Enemy):
    def __init__(self):
        super().__init__("Zombie", 50, 5)


class Vampire(Enemy):
    def __init__(self):
        super().__init__("Vampire", 100, 2)


class Warewolf(Enemy):
    def __init__(self):
        super().__init__("Warewolf", 25, 8)