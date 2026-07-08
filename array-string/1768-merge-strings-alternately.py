"""
Problem: 1768. Merge Strings Alternately
Difficulty: Easy
Topic: Array / String

Idea:
Use two pointers to read characters from both words.
Add one character from word1, then one character from word2.
If one word is longer, add the remaining characters.

Time Complexity: O(n + m)
Space Complexity: O(n + m)
