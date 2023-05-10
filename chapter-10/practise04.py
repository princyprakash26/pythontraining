#class train,get fare,get status:

class train():
    def __init__(self) -> None:
        self.seat=78
        self.fare=175

    def ticketbook(self):
        self.seat-=1
    def getstatus(self):
        print(self.seat)
    def getfareinfo(self):
        print(self.fare)

tr=train()
tr.getfareinfo()
tr.getstatus()
tr.ticketbook()
tr.getstatus()

