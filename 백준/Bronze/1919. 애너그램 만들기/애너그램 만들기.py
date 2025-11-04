from collections import Counter
word1 = input()
word2 = input()

freq1 = Counter(word1)
freq2 = Counter(word2)

diff1 = freq1-freq2
diff2 = freq2-freq1

print(sum(diff1.values())+sum(diff2.values()))