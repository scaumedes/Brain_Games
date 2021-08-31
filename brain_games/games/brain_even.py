def main():
    import random
    import prompt
    print("Welcome to the Brain Games!")
    name = prompt.string('May I have your name? ')
    print('Hello, {}!'.format(name))
    print('Answer "yes" if the number is even, otherwise answer "no".')
    correct_answers_count = 0
    while correct_answers_count < 3:
        n = random.randint(1,40)
        print('Question: {}'.format(n))
        answer = prompt.string('Your answer: ')
        if n % 2 == 0:
            if answer == 'yes':
                print('Correct!')
                correct_answers_count = correct_answers_count + 1
                continue
            else:
                print("'no' is wrong answer ;(. Correct answer was 'yes'. \nLet's try again, {}!".format(name))
                correct_answers_count = 0
                break
        if n % 2 != 0:
            if answer == 'yes':
                print("'yes' is wrong answer ;(. Correct answer was 'no'. \nLet's try again, {}!".format(name))
                correct_answers_count = 0
                break
            elif answer != 'yes' and answer != 'no':
                print("'yes' is wrong answer ;(. Correct answer was 'no'. \nLet's try again, {}!".format(name))
                correct_answers_count = 0
                break
            else:
                print('Correct!')
                correct_answers_count = correct_answers_count + 1
                continue
    if correct_answers_count == 3:
        print('Congratulations, {}!'.format(name))

if __name__ == '__main__':
    main()
