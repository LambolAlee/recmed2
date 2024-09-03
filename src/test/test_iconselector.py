from PySide6.QtWidgets import QWidget, QHBoxLayout, QListView
from modelview.iconmodel import IconModel
from modelview.icondelegate import IconDelegate


class Test:
    def __init__(self) -> None:
        self.w = QWidget()
        layout = QHBoxLayout()
        self.w.setLayout(layout)

        self.model = IconModel(self.w)
        self.delegate = IconDelegate(self.w)
        self.view = QListView(self.w)
        self.w.resize(700, 500)
        self.view.setFlow(QListView.Flow.LeftToRight)
        self.view.setViewMode(QListView.ViewMode.IconMode)
        self.view.setResizeMode(QListView.ResizeMode.Adjust)
        self.view.setModel(self.model)
        self.view.setItemDelegate(self.delegate)
        self.view.horizontalScrollBar().hide()

        layout.addWidget(self.view)

    def test(self):
        self.w.show()
