<b>>Union Find Algorithms</b>
<p>
Here are few implementations of the union find algorithms:
<ol>
  <li>
    <b>Quick Find: (quick-find.py)</b>
In this implementation, the find() operation is quick but the union() operation is slow. This implementation is not useful for large operations since union() does not scale. 
  </li>
                <hr>
  <li>
    <b>Quick Union: (quick-union.py)</b>
This implementation is better than quick find implementation since union() is more optimized by using forest-of-trees representation. 
  </li>
                <hr>
  
  <li>
  <b>Weighted Quick Union: (weighted-quick-union.py)</b>
This implementation works better since it avoids creating trees of large depth. It does this by ensuring that during union(), it is always the smaller tree that gets added to the larger tree. 
  </li>
                <hr>
  <li>
  <b>Weighted Quick Union with Path Compression: (weighted-quick-union-PC.py)</b>
  This provides minor improvements over the weighted quick union implementation by making every examined node link directly to the root. In practical situations, there is no discernable improvement over weighted quick union. 
</li>
                <hr>
</ol>
</p>

<p>
<b> SUMMARY OF ALL UNION-FIND ALGOS </b>
<table>
  <tr>
    <th>Algorithm</th>
    <th>Constructor</th>
    <th>Union</th>
    <th>Find</th>
  </tr>
  <tr>
    <td>Quick Find</td>
    <td>N</td>
    <td>N</td>
    <td>1</td>
  </tr>
  <tr>
    <td>Quick Union</td>
    <td>N</td>
    <td>tree height</td>
    <td>tree height</td>
  </tr>
  <tr>
    <td>Weighted Quick Union</td>
    <td>N</td>
    <td>lg N</td>
    <td>lg N</td>
  </tr>
  <tr>
    <td>Weighted Quick Union with Path Compression</td>
    <td>N</td>
    <td>almost 1</td>
    <td>almost 1</td>
  </tr>
 </table>
 
 </p>
