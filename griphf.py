import  DataSet
import QueryConverter

# listData = DataSet.showGraphER()
listData=[(1,2,"a"),(2,3,"b"),(2,6,"g"),(3,5,"c"),(1,4,"f"),(3,7,"c"),(4,8,"b"),(8,9,"c")]
listVertex =[]
result =[]
def addVertex():
    for d in listData:
        d1=True
        for v in listVertex:
            if v.name == d[0]:
                d1=False
                break
        if d1==True:
            listVertex.append(Vertex(d[0]))
        d2=True
        for v in listVertex:
            if v.name == d[1]:
                d2=False
                break
        if d2 == True:
            listVertex.append(Vertex(d[1]))
class Vertex(object):
    def __init__(self,name):
        self.name = name
        self.last = []
        self.next = []
    def setLastAndNext(self,listdata):
        for ve in listdata:
            if ve[0] == self.name:
                self.last.append((ve[1],ve[2]))
            else:
                if ve[1] == self.name:
                    self.next.append((ve[0],ve[2]))

    def chooseBF(self,v,quary):
        if quary:
            if quary[0] == "-":
                self.checkBack(v,quary)
            else:
                self.checkForward(v,quary)
        else:
            result.append((v,self.name))


    def checkForward(self,v,quary):
        for e in self.last:
            if e[1]==quary[0]:
                for ver in listVertex:
                    if ver.name==e[0]:
                        ver.chooseBF(v,quary[1:])
                        break


    def checkBack(self, v, quary):
        for e in self.next:
            if e[1] == quary[1]:
                for ver in listVertex:
                    if ver.name==e[0]:
                        ver.chooseBF(v, quary[2:])
addVertex()
q="bc"
for v in listVertex:
    v.setLastAndNext(listData)
for ve in listData:
    if ve[2]==q[0]:
        for v in listVertex:
            if v.name==ve[0]:
                v.chooseBF(ve[0],q)

print(result)
print ("######################################")
