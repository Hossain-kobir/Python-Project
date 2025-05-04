class StarCinema:
    HallList=[]
    # def __init__(self,name):
    #     self.name=name
        
    
    @staticmethod
    def EntryHall(Hall):
        StarCinema.HallList.append(Hall)

class Hall(StarCinema):
    def __init__(self,rows,cols,hall_no,name):
        self.seats={}
        self.show_list=[]
        self.rows=rows
        self.cols=cols
        self.hall_no=hall_no
        self.name=name
        StarCinema.EntryHall(self)
        
    def __repr__(self):
        return f"seat : {self.seats} Show List :{self.show_list} Rows {self.rows} Cols {self.cols} hall no {self.hall_no}"
        
    
    def EntryShow(self,Id,MovieName,Time):
        self.show_list.append((Id,MovieName,Time))
        self.seats[Id]=[[0]*self.cols for _ in range(self.rows)]
    
    def BookSeat(self,id,row,col):
        if row >= self.rows or col >= self.cols:
            print("No valid seat")
            return

        seat=self.seats[id]
        
        if seat[row][col] == 1:
            print(f"Seat Row {row} Col {col} is already booked")
        else:
            seat[row][col] = 1
            for s in self.show_list:
                if s[0]==id: # Eta show list er tuple er id/cinema name match koracci
                    print(s[1])
                    
                    # self.ViewAvailableSeat(id)
                    # for i in range(len(seat)):
                    #     for j in range(len(seat[i])):
                    #         print(seat[i][j],end=" ")
                    #     print()    
                    
                    for row in range(self.rows):
                        for col in range(self.cols):
                            # print(seat[row][col]) # 00 01 Booked 03 04
                            if seat[row][col] == 1:
                                print("Booked",end="*")
                            else:
                                print(f"{row}{col}".center(6),end=" ")
                        print()

    def viewShowList(self):
        print(f"Shows Are Runnig in {self.name}")
        for show in self.show_list:
            print(show,end="  \n")
            # print( f"Shows Are Running in {self.name} \n {show}")                
                        
    
    def ViewAvailableSeat(self,Id):
        if Id in self.seats:
            seat=self.seats[Id]
            print(f"Here is your Show Id :{Id}")
            
            for row in range(self.rows):
                for col in range(self.cols):
                    if seat[row][col]==1:
                        print("Booked",end=" ")
                    
                    else:
                        print(f"({row}{col})".center(6),end=" ")
                print()
        else:
            print("No Id Is Here Ok Bro :")
            
            
            
            
            
            
            
            
            
            
            
            
        # seat=self.seats[Id]

        # for row in range(self.rows):
        #     for col in range(self.cols):
        #         if seat[row][col]==1:
        #             print("Booked",end=" ")
        #         else:
                    # print(f"({row} {col})".center(6),end=" ")
        #     print()

# name=StarCinema("Star Cinema")
hall1=Hall(10,10,111,"Star Cinema")
hall1.EntryShow("111","Radhy Your Most wanted Bhai","10.00AM")
hall1.EntryShow("112","Salar Ceesfire-2","10.00AM")
# hall1.BookSeat("111",0,1)
# hall1.viewShowList()
# hall1.ViewAvailableSeat("111")

    # print(self.name)
for hn in hall1.HallList:
    print(f"\nWelcome to {hn.name}")
while True:
            
    print("\nSelect Options :")
    print("\noptions 1 View All Shows")
    print("options 2 View Avaiable Seat")
    print("options 3 Book Tickets\n")
    print("options 4 Terminate The Program\n")
    
    
    option=int(input())
    if option == 1:
        print("View All Shows Today :")
        hall1.viewShowList()
    
    if option == 2:
        
        id=input("Please Enter Show Id:")
        hall1.ViewAvailableSeat(id)
    
    if option == 3:
        id=input("Please Enter Movie Id:")
        if id not in hall1.seats.keys():
            print("Movie Not Found")
            # continue Question ekhane ki continue statement er kono kaj ase ki ?
            
        else:
            row=int(input("Enter Row of the seat :"))
            col=int(input("Enter col of the seat :"))
            hall1.BookSeat(id,row,col)
    
    if option == 4:
        print("Terminate Programme Sucessfully")
        break
    
        

    