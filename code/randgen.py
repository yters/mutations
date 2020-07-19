from random import randint
from collections import Counter
import sys

org = open(sys.argv[1]).read().strip()

org_dist = {}
count = 0
for k, v in Counter(org).items():
    count += v
    org_dist[k] = count

org_rand = ''
for _ in range(len(org)):
    number = randint(1, len(org))
    for k, v in org_dist.items():
        if number <= v:
            org_rand += k
            break

sys.stdout.write(org_rand)
