from person import *
class Member(Person):
    last_id = 1000
    def __init__(self, name, age, member_id):
        id_ = "M" + str(Member.last_id)
        super().__init__(name, age, id_)
        self.member_id = member_id
        Member.last_id += 1

    def introduce(self):
        return f"Member {self.name} Id: {self.member_id}"