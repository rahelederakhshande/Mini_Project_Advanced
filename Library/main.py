from library import *
from librarian import *
from member import *
from book import *

if __name__ == "__main__":
    l = Library('dehkhoda')
    li = Librarian('meisam', 25, '1256')
    m = Member('hossein', 28, '4589')
    m1 = Member('ali', 23, '445459')

    b = Book(123, 'python', 'john', '6988-5269-52')

    l.add_data(li)
    l.add_data(m)
    l.add_data(b)
    l.add_data(m1)
    l.display()
