from PySide6.QtWidgets import QWidget

from ... import cwimpl
from .viewport import PatientInfoViewport



def instance():
    return PatientInfo()


class PatientInfo:
    @cwimpl
    def viewport(self, parent: QWidget=None):
        return PatientInfoViewport(parent)
