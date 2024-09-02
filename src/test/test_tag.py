from ui.tagcontainer import TagContainer
from tag import Tag
from PySide6.QtWidgets import QWidget, QPushButton, QVBoxLayout
from descriptivecontrol import getDesciptor


class Test:
    def test(self):
        self.w = QWidget()
        layout = QVBoxLayout()
        self.c = TagContainer(self.w)
        self.tt = Tag("example2", fg="#ff0000")
        self.c.addTag(Tag("example"), self.tt, Tag("hello world", bg="#00ff00"), Tag(":wonSign>"))
        # c.addTag(Tag(":wonSign>"))
        b = QPushButton("edit mode", self.w)
        b.clicked.connect(lambda: self.c.setEditMode(not self.c.isInEdit()))
        # b.clicked.connect(self.showColorEditor)
        layout.addWidget(self.c)
        layout.addWidget(b)
        self.w.setLayout(layout)
        self.w.show()

    def showColorEditor(self):
        e = getDesciptor(self.tt, "bg")
        e.build().show()
