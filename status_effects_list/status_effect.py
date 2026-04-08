from dice_roller import d20

class StatusEffect:
    def __init__(self, name, duration, dc=None, save_stat=None):
        self.name = name
        self.duration = duration
        self.current_duration=0
        self.dc =dc
        self.save_stat = save_stat

    def apply(self, entity):
        pass

    def on_turn(self, entity):
        pass

    def is_expired(self):
        return self.current_duration <=0
    
    def on_expire(self, entity):
        pass

    def saving_throw(self, entity):
        if self.dc is not None:
            stat = getattr(entity, self.save_stat)
            modifier = entity.get_modifier(stat)
            die = d20(bonus=modifier)
            _, roll = die.roll_dice()
            return roll >= self.dc
        return False