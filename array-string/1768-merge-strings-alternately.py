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

class Solution:
  def mergeAlternately(self, word1: str, word2: str) -> str:
      result = []
      i = 0

      while i < len(word1) or i < len(word2):
        if i < len(word1):
            result.append(word1[i])
        if i < len(word2):
            result.append(word2[i])
        i += 1
      return "".join(result)
