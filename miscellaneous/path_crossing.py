


class Solution(object):
    def isPathCrossing(self, path):
        """
        :type path: str
        :rtype: bool
        """
        origin = (0, 0)
        seen_points = {origin}
       
        #   N
        # W   E
        #   S
        
        for p in path:
            point = origin
            x, y = point
            if p == 'E':
                x += 1
            elif p == 'W':
                x -= 1
            elif p == 'N':
                y += 1
            elif p == 'S':
                y -= 1
            
            if point in seen_points:
                return True
            
            seen_points.add(point)
        
        print(seen_points)
        return False

if __name__ == "__main__":
    path = "NESSS"
    print(Solution().isPathCrossing(path))