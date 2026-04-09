from .status_effect import StatusEffect

class DamageDebuffEffect(StatusEffect):
    def __init__(self, name, duration, debuff_amount, dc=None, save_stat=None,
                 apply_message="", expire_message=""):
        super().__init__(name, duration, dc, save_stat)
        self.debuff_amount = debuff_amount
        self.apply_message = apply_message
        self.expire_message = expire_message

    def apply(self, entity):
        super().apply(entity)
        entity.temp_dmg_debuff = self.debuff_amount
        self.current_duration = self.duration
        print(self.apply_message.format(entity=entity, effect=self))

    def on_expire(self, entity):
        if self.is_expired():
            entity.temp_dmg_debuff = 0
            if self in entity.active_effects:
                entity.active_effects.remove(self)
            print(self.expire_message.format(entity=entity, effect=self))

class Mark(DamageDebuffEffect):
    def __init__(self):
        super().__init__(
            name="Mark",
            duration=3,
            debuff_amount=4,
            dc=15,
            save_stat="dex",
            apply_message="{entity.name} is Marked!",
            expire_message="{entity.name} is no longer Marked!"
        )

class Hex(DamageDebuffEffect):
    def __init__(self):
        super().__init__(
            name="Hex",
            duration=3,
            debuff_amount=4,
            dc=12,
            save_stat="wis",
            apply_message="{entity.name} is Hexed!",
            expire_message="{entity.name} is no longer Hexed!"
        )