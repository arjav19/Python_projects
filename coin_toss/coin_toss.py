import random

def toss_coin():
    list1 = ["heads", "tails"]
    return random.choice(list1)

def main():
    while True:
        flag = False

        answer = input('Pick a side for coin toss (heads/tails): ')
        if answer.lower() not in ['heads', 'tails']:
            continue

        result = toss_coin()
        print(f'You got ... {result} ')
        
        # Bug Fix 1: Added () to execute answer.lower()
        if answer.lower() == result:
            # Bug Fix 2: Fixed typo "thr" -> "the"
            print('Nice you have won the coin toss !')
        else:
            print('PPF. Better luck next time.')
        
        while True:
            answer_y = input("Wanna play again? (yes/no): ")
            if answer_y.lower() in ['no', 'n']:
                flag = True
                break
            elif answer_y.lower() in ['yes', 'y']:
                break
            else:
                continue

        if flag:
            break    

# Bug Fix 3: Added () to call main()
if __name__ == "__main__":
    main()
