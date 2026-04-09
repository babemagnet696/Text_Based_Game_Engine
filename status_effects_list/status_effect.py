from dice_roller import d20

class StatusEffect:
    def __init__(self, name, duration, dc=None, save_stat=None):
        self.name = name
        self.duration = duration
        self.current_duration=0
        self.dc = dc
        self.save_stat = save_stat

    def apply(self, entity):
        existing = self.is_active(entity)
        if existing:
            existing.current_duration += self.duration
            return
        self.current_duration = self.duration
        entity.active_effects.append(self)

    def on_turn(self, entity):
        if self.current_duration > 0:
            self.current_duration -= 1

    def is_expired(self):
        return self.current_duration <=0
    
    def is_active(self, entity):
        for effect in entity.active_effects:
            if effect.name == self.name:
                return effect
        return None
    
    def on_expire(self, entity):
        if self.is_expired():
            entity.active_effects.remove(self)

    def saving_throw(self, entity):
        if self.dc is not None:
            stat = getattr(entity, self.save_stat)
            modifier = entity.get_modifier(stat)
            die = d20(bonus=modifier)
            _, roll = die.roll_dice()
            return roll >= self.dc
        return False