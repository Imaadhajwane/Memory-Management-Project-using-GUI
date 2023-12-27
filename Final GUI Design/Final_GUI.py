import tkinter as tk
from tkinter import ttk
from tkinter import simpledialog
import matplotlib.pyplot as plt


class MemoryPartition:
    """Class for memory partition"""

    def __init__(self, name, size):
        self.name = name
        self.size = size
        self.process = None


class Process:
    """Class for process"""

    def __init__(self, size):
        self.size = size
        self.starting_address = None
        self.ending_address = None


class MemoryAllocatorApp:
    """Class for GUI"""

    def __init__(self, root):
        """Initialize GUI"""
        self.root = root
        self.root.title("Memory Fragmentation Analysis Tool")
        self.root.geometry("900x500")

        # Define label and entry fonts and styles
        label_font = ('Helvetica', 16)
        label_style = {'bg': 'lightblue', 'fg': 'darkblue', 'font': label_font}
        entry_font = ('Helvetica', 14)
        entry_style = {'font': entry_font, 'font': label_font}

        custom_font = ttk.Style()
        custom_font.configure("TLabel", **label_style)
        custom_font.configure("TEntry", **entry_style)

        custom_button_style = ttk.Style()
        custom_button_style.configure("Custom.TButton", font=(
            "TkDefaultFont", 14), background="light blue", foreground="dark blue")

        self.total_memory_label = ttk.Label(
            root, text="Enter total memory size:", style="TLabel")
        self.total_memory_label.grid(row=0, column=0, padx=10, pady=10)
        self.total_memory_entry = ttk.Entry(root, style="TEntry")
        self.total_memory_entry.grid(row=0, column=1, padx=10, pady=10)

        self.num_processes_label = ttk.Label(
            root, text="Enter the number of processes:", style="TLabel")
        self.num_processes_label.grid(row=1, column=0, padx=10, pady=10)
        self.num_processes_entry = ttk.Entry(root, style="TEntry")
        self.num_processes_entry.grid(row=1, column=1, padx=10, pady=10)

        self.fragmentation_type_label = ttk.Label(
            root, text="Select fragmentation type:", style="TLabel")
        self.fragmentation_type_label.grid(row=2, column=0, padx=10, pady=10)
        self.fragmentation_type = ttk.Combobox(
            root, values=["Internal Fragmentation", "External Fragmentation"])
        self.fragmentation_type.grid(row=2, column=1, padx=10, pady=10)

        self.submit_button = ttk.Button(
            root, text="Submit", command=self.submit, style="Custom.TButton")
        self.submit_button.grid(
            row=2, column=3, columnspan=2, padx=10, pady=10)

        self.processes = []
        self.partitions = []
        self.allocation_info = {}
        self.total_memory = 0

    def submit(self):
        """Submit button callback"""
        total_memory = self.total_memory_entry.get()
        num_processes = self.num_processes_entry.get()
        fragmentation_type = self.fragmentation_type.get()

        if not total_memory.isnumeric():
            self.display_error(
                "Please enter a valid numeric value for total memory size.")
            return

        if not num_processes.isnumeric():
            self.display_error(
                "Please enter a valid positive integer for the number of processes.")
            return

        self.total_memory = float(total_memory)

        if fragmentation_type == "Internal Fragmentation":
            self.processes = []
            for i in range(int(num_processes)):
                process_size_str = self.get_process_input(i+1)
                if process_size_str and process_size_str.isnumeric():
                    process_size = float(process_size_str)
                    self.processes.append(Process(process_size))
                else:
                    self.display_error(
                        f"Please enter a valid numeric value for process {i + 1} size.")
                    return

            self.partitions = [MemoryPartition(f"Block {i + 1}", self.total_memory / len(self.processes))
                               for i in range(len(self.processes))]
            self.allocation_info = {process: [] for process in self.processes}

            self.display_fragmentation_algorithm_options()

        elif fragmentation_type == "External Fragmentation":
            self.processes = []
            total_memory_processor = 0
            process_number = 1
            while total_memory_processor < self.total_memory:
                process_size_str = self.get_process_input(process_number)
                if process_size_str and process_size_str.isnumeric():
                    process_size = float(process_size_str)
                    if total_memory_processor + process_size <= self.total_memory:
                        self.processes.append(Process(process_size))
                        total_memory_processor += process_size
                        process_number += 1
                    else:
                        self.display_error(
                            f"Process {len(self.processes) + 1} with size {process_size} cannot be allocated and is terminated.")
                else:
                    self.display_error(
                        f"Please enter a valid numeric value for process {len(self.processes) + 1} size.")
                    return

            self.partitions = [MemoryPartition(f"Block {i + 1}", process.size)
                               for i, process in enumerate(self.processes)]
            self.allocation_info = {process: [] for process in self.processes}

            self.display_fragmentation_algorithm_options()

    def best_fit(self):
        """Best fit algorithm"""
        for process in self.processes:
            best_fit_partition = None
            best_fit_size = float('inf')

            for partition in self.partitions:
                if not partition.process and partition.size >= process.size:
                    if partition.size - process.size < best_fit_size:
                        best_fit_partition = partition
                        best_fit_size = partition.size - process.size

            if best_fit_partition:
                best_fit_partition.process = process
                process.starting_address = best_fit_partition.name
                process.ending_address = f"{
                    best_fit_partition.name}+{process.size}"
                self.allocation_info[process].append(best_fit_partition.name)
            else:
                self.display_error(
                    f"Process with size {process.size} cannot be allocated and is terminated.")

        self.display_memory_info()

    def worst_fit(self):
        """Worst fit algorithm"""
        for process in self.processes:
            worst_fit_partition = None
            worst_fit_size = -1

            for partition in self.partitions:
                if not partition.process and partition.size >= process.size:
                    if partition.size > worst_fit_size:
                        worst_fit_partition = partition
                        worst_fit_size = partition.size

            if worst_fit_partition:
                worst_fit_partition.process = process
                process.starting_address = worst_fit_partition.name
                process.ending_address = f"{
                    worst_fit_partition.name}+{process.size}"
                self.allocation_info[process].append(worst_fit_partition.name)
            else:
                self.display_error(
                    f"Process with size {process.size} cannot be allocated and is terminated.")

        self.display_memory_info()

    def first_fit(self):
        """First fit algorithm"""
        for process in self.processes:
            allocated = False
            for partition in self.partitions:
                if not partition.process and partition.size >= process.size:
                    partition.process = process
                    process.starting_address = partition.name
                    process.ending_address = f"{partition.name}+{process.size}"
                    self.allocation_info[process].append(partition.name)
                    allocated = True
                    break
            if not allocated:
                self.allocation_info[process].append("Not Allocated")

        self.display_memory_info()

    def display_error(self, message):
        """Display error message"""
        error_label = ttk.Label(self.root, text=message, foreground="red")
        error_label.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

    def get_process_input(self, process_number):
        """Get input for process"""
        process_size_str = simpledialog.askstring(
            "Process Size", f"Enter memory requirement for process {process_number}: ")
        if process_size_str and process_size_str.isnumeric():
            process_size = float(process_size_str)
            process_info_label = ttk.Label(
                self.root, text=f"Memory required for process {process_number}: {process_size}", foreground="black")
            process_info_label.grid(
                row=8 + process_number, column=0, columnspan=2, padx=10, pady=5)
            return process_size_str
        return None

    def display_fragmentation_algorithm_options(self):
        """Display fragmentation algorithm options"""
        self.allocation_algorithm_label = ttk.Label(
            self.root, text="Select allocation algorithm:")
        self.allocation_algorithm_label.grid(row=5, column=0, padx=10, pady=10)
        self.allocation_algorithm = ttk.Combobox(
            self.root, values=["Best Fit", "Worst Fit", "First Fit"])
        self.allocation_algorithm.grid(row=5, column=1, padx=10, pady=10)

        self.memory_info_button = ttk.Button(
            self.root, text="Allocate Memory + Show Graph", command=self.allocate_memory, style="Custom.TButton")
        self.memory_info_button.grid(row=6, column=0, padx=10, pady=10)

        self.clear_button = ttk.Button(
            self.root, text="Clear", command=self.clear, style="Custom.TButton")
        self.clear_button.grid(row=6, column=1, columnspan=2, padx=10, pady=10)

    def allocate_memory(self):
        """Allocate memory"""
        allocation_algorithm = self.allocation_algorithm.get()
        for partition in self.partitions:
            partition.process = None

        for process in self.processes:
            process.starting_address = None
            process.ending_address = None
            self.allocation_info[process] = []

        if allocation_algorithm == "Best Fit":
            self.best_fit()
        elif allocation_algorithm == "Worst Fit":
            self.worst_fit()
        elif allocation_algorithm == "First Fit":
            self.first_fit()
        else:
            self.display_error("Please select a valid allocation algorithm.")

        for widget in self.root.winfo_children():
            if widget.winfo_class() == 'Labelframe':
                widget.destroy()

    def display_memory_info(self):
        """Display memory information"""
        data = []

        block_labels = []
        process_numbers = []
        block_statuses = []
        space_required = []
        block_sizes = []
        unused_space = []

        for partition in self.partitions:
            process = partition.process
            block_name = partition.name
            block_size = partition.size
            process_status = "Used" if process else "Empty"
            space_req = process.size if process else 0
            unused = block_size - space_req if process else block_size

            if process:
                process_number = self.processes.index(process) + 1
            else:
                process_number = "N/A"

            block_labels.append(block_name)
            process_numbers.append(process_number)
            block_statuses.append(process_status)
            space_required.append(space_req)
            block_sizes.append(block_size)
            unused_space.append(unused)

        headers = [
            "Block Name",
            "Process No",
            "Block Status",
            "Space Required",
            "Block Size",
            "Unused Space"
        ]

        data = list(zip(block_labels, process_numbers, block_statuses,
                        space_required, block_sizes, unused_space))

        memory_info_table = ttk.LabelFrame(
            self.root, text="Memory Partition Information")
        memory_info_table.grid(row=8, column=0, columnspan=2, padx=10, pady=10)

        table_frame = tk.Frame(memory_info_table)
        table_frame.grid(row=0, column=0, padx=10, pady=10)

        tree = ttk.Treeview(table_frame, columns=headers, show="headings")
        for header in headers:
            tree.heading(header, text=header)
            tree.column(header, width=100)
        for row in data:
            tree.insert('', 'end', values=row)
        tree.pack()

        num_blocks = len(self.partitions)
        x = range(num_blocks)
        bar_width = 0.15

        fig, ax = plt.subplots(figsize=(12, 6))
        bar1 = ax.bar(x, space_required, bar_width,
                      label="Space Required", color="g")
        bar2 = ax.bar([i + bar_width for i in x], block_sizes,
                      bar_width, label="Block Size", color="b")
        bar3 = ax.bar([i + 2 * bar_width for i in x], unused_space,
                      bar_width, label="Unused Space", color="r")

        ax.set_xlabel("Block Names")
        ax.set_ylabel("Size")
        ax.set_title("Memory Partition Information")
        ax.set_xticks([i + bar_width for i in x])
        ax.set_xticklabels(block_labels)
        ax.legend()

        plt.show()

    def clear(self):
        """Clear GUI"""
        for widget in self.root.winfo_children():
            widget.destroy()
        self.__init__(self.root)


def main():
    root = tk.Tk()
    app = MemoryAllocatorApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()
