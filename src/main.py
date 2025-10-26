import sys
from handlers import h_input
def main():
    if not h_input.handle_input(sys.argv):
        print("\nExit code: Error")
        return (False)
    print("\nExit code: Success")
    return (True)
    
if __name__ == "__main__":
    main()

# ─────────────────────────────────────────────
# LIST OF SORTING ALGORITHMS
# ─────────────────────────────────────────────

# 🔹 Simple (O(n²)) sorting algorithms
# -----------------------------------
# Bubble Sort [DONE]
# Selection Sort
# Insertion Sort
# Gnome Sort
# Cocktail Shaker Sort
# Comb Sort
# Odd-Even Sort

# 🔹 Efficient comparison-based algorithms
# ----------------------------------------
# Merge Sort
# Quick Sort
# Heap Sort
# Shell Sort
# Tim Sort
# Intro Sort
# Smooth Sort

# 🔹 Non-comparison-based algorithms
# ----------------------------------
# Counting Sort
# Radix Sort
# Bucket Sort
# Pigeonhole Sort
# Flash Sort

# 🔹 Hybrid / Specialized algorithms
# ----------------------------------
# Bitonic Sort
# Pancake Sort
# Cycle Sort
# Stooge Sort
# Bogo Sort (JOKE)
# Sleep Sort (JOKE)

# ─────────────────────────────────────────────
#   Powerful
#     - Tim Sort (Python)
#     - Merge Sort
#     - Quick Sort
#     - Heap Sort
# ─────────────────────────────────────────────
