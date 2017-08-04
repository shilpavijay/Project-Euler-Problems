""" Longest Collatz sequence  """

"""
The following iterative sequence is defined for the set of positive integers:

n → n/2 (n is even)
n → 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:

13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1

It can be seen that this sequence (starting at 13 and finishing at 1) contains
10 terms. Although it has not been proved yet (Collatz Problem), it is thought
that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.

"""


def collatzSeqLen(N):
  count = 0
  while(N > 1):
    N = N // 2 if N % 2 == 0 else 3 * N + 1
    count += 1
  return count + 1


def findNum():
  longest, stnum = 0, 0
  lst = [collatzSeqLen(x) for x in range(13, 1000000)]
  longest = max(lst)
  stnum = lst.index(longest) + 13
  return stnum


if __name__ == "__main__":
  print("Collatz sequence:")
  print("Num (under 1 Million) producing the longest chain: ")
  print(findNum())
