
### Dutch Flag Problem
[BookChapter 27: Two Pointers: Dutch Flag Problem](https://start.interviewing.io/beyond-ctci/part-vii-catalog/two-pointers#dutch-flag-problem)
#### Approach 1: Using hashmap
Use hashmap to store and then keep count, then just put values 1 by 1
#### Approach 2:
1. Count all 'R'
2. Count all 'W'
3. Then put 'R' first then 'W' and then put 'B' into remainings


### Most Weekly Sales
[BookChapter 38: Sliding Windows: Most Weekly Sales](https://start.interviewing.io/beyond-ctci/part-vii-catalog/sliding-windows#most-weekly-sales)
#### Approach 1: 
Use a sliding window for every 7 day sales and count the max sales

[Note] This is a fixed sliding window problem. Check this [Longest Repeating Character Replacement](https://leetcode.com/problems/longest-repeating-character-replacement/description/), which is a varying sliding window problem.


### Search in Sorted Array
[BookChapter 29: Binary Search: Search in Sorted Array](https://start.interviewing.io/beyond-ctci/part-vii-catalog/binary-search#search-in-sorted-array)
#### Approach 1: 
Use binary search to find the target

[Note] similar problem would be [Search in rotated sorted array](https://leetcode.com/problems/search-in-rotated-sorted-array/description/)


### 2-sum
[BookChapter 27: Two Pointers: 2-Sum](https://start.interviewing.io/beyond-ctci/part-vii-catalog/two-pointers#two-sum)
#### 3 Approaches:
1. Using nested loops, with 2 loops we can find the indices => TO: O(n^2)
2. Using hashmap we can keep one value and then check if any other value adds to 0 => TO: O(n)
3. As the array is sorted, we can traverse the array with 2 pointers, start and end
  - If sum is greater than 0 then it means, we need to reduce the sum so we move left. 
  - If the sum is less than 0 then we move the start pointer to right so that the sum gets closer to 0. => TO: O(n)

