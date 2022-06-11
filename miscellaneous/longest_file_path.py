import re
import collections

class Solution:
    """
    @param input: an abstract file system
    @return: return the length of the longest absolute path to file
    """
    def length_longest_path(self, input: str) -> int:
        paths = collections.defaultdict(lambda: "")
        res = 0

        for line in input.split("\n"):
            levels = line.count('\t')
            line = paths[levels - 1] + re.sub("\\t+", "/", line)
            if '.' in line:
                res = max(res, len(line))
            paths[levels] = line

        return res

if __name__ == "__main__":
    s = Solution()
    # p = "dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext"
    p = "dir\n\tsubdir1\n\tsubdir2\n\t\tfile.ext"
    print(s.length_longest_path(p))