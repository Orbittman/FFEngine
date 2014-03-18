import GameParser

class GameRunner(object):
    def Run(self, game):
        print(game.Data.description)
        print(self.GetPage(game.Data.pages, "1").text)

    def GetPage(self, pageCollection, page):
        return pageCollection[page]

class Game():
    def __init__(self, game):
        self.Data = GameParser.json2obj(game)
