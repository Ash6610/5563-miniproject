class QuickFitMemoryAllocation:
    def __init__(self):
        # Initial memory block lists
        self.memory_blocks = {
            "50KB": ["Block 1", "Block 2"],
            "100KB": ["Block 3", "Block 4"],
            "200KB": ["Block 5", "Block 6"],
            "300KB": ["Block 7"],
        }
        self.allocations = {}  # Allocated processes
        self.small_blocks = []  # For blocks smaller than size-specific lists

    def allocate_memory(self, process, size):
        size_key = f"{size}KB"
        available_blocks = self.memory_blocks.get(size_key, [])

        if available_blocks:
            # Allocate the first block in the list
            allocated_block = available_blocks.pop(0)
            self.allocations[process] = f"{size}KB ({allocated_block})"
        else:
            # If no exact match, use best-fit or split larger blocks
            for key, blocks in self.memory_blocks.items():
                block_size = int(key[:-2])  # Remove 'KB' and convert to int
                if block_size > size and blocks:
                    allocated_block = blocks.pop(0)
                    remaining_size = block_size - size

                    self.allocations[process] = f"{size}KB (from {allocated_block})"

                    if remaining_size > 0:
                        small_key = f"{remaining_size}KB"
                        self.memory_blocks.setdefault(small_key, []).append(f"New Block from {allocated_block}")
                    return

            # If no suitable block found, allocation fails
            print(f"Failed to allocate memory for {process}")

    def display_memory(self):
        print("\nAvailable Memory Blocks:")
        for size, blocks in self.memory_blocks.items():
            print(f"{size} List: {', '.join(blocks) if blocks else 'None'}")

        if self.small_blocks:
            print(f"Small Blocks: {', '.join(self.small_blocks)}")

    def display_allocations(self):
        print("\nAllocated Processes:")
        for process, block in self.allocations.items():
            print(f"{process}: {block}")

if __name__ == "__main__":
    allocator = QuickFitMemoryAllocation()

    # Display initial state
    allocator.display_memory()

    # Allocate memory to processes
    allocator.allocate_memory("Process A", 50)
    allocator.allocate_memory("Process B", 200)
    allocator.allocate_memory("Process C", 300)
    allocator.allocate_memory("Process D", 150)

    # Display final state
    allocator.display_memory()
    allocator.display_allocations()
