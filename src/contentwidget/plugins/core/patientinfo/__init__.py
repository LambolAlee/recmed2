from PySide6.QtWidgets import QWidget

from ... import cwimpl, IContentWidget
from .viewport import PatientInfoViewport



class PatientInfo(IContentWidget):
    @cwimpl
    def viewport(self, parent: QWidget=None):
        return PatientInfoViewport(parent)



def entry():
    return PatientInfo()
