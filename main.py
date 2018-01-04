from controller.controller import Controller
from ui.ui import UI
from dao.dao import Dao


def main():
    ui = UI()
    dao = Dao()
    controller = Controller(ui, dao)


if __name__ == '__main__':
    main()