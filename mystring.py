class MyString(str):
    
    def find_all(self,substr):
        self = self.lower()
        index_str = []
        for i in range(len(self)):
            if self.startswith(substr,i):
                index_str.append(i)
        return index_str
    
    def count_vowels(self):
        count_vow = 0
        vowes = "aioue"

        self = self.lower()
        for i in self:
            if i in vowes:
                count_vow += 1
        print(f"Count of Vowel is: {count_vow}")
    
    def is_palindrome(self):
        if self == self[::-1]:
            return True
        else:
            return False
    def upper(self):
        vowel= "aeiouAEIOU"
        result = []
        for char in self:
            if char in vowel:
                char =  char.upper()
                result.append(char)
            else:
                result.append(char)
        

        result = ''.join(result)
        print(result)



m1 = MyString("I really gad to learn python, but python is really hard.")
m2 = MyString("radar")
print(m1.find_all("python"))
m1.count_vowels()
print(f"is palindrome: {m2.is_palindrome()}")
m2.upper()