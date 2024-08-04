from ... import cwimpl



def instance():
    return PatientInfo()


class PatientInfo:
    @cwimpl
    def viewport(self):
        pass
