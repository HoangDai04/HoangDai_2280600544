def tao_tupple_tu_list(lst):
    return tuple(lst)
input_list = input("Nhập danh sách các số, cách nhau bằng dấu phẩy:")
numbers = list(map(int, input_list.split(',')))
my_tuple = tao_tupple_tu_list(numbers)
print("List:", numbers)
print("Tupple từ list:", my_tuple)