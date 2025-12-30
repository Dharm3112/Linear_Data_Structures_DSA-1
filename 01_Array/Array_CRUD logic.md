
# Array CRUD Operations (Under-the-Hood Logic)

## 📌 Overview
This directory contains a pure Python implementation of **Array CRUD Operations** (Create, Read, Update, Delete). 

Unlike standard Python lists that handle memory management automatically, this implementation simulates **fixed-size array logic**. It manually handles the algorithms for **shifting elements** during insertions and deletions.

**Why is this useful?**
- **Interview Prep:** This is exactly how arrays work in low-level languages (C/C++) and how you are expected to explain them in Data Structures & Algorithms (DSA) interviews.
- **Deep Understanding:** Learn what happens "under the hood" when you call `list.insert()` or `list.pop()`.

---

## ⚙️ The Logic Explained

### 1. Create (Insertion)
There are two ways to add data:
* **Append (Add to End):** fast and simple. We place the item at the first available empty index.
* **Insert (Add to Middle):** Complex. 
    * **Logic:** To insert a value at `index`, we must make space. We iterate from the *end* of the array backwards to the `index`, shifting every element one step to the **right**.
    * *Visual:* `[A, B, C, _]` -> Insert X at index 1 -> Shift C, Shift B -> `[A, _, B, C]` -> `[A, X, B, C]`

### 2. Read (Traversal & Search)
* **Get by Index:** Instant access using the memory address calculation.
* **Search by Value:** We must loop through the array (Linear Search) to find the matching value.

### 3. Update
* This is the fastest operation. We go directly to the specific `index` and overwrite the value stored there. No shifting is required.

### 4. Delete
Removing an element creates a "hole" in the contiguous memory block. We cannot leave holes.
* **Logic:** We iterate from the deleted `index` to the end of the array, shifting every element one step to the **left** to fill the gap.
* *Visual:* `[A, X, B, C]` -> Delete X -> Shift B, Shift C -> `[A, B, C, _]`

---

## 📊 Time Complexity Analysis

| Operation | Scenario | Complexity | Why? |
| :--- | :--- | :--- | :--- |
| **Access** | Get by Index | **O(1)** | Direct memory access. |
| **Search** | Find Value | **O(N)** | Must check every element. |
| **Insert** | At End | **O(1)** | No shifting needed. |
| **Insert** | At Start/Middle | **O(N)** | Requires shifting N elements right. |
| **Delete** | At End | **O(1)** | No shifting needed. |
| **Delete** | At Start/Middle | **O(N)** | Requires shifting N elements left. |

---

## 💻 Code Structure

The code is contained in `array_crud.py`. It features a class `ArrayCRUD` that simulates a fixed-capacity array.

**Key Methods:**
- `add(value)`: Adds to the end.
- `insert_at(index, value)`: Inserts at index (with manual shifting).
- `update(index, value)`: Updates value.
- `delete_at(index)`: Deletes at index (with manual shifting).
- `display()`: customized print method to show only active elements.

## 🚀 How to Run

1. Ensure you have Python installed.
2. Run the script to see the driver code demonstrate operations:
   ```bash
   python array_crud.py
