#!/usr/bin/env python
def main():
    print("Welcome to the Brain Games!")
    import prompt
    from brain_games.cli import welcome_user
    welcome_user()


if __name__ == '__main__':
    main()
