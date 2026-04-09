from status_effects_list.status_effect import StatusEffect

class GainAC(StatusEffect):
    def __init__(self):
        super().__init__("Gain AC", duration=3)
    
    def apply(self, entity):
        super().apply(entity)
        print(f"{entity.name} gained AC!")
        entity.temp_ac_bonus = entity.get_modifier(entity.con)
        self.current_duration = self.duration

    def on_expire(self, entity):
        if self.is_expired():
            entity.temp_ac_bonus = 0
            entity.active_effects.remove(self)
            print(f"{entity.name}'s AC buff removed!")

            
class LoseAC(StatusEffect):
    def __init__(self):
        super().__init__("Lose AC", duration=3, dc=10, save_stat="int")
    
    def apply(self, entity):
        super().apply(entity)
        print(f"{entity.name} lost AC")
        entity.temp_ac_bonus = -2
        self.current_duration = self.current_duration

    def on_expire(self, entity):
        if self.is_expired():
            entity.temp_ac_bonus = 0
            entity.active_effects.remove(self)
            print(f"{entity.name}'s AC debuff removed!")