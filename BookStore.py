from SortableBook import Book
import ArrayList
import ArrayQueue
import RandomQueue
#import DLList
#import SLLQueue
#import ChainedHashTable
import BinarySearchTree
import BinaryHeap
#import AdjacencyList
import time



class BookStore:
    '''
    BookStore: It simulates a book system such as Amazon. It allows  searching,
    removing and adding in a shopping cart. 
    '''

    def __init__(self):
        self.bookCatalog = None
        self.shoppingCart = ArrayQueue.ArrayQueue()

    def loadCatalog(self, fileName: str):
        '''
            loadCatalog: Read the file filenName and creates the array list with all books.
                book records are separated by  ^. The order is key, 
                title, group, rank (number of copies sold) and similar books
        '''
        self.bookCatalog = ArrayList.ArrayList()
        with open(fileName, encoding="utf8") as f:
            # The following line is the time that the computation starts
            start_time = time.time()
            for line in f:
                (key, title, group, rank, similar) = line.split("^")
                s = Book(key, title, group, rank, similar)
                self.bookCatalog.append(s)
            # The following line is used to calculate the total time 
            # of execution
            elapsed_time = time.time() - start_time
            print(f"Loading {self.bookCatalog.size()} books in {elapsed_time} seconds")

    def setRandomShoppingCart(self):
        q = self.shoppingCart
        start_time = time.time()
        self.shoppingCart = RandomQueue.RandomQueue()
        while q.size() > 0:
            self.shoppingCart.add(q.remove())
        elapsed_time = time.time() - start_time
        print(f"Setting radomShoppingCart in {elapsed_time} seconds")

    def setShoppingCart(self):
        q = self.shoppingCart
        start_time = time.time()
        self.shoppingCart = ArrayQueue.ArrayQueue()
        while q.size() > 0:
            self.shoppingCart.add(q.remove())
        elapsed_time = time.time() - start_time
        print(f"Setting radomShoppingCart in {elapsed_time} seconds")

    def removeFromCatalog(self, i: int):
        '''
        removeFromCatalog: Remove from the bookCatalog the book with the index i
        input: 
            i: positive integer    
        '''
        # The following line is the time that the computation starts
        start_time = time.time()
        self.bookCatalog.remove(i)
        # The following line is used to calculate the total time 
        # of execution
        elapsed_time = time.time() - start_time
        print(f"Remove book {i} from books in {elapsed_time} seconds")

    def addBookByIndex(self, i: int):
        '''
        addBookByIndex: Inserts into the playlist the song of the list at index i 
        input: 
            i: positive integer    
        '''
        # Validating the index. Otherwise it  crashes
        if i >= 0 and i < self.bookCatalog.size():
            start_time = time.time()
            s = self.bookCatalog.get(i)
            self.shoppingCart.add(s)
            elapsed_time = time.time() - start_time
            print(f"Added to shopping cart {s} \n{elapsed_time} seconds")

    def removeFromShoppingCart(self):
        '''
        removeFromShoppingCart: remove one book from the shoppung cart  
        '''
        start_time = time.time()
        if self.shoppingCart.size() > 0:
            u = self.shoppingCart.remove()
            elapsed_time = time.time() - start_time
            print(f"removeFromShoppingCart {u} Completed in {elapsed_time} seconds")

    def bestsellers_with(self, infix, structure, n12 = 0):
        best_sellers = None
        if structure == 1:
            best_sellers = BinarySearchTree.BinarySearchTree()
        elif structure == 2:
            best_sellers = BinaryHeap.BinaryHeap()
        else:
            print("Invalid data structure.")

        if best_sellers is not None:
            if infix == "":
                print("Invalid infix.")
                return
        if n12 < 0:
            print('Invalid number of titles')
        else:
            start_time = time.time()
            if structure == 1:
                books0 = []
                for book in self.bookCatalog:
                    if infix in book.title:
                        best_sellers.add(book.rank, book)
                if best_sellers.r is None:
                    return
                best_sellers1 = best_sellers.in_order()
                if n12 == 0:
                    for i in range(len(best_sellers1) - 1, -1, -1):
                        print(best_sellers1[i])
                else:
                    for i in range(len(best_sellers1) - 1, len(best_sellers1) - (n12 + 1), -1):
                        if len(best_sellers1) > i > -1:
                            print(best_sellers1[i])

            elif structure == 2:
                books0 = []
                for book in self.bookCatalog:
                    if infix in book.title:
                        book.rank *= -1
                        best_sellers.add(book)
                best_sellers1 = []
                for i in range(best_sellers.n):
                    best_sellers1.append(best_sellers.remove())
                for book in best_sellers1:
                    book.rank *= -1
                if n12 == 0:
                    for i in range(len(best_sellers1)):
                        print(best_sellers1[i])
                else:
                    for i in range(min(n12, len(best_sellers1))):
                        print(best_sellers1[i])
            elapsed_time = time.time() - start_time
            print(f"Displayed bestsellers_with({infix}, {structure}, {n12}) in {elapsed_time} seconds")


    def display_catalog(self, n):
        for i in range(n):
            print(self.bookCatalog[i])