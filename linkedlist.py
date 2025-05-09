class linkedlistNode:
    
    def __init__(self,value,nextNode=None):
        self.value = value
        self.nextNode = nextNode

node1=linkedlistNode(3)
node2=linkedlistNode(2)
node3=linkedlistNode(56)
#CREATING RELATION BETWEEN THE FIRST NODE AND THE NEXT NODE

node1.nextNode = node2
node2.nextNode = node3
#node1 -> node2 -> node->3

currentValue = node1
while True:
    print  (currentValue.value, end=" --> ")
    if currentValue.nextNode is None:#PREVENTS THE TAIL FROM BEING THE NEXT NODE IN LIST
         print ("None")
         break    
    #IT FIRST PRINTS THE FIRST NODE AND IF THE NEXT NODE IS NONE ,IT PRINTS NONE
    #OTHERWISE IT PRINTS THE NEXT NODE WHICH IS 2
    currentValue = currentValue.nextNode