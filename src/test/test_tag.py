from ui.pilltagwidget import TagContainer
from tag import Tag
from PySide6.QtWidgets import QWidget, QPushButton, QVBoxLayout


class Test:
    def test(self):
        self.w = QWidget()
        layout = QVBoxLayout()
        self.c = TagContainer(self.w)
        self.c.addTag(Tag("example"), Tag("example2", fg="#ff0000"), Tag("hello world", bg="#00ff00"), Tag(":wonSign>"))
        # c.addTag(Tag(":wonSign>"))
        b = QPushButton("edit mode", self.w)
        b.clicked.connect(lambda: self.c.setEditMode(not self.c.isInEdit()))
        layout.addWidget(self.c)
        layout.addWidget(b)
        self.w.setLayout(layout)
        self.w.show()