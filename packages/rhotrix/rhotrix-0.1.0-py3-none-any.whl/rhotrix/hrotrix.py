from typing import List, Tuple, Union
from copy import deepcopy

_types: Tuple[str, str] = ['rhomboid', 'coupled']

class HRotrix:
    def __init__(self, rhotrix: List[List[float]]) -> None:
        if not isinstance(rhotrix, list):
            raise TypeError("rhotrix must be a numpy array")

        self.type: str = self._check_input_type(rhotrix=rhotrix)
        
        if self.type == _types[0]:
            self.rhotrix: List[List[float]] = rhotrix
        elif self.type == _types[1]:
            self.rhotrix: List[List[float]] =  self._parse_couple_into_romboid(rhotrix=rhotrix)
        
        self.dim : int = len(self.rhotrix)

    def __str__(self) -> str:
        max_length: int = max(len(row) for row in self.rhotrix)

        total_height: int = len(self.rhotrix)

        final_string: str = ''

        # Print the upper part of the diamond
        for i in range(total_height // 2 + 1):
            row = self.rhotrix[i]
            padding = '\t' * (max_length - len(row))
            final_string += padding + '\t\t'.join(map(str, row)) + '\n'

        # Print the lower part of the diamond
        for i in range(total_height // 2 + 1, total_height):
            row = self.rhotrix[i]
            padding = '\t' * (max_length - len(row))
            final_string += padding + '\t\t'.join(map(str, row)) + '\n'

        return final_string
    
    def __add__(self, other: 'HRotrix') -> 'HRotrix':
        if not isinstance(other, HRotrix):
            return NotImplemented
        
        if self.dim != other.dim:
            raise ValueError("Matrices must have the same dimension")

        temp_rhotrix: List[List[float]] = self.data_copy()
        
        for n_row in range(len(temp_rhotrix)):
            for m_col in range(len(temp_rhotrix[n_row])):
                temp_rhotrix[n_row][m_col] += other.rhotrix[n_row][m_col]

        return HRotrix(temp_rhotrix)
    
    def __sub__(self, other: 'HRotrix') -> 'HRotrix':
        if not isinstance(other, HRotrix):
            return NotImplemented
        
        if self.dim != other.dim:
            raise ValueError("Matrices must have the same dimension")

        temp_rhotrix: List[List[float]] = self.data_copy()
        
        for n_row in range(len(temp_rhotrix)):
            for m_col in range(len(temp_rhotrix[n_row])):
                temp_rhotrix[n_row][m_col] -= other.rhotrix[n_row][m_col]

        return HRotrix(temp_rhotrix)
    
    def __mul__(self, other: Union['HRotrix', int, float]) -> 'HRotrix':
        if not (isinstance(other, HRotrix) or isinstance(other, int) or isinstance(other, float)):
            return NotImplemented

        if isinstance(other, HRotrix):
            if self.dim != other.dim:
                raise ValueError("Matrices must have the same dimension")
            temp_rhotrix: List[List[float]] = self.data_copy()
            
            for n_row in range(len(temp_rhotrix)):
                for m_col in range(len(temp_rhotrix[n_row])):
                    temp_rhotrix[n_row][m_col] = temp_rhotrix[n_row][m_col]*other.heart() + other.rhotrix[n_row][m_col]*self.heart()


            return HRotrix(temp_rhotrix)

        elif isinstance(other, int) or isinstance(other, float):
            temp_rhotrix: List[List[float]] = self.data_copy()
            
            for n_row in range(len(temp_rhotrix)):
                for m_col in range(len(temp_rhotrix[n_row])):
                    temp_rhotrix[n_row][m_col] *= other

            return HRotrix(temp_rhotrix)
    
    def data_copy(self) -> List[List[float]]:
        return deepcopy(self.rhotrix)
    
    def _check_input_type(self, rhotrix: List[List[float]]) -> str:
        lenghts: List[int] = [len(x) for x in rhotrix]

        if all(i == lenghts[0] for i in lenghts): return _types[1]
        
        mid: int = len(rhotrix) // 2
        
        for n in range(mid):
            if lenghts[n] + 2 != lenghts[n + 1]:
                raise ValueError("Rhotrix must be a rhomboidal matrix")

            if lenghts[-(n + 1)] + 2 != lenghts[-(n + 1) - 1]:
                raise ValueError("Rhotrix must be a rhomboidal matrix")

            if lenghts[-(n + 1)] != lenghts[n]:
                raise ValueError("Rhotrix must be a rhomboidal matrix")

        return _types[0]
    
    def _parse_couple_into_romboid(self, *, rhotrix: List[List[float]]) -> List[List[float]]:
        seed: Tuple[int, int, int] = tuple(x for x in range(int(len(rhotrix) - (len(rhotrix) - 1)/2)))
        
        temp_rhotrix: List[List[float]] = [[] for _ in range(len(rhotrix))]

        for it, row in enumerate(rhotrix):
            row: List[float] = [x for x in row if x is not None]
            for n, element in enumerate(row):
                temp_rhotrix[seed[n]].append(element)
            
            seed = tuple(x + 1 for x in seed) if it%2 == 0 else seed

        return [row[::-1] for row in temp_rhotrix]
                    
    def identity(self) -> 'HRotrix':
        temp_rhotrix: List[List[float]] = self.rhotrix.copy()

        for n in range(len(temp_rhotrix)):
            temp_rhotrix[n] = [1 if i == len(temp_rhotrix[n])//2 else 0 for i in range(len(temp_rhotrix[n]))]

        return HRotrix(temp_rhotrix)

    def heart(self) -> float:
        axis: List[float] = self.rhotrix[self.dim // 2]
        
        return axis[self.dim // 2]
    
if __name__ == '__main__':
    rhotrix: List[List[float]] = [[1],
                               [4, 5, 6],
                            [3, 4, 5, 6, 3],
                               [3, 5, 3],
                                  [3]]
    
    rhotrix_2_0: List[List[float]] = [
        [1, None, 6, None, 3],
        [None, 5, None, 6, None],
        [4, None, 5, None, 3],
        [None, 4, None, 5, None],
        [3, None, 3, None, 3]
    ]
    
    rhotrix_2_1: List[List[float]] = [
        [3, None, 5, None, 6],
        [None, 5, None, 2, None],
        [4, None, 4, None, 3],
        [None, 5, None, 5, None],
        [6, None, 7, None, 8]
    ]
    
    rhotrix_3: List[List[float]] = [
        [1, None, 6, None, 3, None, 2],
        [None, 5, None, 6, None, 4, None],
        [4, None, 5, None, 3, None, 7],
        [None, 4, None, 5, None, 4, None],
        [3, None, 3, None, 3, None, 1],
        [None, 2, None, 4, None, 5, None],
        [7, None, 3, None, 2, None, 4]
    ]
    
    rhotrix_10: List[List[float]] = [
        [1, None, 6, None, 3, None, 2, None, 7],
        [None, 5, None, 6, None, 4, None, 8, None],
        [4, None, 5, None, 3, None, 7, None, 1],
        [None, 4, None, 5, None, 4, None, 9, None],
        [3, None, 3, None, 3, None, 1, None, 2],
        [None, 2, None, 4, None, 5, None, 3, None],
        [7, None, 3, None, 2, None, 4, None, 5],
        [None, 1, None, 7, None, 2, None, 6, None],
        [6, None, 4, None, 8, None, 5, None, 3]
    ]

        
    hrotrix = HRotrix(rhotrix_3)

    hrotrix_2_0 = HRotrix(rhotrix_2_0)
    hrotrix_2_1 = HRotrix(rhotrix_2_1)
    
    print(f'Sum of \n{hrotrix_2_0} and \n{hrotrix_2_1} is \n{hrotrix_2_0 + hrotrix_2_1}')
    
    print(f'Substraction of \n{hrotrix_2_0} and \n{hrotrix_2_1} is \n{hrotrix_2_1 + hrotrix_2_0}')
        
    print(f'Multiplication of  \n{hrotrix_2_1} and \n{hrotrix_2_0} is \n{hrotrix_2_1 * hrotrix_2_0}')
    
    print(f'Escalar Multiplication of  \n5 and \n{hrotrix_2_0} is \n{hrotrix_2_0 * 1523}')
    
    