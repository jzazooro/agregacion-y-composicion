class pared: 
    def __init__(self, horientacion):
        self.horientacion=horientacion

class ventana(pared):
    def __init__(self, horientacion, superficie):
        super().__init__(horientacion)
        self.superficie=superficie
        return self.superficie

class casa(ventana):
    def __init__(self, paredes, horientacion, superficie):
        super().__init__(horientacion, superficie)
        self.paredes=paredes
    def superficieacristalada(self, acristalado):
        self.acristalado=acristalado
        return(self.paredes.superficie)

class cortina:
    def __init__(self, horientacion, superficie):
        pared.__init__(self, horientacion, superficie)
        ventana.__init__(self, superficie, "ninguna")