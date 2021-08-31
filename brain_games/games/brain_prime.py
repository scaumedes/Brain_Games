def main():
    import prompt
    import random
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print('Hello, {}!'.format(name))
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    correct_answers_count = 0
    while correct_answers_count < 3:
        generated_number = random.randint(1, 100)
        print('Question: {}'.format(generated_number))
        user_answer = prompt.string('Your answer: ')
        if generated_number > 1:
            for i in range(2, int(generated_number / 2) + 1):
                if (generated_number % i) == 0:
                    true_answer = 'no'
                    break
                else:
                    true_answer = 'yes'
        else:
            true_answer = 'no'
        if user_answer == true_answer:
            correct_answers_count = correct_answers_count + 1
            print('Correct!')
            continue
        else:
            correct_answers_count = 0
            print("'{}' is wrong answer ;(. Correct answer was '{}'.".format(user_answer, true_answer))
            print("Let's try again, {}!".format(name))
            break
    if correct_answers_count == 3:
        print('Congratulations, {}!'.format(name))


if __name__ == '__main__':
    main()
