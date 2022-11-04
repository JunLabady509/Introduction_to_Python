class weapon:
  def __init__(self,name,force,critical_chance):
    self.name = name
    self.force = force
    self.critical_chance = critical_chance
    
  def equip(self, player):
    if player.equipped_weapon != None:
      player.equipped_weapon.desequip(player)

    player.force += self.force
    player.critical_chance += self.critical_chance
    player.equipped_weapon = self

  def desequip(self,player):
    player.force -= self.force
    player.critical_chance -= self.critical_chance

  def description(self):
    print("l'arme s'appelle",self.name)

class protection_wand(weapon):
  def __init__(self,name,force,critical_chance,protection):
    super().__init__(name,force,critical_chance)
    self.protection = protection

  def equip(self,player):
    super().equip(player)
    player.defense += self.protection

  def desequip(self,player):
    super().desequip(player)
    player.defense -= self.protection

class potion:
  def __init__(self,name,number_of_use,effect,power):
    self.name = name 
    self.number_of_use = number_of_use
    self.effect = effect
    self.power = power

  def use(self,target):
    self.number_of_use -= 1
    if self.effect == "Heal" : 
      target.pv += self.power
    elif self.effect == "Strength":
      target.force += self.power
    elif self.effect == "Defense":
      target.defense += self.power
      
def use_inventory(self):
  for i in range(len(self.inventory)):
    print(i,":",self.inventory[i].name)

    print("Choisissez une arme :")
    choice = int(input())

    self.inventory[choice].equip(self)


def see_inventory(self):
  for i in range(len(self.inventory)):
    print(i,":",self.inventory[i].name)
