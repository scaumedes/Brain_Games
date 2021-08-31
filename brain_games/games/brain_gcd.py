def main():
    import prompt
    import random
    from math import gcd
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print('Hello, {}!'.format(name))
    print('Find the greatest common divisor of given numbers.')
    correct_answers_count = 0
    while correct_answers_count < 3:
        n1 = random.randint(1,100)
        n2 = random.randint(1,100)
        print('Question: {} {}'.format(n1, n2))
        user_answer = int(prompt.string('Your answer: '))
        true_asnswer = gcd(n1, n2)
        if user_answer == true_asnswer:
            correct_answers_count = correct_answers_count + 1
            print('Correct!')
            continue
        else:
            correct_answers_count = 0
            print("'{}' is wrong answer ;(. Correct answer was '{}'.".format(user_answer, true_asnswer))
            print("Let's try again, {}!".format(name))
            break
    if correct_answers_count == 3:
        print('Congratulations, {}!'.format(name))


if __name__ == '__main__':
    main()