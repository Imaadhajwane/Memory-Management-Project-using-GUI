import matplotlib.pyplot as plt

class MemoryAllocator:
    def __init__(self, total_memory):
        self.total_memory = total_memory
        self.memory = [0] * total_memory  # Memory block initialized to 0 (unallocated)
        self.allocations = []  # A list to keep track of allocated memory blocks
        self.fig, self.ax = plt.subplots()

    def first_fit(self, size):
        # First-fit memory allocation strategy implementation (similar to previous examples)
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

    def best_fit(self, size):
        # Best-fit memory allocation strategy implementation
        best_fit_start = -1
        best_fit_size = float('inf')

        for i in range(self.total_memory):
            if self.memory[i] == 0:
                current_size = 0
                while i < self.total_memory and self.memory[i] == 0:
                    current_size += 1
                    i += 1

                if current_size >= size and current_size < best_fit_size:
                    best_fit_start = i - current_size
                    best_fit_size = current_size

        if best_fit_start != -1:
            for i in range(best_fit_start, best_fit_start + size):
                self.memory[i] = 1  # Allocate memory
            self.allocations.append((best_fit_start, best_fit_start + size))
            return best_fit_start
        else:
            return -1  # Allocation failed

    def worst_fit(self, size):
        # Worst-fit memory allocation strategy implementation
        worst_fit_start = -1
        worst_fit_size = 0
        current_start = -1
        current_size = 0

        for i in range(self.total_memory):
            if self.memory[i] == 0:
                current_size += 1

                if current_start == -1:
                    current_start = i

                if current_size >= size:
                    if current_size > worst_fit_size:
                        worst_fit_start = current_start
                        worst_fit_size = current_size

                    current_start = -1
                    current_size = 0

        if worst_fit_start != -1:
            for i in range(worst_fit_start, worst_fit_start + size):
                self.memory[i] = 1  # Allocate memory
            self.allocations.append((worst_fit_start, worst_fit_start + size))
            return worst_fit_start
        else:
            return -1  # Allocation failed

    def deallocate(self, start):
        # Deallocation logic (similar to previous examples)
        for allocation in self.allocations:
            if allocation[0] == start:
                self.allocations.remove(allocation)

                for i in range(start, allocation[1]):
                    self.memory[i] = 0  # Deallocate memory
                break

    def visualize(self):
        # Visualization logic (similar to previous examples)
        self.ax.clear()
        self.ax.set_xlim(0, self.total_memory)
        self.ax.set_ylim(0, 1)

        for allocation in self.allocations:
            self.ax.broken_barh([allocation], (0, 1), facecolors='blue')

        plt.xlabel('Memory')
        plt.title('Memory Allocation and Fragmentation')
        plt.show()

    def redraw(self):
        # Redraw the plot (similar to previous examples)
        self.ax.clear()
        self.ax.set_xlim(0, self.total_memory)
        self.ax.set_ylim(0, 1)

        for allocation in self.allocations:
            self.ax.broken_barh([allocation], (0, 1), facecolors='blue')

        plt.xlabel('Memory')
        plt.title('Memory Allocation and Fragmentation')
        plt.draw()

def main():
    total_memory = int(input("Enter the total memory size: "))
    memory_allocator = MemoryAllocator(total_memory)

    while True:
        print("\nMemory Allocation Strategies:")
        print("1. First Fit")
        print("2. Best Fit")
        print("3. Worst Fit")
        print("4. Deallocate memory")
        print("5. Visualize")
        print("6. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            size = int(input("Enter memory size to allocate (First Fit): "))
            start = memory_allocator.first_fit(size)
            if start != -1:
                print(f"Memory allocated at address {start}")
                memory_allocator.redraw()
            else:
                print("Memory allocation failed. Not enough contiguous memory.")

        elif choice == '2':
            size = int(input("Enter memory size to allocate (Best Fit): "))
            start = memory_allocator.best_fit(size)
            if start != -1:
                print(f"Memory allocated at address {start}")
                memory_allocator.redraw()
            else:
                print("Memory allocation failed. Not enough contiguous memory.")

        elif choice == '3':
            size = int(input("Enter memory size to allocate (Worst Fit): "))
            start = memory_allocator.worst_fit(size)
            if start != -1:
                print(f"Memory allocated at address {start}")
                memory_allocator.redraw()
            else:
                print("Memory allocation failed. Not enough contiguous memory.")

        elif choice == '4':
            start = int(input("Enter the memory address to deallocate: "))
            memory_allocator.deallocate(start)
            memory_allocator.redraw()

        elif choice == '5':
            memory_allocator.visualize()

        elif choice == '6':
            print("Exiting the program.")
            break

        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
