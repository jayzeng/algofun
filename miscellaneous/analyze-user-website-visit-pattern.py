from typing import List
from itertools import combinations
import collections


class Solution:
    def mostVisitedPattern(self, username: List[str], timestamp: List[int], website: List[str]) -> List[str]:
        users = collections.defaultdict(list)

        for u, t, w in sorted(zip(username, timestamp, website), key=lambda x: (x[0], x[1])):
            users[u].append(w)

        patterns = collections.Counter()

        for user, websites in users.items():
            # patterns.update(collections.Counter(combinations(websites, 3)))
            for triplet in set(combinations(websites, 3)):
                patterns[triplet] += 1
        
        return max(sorted(patterns), key=patterns.get)

if __name__ == "__main__":
    username = ["joe","joe","joe","james","james","james","james","mary","mary","mary"]
    timestamp = [1,2,3,4,5,6,7,8,9,10]
    website = ["home","about","career","home","cart","maps","home","home","about","career"]
    print(Solution().mostVisitedPattern(username, timestamp, website))