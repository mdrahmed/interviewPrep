
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