## Interval Tree
Similar to segment tree.
Stores intervals, optimized for querying "which intervals overlap with a given interval" OR point queries. 

- O(nlogn) preprocessing.
- O(k + logn) query.
- O(n) space.

Discussion: https://stackoverflow.com/questions/17466218/what-are-the-differences-between-segment-trees-interval-trees-binary-indexed-t