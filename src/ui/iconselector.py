from PySide6.QtCore import Qt, QModelIndex, Signal
from PySide6.QtWidgets import QListView, QWidget, QVBoxLayout, QLineEdit

from modelview.iconmodel import IconModel
from modelview.icondelegate import IconDelegate

from utils import singleton
from recmedtyping import RMIconType



class IconView(QListView):
    iconSelected = Signal(RMIconType)
    def __init__(self, parent: QWidget | None=None):
        super().__init__(parent)
        self.setUniformItemSizes(True)
        self.setFlow(QListView.Flow.LeftToRight)
        self.setViewMode(QListView.ViewMode.IconMode)
        self.setResizeMode(QListView.ResizeMode.Adjust)
        self.setItemAlignment(Qt.AlignmentFlag.AlignCenter)
        self.horizontalScrollBar().hide()
        self.setVerticalScrollMode(QListView.ScrollMode.ScrollPerPixel)
        self.verticalScrollBar().setSingleStep(20)
        self.setFixedSize(530, 500)

        self.doubleClicked.connect(self.onDoubleClicked)

    def onDoubleClicked(self, index: QModelIndex):
        name = self.model().data(index, role=Qt.ItemDataRole.UserRole)
        self.iconSelected.emit(RMIconType[name])



@singleton
class IconSelector(QWidget):
    iconSelected = Signal(RMIconType)

    def __init__(self):
        super().__init__()
        self.setWindowFlag(Qt.WindowType.Popup)
        self.build()

    def build(self):
        layout = QVBoxLayout()
        self.searchBox = QLineEdit(self)
        self.searchBox.setPlaceholderText("Search Icon Name...")
        self.searchBox.setClearButtonEnabled(True)
        self.searchBox.textEdited.connect(self.onTextEdited)
        layout.addWidget(self.searchBox)

        self.view = IconView(self)
        self.model = IconModel(self)
        self.delegate = IconDelegate(self)
        self.view.setModel(self.model)
        self.view.setItemDelegate(self.delegate)
        layout.addWidget(self.view)

        self.setLayout(layout)

        self.view.iconSelected.connect(self.select)

    def select(self, icon: RMIconType):
        self.iconSelected.emit(icon)
        self.close()

    def onTextEdited(self, text: str):
        if text == "":
            self.model.setSearchMode(False)
            self.model.setSearchText("")
            self.view.clearSelection()
            self.view.viewport().update()
            return

        self.model.setSearchMode(True)
        self.model.setSearchText(text)
        self.view.clearSelection()
        self.view.scrollTo(self.model.index(0, 0))
        self.view.viewport().update()


