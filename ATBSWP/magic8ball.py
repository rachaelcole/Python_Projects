# defines a function that returns a different string depending on what number it is passed as an argument
import random


def get_answer(ans_num):
    if ans_num == 1:
        return 'It is certain'
    elif ans_num == 2:
        return 'It is decidedly so'
    elif ans_num == 3:
        return 'Signs point to yes'
    elif ans_num == 4:
        return 'Signs point to no'
    elif ans_num == 5:
        return 'Yes'
    elif ans_num == 6:
        return 'No'
    elif ans_num == 7:
        return 'Reply hazy, try again'
    elif ans_num == 8:
        return 'Ask again later'
    elif ans_num == 9:
        return 'Concentrate and ask again'
    elif ans_num == 10:
        return 'Outlook not so good'
    elif ans_num == 11:
        return 'Very doubtful'


fortune = get_answer(random.randint(1, 11))
print(fortune)
