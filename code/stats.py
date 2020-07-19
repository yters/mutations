from Levenshtein import editops
from collections import Counter
import sys

orgA = open(sys.argv[1]).read().strip()
orgB = open(sys.argv[2]).read().strip()

bases = Counter(orgA) + Counter(orgB)

ops = editops(orgA, orgB) 
mutations = [(orgA[a], orgB[b]) for (t, a, b) in ops if t == 'replace']
transitions = [(a, b) for (a, b) in mutations if (a, b) == ('a', 'g') or (a, b) == ('g', 'a') or (a, b) == ('c', 't') or (a, b) == ('t', 'c')]
a_t = [(a, b) for (a, b) in mutations if (a, b) == ('a', 't') or (a, b) == ('t', 'a')]
g_c = [(a, b) for (a, b) in mutations if (a, b) == ('c', 'g') or (a, b) == ('g', 'c')]
a_clg_t = [(a, b) for (a, b) in mutations if (a, b) == ('a', 'c') or (a, b) == ('c', 'a') or (a, b) == ('c', 'g') or (a, b) == ('g', 'c')]
print('transitions', len(transitions)/len(orgA+orgB))
print('a<->t', len(a_t)/(bases['a'] + bases['t']))
print('g<->c', len(g_c)/(bases['g'] + bases['c']))
print('a<->c|g<->t', len(a_clg_t)/len(orgA+orgB))
