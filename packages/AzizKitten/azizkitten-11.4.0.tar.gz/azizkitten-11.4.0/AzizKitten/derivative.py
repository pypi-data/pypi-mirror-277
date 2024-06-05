def derivative(func, value):
    h=1e-10
    ans=(func(value+h)-func(value))/h
    return ans