import GameParser
import random

class GameRunner(object):
    def Run(self, game):
        self.ProcessPage(self.GetPage(game.Data.pages, "1"))

    def GetPage(self, pageCollection, page):
        return pageCollection[page]

    def ProcessPage(self, page):
        print(page.text)

        combatResult = 0
        if hasattr(page, 'combats'):
            combatResult = self.ProcessFight(page.combats)

        for action in page.actions:
            if (action != "dict"):
                print("{0} ({1})".format(page.actions[action], action))

    def ProcessFight(self, combats):
        for combat in combats:
            print("{0}: skill {1}: stamina {2}".format(combat.name, combat.skill, combat.stamina))
            #result = raw_input("Attack:")
            yourRoll = self.GetCombatRollValue()
            theirRoll = self.GetCombatRollValue()
            print("outcome: you {0}/{1} {2}".format(yourRoll, combat.name, theirRoll))


    def GetCombatRollValue(self):
        return random.randint(1, 6) + random.randint(1, 6)

class Game():
    def __init__(self, game):
        self.Data = GameParser.json2obj(game)
