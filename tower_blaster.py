def instruction():
    '''
    This function tells the rule of the game.
    '''

    print("Game starts here!")
    print("A Tower Blaster game starts with a main pile of 60 bricks, each numbered from 1 to 60.")
    print("Think of the numbers on the bricks as the width of the bricks.")
    print("The objective is to be the first player to arrange 10 bricks in your own tower from lowest to highest (from the top down), because the tower will be unstable otherwise.")
    print("="*50)

def setup_bricks():
    '''
    This function creates the 60-brick main pile and the 0-brick discard pile at the beginning of the game.
    '''

    main_pile = list(range(1,61))
    discard = []
    return main_pile, discard

def shuffle_bricks(bricks):
    '''
    This function shuffles the given bricks.
    '''

    import random
    random.shuffle(bricks)

def check_bricks(main_pile, discard):
    '''
    This function checks if there are any cards left in the given main pile of bricks.
    If not, this function shuffles the discard pile and moves those bricks to the main pile.
    Then this function turns over the top card to be the start of the new discard pile.
    '''

    if main_pile == []:
        shuffle_bricks(discard)
        main_pile.extend(discard)
        discard.clear()
        discard.append(main_pile[0])
        main_pile.pop(0)

def check_tower_blaster(tower):
    '''
    This function checks if stability of a tower has been achieved.
    '''

    tower1 = tower.copy()
    tower1.sort()
    if (tower1 == tower):
        return True
    else:
        return False

def get_top_brick(brick_pile):
    '''
    This function removes and returns the top brick from any given pile of bricks.
    '''

    top = brick_pile[0]
    brick_pile.pop(0)
    return top

def deal_initial_bricks(main_pile):
    '''
    This function starts the game by dealing two sets of 10 bricks each, from the given main_pile.
    '''

    computer_tower = []
    user_tower = []
    for i in range(0,10):
        computer_tower.insert(0, get_top_brick(main_pile))
        user_tower.insert(0, get_top_brick(main_pile))

    return computer_tower, user_tower

def add_brick_to_discard(brick, discard):
    '''
    This function adds the given brick to the top of the given discard pile.
    '''

    discard.insert(0, brick)

def find_and_replace(new_brick, brick_to_be_replaced, tower, discard):
    '''
    This function finds the given brick to be replaced in the given tower and replaces it with the given new brick.
    This function checks if the given brick to be replaced in the given tower is truly replaced with the given new brick.
    '''

    if brick_to_be_replaced in tower:
        desired_index = tower.index(brick_to_be_replaced)
        tower[desired_index] = new_brick
        discard.insert(0, brick_to_be_replaced)
        return True
    else:
        return False

def computer_play(tower, main_pile, discard):
    '''
    This function is the computer's strategy of replacing bricks and returns the picked brick and the new tower.
    '''

    # If the top brick of the discard pile <= 30, pick it.
    # If the top brick of the discard pile >30, pick the top brick of the main pile anyway.
    # The replacement rule is:
    # If the top brick of the pile is 1-6, replace the 1st brick of the computer tower with it.
    # If 7-12, replace the 2nd brick with it.
    # If 13-18, replace the 3rd brick with it.
    # If 19-24, replace the 4th brick with it.
    # If 25-30, replace the 5th brick with it.
    # If 31-36, replace the 6th brick with it.
    # If 37-42, replace the 7th brick with it.
    # If 43-48, replace the 8th brick with it.
    # If 49-54, replace the 9th brick with it.
    # If 55-60, replace the 10th brick with it.

    discard_top = discard[0]

    if discard_top <= 30:
        computer_index = (discard_top - 1) // 6
        brick_replaced = tower[computer_index]
        tower[computer_index] = discard_top
        discard[0] = brick_replaced
        # Print the brick the computer picked from the discard pile and return the new computer tower (not printed).
        print("The computer picked", tower[computer_index], "from the discard pile.")
        return tower
    if discard_top > 30:
        main_top = get_top_brick(main_pile)
        computer_index = (main_top - 1) // 6
        brick_replaced = tower[computer_index]
        tower[computer_index] = main_top
        discard.insert(0, brick_replaced)
        # Print the brick the computer picked from the main pile and return the new computer tower (not printed).
        print("The computer picked", tower[computer_index], "from the main pile.")
        return tower



