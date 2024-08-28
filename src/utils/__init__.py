"""
Some python files in this directory is used to help develop the program
which means some of them are not used in the final version.
"""

from .singleton import Singleton
from .flowlayout import FlowLayout


from PySide6.QtCore import Qt
from PySide6.QtWidgets import QWidget, QLayout
def fillPlaceholderWidget(oldWidget: QWidget, newWidget: QWidget, layout: QLayout) -> QWidget:
    """Replace a placeholder widget with the real used widget."""
    layout.replaceWidget(oldWidget, newWidget, Qt.FindChildOption.FindDirectChildrenOnly)
    oldWidget.deleteLater()
    return newWidget
