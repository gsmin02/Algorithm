import sys

input = sys.stdin.readline

S, P = map(int, input().split())
DNA = input().strip()
A,C,G,T = map(int, input().split())
ACGT = {'A': 0, 'C':0, 'G':0, 'T':0}

answer = 0
i, j = 0, P-1
curr = DNA[i:j]

for ch in curr:
    ACGT[ch] += 1

while j <= S-1:
    ACGT[DNA[j]] += 1
    
    if ACGT['A'] >= A and ACGT['C'] >= C and ACGT['G'] >= G and ACGT['T'] >= T:
        answer += 1
    
    ACGT[DNA[i]] -= 1
    
    i += 1
    j += 1

print(answer)