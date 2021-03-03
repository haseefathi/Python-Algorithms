# Sorting Algorithms 
Given an array of n elements, sort them according to a comparison operator on the elements.
## Selection Sort
### File name: selection-sort.py
In this algorithm, you sort the array by repeatedly finding the minimum element (in ascending order) from the unsorted part of the array and put it at the beginning. This algorithm has same performance irregardless of the nature of the input, having time complexity of O(n^2). 
### Input and Output Samples
<p align = "center">
    <img src="https://github.com/haseefathi/Python-Algorithms/blob/main/Sorting%20Algorithms/images/selection-sort.png" width="450" height="200" />
</p>

## Insertion Sort
### File name: insertion-sort.py
In this algorithm, you sort the array by virtually splitting the array into sorted and unsorted part, and picking elements from the unsorted part and inserting them in their correct position in the sorted part of the array. Insertion sort performs well for partially sorted arrays. 
### Analysis
<table>
    <tr>
        <th>
            Case
        </th>
        <th>
            Time Complexity
        </th>
    </tr>
    <tr>
        <td>
            Best - Already sorted array
        </td>
        <td>
            Linear time
        </td>
    </tr>
    <tr>
        <td>
            Average 
        </td>
        <td>
            O(n^2)
        </td>
    </tr>
    <tr>
        <td>
            Worst - Array in reverse order 
        </td>
        <td>
            O(n^2)
        </td>
    </tr>
</table>
### Input and Output Samples
<p align = "center">
    <img src="https://github.com/haseefathi/Python-Algorithms/blob/main/Sorting%20Algorithms/images/insertion-sort.png" width="450" height="200" />
</p>

## Shell Sort
### File name: shell-sort.py
Shell sort is a variation of Insertion sort in which you first h-sort the array for some large value of h and then keep reducing the value of h till it becomes 1. In the given code, the h value starts from the largest value of h less than N/3 from the sequence 3k+1. 
### Input and Output Samples
<p align = "center">
    <img src="https://github.com/haseefathi/Python-Algorithms/blob/main/Sorting%20Algorithms/images/shell-sort.png" width="450" height="200" />
</p>

