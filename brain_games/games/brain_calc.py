def main():
    import random
    import prompt
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print('Hello, {}!'.format(name))
    print('What is the result of the expression?')
    correct_answers_count = 0
    while correct_answers_count < 3:
        n1 = random.randint(1, 40)
        n2 = random.randint(1, 40)
        list_used_symbols = ['-', '+', '*']
        action = random.choice(list_used_symbols)
        user_answer = prompt.string('Question: {} {} {}\n'.format(n1, action, n2))
        if action == '-':
            true_asnswer = n1 - n2
        elif action == '+':
            true_asnswer = n1 + n2
        elif action == '*':
            true_asnswer = n1 * n2
        if int(user_answer) == true_asnswer:
            print('Correct!')
            correct_answers_count = correct_answers_count + 1
            continue
        else:
            print("{} is wrong answer ;(. Correct answer was {}.".format(user_answer, true_asnswer))
            print("Let's try again, {}!".format(name))
            correct_answers_count = 0
            break
    if correct_answers_count == 3:
        print('Congratulations, {}!'.format(name))


if __name__ == '__main__':
    main()
