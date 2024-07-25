import sys

from ui.recmedapp import RecMedApp


def main():
    with RecMedApp(sys.argv) as app:
        app.launch()


if __name__ == '__main__':
    main()
