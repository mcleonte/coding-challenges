# https://leetcode.com/problems/word-search-ii/

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:

        letters_trace = []
        letters_trace_idx = []

        def walk(center_idx):
            x,y = center_idx
            for l,let in enumerate(word[1:]):
                x,y = letters_trace[-1]
                conditions = (x>0,
                              y>0,
                              x<len(board-2),
                              y<len(letters-2))
                adjacent_idx = ((x-1,y),
                                (x,y-1),
                                (x+1,y),
                                (x,y+1)
                               )
                return [ a for c,a in zip(conditions,adjacent_idx) if c and (a not in letters_trace) and (board[ a[0] ][ a[1] ] == l)]
        out = []
        for word in words:
            for i, letters in enumerate(board):
                for j, letter in enumerate(letters):
                    if word[0] == letter:
                        letters_trace = [ word[0] ]
                        letters_trace_idx = [ (i,j) ]

                        for k in walk():
                            if k and walk(


                        for l,let in enumerate(word[1:]):
                            x,y = letters_trace[-1]
                            conditions = (x>0,
                                          y>0,
                                          x<len(board-2),
                                          y<len(letters-2))
                            adjacent_idx = ((x-1,y),
                                            (x,y-1),
                                            (x+1,y),
                                            (x,y+1)
                                           )
                            adjacent_idx_found = [ a for c,a in zip(conditions,adjacent_idx) if c and (a not in letters_trace) and (board[ a[0] ][ a[1] ] == l)]
        return out
