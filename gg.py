# # import excel
# # # path = input('Book1.xlsx')


# # wb = excel.load_workbook('Book1.xlsx')
# # ws = wb.active


# # s = excel.excel()
# # # s =excel()
# # s.title()
# # # s.get_columns_values()
# # s.get_name_and_row_num("Abhishek")
# # s.show_columns_with_values()

# # import os

# # def find_files(filename, search_path):
# #    result = []
# #    dirr = []
# # # Wlaking top-down from the root
# #    for root, dir, files in os.walk(search_path):
# #       if filename in files:
# #          result.append(os.path.join(root, filename))
# #          print(dirr.append(dir))
# #    return result
# # print(find_files('Book1.xlsx','C:'))


# # # Function to convert number into string
# # # Switcher is dictionary data type here
# # def numbers_to_strings():
# #     switcher = {
# #         0: print("sjhjjsbxj")              
# #         ,
# #         1: print("fdhicnkndvkinikn"),
# #         2: "two",
# #     }
# #     return switcher.get(argument, "nothing")
 
# # Driver program
# # if __name__ == "__main__":
# #     argument=0
# #     print(numbers_to_strings())

# # def add(num1,num2):
# #    return num1+num2
# # switcher = {
# #   0: print(add(456,6))              
# #         ,
# #         1:add(5,6),
# #         2: add(1,3)
# # }
 
# from asyncio.windows_events import INFINITE
# from fileinput import filename
# import time,os 

# # for i in range(0,INFINITE):
# #    if int(time.time()) == last_timer:
# #       break
# #    else:
# #       print(time.time())

# def find_files(filename, search_path):
#    result = []
#    for root, dir, files in os.walk(search_path):
#       if int(time.time()) == last_timer:
#          break
#       else:
#        if filename in files:
#           result.append(os.path.join(root, filename))
#    return result
# filename = 'jarvis.py'
# seconds = int(time.time())
# last_timer = seconds +10


# switcher  = {
#                 1:print(find_files(filename,'C:')),
#                 2:print(find_files(filename,'D:'))
#                 ,
#                 3:print(find_files(filename,'E:'))
#             }
# class Solution:
#     def subArraySum(self,arr, n, sum_): 
#         # Initialize curr_sum as
#         # value of first element
#         # and starting point as 0 
#         A = []
#         curr_sum = arr[0]
#         start = 0

#         # Add elements one by 
#         # one to curr_sum and 
#         # if the curr_sum exceeds 
#         # the sum, then remove 
#         # starting element 
#         i = 1
#         while i <= n:
        
#             # If curr_sum exceeds
#             # the sum, then remove
#             # the starting elements
#             while curr_sum > sum_:
        
#                 curr_sum = curr_sum - arr[start]
#                 start += 1
            
#             # If curr_sum becomes
#             # equal to sum, then
#             # return true
#             if curr_sum == sum_:
#                 A.append(start+1)
#                 A.append(i)
#                 return A

#             # Add this element 
#             # to curr_sum
#             if i < n:
#                 curr_sum = curr_sum + arr[i]
#             i += 1

#         # If we reach here, 
#         # then no subarray
#         A.append(-1)
#         return A

# s = Solution()
# print(s.subArraySum([1,2,3,12,7,5],6,12))

a =[1,5,4,5754,21,1]
if len(a) == 0:
    print("hscxjccj")
    a.sort()
print(a)
list(a)
