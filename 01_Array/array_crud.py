
class ArrayCRUD:
    def __init__(self, capacity):
        """
        Initialize the array with a fixed capacity.
        We use 'None' to represent empty memory slots.
        """
        self.capacity = capacity
        self.size = 0
        self.arr = [None] * capacity

    # --- 1. CREATE (Insert) ---
    def add(self, value):
        """Adds an element to the end of the array (O(1))."""
        if self.size == self.capacity:
            print("Error: Array is full!")
            return

        self.arr[self.size] = value
        self.size += 1
        print(f"[Create] Added {value} at index {self.size - 1}")

    def insert_at(self, index, value):
        """
        Inserts element at specific index.
        Logic: Shift elements to the RIGHT to make space (O(N)).
        """
        if self.size == self.capacity:
            print("Error: Array is full!")
            return
        if index < 0 or index > self.size:
            print("Error: Invalid Index")
            return

        # Start from the last element and move backwards
        for i in range(self.size - 1, index - 1, -1):
            self.arr[i + 1] = self.arr[i]

        self.arr[index] = value
        self.size += 1
        print(f"[Insert] Inserted {value} at index {index}")

    # --- 2. READ (Search/Traverse) ---
    def display(self):
        """Displays only the valid elements currently in the array."""
        current_data = self.arr[:self.size]
        print(f"Current Array: {current_data}")

    def search(self, value):
        """Linear search to find a value's index (O(N))."""
        for i in range(self.size):
            if self.arr[i] == value:
                return i
        return -1

    # --- 3. UPDATE ---
    def update(self, index, value):
        """Overwrites the value at a specific index (O(1))."""
        if 0 <= index < self.size:
            self.arr[index] = value
            print(f"[Update] Updated index {index} to {value}")
        else:
            print("Error: Index out of bounds")

    # --- 4. DELETE ---
    def delete_at(self, index):
        """
        Deletes element at index.
        Logic: Shift elements to the LEFT to close the gap (O(N)).
        """
        if index < 0 or index >= self.size:
            print("Error: Index out of bounds")
            return

        deleted_val = self.arr[index]

        # Start from the gap and pull the next value in
        for i in range(index, self.size - 1):
            self.arr[i] = self.arr[i + 1]

        self.arr[self.size - 1] = None  # Clear ghost data
        self.size -= 1
        print(f"[Delete] Removed {deleted_val} from index {index}")

# --- DRIVER CODE ---
if __name__ == "__main__":
    print("--- Initializing Array with Capacity 10 ---")
    my_array = ArrayCRUD(10)

    # 1. Add Data
    my_array.add(10)
    my_array.add(20)
    my_array.add(40)
    my_array.display()

    # 2. Insert (Shift Logic)
    # We want 30 to be between 20 and 40
    my_array.insert_at(2, 30)
    my_array.display()

    # 3. Update
    my_array.update(0, 99)
    my_array.display()

    # 4. Delete (Shift Logic)
    # Removing 20 (at index 1) causes 30 and 40 to shift left
    my_array.delete_at(1)
    my_array.display()
