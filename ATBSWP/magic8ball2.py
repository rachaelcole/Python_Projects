import random

messages = ['It is certain',
            'It is decidedly so',
            'Signs point to yes',
            'Signs point to no',
            'Yes',
            'No',
            'Reply hazy, try again',
            'Concentrate and ask again',
            'Outlook not so good',
            'Very doubtful',
            'Trust yourself'
            ]

print(messages[random.randint(0, len(messages) - 1)])
