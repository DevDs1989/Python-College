user_list = ['']
print("Enter strings into list: ")
while True:
    user_input = input()
    if user_input == '':
        break
    user_list.append(user_input)
    
while '' in user_list:
    user_list.remove('')
user_set = list(set(user_list))
print(user_set)
