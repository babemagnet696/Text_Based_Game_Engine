from .status_effect import StatusEffect

class Burn(StatusEffect):
    def __init__(self):
        super().__init__("Burn", duration=3, dc=12, save_stat="dex")
        self.dmg_per_turn = 3

    def apply(self, entity):
        super().apply(entity)
        print(f"{entity.name} is burning!")
        self.current_duration = self.duration

    def on_turn(self, entity):
        super().on_turn(entity)
        entity.take_damage(self.dmg_per_turn)
        print(f"{entity.name} burned for {self.dmg_per_turn} damage!")

    def on_expire(self, entity):
        super().on_expire(entity)
        print(f"{entity.name} is no longer burning")