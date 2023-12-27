import matplotlib.pyplot as plt

class MemoryAllocator:
    def __init__(self, total_memory):
        self.total_memory = total_memory
        self.memory = [0] * total_memory  # Memory block initialized to 0 (unallocated)
        self.allocations = []  # A list to keep track of allocated memory blocks
        self.fig, self.ax = plt.subplots()

    def worst_fit(self, size):
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
        self.ax.clear()
        self.ax.set_xlim(0, self.total_memory)
        self.ax.set_ylim(0, 1)

        for allocation in self.allocations:
            self.ax.broken_barh([allocation], (0, 1), facecolors='blue')

        plt.xlabel('Memory')
        plt.title('Memory Allocation and Fragmentation (Worst-Fit)')
        plt.show()

    def redraw(self):
        self.ax.clear()
        self.ax.set_xlim(0, self.total_memory)
        self.ax.set_ylim(0, 1)

        for allocation in self.allocations:
            self.ax.broken_barh([allocation], (0, 1), facecolors='blue')

        plt.xlabel('Memory')
        plt.title('Memory Allocation and Fragmentation (Worst-Fit)')
        plt.draw()

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
            start = memory_allocator.worst_fit(size)

            if start != -1:
                print(f"Memory allocated at address {start}")
                memory_allocator.redraw()  # Redraw the plot immediately after allocation
            else:
                print("Memory allocation failed. Not enough contiguous memory.")

        elif choice == '2':
            start = int(input("Enter the memory address to deallocate: "))
            memory_allocator.deallocate(start)
            memory_allocator.redraw()  # Redraw the plot immediately after deallocation

        elif choice == '3':
            memory_allocator.visualize()

        elif choice == '4':
            break

        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
