from WeatherApp import *


def main():
    application = QApplication([])
    window = MainMenu()
    window.show()
    application.exec()


if __name__ == '__main__':
    main()
