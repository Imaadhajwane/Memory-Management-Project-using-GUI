import matplotlib.pyplot as plt
import random

class MemoryAllocator:
    def __init__(self, total_memory):
        self.total_memory = total_memory
        self.memory = [0] * total_memory  # Memory block initialized to 0 (unallocated)
        self.allocations = []  # A list to keep track of allocated memory blocks

    def best_fit(self, size):
        best_fit_index = -1
        best_fit_size = float('inf')

        for i in range(self.total_memory):
            if self.memory[i] == 0:
                current_size = 0
                while i < self.total_memory and self.memory[i] == 0:
                    current_size += 1
                    i += 1

                if current_size >= size and current_size < best_fit_size:
                    best_fit_size = current_size
                    best_fit_index = i - current_size

        if best_fit_index != -1:
            for i in range(best_fit_index, best_fit_index + size):
                self.memory[i] = 1  # Allocate memory
            self.allocations.append((best_fit_index, best_fit_index + size))
            return best_fit_index
        else:
            return -1  # Allocation failed

    def deallocate(self, start):
        for allocation in self.allocations:
            if allocation[0] == start:
                self.allocations.remove(allocation)
                for i in range(start, allocation[1]):
                    self.memory[i] = 0  # Deallocate memory
                break

    def visualize(self):
        fig, ax = plt.subplots()
        ax.set_xlim(0, self.total_memory)
        ax.set_ylim(0, 1)

        for allocation in self.allocations:
            ax.broken_barh([allocation], (0, 1), facecolors='blue')

        plt.xlabel('Memory')
        plt.title('Memory Allocation and Fragmentation (Best-Fit)')
        plt.show()

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
            start = memory_allocator.best_fit(size)

            if start != -1:
                print(f"Memory allocated at address {start}")
            else:
                print("Memory allocation failed. Not enough contiguous memory.")

        elif choice == '2':
            start = int(input("Enter the memory address to deallocate: "))
            memory_allocator.deallocate(start)

        elif choice == '3':
            memory_allocator.visualize()

        elif choice == '4':
            break

        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
