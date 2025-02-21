import random

class QuickSort:
    def __init__(self, arr):
        self.arr = arr
        self.lenght = len(arr)
        self.index_result = 0
        self.i = 0
        self.j = 0
        self.left = 0 
        self.right = len(arr)-1
        self.pivot = random.randint(self.left,self.right)
        self.pivot_value = arr[self.pivot]    
    
    def Reset(self):
        self.index_result = 0
        self.i = 0
        self.j = 0
        self.left = 0 
        self.right = len(self.arr)-1
        self.pivot = random.randint(self.left,self.right)
        self.pivot_value = self.arr[self.pivot] 
    
    def Swap(self, i, j):
        aux = self.arr[i]
        self.arr[i] = self.arr[j]
        self.arr[j] = aux

    def QuickSelect(self, quick_type, n):
        result = 0
        
        if quick_type == "max":
            self.index_result = self.lenght - n 
        else:
            self.index_result = n-1
        
        #print(self.index_result)
        
        self.Swap(self.pivot, self.right)
        while True:
            #print(self.arr)
            if self.left == self.right:
                #print("sali por indice left y right")
                break
                
            if self.j == self.right:
                
                self.Swap(self.i, self.right)
                if (self.i == self.index_result):
                    #print("sali por que encontre el resultado")
                    break
                elif(self.i < self.index_result):
                    self.left = self.i+1
                else:
                    self.right = self.i-1
                        
                self.i=self.left
                self.j=self.left
                
                self.pivot = random.randint(self.left,self.right)
                self.pivot_value = self.arr[self.pivot] 
                self.Swap(self.pivot, self.right)
                pass
                    
            if self.arr[self.j] < self.pivot_value:
                self.Swap(self.i, self.j)
                self.i += 1
                self.j += 1
            else:
                self.j += 1
        if quick_type == "max":
            index_aux = self.index_result
            for i in range(n):
                result += self.arr[index_aux]
                index_aux += 1
        else:
            for i in range(n):
                result += self.arr[i]
                #print(self.arr[i])
        #print(arr)
        
        self.Reset()
        return result
        
def miniMaxSum(arr):
    # Write your code here
    n = 4
    my_quick_sort = QuickSort(arr)
    min = my_quick_sort.QuickSelect("min", n)
    max = my_quick_sort.QuickSelect("max", n)
    
    print(str(min)+" "+str(max))