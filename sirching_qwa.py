if __name__ == "__main__":
   
    import numpy as np
    from numpy.linalg import norm
    a = np.array([1,0])
    b = np.array([0,1])
    c = norm(a-b)
    print(c*c)
