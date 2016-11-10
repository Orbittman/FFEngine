"""The FF Engine"""
import sys

from GameEngine import GameRunner, Game

def main():
    """The FF Engine entry point"""
    game_name = sys.argv[1]
    game_file = ""

    if game_name is None:
        print "There was no game specified"
        SystemExit("There was no game specified")

    try:
        with open(game_name, 'r') as game_file:
            game_import = game_file.read()
    except IOError as exception:
        print "I/O error({0}): {1}".format(exception.errno, exception.strerror)

    game = Game(game_import)

    game_runner = GameRunner()
    game_runner.Run(game)

# main init #
if __name__ == "__main__":
    main()

