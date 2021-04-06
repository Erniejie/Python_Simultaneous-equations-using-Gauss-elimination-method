#python_Simultaneous equations using Gauss elimination
#Computer Tutor Programming_April 04,2021

import traceback
import sys

class Gauss_Elimination:
    def __init__(self):
        self.a = [
            [1,1,1,3],
            [1,2,3,0],
            [1,3,2,3],
            ]
        self.n = len(self.a)

    def rungauss(self):
        try:
            self.__show_equations()
            for m in range(self.n -1):
                for i in range(m+1,self.n):
                    d = self.a[i][m]/self.a[m][m]
                    for j in range(m+1,self.n +1):
                        self.a[i][j] -=self.a[m][j]*d

            for i in range(self.n -1,-1,-1):
                d= self.a[i][self.n]
                for z in range(i+1,self.n):
                    d -=self.a[i][z]*self.a[z][self.n]
                self.a[i][self.n] = d/self.a[i][i]
            self.__display_result()
        except Exception as e:
            raise
    def __show_equations(self):
        #Display of the Given Equations
        try:
            for i in range(self.n):
                for j in range(self.n):
                    print("{:+d}x{:d}".format(self.a[i][j],j+1),end="")
                print("={:+d}".format(self.a[i][self.n]))

        except Exception as e:
            raise
    def __display_result(self):
        """Displaying of the Answer"""
        try:
            for m in range(self.n):
                print("x{:d}={:f}".format(m+1,self.a[m][self.n]))
        except Exception as e:
            raise
if __name__=='__main__':
    try:
        obj=Gauss_Elimination()
        obj.rungauss()
    except Exception as e:
        traceback.print_exc()
        sys.exit(1)
                        
                
