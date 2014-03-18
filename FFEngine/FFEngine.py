import sys
from GameEngine import GameRunner, Game

def main():
    gameName = sys.argv[1]
    gameFile = ""

    if gameName == None:
        print("There was no game specified")
        sys.exit

    try:
        with open(gameName, 'r') as gameFile:
            gameImport = gameFile.read()
    except IOError as e:
        print("I/O error({0}): {1}".format(e.errno, e.strerror))

    game = Game(gameImport)

    gameRunner = GameRunner()
    gameRunner.Run(game)

# main init #
if __name__ == "__main__":
    main()

