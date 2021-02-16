Union Find Algorithms

Here are few implementations of the union find algorithms:
1) Quick Find: (quick-find.py)
  In this implementation, the find() operation is quick but the union() operation is slow. This implementation is not useful for large operations since union() does not scale. 
_____________________________________________________________________________________

2) Quick Union: (quick-union.py)
  This implementation is better than quick find implementation since union() is more optimized by using forest-of-trees representation. 
_____________________________________________________________________________________

3) Weighted Quick Union: (weighted-quick-union.py)
  This implementation works better since it avoids creating trees of large depth. It does this by ensuring that during union(), it is always the smaller tree that gets added to the larger tree. 
_____________________________________________________________________________________

4) Weighted Quick Union with Path Compression: (weighted-quick-union-PC.py)
  This provides minor improvements over the weighted quick union implementation by making every examined node link directly to the root. In practical situations, there is no discernable improvement over weighted quick union. 
_____________________________________________________________________________________
