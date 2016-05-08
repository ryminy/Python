srcMyself = 'p'
destArduino = 'a'
crcDefault = '.'
typeDefault = '0'
dataDefault = "00"

class packet:

    def __init__(self):
        self.src = srcMyself
        self.dest = destArduino
        self.type = typeDefault
        self.data = dataDefault[0:2]
        self.crc = crcDefault

##    def __init__(self, msgType, msgData):
##        self.src = srcMyself
##        self.dest = destArduino
##        self.type = msgType
##        self.data[0:1] = msgData
##        self.crc = crcDefault

    def getSrc(self):
        print("Packet source:" + self.src)

    def getDest(self):
        print("Packet destination:" + self.dest)

    def getType(self):
        print("Packet type:"  + self.type)

    def getData(self):
        print("Packet data:" +  self.data)

    def getCrc(self):
        print("Packet crc:"  + self.crc)

    def printPacket(self):
        self.getSrc()
        self.getDest()
        self.getType()
        self.getData()
        self.getCrc()

    def calculateCrc(self):
        self.crc = chr((ord(self.src) + ord(self.dest) + ord(self.type)
                        + ord(self.data[0]) + ord(self.data[1])) % 127)

    def packetToString(self):
        return  ''.join([self.src ,self.dest, self.type, self.data[0],
                self.data[1], self.crc])

    def stringToPacket(self,string):
        self.src = string[0]
        self.dest = string[1]
        self.type = string[2]
        self.data = string[3:4]
        self.crc = string[5]

    def setDest(self, dest):
        self.dest = dest

    def setSrc(self, src):
        self.Src = src

    def setData(self,data):
        self.data = data[0:2]

    def setType(self,msgType):
        self.type = msgType






