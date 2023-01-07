def random_wish (name):
    import random

    
    wish_list = [
        "I wish you a fantastic New Year!",
        "May the coming year bring success to you.",
        "I wish you happiness in the year to come.",
        "Wishing you a New Year filled with happiness and good fortune!",
        "I wish you good health and happiness for the New Year!",
        "May your wishes come true!",
        "Have a promising and great New year!",
        "I wish you a smashing New Year filled with joy.",
        "I wish you happiness, health and so many good things in your life.",
        "I wish you magical moments, wonderful memories, and positive!"
    ]
    
    wish_num = random.randint(0, len(wish_list)-1)
    
    print(f'Happy New Year to you, {name}!')
    print(wish_list[wish_num])
    
    
name = input('Please, enter Your name: ')
random_wish(name)