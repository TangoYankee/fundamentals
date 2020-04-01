[Home](/fundamentals/)

# Sorting

## Discussions

### Heap Sort
- Maintains its unsorted region in a heap data structure

### Radix Sort
[Pierre Terdiman Radix Sort Revisited](http://codercorner.com/RadixSortRevisited.htm)
- Stable (use offset table to resolve collisions)
- Time Complexity O(k(n+k))
  - Uses counting sort for each radix
- Space complexity O(k+n)
  - Creates a additional data structures to hold the processed data
  - Data could be sorted concurrently or even in parallel, as data is segregated into buckets.
- Because it preserves the order, it can look at only one radix and sort it, without undoing
  the sort for the previous radix.
- Can still work with positive float numbers, depending on their representation in memory
- Pro: Stabile with a low time complexity when k is low. Can even be run in parallel.
- Cons: 
  - Limited to lexicographical order. 
  - Requires additional memory. 
  - It will run in the same time, even when the list is already sorted.
