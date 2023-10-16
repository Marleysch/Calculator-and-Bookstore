Calculator 

The calculator exemplifies the use of Stacks, HashTables and BinaryTrees. It allows defining mathematical expression with variables, assigning values to the variables and evaluate it.

BookStore

BookStore uses a fraction of the Amazon database to exemplify the use of several data structures
such as Queues, Lists, HashTables, BinarySearch Trees, Heaps, Graphs and sorting. The program
allows adding books to a shopping cart. 

The entry point (main program) is the file main.py. That is done using the 
following lines: 

if __name__ == "__main__":
    main()

To run the program in command line use:

% python3.8 main.py

In Pycharm you can use the options in the "run" tab.

The program will present the main menu with three options:
        1 Calculator
        2 Bookstore System
        0 Exit/Quit
Pressing 1 or 2 and the enter will take you to a second menu with different 
options. The python function that allows to accept an input from the keyboard 
is input(). Use the same pattern to add new options accordingly.

The project is organized in different files (modules):
main.py: The main entry point of the program. It will present the menu that executes the assignments
Calculator.py: The calculator system 
BookStore.py: The book store system 
Book.py: Data class that holds the attributes of a book. The class allows to compare ranks using the operator < or >
SortableBook.py: Data class that holds the attributes of a book. The class allows to compare by alphabetical order using the operator < or >
Interfaces.py: The interfaces: Stack, Queue, Deque, List, Set, Graph
ArrayStack.py: Implements interface Stack
ArrayQueue.py: Implements interface Queue
ArrayList.py: Implements interface List
ArrayDeque.py: Implements interface Deque. It is a specialization (Inheritance) of ArrayList
RandomQueue.py: Implements interface Queue. It is a specialization (Inheritance) of ArrayQueue
SLLStack.py: Implements interface Stack
SLLQueue.py: Implements interface Queue
DLList.py: Implements interface List
DLLDeque.py: It implements the interface Deque. It is a specialization (Inheritance) of DLLList.
ChainedHashTable.py: It implements the interface Set
BinarySearchTree.py: It implements the interface Set
BinaryHeap.py: It implements the interface Queue. It removes the element with highest priority
AdjacencyList.py: It implements the Graph interface using the adjencency list
AdjacencyMatrix.py: It implements the Graph interface in using the adjacency matrix


Stack
    |- ArrayStack
    |- SLLStack     
Queue   
    |- ArrayQueue
            |- RandomQueue
            |- MaxQueue
    |- SLLQueue
    |- BinaryHeap
List                            Dequeue
    |- ArrayList                 |
                |- ArrayDeque   -|
    |- DLList                    |
                |- DLLDeque     -|
Set
    |- ChainedHashTable
    |- BinarySearchTree
Graph
    |- AdjacencyMatrix
    |- AdjacencyList


