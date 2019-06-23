# Once a week, Vietlott will conduct a draw.
# The draw will generate 6 numbers between 0 and 45 (use Math random to do this)
import random


def draw_jackpot():
    lottery_ticket = {random.randint(0, 45)}
    while len(lottery_ticket) < 6:
        lottery_ticket.add(random.randint(0, 45))
    return lottery_ticket

# ---------------------------------------------------------------------------------------------
# Buy by generate 6 random numbers (0-45) until they match the Vietlott number (jackpot).
# Print the number of times the buying process needs before the matching happens.
# Show number in a line and stop when the jackpot happens.


def buy_till_jackpot(jackpot: set):
    if len(jackpot) != 6:
        print("You haven't drawn any jackpot yet :)")
        return -1
    else:
        bought_lottery = draw_jackpot()
        times_bought = 1
        print("Round {}: {}".format(times_bought, bought_lottery))
        while not bought_lottery.issubset(jackpot):
            bought_lottery = draw_jackpot()
            print("Round {}: {}".format(times_bought, bought_lottery))
            times_bought += 1
        print("----------------------------\nThe jackpot is: " + str(jackpot))
        return times_bought

# ---------------------------------------------------------------------------------------
# Run the trigger 5 times and calculate the average number of times
# one needs to buy to become a winner.


def five_time_average(jackpot: set):
    total_lotteries_bought = 0
    if len(jackpot) != 6:
        print("You haven't drawn any jackpot yet :)")
        return -1
    else:
        total_lotteries_bought += buy_till_jackpot(jackpot)
        total_lotteries_bought += buy_till_jackpot(jackpot)
        total_lotteries_bought += buy_till_jackpot(jackpot)
        total_lotteries_bought += buy_till_jackpot(jackpot)
        total_lotteries_bought += buy_till_jackpot(jackpot)
        print("----------------------------\nAverage 5 times = {}".format(total_lotteries_bought/5))
