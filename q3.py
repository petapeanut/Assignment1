#
# list2 = []
# def fib(n, list):
#
#     # if (n not in list):
#     list.append(n)
#     print(list)
#
#
#     if n ==0 or n == 1:
#         return n
#
#     else:
#         if n in list2:
#             return list2[n]
#         else:
#             value = fib(n - 1, list) + fib(n - 2, list)
#             list2[n] = value
#             return value
#
# f = fib(6,[])
# fib(6,[])
# print(f)

fib_dict = {}

def fib(n,l):

    l.append(n)
    print(l)

    if n == 0 or n == 1:
        return n
    else:
        if n in fib_dict:
            return fib_dict[n]
        else:
            value = fib(n - 1, l) + fib(n - 2, l)
            fib_dict[n] = value
            return value

# fib(6, [])
# print(fib_dict)