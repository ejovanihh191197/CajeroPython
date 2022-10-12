import datetime

class Historia:
    fecha = None
    saldoAnt:float = 0.0
    saldoAct:float = 0.0

    def __init__(self, saldoAnt:float, saldoAct:float):
        x = datetime.datetime.now()
        d = str(x.day)
        m = str(x.month)
        a = str(x.year)
        h = str(x.hour)
        min = str(x.minute)
        s = str(x.second)
        fechaActual = a+"/"+m+"/"+d+" "+h+":"+min+":"+s
        self.setFecha(fechaActual)
        self.setSaldoAct(saldoAct)
        self.setSaldoAnt(saldoAnt)

    def getFecha(self):
        return self.fecha

    def setFecha(self, fecha:str):
        self.fecha = fecha

    def getSaldoAnt(self):
        return self.saldoAnt

    def setSaldoAnt(self, saldoAnt:float):
        self.saldoAnt = saldoAnt

    def getSaldoAct(self):
        return self.saldoAct

    def setSaldoAct(self, saldoAct:float):
        self.saldoAct = saldoAct

    def __str__(self):
        return "fecha= " + self.fecha + ", saldo Anterior= " + str(self.saldoAnt) + ", saldo Actual= " + str(self.saldoAct)
