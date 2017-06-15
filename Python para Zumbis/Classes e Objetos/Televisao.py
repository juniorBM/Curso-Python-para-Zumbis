class Televisao:
    
    def __init__(self):
        self.ligada = False
        self.canal = 2

    # def __init__(self, ligada, canal):
    #     self.ligada = ligada
    #     self.canal = canal

    def mudcaCanalBaixo(self):
        self.canal -= 1
    def mudaCanalCima(self):
        self.canal += 1

tvQuarto = Televisao()
tvQuarto.mudaCanalCima()
print(tvQuarto.ligada)
print(tvQuarto.canal)