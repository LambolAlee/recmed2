from PySide6.QtWidgets import QWidget

from ... import cwimpl
from .viewport import PatientInfoViewport



@cwimpl
def viewport(parent: QWidget=None):
    return PatientInfoViewport(parent)
