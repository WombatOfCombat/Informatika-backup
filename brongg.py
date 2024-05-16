import numpy as np
arr=np.array([[[[1,2],[3,4]],[[5,6],[7,8]]],[[[9,10],[11,12]],[[13,14],[16,17]]],[[[1,2],[3,4]],[[5,6],[7,8]]],[[[9,10],[11,12]],[[13,14],[16,17]]]])
def f(x):
    return x**2+x+2
def elements_wise(arr:np.ndarray,func_used):
    program=''
    command='arr'
    for i in range(arr.ndim):
        program+=f'for di{i} in range(arr.shape[{i}]):\n'+(i+1)*'    '
        command+=f'[di{i}]'
    program+=command+'=func_used('+command+')'
    exec(program) 
elements_wise(arr,f)
print(arr)