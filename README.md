# Memory Allocation Algorithms

This repository implements three memory allocation algorithms: Best-Fit, First-Fit, and Worst-Fit. 
Each algorithm has its unique approach to managing and allocating memory.  


## Best-Fit

Best-Fit allocates memory by selecting the smallest available block that fits the requested size. This algorithm minimizes wasted memory but may lead to fragmentation.

### Steps:
1. Initialize a memory block with zeros (unallocated).
2. Implement the `best_fit` method to find the best fit for a given memory size.
3. Allocate memory by marking the selected block as allocated.
4. Keep track of allocations in the `allocations` list.
5. Implement the `deallocate` method to free up previously allocated memory.
6. Visualize memory allocations and fragmentation using the `visualize` method.

## First-Fit

First-Fit allocates memory by selecting the first available block that is large enough to accommodate the requested size. This algorithm is simple but may lead to fragmentation.

### Steps:
1. Initialize a memory block with zeros (unallocated).
2. Implement the `first_fit` method to find the first fit for a given memory size.
3. Allocate memory by marking the selected block as allocated.
4. Keep track of allocations in the `allocations` list.
5. Implement the `deallocate` method to free up previously allocated memory.
6. Visualize memory allocations and fragmentation using the `visualize` method.

## Worst-Fit

Worst-Fit allocates memory by selecting the largest available block, even if it is larger than the requested size. This algorithm can lead to less fragmentation but may result in wasted memory.

### Steps:
1. Initialize a memory block with zeros (unallocated).
2. Implement the `worst_fit` method to find the worst fit for a given memory size.
3. Allocate memory by marking the selected block as allocated.
4. Keep track of allocations in the `allocations` list.
5. Implement the `deallocate` method to free up previously allocated memory.
6. Visualize memory allocations and fragmentation using the `visualize` method.
7. Introduce the `redraw` method to update visualizations immediately after allocation or deallocation.

# GUI for Memory Allocation Algorithms

This repository also include a GUI for memory allocation algorithms.

The Memory Fragmentation Analysis Tool is a Python application that provides a graphical user interface (GUI) for analyzing memory fragmentation using different allocation algorithms. 

The tool is built using the Tkinter library for the GUI and Matplotlib for visualizations.

## Features
• User-Friendly Interface: The GUI allows users to input the total memory size, the number of processes, and choose between internal and external fragmentation analysis.

• Allocation Algorithms: The tool supports three memory allocation algorithms:

• Best Fit: Allocates memory to the process that best fits the available memory partition.
• Worst Fit: Allocates memory to the process that requires the largest available memory partition.
• First Fit: Allocates memory to the first available memory partition that can accommodate the process.

• Dynamic Process Input: Users can input the memory requirements for each process dynamically through a simple dialog box.

• Visualization: The tool provides a visual representation of memory partition information through a bar chart, illustrating space required, block size, and unused space.

## Getting Started

### Prerequisites
Ensure you have the following installed:

• Python

• Tkinter

• Matplotlib

## Usage
• Enter the total memory size.

• Enter the number of processes.

• Choose between internal and external fragmentation.

• Click the "Submit" button.

• Input memory requirements for each process as prompted.

• Select an allocation algorithm: Best Fit, Worst Fit, or First Fit.

• Click the "Allocate Memory + Show Graph" button.

• View the visualized memory partition information.


#### Feel free to contribute, report issues, or suggest improvements!
