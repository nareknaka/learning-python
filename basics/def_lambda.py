# def test_func(word):
#     print("word" , end="")
#     print("!")


# test_func("hi")
# test_func("3")
# test_func("5.6")




# def summa(a, b):
#     return a + b

# res = summa(5.5, 7.5)
# print(res)
# print(summa("H", "i"))









nums1 = [5, 7, 2, 9, 4]

min = nums1[0]
for el in nums1:
    if el < min:
        min = el

print(min)