def main():
    '''
    This function puts everything together.
    All user input should take place in the main function.
    '''

    main_pile = setup_bricks()[0]
    shuffle_bricks(main_pile)
    discard = setup_bricks()[1]
    add_brick_to_discard(get_top_brick(main_pile), discard)

    initial = deal_initial_bricks(main_pile)
    computer_tower = initial[0]
    user_tower = initial[1]
    instruction()
    print("Computer tower:", computer_tower)
    print("Your tower:", user_tower)

    while check_tower_blaster(computer_tower) == False and check_tower_blaster(user_tower) == False:

        print("-" * 50)
        print("COMPUTER'S TURN:")
        print("The top brick on the discard pile is", discard[0])
        # Call the computer_play function and get the brick the computer picked (which will be printed) and the new computer tower (which will not be printed).
        computer_play(computer_tower, main_pile, discard)

        print("The computer replaced a brick.")

        # Call the check_bricks function to check if the main pile is empty after each turn.
        # If it is empty, move all the bricks in the discard pile to main pile and turn over the top brick to the discard pile.
        check_bricks(main_pile, discard)


        if check_tower_blaster(computer_tower) == True or check_tower_blaster(user_tower) == True:
            print("-"*50)
            print("Game over!")
            if check_tower_blaster(computer_tower) == True:
                print("Computer wins!")
            if check_tower_blaster(user_tower) == True:
                print("You win!")
            break

        print("-"*50)

        print("NOW IT'S YOUR TURN!")
        print("Your tower:", user_tower)
        print("The top brick on the discard pile is", discard[0])
        while 1==1:
            choice = input("Type 'D' to take the discard brick or 'M' for a mystery brick.")
            if choice[0] == 'D' or choice[0] == 'd':
                print("You picked", discard[0], "from the discard pile.")

                while 1==1:
                    d_where_replace = int(input("Where do you want to place this brick? Type a brick number to replace in your tower."))

                    if find_and_replace(discard[0], d_where_replace, user_tower, discard) == True:
                        find_and_replace(discard[0], d_where_replace, user_tower, discard)
                        print("You replaced", d_where_replace, "with", discard[1])
                        discard.pop(1)
                        print("Your Tower:", user_tower)
                        break
                break


            if choice[0] == 'M' or choice[0] == 'm':
                m = get_top_brick(main_pile)
                print("The top brick of the main pile is", m)

                while 1==1:
                    yes_or_no = input("Do you want to use this brick? Type 'Y' or 'N' to skip turn.")
                    if yes_or_no[0] == 'Y' or yes_or_no[0] == 'y':
                        while 1 == 1:
                            d_where_replace = int(input("Where do you want to place this brick? Type a brick number to replace in your tower."))

                            if find_and_replace(m, d_where_replace, user_tower, discard) == True:
                                find_and_replace(m, d_where_replace, user_tower, discard)
                                print("You replaced", d_where_replace, "with", m)

                                print("Your Tower:", user_tower)
                                break
                        break


                    if yes_or_no[0] == 'N' or yes_or_no[0] == 'n':
                        print("Your tower is still", user_tower)
                        add_brick_to_discard(m, discard)
                        break

                break

        # Call the check_bricks function to check if the main pile is empty after each turn.
        # If it is empty, move all the bricks in the discard pile to main pile and turn over the top brick to the discard pile.
        check_bricks(main_pile, discard)


        if check_tower_blaster(computer_tower) == True or check_tower_blaster(user_tower) == True:
            print("-"*50)
            print("Game over!")
            if check_tower_blaster(computer_tower) == True:
                print("Computer wins!")
            if check_tower_blaster(user_tower) == True:
                print("You win!")
            break



if __name__ == '__main__':
    main()


