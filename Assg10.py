def stack_operations():
    stack = []  # Creating an empty stack
    # Push function to add elements to the stack
    def push_stack(element):
        stack.append(element)
        print(f"Pushed element '{element}' onto the stack.")

    # Pop function to remove elements from the stack
    def pop_stack():
        if not stack:
            print("Stack is empty. Cannot pop.")
            return None
        else:
            popped_element = stack.pop()
            print(f"Popped element from the stack: {popped_element}")
            return popped_element

    while True:
        print("\nStack Operations:")
        print("1. Push")
        print("2. Pop")
        print("3. Exit")

        choice = input("Enter your choice (1/2/3): ")

        if choice == '1':
            element = input("Enter element to push: ")
            push_stack(element)
        elif choice == '2':
            popped = pop_stack()
            if popped is not None:
                print("Element popped:", popped)
        elif choice == '3':
            print("Exiting stack operations.")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

# Queue operations
def queue_operations():
    queue = []  # Creating an empty queue

    # Enqueue function to add elements to the queue
    def enqueue(element):
        queue.append(element)
        print(f"Enqueued element '{element}'.")

    # Dequeue function to remove elements from the queue
    def dequeue():
        if not queue:
            print("Queue is empty. Cannot dequeue.")
            return None
        else:
            dequeued_element = queue.pop(0)
            print(f"Dequeued element from the queue: {dequeued_element}")
            return dequeued_element

    while True:
        print("\nQueue Operations:")
        print("1. Enqueue")
        print("2. Dequeue")
        print("3. Exit")

        choice = input("Enter your choice (1/2/3): ")

        if choice == '1':
            element = input("Enter element to enqueue: ")
            enqueue(element)
        elif choice == '2':
            dequeued = dequeue()
            if dequeued is not None:
                print("Element dequeued:", dequeued)
        elif choice == '3':
            print("Exiting queue operations.")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

# Ask user for stack or queue operations
while True:
    print("\nChoose data structure:")
    print("1. Stack Operations")
    print("2. Queue Operations")
    print("3. Exit")

    data_structure_choice = input("Enter your choice (1/2/3): ")

    if data_structure_choice == '1':
        stack_operations()
    elif data_structure_choice == '2':
        queue_operations()
    elif data_structure_choice == '3':
        print("Exiting the program.")
        break
    else:
        print("Invalid choice. Please enter 1, 2, or 3.")