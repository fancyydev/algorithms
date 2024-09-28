# class Solution:
#     def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
#         """
#         No retorna nada, modifica nums1 en su lugar.
#         """
#         if m > 0 and n > 0:
#             # Agregar los elementos de nums2 a nums1 desde la posición m
#             index = m
#             for i in range(n):
#                 nums1[index] = nums2[i]
#                 index += 1
#             nums1.sort()  # Ordenar nums1 después de añadir elementos
#         elif n > 0:
#             # Copiar los elementos de nums2 directamente a nums1
#             nums1[:n] = nums2  # Modifica nums1 en su lugar

#PARA USAR TWO POINTER TECHNIQUE LAS DOS LISTAS A UTILIZAR DEBEN ESTAR ORDENADAS

class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        p1, p2 = m - 1, n - 1  
        p = m + n - 1
        while p1 >= 0 and p2 >= 0:
            
            if nums1[p1] > nums2[p2]:
                nums1[p] = nums1[p1]
                p1 -= 1
            else:
                nums1[p] = nums2[p2]
                p2 -= 1
            p -= 1
        #Estudiar como funcionan este tipo de cadenas
        nums1[:p2 + 1] = nums2[:p2 + 1]
        
        print(nums1)
        
solution = Solution()
# solution.merge([3,0,0,0],1,[2,5,6],3)
solution.merge([1,2,3,0,0,0],3,[1,5,6],3)
# solution.merge([1],1,[],0)
# solution.merge([0],0,[1],1)