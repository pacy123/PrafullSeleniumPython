#to inherit the parent class
from Learning.OOpsDemo import Calculator


class ChildImpl(Calculator):
    num2 =200

    def __init__(self):
        Calculator.__init__(self,2,10)


    def gtCompleteData(self):
        return self.num2+ self.num+self.Summstion()


obj =ChildImpl()
print(obj.gtCompleteData())

