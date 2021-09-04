def main():
    import prompt
    import random
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print('Hello, {}!'.format(name))
    print('What number is missing in the progression?')
    correct_answers_count = 0
    while correct_answers_count < 3:
        difference = random.randint(1, 10)
        first_number = random.randint(1, 50)
        list_of_numbers = [first_number, ]
        generated_number = first_number
        hidden_number = random.randint(2, 9)
        i = 1
        k = 0
        while i <= 9:
            generated_number = generated_number + difference
            list_of_numbers.append(generated_number)
            i = i + 1
        print('Question:', end=' ')
        while k <= 8:
            if k == hidden_number:
                print('..', end=' ')
            else:
                print(list_of_numbers[k], end=' ')
            k = k + 1
        user_answer = int(prompt.string('\nYour answer: '))
        if user_answer == list_of_numbers[hidden_number]:
            correct_answers_count = correct_answers_count + 1
            print('Correct!')
            continue
        else:
            correct_answers_count = 0
            print("'{}' is wrong answer ;(. Correct answer was '{}'.".format(user_answer, list_of_numbers[hidden_number]))
            print("Let's try again, {}!".format(name))
            break
    if correct_answers_count == 3:
        print('Congratulations, {}!'.format(name))


if __name__ == '__main__':
    main()
