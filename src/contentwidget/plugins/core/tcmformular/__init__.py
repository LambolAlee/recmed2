from PySide6.QtWidgets import QWidget

from ... import cwimpl
from .viewport import TCMFormularViewport



@cwimpl
def viewport(parent: QWidget=None):
    return TCMFormularViewport(parent)
