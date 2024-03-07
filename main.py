"Hallo"
import datetime

class Implante:
    def __init__(self) -> None:
        self.__fecha_implantacion = None
        self.__medico = None
        self.__estado = None
        self.__fecha_revision = None
        self.__fecha_mantenimiento = None

    def ver_fecha_implantacion(self):
        return self.__fecha_implantacion
    def ver_medico(self):
        return self.__medico
    def ver_estado(self):
        return self.__estado
    def ver_fecha_revision(self):
        return self.__fecha_revision
    def ver_fecha_mantenimiento(self):
        return self.__fecha_mantenimiento
    def set_fecha_implantacion(self, fecha):
        self.__fecha_implantacion = fecha
    def set_medico(self, medico):
        self.__medico = medico
    def set_estado(self, estado):
        self.__estado = estado
    def set_fecha_revision(self, fecha):
        self.__fecha_revision = fecha
    def set_fecha_mantenimiento(self, fecha):
        self.__fecha_mantenimiento = fecha

class Paciente:
    def __init__(self) -> None:
        self.__id = None
        self.__implantes = set()

    def ver_id(self):
        return self.__id
    def set_id(self, id):
        self.__id = id
    def agregar_implante(self, implante):
        self.__implantes.add(implante)
    def eliminar_implante(self, implante):
        self.__implantes.discard(implante)

class Marcapasos:
    def __init__(self) -> None:
        self.__num_electrodos = None
        self.__es_inalambrico = None
        self.__frecuencia_estimulacion = None
    
    def ver_num_eletrodos(self):
        return self.__num_electrodos
    def ver_es_alambrico(self):
        return self.__es_inalambrico
    def ver_frecuencia_estimulacion(self):
        return self.__frecuencia_estimulacion
    def set_num_eletrodos(self, num):
        self.__num_electrodos = num
    def set_es_alambrico(self, es):
        self.__es_inalambrico = es
    def set_frecuencia_estimulacion(self, frecuencia):
        self.__frecuencia_estimulacion = frecuencia

class StentCoronario:
    def __init__(self) -> None:
        self.__longitud = None
        self.__diametro = None
        self.__material = None

    def ver_longitud(self):
        return self.__longitud
    def ver_diametro(self):
        return self.__diametro
    def ver_material(self):
        return self.__material
    def set_longitud(self, longitud):
        self.__longitud = longitud
    def set_diametro(self, diametro):
        self.__diametro = diametro
    def set_material(self, material):
        self.__material = material

class ImplanteRodilla:
    def __init__(self) -> None:
        self.__material = None
        self.__tipo_fijacion = None
        self.__tamaño = None
    
    def ver_material(self):
        return self.__material
    def ver_tipo_fijacion(self):
        return self.__tipo_fijacion
    def ver_tamaño(self):
        return self.__tamaño
    def set_material(self, material):
        self.__material = material
    def set_tipo_fijacion(self, tipo):
        self.__tipo_fijacion = tipo
    def set_tamaño(self, tamaño):
        self.__tamaño = tamaño




   