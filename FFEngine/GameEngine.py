"""The FF Game Engine"""
import random
import GameParser

class GameRunner(object):
    """ Game runner """
    def __init__(self):
        self.Game = None

    def Run(self, game):
        print("Skill: {0} Stamina: {1} Luck: {2}".format(game.Stats.Skill, game.Stats.Stamina, game.Stats.Luck))
        self.Game = game
        self.ProcessPage(self.GetPage(game.Data.pages, "1"))

    def GetPage(self, pageCollection, page):
        return pageCollection[page]

    def ProcessPage(self, page):
        print(page.text)

        combatResult = 0
        if hasattr(page, 'combats'):
            combatResult = self.ProcessFight(page.combats)

        for action in page.actions:
            if (action != "format"):
                print("{0} ({1})".format(page.actions[action].text, action))

        chosenAction = input(": ")
        newPage = page.actions[chosenAction].page
        self.ProcessPage(self.GetPage(self.Game.Data.pages, newPage))

    def ProcessFight(self, combats):
        for combat in combats:
            print("{0}: skill {1}: stamina {2}".format(combat.name, combat.skill, combat.stamina))
            result = input("Attack:")
            yourRoll = self.GetCombatRollValue(self.Game.Stats.Skill)
            theirRoll = self.GetCombatRollValue(combat.skill)
            print("outcome: you {0}/{1} {2}".format(yourRoll, combat.name, theirRoll))

    def GetCombatRollValue(self, skill):
        return skill + random.randint(1, 6)


class Game():
    def __init__(self, game):
        self.Data = GameParser.json2obj(game)
        self.Stats = Stats()

class Stats():
    def __init__(self):
        self.Skill = random.randint(1, 6) + 6
        self.Luck = random.randint(1, 6) + 6
        self.Stamina = random.randint(1, 6) + 12

