import sys
from pathlib import Path

from ui.recmedapp import RecMedApp
from recmedtyping import PathManager


def main():
    PathManager().init(Path(__file__))
    with RecMedApp(sys.argv) as app:
        app.launch()
        # app.testUi()


if __name__ == '__main__':
    main()
