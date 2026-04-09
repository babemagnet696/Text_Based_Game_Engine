from .status_effect import StatusEffect

class Bleed(StatusEffect):
    def __init__(self):
        super().__init__("Bleed", duration=3, dc=11, save_stat="con")
        self.dmg_per_turn = 3

    def apply(self, entity):
        super().apply(entity)
        print(f"{entity.name} is bleeding!")

    def on_turn(self, entity):
        super().on_turn(entity)
        entity.take_damage(self.dmg_per_turn)
        print(f"{entity.name} bleeds for {self.dmg_per_turn} damage!")

    def on_expire(self, entity):
        super().on_expire(entity)
        print(f"{entity.name} is no longer bleeding!")