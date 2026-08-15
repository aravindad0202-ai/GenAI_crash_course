# # =================================== HIGHER FUNCTIONS ===========================
# """
# It must have any one of the two properties given below.
# - A function must take another function as a `Argument`
# - A function must return another function. 
# """

# #------------------------------------------ Property 1 ---------------------------------

# def process_list(my_numbers, operation):
#     result = []
#     for i in my_numbers:
#         result.append(operation(i))
#     return result

# def square(n):
#     return n**2

# def convert_string(n):
#     return str(n)

# def add_2(n):
#     return n+2

# numbers = [1,2,3,4,5,6]

# squares = process_list(numbers, square)
# print(squares)
# strings = process_list(numbers, convert_string)
# print(strings)

# # ----------------------------------------- Property 2 ------------------------------------
# "<h>Wikipedia</h1>" # ---> HTML tag
# ""
# def htm_tager(tag_name):
#     def wrapper(text_context):
#         return f"<{tag_name}>{text_context}</{tag_name}>"
#     return wrapper

# make_header = htm_tager('h')
# print(make_header('Wikipedia'))

# paragrah_crator = htm_tager('p')
# print(paragrah_crator('This is an Wikipedia page'))


# ================================= DECORATOR ======================================
def validator(original_func): # 1 take function as argument
    def wrapper(*args, **kwargs): # 2 Inner function must take dynamic arguments
        print('wrapper')
        if args[0] != str:
            print('executed')
            raise Exception("limit must be string")
        result = original_func(*args, **kwargs) # Function taken as argumnet must be called.
        return result
    return wrapper

@validator
def calculate_sum(limit):
    print('calculator')
    return sum(range(limit))

def func2(a, b):
    pass

print(calculate_sum('a'))