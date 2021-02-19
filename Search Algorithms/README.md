# Search Algorithms 
Given a sorted array of n elements, search for a given element 'key' in the array.
## Binary Search 
### File name: binary-search.py
In this algorithm, you repeatedly divide the array by half in every interation. Since the problem is divided by half, the time complexity of this algorithm is Theta(log n), which makes this algorithm efficient. 
### Input and Output Samples

<table>
    <tr>
        <th>
            Case 1: Key is found
        </th>
        <th>
            Case 2: Key is not found
        </th>
    </tr>
    <tr>
        <td>
            <p align = "center">
            <img src="https://github.com/haseefathi/Python-Algorithms/blob/main/Search%20Algorithms/images/binarysearch-1.png" width="350" height="200" />
            </p>
        </td>
        <td>
            Case 2: Key is not found
            <p align = "center">
            <img src="https://github.com/haseefathi/Python-Algorithms/blob/main/Search%20Algorithms/images/binarysearch-2.png" width="350" height="200" />
            </p>
        </td>
    </tr>
</table>

