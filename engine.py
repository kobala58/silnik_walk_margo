from character_clac import character

class fight(character):
    def __init__():
        pass #need to end

    def simplehit(self, attacker: character, defender: character):
        if defender.armor - defender.power <= 0:
            hit = 0 
        else: 
            defender.hp = defender.hp - (defender.armor-attacker.power)
    def onhits(self):
        pass
        
        



    