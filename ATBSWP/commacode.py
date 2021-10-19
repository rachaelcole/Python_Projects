def comma_code(list):
    # Check for empty list
    if len(list) == 0:
        print('The list is empty!')
        return
    if len(list) == 1:
        print(list[0])
        return
    for i in range(0, len(list) - 1):
        print(f'{list[i]}, ', end='')
    print(f'and {list[-1]}.')


my_list = ['Jake', 'Hazel', 'Pickles', 'Tofu']
my_empty_list = []
third_list = ['bananas', 21, 'apples', 'cherry', 600, 'weights', 'Saturday']

comma_code(my_list)
comma_code(my_empty_list)
comma_code(third_list)
