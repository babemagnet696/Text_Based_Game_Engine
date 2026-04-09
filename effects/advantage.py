from .status_effect import StatusEffect

class GainAdvantage(StatusEffect):
    def __init__(self):
        super().__init__("Gain Advantage", duration=2)

    def apply(self, entity):
        super().apply(entity)
        print(f"{entity.name} gained advantage!")
        self.current_duration = self.duration
        entity.advantage = True

    def on_expire(self, entity):
        if self.is_expired():
            entity.active_effects.remove(self)
            print(f"{entity.name} lost Advantage!")
            entity.advantage = False

class GainDisadvantage(StatusEffect):
    def __init__(self):
        super().__init__("Gain Disadvantage", duration=2, dc=14, save_stat="cha")

    def apply(self, entity):
        super().apply(entity)
        print(f"{entity.name} gained Disadvantage!")
        self.current_duration = self.duration
        entity.disadvantage = True

    def on_expire(self, entity):
        if self.is_expired():
            entity.active_effects.remove(self)
            print(f"{entity.name} lost Disadvantage!")
            entity.disadvantage = False

class DarkSurge(GainAdvantage):
    def __init__(self):
        super().__init__()

    def on_turn(self, entity):
        entity.current_hp -= 4
        print(f"{entity.name} took 4 damage from Dark Surge!")