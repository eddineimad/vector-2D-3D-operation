class Vecteur2D :
    _count = 0
    def __init__(self, X = 1.5, Y = 2):
        self.__X = X
        self.__Y = Y
        self._count += 1

    # getter X
    def GetX(self):
        return self.__X

    # getter Y
    def GetY(self):
        return self.__Y
    
    # getter  _count
    def Getcount(self):
        return self._count

    # setter  X
    def SetX(self, X1):
        self.__X = X1

    # setter  Y
    def SetY(self, Y1):
        self.__Y = Y1

    def Str(self):
        return "X = " + str(self.GetX()) + " Y = " + str(self.GetY())
    
    def Equals(self, vecteur1) :
        if vecteur1.GetX() == self.GetX() and vecteur1.GetY() == self.GetY() :
            return True
        else : 
            return False 
        
    # vector norm
    def Norme (self) :
        return (self.GetX()**2 + self.GetY()**2)**0.5

class Vecteur3D (Vecteur2D) :
    def __init__(self, X = 1.5, Y = 2, Z = 5) :
        super().__init__(X, Y)
        self.__Z = Z
        self._count += 1

    # getter Z
    def GetZ(self):
        return self.__Z

    # setter Z
    def SetZ(self, Z1):
        self.__Z = Z1

    def Str(self):
        return "X = " + str(self.GetX()) + " Y = " + str(self.GetY()) + " Z = " + str(self.GetZ())

    def Equals(self, vecteur1) :
        if vecteur1.GetX() == self.GetX() and vecteur1.GetY() == self.GetY() and vecteur1.GetZ() == self.GetZ() :
            return True
        else : 
            return False 
        
    # vector norm
    def Norme (self) :
        return (self.GetX()**2 + self.GetY()**2 + self.GetZ()**2)**0.5