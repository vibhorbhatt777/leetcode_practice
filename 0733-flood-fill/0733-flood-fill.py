class Solution(object):
    def floodFill(self, image, sr, sc, color):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type color: int
        :rtype: List[List[int]]
        """
        start_color = image[sr][sc]
        def flood_fills(x,y):
            if (x < 0 or x >= len(image)) or (y < 0 or y >= len(image[0])) or (image[x][y] == color) or (image[x][y] != start_color): return

            if image[x][y] == color:return
            if image[x][y] != start_color: return

            image[x][y] = color
            flood_fills(x-1,y)
            flood_fills(x+1,y)
            flood_fills(x,y+1)
            flood_fills(x,y-1)
        
        flood_fills(sr,sc)
        return image


        