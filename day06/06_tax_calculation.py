def tax_calc(price:float, base_tax:float, **kwargs):
    tax = price * base_tax

    for i in kwargs:
        print(i, kwargs[i])
        tax += price * kwargs[i]
    return tax