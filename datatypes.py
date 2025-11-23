
def array_impl():

    # Use python inbuild array
    print("Initialize array")
    arr = [1, 2, 3, 4, 5]

    # Access
    print("Testing array access")
    assert 1 == arr[0]

    # Insert
    print("Testing array insert")
    arr.append(6)
    
    assert 6 == len(arr)

    # Delete
    print("Testing array delete")
    del arr[5]

    assert 5 == len(arr)

# Class to represent a matrix
class Matrix:

    def __init__(self):
        self.data = []
        self.rows = 0
        self.cols = 0
        pass

    # Inserts a row of data into the matrix    
    def insert(self, row):
        if self.data:
            # All rows in a matrix must have the same number of columns
            assert len(self.data[0]) == len(row)
        
        self.data.append(row)

        self.rows += 1
        self.cols = len(row)

    # Retrieves a specific cell from the matrix
    def retrieve(self, row, col):
        assert row < self.rows and col < self.cols

        return self.data[row][col]

    # Deletes a row from the matrix
    def delete_row(self, row):
        assert row < self.rows

        del self.data[row]
        self.rows -= 1

    # Deletes a column from the matrix
    def delete_col(self, col):
        assert col < self.cols

        # Deleting a column requires traversing all the rows and deleting the columns
        for row in self.data:
            del row[col]

        self.cols -= 1

    # Returns the number of rows
    def size_rows(self):
        return self.rows

    # Returns the number of columns
    def size_cols(self):
        return self.cols

def matrix_impl():

    print("Initialize matrix")
    test_matrix = Matrix()

    # Insert
    print("Testing matrix insert")
    test_matrix.insert([1, 2, 3])

    assert 1 == test_matrix.size_rows()

    assert 3 == test_matrix.size_cols()

    # Access
    print("Testing matrix retrieve")
    assert 2 == test_matrix.retrieve(0, 1)

    # Insert 
    print("Testing matrix insert")
    test_matrix.insert([4, 5, 6])

    assert 2 == test_matrix.size_rows()

    # Delete row
    print("Testing matrix delete row")
    test_matrix.delete_row(0)

    assert 1 == test_matrix.size_rows()

    # Insert
    test_matrix.insert([1, 2, 3])

    # Delete column
    print("Testing matrix delete column")
    test_matrix.delete_col(1)

    assert 2 == test_matrix.size_cols()
    assert 6 == test_matrix.retrieve(0, 1)

# Class to represent a stack
class Stack:

    def __init__(self):
        self.data = []

    # Push an entry into the stack, making it the top of the stack
    def push(self, val):
        self.data.append(val)

    # Pop the top most entry from the stack
    def pop(self):
        return self.data.pop()

    # Get the top most entry from the stack
    def peek(self):
        return self.data[-1]

    # Get the size of the stack
    def size(self):
        return len(self.data)

def stack_impl():

    print("Initialize stack")
    test_stack = Stack()

    # Push
    print("Testing stack push")
    test_stack.push(1)

    # Push
    test_stack.push(2)

    # Peek
    print("Testing stack peek")
    assert 2 == test_stack.peek()

    # Pop
    print("Testing stack pop")
    assert 2 == test_stack.pop()

    # Peek
    assert 1 == test_stack.peek()

    # Size
    print("Testing stack size")
    assert 1 == test_stack.size()

# Class to represent a queue
class Queue:

    def __init__(self):
        self.data = []

    # Queue an item into the back of the queue
    def enqueue(self, val):
        self.data.append(val)

    # Remove and return the item from the front of the queue
    def dequeue(self):
        val = self.data[0]
        del self.data[0]
        return val

    # Get the item from the front of the queue
    def peek(self):
        return self.data[0]

    # Get the size of the queue
    def size(self):
        return len(self.data)

def queue_impl():

    print("Initialize queue")
    test_queue = Queue()

    # Enqueue
    print("Testing queue enqueue")
    test_queue.enqueue(1)

    # Enqueue
    test_queue.enqueue(2)

    # Peek
    print("Testing queue peek")
    assert 1 == test_queue.peek()

    # Dequeue
    print("Testing queue dequeue")
    assert 1 == test_queue.dequeue()

    # Peek
    assert 2 == test_queue.peek()

    # Size
    print("Testing queue size")
    assert 1 == test_queue.size()

# Class representing a node in the linked list
class Node:

    def __init__(self, val):
        # val holds the value of the node
        self.val = val
        # next points to the next node in the linked list
        self.next = None

# Class representing the linked list
class LinkedList:

    def __init__(self):
        # Head points to the first item in the list
        self.head = None
        self.count = 0

    # Get an item at specfied index in the linked list
    def get(self, index):
        curr = self.head
        idx = -1
        while curr:
            idx += 1
            if idx == index:
                return curr.val
            else:
                curr = curr.next
        
        return None

    # Find the position of a value in the linked list. First index of value is returned
    def search(self, val):
        curr = self.head
        idx = -1
        while curr:
            idx += 1
            if curr.val == val:
                break
            else:
                curr = curr.next
        
        return idx

    # Add an element to the front of the linked list
    def prepend(self, val):
        n_node = Node(val)
        n_node.next = self.head

        self.head = n_node
        self.count += 1

    # Add an element at the specified index
    def insert(self, index, val):
        if not self.head:
            self.head = Node(val)
            self.count += 1

            return
        
        if index == 0:
            self.prepend(val)

            return
        
        curr = self.head
        idx = -1
        while curr:
            idx += 1
            if idx == index - 1:
                n_node = Node(val)
                n_node.next = curr.next
                curr.next = n_node
                self.count += 1

                break
            else:
                curr = curr.next

    # Delete item at index
    def delete(self, index):

        if index == 0 and self.count:
            self.head = self.head.next
            self.count -= 1

            return
        
        curr = self.head
        idx = -1
        while curr:
            idx += 1
            if idx == index - 1 and curr.next:
                curr.next = curr.next.next
                self.count -= 1
                break
            else:
                curr = curr.next

    # Get the size of the linked list
    def size(self):
        return self.count

def linked_list_impl():

    test_ll = LinkedList()

    # Insert
    print("Testing linked list insert")
    test_ll.insert(0, 1)

    # Insert
    test_ll.insert(1, 2)

    # Get
    print("Testing linked list get")
    assert 1 == test_ll.get(0)

    # Get
    assert 2 == test_ll.get(1)

    # Prepend
    print("Testing linked list prepend")
    test_ll.prepend(3)

    # Get
    assert 3 == test_ll.get(0)

    # Size
    print("Testing linked list size")
    assert 3 == test_ll.size()

    # Delete
    print("Testing linked list delete")
    test_ll.delete(1)

    # Get
    assert 2 == test_ll.get(1)

    # Size
    assert 2 == test_ll.size()

if __name__ == "__main__":

    print("Testing arrays")
    array_impl()

    print("Testing matrix")
    matrix_impl()

    print("Testing stack")
    stack_impl()

    print("Testing queue")
    queue_impl()

    print("Testing linked list")
    linked_list_impl()

    print("OK")
