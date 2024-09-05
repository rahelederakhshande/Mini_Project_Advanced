class BookClub:
    total_members = 0
    def __init__(self,id_i,club_name,member_name,book_name) :
        self.id_i = id_i
        self.member_name = member_name
        self.book_name = book_name
        self.club_name = club_name
        self.members={}

    def add_member(self,member_name):
        
        self.members[member_name]=self.book_name
        BookClub.total_members +=1
        print(f"Added!>>> {self.members}")
        
    
    def display(self,id_i):
        if self.id_i == id_i:
            print()
            for i in self.members.items():
                print(f"ID:{self.id_i},Club Name: {self.club_name},{i}")
        else: 
            print("Not Found!")

    def remove(self,member_name):
        if member_name in self.members:
            del self.members[member_name]
            BookClub.total_members -=1
            print("removed!")
        else:
            print("Not found!")

    @classmethod
    def total_members_club(cls):
        print(f"Total Members: {cls.total_members}")
    
    





if __name__ == "__main__":
    b1=BookClub("1","History","ali","iran")
    b2=BookClub("1","History","alireza","iran1")
    b3=BookClub("2","Python","mina","iran2")
    b4=BookClub("2","Python","mona","iran3")
    b5=BookClub("2","Python","sina","iran4")
    b1.add_member("ali")
    b2.add_member("alireza")
    b3.add_member("mina")
    b4.add_member("mona")
    b5.add_member("sina")
    print(f"user1: {b1.total_members}")
    b1.display("1")
    b2.display("1")
    b3.display("2")
    b4.display("2")
    b5.display("2")
    
    b1.display("1")
    b2.display("1")
        
    BookClub.total_members_club()
    b1.remove("ali")
    BookClub.total_members_club()