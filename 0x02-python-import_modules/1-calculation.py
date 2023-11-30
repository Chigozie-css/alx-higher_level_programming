#!/usr/bin/python3
if __name__ == "__main__":
    """Print the sum, difference, product, and quotient of 10 and 5."""

    from calculator_1 import add as add_func, sub as sub_func, mul as mul_func, div as div_func

    a = 10
    b = 5

    result_add = add_func(a, b)
    result_sub = sub_func(a, b)
    result_mul = mul_func(a, b)
    result_div = div_func(a, b)

    print("{} + {} = {}".format(a, b, result_add))
    print("{} - {} = {}".format(a, b, result_sub))
    print("{} * {} = {}".format(a, b, result_mul))
    print("{} / {} = {}".format(a, b, result_div))
