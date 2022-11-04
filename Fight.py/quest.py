class Quest:
  def __init__(self, description, action, reward, difficulty_level, next_quest = None):
    self.description = description
    self.action = action
    self.reward = reward
    self.difficulty_level = difficulty_level
    self.next_quest = next_quest

  def check_active_quest(self,action):
    for quest in self.quest_list:
      if quest.action == action:
        print("Vous avez reussi une quete")
        self.inventory.append(quest.reward)
        self.quest_list.remove(quest)
  