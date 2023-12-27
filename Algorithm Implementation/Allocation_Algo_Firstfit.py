import matplotlib.pyplot as plt
from IPython.display import display, clear_output
import time

class MemoryAllocator:
    def __init__(self, total_memory):
        self.total_memory = total_memory
        self.memory = [0] * total_memory  # Memory block initialized to 0 (unallocated)
        self.allocations = []  # A list to keep track of allocated memory blocks

    def first_fit(self, size):
        start = -1
        for i in range(self.total_memory):
            if self.memory[i] == 0:
                current_size = 0
                while i < self.total_memory and self.memory[i] == 0:
                    current_size += 1
                    i += 1
                if current_size >= size:
                    start = i - current_size
                    break

        if start != -1:
            for i in range(start, start + size):
                self.memory[i] = 1  # Allocate memory
            self.allocations.append((start, start + size))
            return start
        else:
            return -1  # Allocation failed

    def deallocate(self, start):
        deallocated_allocation = None
        for allocation in self.allocations:
            if allocation[0] == start:
                deallocated_allocation = allocation
                break

        if deallocated_allocation:
            self.allocations.remove(deallocated_allocation)

            # Deallocate memory
            for i in range(start, deallocated_allocation[1]):
                self.memory[i] = 0

    def visualize(self):
        plt.figure()  # Create a new figure for visualization
        plt.xlim(0, self.total_memory)
        plt.ylim(0, 1)

        for allocation in self.allocations:
            plt.broken_barh([allocation], (0, 1), facecolors='blue')

        plt.xlabel('Memory')
        plt.title('Memory Allocation and Fragmentation (First-Fit)')
        plt.show()  # Display the plot

def main():
    total_memory = 100
    memory_allocator = MemoryAllocator(total_memory)

    while True:
        print("1. Allocate memory")
        print("2. Deallocate memory")
        print("3. Visualize")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            size = int(input("Enter memory size to allocate: "))
            start = memory_allocator.first_fit(size)

            if start != -1:
                print(f"Memory allocated at address {start}")
            else:
                print("Memory allocation failed. Not enough contiguous memory.")

        elif choice == '2':
            start = int(input("Enter the memory address to deallocate: "))
            memory_allocator.deallocate(start)
            clear_output(wait=True)  # Clear the output in Jupyter Notebook

        elif choice == '3':
            memory_allocator.visualize()

        elif choice == '4':
            break

        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
