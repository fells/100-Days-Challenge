"""
        SOLVING BUGS

        Examples:

        1 -

        def my_function():
            for i in range (1, 20):
                if i == 20:  correct is 21 ----> This will be a bug, since there can't be a 20th index in the array, rather 19 indexes
                print("You got it.")
        my_function()

        2 -

        from random import randint

        dice_img = ["1", "2", "3", "4", "5", "6"]
        dice_num = random.randint(0,5)  ---> This will be choosing between 1,2,3,4,5,6, and it will never print the first index and it will give a error when it chooses the 6
        print(dice_img[dice_num])

        3 -

        year = int(input("What's your year of birth"))
        if year > 1980 and year < 1994:
            print("You are a millennial")
        elif year >= 1994:   ---> There should be a equal sign, so it can also include the year 1994
            print("You are a Gen Z")

        4 -

        age = int(input("What's your age ?"))   --> This should be an int input, so it can be checked by the if statement

        if age > 18:
            print(f"You can drive at age {age}")

        5 -

        pages = 0
        word_per_page = 0
        pages = int(input("Number of pages: "))
        word_per_page = int(input("Number of words in a page: )) --> This is supposed to be with only 1 equal sign

        total_words = pages * word_per_page
        print(total_words)

        6 -

        def mutate(a_list):
            b_list = []
            for item in a_list:
                new_item = item * 2
                b_list.append(new_item)  ---> This has to be indented inside the For loop in order to append to b_list
            print(b_list)

        mutate([1,2,3,4,5,8,13])
"""

# FINAL PROJECT

