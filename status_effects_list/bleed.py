from status_effects_list.status_effect import StatusEffect

class Bleed(StatusEffect):
    def __init__(self):
        super().__init__("Bleed", duration=3, dc=11, save_stat="con")
        self.dmg_per_turn = 3

    def apply(self, entity):
        super().apply(entity)
        print(f"{entity.name} is bleeding!")

    def on_turn(self, entity):
        entity.take_damage(self.dmg_per_turn)
        print(f"{entity.name} bleeds for {self.dmg_per_turn} damage!")
        self.current_duration -= 1

    def on_expire(self, entity):
        if self.is_expired():
            entity.active_effects.remove(self)