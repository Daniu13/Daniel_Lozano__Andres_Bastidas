"Hallo"

class Implante:
    def __init__(self) -> None:
        self.__fecha_implantacion = None
        self.__medico = None
        self.__estado = None
        self.__fecha_revision = None
        self.__fecha_mantenimiento = None

    def ver_fecha_implantacion(self):
        pass
    def ver_medico(self):
        pass
    def ver_estado(self):
        pass
    def ver_fecha_revision(self):
        pass
    def ver_fecha_mantenimiento(self):
        pass
    def set_fecha_implantacion(self):
        pass
    def set_medico(self):
        pass
    def set_estado(self):
        pass
    def set_fecha_revision(self):
        pass
    def set_fecha_mantenimiento(self):
        pass

class Paciente:
    def __init__(self) -> None:
        self.__id = None
        self.__implantes = set()

    def ver_id(self):
        pass
    def set_id(self):
        pass
    def agregar_implante(self):
        pass
    def eliminar_implante(self):
        pass