### Table of Contents
- [DP](https://github.com/mdrahmed/interviewPrep/tree/main/random#dynamic-programming)
- [Binary Search](https://github.com/mdrahmed/interviewPrep/tree/main/random#binary-search-problems)
- [Sliding Window](https://github.com/mdrahmed/interviewPrep/tree/main/random#sliding-window)
- [Two pointers](https://github.com/mdrahmed/interviewPrep/tree/main/random#two---pointers)
- [String Manipulation](https://github.com/mdrahmed/interviewPrep/tree/main/random#string-manipulation)


***
## Dynamic Programming

***
## Binary Search problems
**Most important is to find the termination point & how left, right pointers will update**
There are 3 different termination point, I found so far,
1. left <= right # use when result might not present left will exceed right
  - left and right will be updated to left = mid + 1 & right = mid - 1
  - return target when found otherwise at the end return -1
2. left < right  # use when result will present at left == right
  - left will be updated to mid and right to mid - 1 or vice versa depending on the problem
  - Return left or right as both are equal
3. right - left > 1 # use when result is present when left & right is adjacent to each other e.g., left+1 == right
  - left and right will be updated to mid => left = mid, right = mid
  - return right
**Check the questions of problem: Race Overtaking**

### Search in Sorted Array
[BookChapter 29: Binary Search: Search in Sorted Array](https://start.interviewing.io/beyond-ctci/part-vii-catalog/binary-search#search-in-sorted-array)
#### Approach 1: 
Use binary search to find the target

[Note] similar problem would be [Search in rotated sorted array](https://leetcode.com/problems/search-in-rotated-sorted-array/description/)

### Race Overtaking
<u>Approach:</u> Can be done using linear or binary search. Optimal is to use binary search
**At first, find the termination point** 
If the termination is at adjacent and we keep setting l to mid, then it will be infinite loop. Again, if we set l = mid+1 and r=mid-1, then we terminate loop without the answer.

**Try to answer this question**
1. Think about what happens during your binary search:
* When p2[mid] < p1[mid], you move l to mid (overtake hasn't happened yet)
* When p2[mid] > p1[mid], you move r to mid (overtake has already happened)
So as the search progresses, what property does the index at l have, and what property does the index at r have?

2. Let's reconsider:
* When p2[mid] < p1[mid] (overtake hasn't happened yet), you move l to mid
* When p2[mid] > p1[mid] (overtake has happened), you move r to mid
So l is being set to positions where the overtake hasn't happened yet, and r is being set to positions where the overtake has happened.
Given that, what will l and r represent when they're next to each other?

=> l will represent the point just before overtake happened and r will represent the exact point where overtake happened

=> So your loop would be while l + 1 != r. Another common way to write this is while r - l > 1.


### CCTV Footage
[BookChapter 29: Binary Search:CCTV Footage](https://start.interviewing.io/beyond-ctci/part-vii-catalog/binary-search#cctv-footage)

**Find the termination point at first:** Whats the logic behind the termination point?
It will terminate when left and right are closest to each other e.g., left + 1 == right. Because we need to find the timestamp when the bike went missing first.

**Why left and right are set to mid?**
Right and left set to mid because, left represents the timestamp where bike is still present, right represents the timestamp where the bike went missing.




***
## Sliding Window

### Most Weekly Sales
[BookChapter 38: Sliding Windows: Most Weekly Sales](https://start.interviewing.io/beyond-ctci/part-vii-catalog/sliding-windows#most-weekly-sales)
#### Approach 1: 
Use a sliding window for every 7 day sales and count the max sales

[Note] This is a fixed sliding window problem. Check this [Longest Repeating Character Replacement](https://leetcode.com/problems/longest-repeating-character-replacement/description/), which is a varying sliding window problem.


### Remove Sandwiched Negatives
It was told to **modify the array in-place** that's why, needed sliding window, otherwise, counting only negatives between same positives would be fine.


***
## Two - pointers

### Dutch Flag Problem
[BookChapter 27: Two Pointers: Dutch Flag Problem](https://start.interviewing.io/beyond-ctci/part-vii-catalog/two-pointers#dutch-flag-problem)
#### Approach 1: Using hashmap
Use hashmap to store and then keep count, then just put values 1 by 1
#### Approach 2:
1. Count all 'R'
2. Count all 'W'
3. Then put 'R' first then 'W' and then put 'B' into remainings


### 2-sum
[BookChapter 27: Two Pointers: 2-Sum](https://start.interviewing.io/beyond-ctci/part-vii-catalog/two-pointers#two-sum)
#### 3 Approaches:
1. Using nested loops, with 2 loops we can find the indices => TO: O(n^2)
2. Using hashmap we can keep one value and then check if any other value adds to 0 => TO: O(n)
3. As the array is sorted, we can traverse the array with 2 pointers, start and end
  - If sum is greater than 0 then it means, we need to reduce the sum so we move left. 
  - If the sum is less than 0 then we move the start pointer to right so that the sum gets closer to 0. => TO: O(n)

###  Palindromic Sentence
[BookChapter 27: Two Pointers: Palindromic Sentence](https://start.interviewing.io/beyond-ctci/part-vii-catalog/two-pointers#palindrome-check)

**Python functions that is important to remember:**
```
ch.lower(), str.lower()
ch.isalpha(), str.isalpha()
```

Other functions:
```
str.isalnum(), ch.isalnum()
str.upper(), ch.upper()
```
To convert string into lowercase by removing punctuation, commas and spaces:
`str = ""join(ch for ch in s if(ch.isalpha())`

Actually, strings in Python are immutable. When you remove punctuation or convert to lowercase, you are creating new strings. So, Space complexity to remove or checking if its palindrome with `s == s[::-1]` is creating new string, so, `SO = O(n)`

In python,
```
    while not s[start].isalpha(): start += 1
    while not s[end].isalpha(): end -= 1
```

### Merge Two Sorted Arrays
[BookChapter 27: Two Pointers Merge Two Sorted Arrays](https://start.interviewing.io/beyond-ctci/part-vii-catalog/two-pointers#merge-two-sorted-arrays)

#### Approach
Use 2 pointers, each pointing 2 arrays, put the values in result after sorting.

## Random Problems
### Topological Ordering
[Topological Ordering](https://start.interviewing.io/beyond-ctci/solution/topological-ordering)

TO & SO: `O(n+m)`

For details check `adv_algo/Topological Order` folder.


***
## String Manipulation

### String Join
[BookChapter 26: String Manipulation: String Join](https://start.interviewing.io/beyond-ctci/part-vii-catalog/string-manipulation#string-join)

Just iterate the string and put s in between. Avoid the 1st str element and put s at the end after every element.
If there is only 1 str element then s can't be placed in between.

### Remove Duplicates from String
Store as list as list is mutable, it’s possible to update the code in place. But if I use tuple then I can’t update it in place, as tuples are immutable.
