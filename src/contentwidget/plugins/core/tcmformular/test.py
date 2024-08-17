import sys

from PySide6.QtWidgets import QTableView, QApplication, QHeaderView

from .formulardelegate import FormularDelegate
from .formularmodel import FormularTableModel



def main():

    app = QApplication([])
    view = QTableView()
    view.setMinimumWidth(600)
    d = FormularDelegate(view)
    f = [
        {"name": "熟大黄", "dose": 45, "decoction": "先煎"},
        {"name": "土鳖虫", "dose": 45},
        {"name": "水蛭", "dose": 45, "decoction": "后下"},
        {"name": "虻虫", "dose": 45},
        {"name": "蛴螬", "dose": 45},
        {"name": "干漆", "dose": 45},
        {"name": "桃仁", "dose": 45},
        {"name": "苦杏仁", "dose": 45},
        {"name": "白花蛇舌草", "dose": 45},
        {"name": "地黄", "dose": 45},
    ]
    m = FormularTableModel(f, view)
    # for i in m._formular.data:
    #     print(i)
    view.setModel(m)
    view.setItemDelegate(d)
    view.horizontalHeader().hide()
    view.verticalHeader().hide()
    view.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
    view.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()