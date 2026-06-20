class movie:
    def __init__(self,movie_name : str,total_seats:int,ticket_price:int):
        self.movie_name=movie_name
        self.total_seats=total_seats
        self.ticket_price=ticket_price
        self.book_seats=0
    def book_ticket(self,num_tickets):
        if num_tickets>self.total_seats-self.book_seats:
            print(f"sorry ,no more seats are avaialable , seats available {self.total_seats}")
        else:
            self.book_seats+=num_tickets
            self.total_seats-=num_tickets
            print(f"congrats ! your ticket has been booked")
            print(f"total ticket fare {num_tickets*self.ticket_price}") 
               
    def show_status(self):
        print(f"movies name = {self.movie_name}") 
        print(f"total seats available {self.total_seats}")
        print(f"total price ={self.ticket_price}")   
    
film1=movie("avatar",100,399)   
film1.book_ticket(40)
film1.show_status()   



  
        