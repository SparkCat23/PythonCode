class Televisao:
    def __init__(self, min, max):
        self.ligada = False
        self.canal = 2
        self.cMin = min
        self.cMax = max
    
    def aumenta_canal(self):
        if self.canal == self.cMax:
            self.canal = self.cMin
        else:
            self.canal = self.canal + 1
        print('Canal',self.canal)

    def diminui_canal(self):
        if self.canal == self.cMin:
            self.canal = self.cMax
        else:
            self.canal = self.canal - 1
        print('Canal',self.canal)

    def select_canal(self,num):
        self.canal = num
        print('Canal',self.canal)