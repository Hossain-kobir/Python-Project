class calculator:
    queue=[]
    
    def sum(self,a,b):
        add=a+b
        print(add)
        self.queue.append(add)
    
    def undo(self):
        while not self.queue.empty():
            v=self.queue.
    
    def redo(self):
        pass
    
while True:
    print("\nSelect Options:")
    print("option 1 Sum Two Value")
    print("option 2 Undo Previous Result")
    print("option 3 Redo Result")
    print("option 4 Terminate Programme")
    op=int(input("input option"))    # 6,8,10
    if op==1:
        a=int(input("Enter value A:"))
        b=int(input("Enter value B:"))
        sum(a,b)
    
    if op == 2:
        pass
    if op == 3:
        pass
    if op == 4:
        print("Terminate Programme Sucessfully")
        break