class pcm:
    def __init__(self,phy,chem,math):
        self.phy=phy
        self.chem=chem
        self.math=math
    def show(self):
        print("phy=",self.phy)
        print("chem",self.phy)
        print("math",self.math)
class nonpcm:
    def __init__(self,eng,bio):
        self.eng=eng
        self.bio=bio
    def show(self):
        print("eng = ",self.eng)
        print("bio = ",self.bio)

class marks(pcm,nonpcm):
    
    def _init_(self,phy,chem,math,eng,bio):
        def __init__(self,phy,chem,math,eng,bio):
            pcm.__init__(self,phy,chem,math)
            nonpcm.__init__(self,eng,bio)
    def show(self):
        pcm.show(self)
        nonpcm.show(self)

m=marks(99,77,55,44,33)
m.show()


        
