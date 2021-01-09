# Coin Toss Simulation and Probability
import numpy as np


def flip_coin():
    """Simulate flipping a coin.

    Returns
    -------
    str
        "H" for heads/ "T" for tails.
    """
    flip = np.random.binomial(1, .5, 1)
    if flip[0] == 1:
        side = "H"
    else:
        side = "T"
    return side


def flip_condition(stop_condition=['H', 'T'], print_opt=False):
    """Flip coin until flip pattern is met.

    Parameters
    ----------
    stop_condition: list
        The sequence of flips to be matched before flipping stops.

    print_opt: bool
        Option to print the sequence of flips.

    Returns
    -------
    int
        The number of flips it took to match the pattern.
    """
    flip_list = []

    current_index = 0
    current_condition = None
    while current_condition != stop_condition:
        flip_list.append(flip_coin())
        if len(flip_list) >= len(stop_condition):
            current_condition = [flip_list[i] for i in
                                 range(current_index - len(stop_condition) + 1, current_index + 1)]
        else:
            pass
        current_index += 1

    if print_opt:
        print(flip_list)
    return current_index

#mean_ht = np.mean([flip_condition(['H', 'T']) for i in range(1000000)])
#mean_hh = np.mean([flip_condition(['H', 'H']) for i in range(1000000)])
mean_hhh = np.mean([flip_condition(['H', 'H', 'H', 'H', 'H', 'H', ]) for i in range(1000000)])

#print("Average # of flips to achieve heads and then heads again: {}".format(mean_hh))
#print("Average # of flips to achieve heads and then tails: {}".format(mean_ht))
print("Average # of flips to achieve heads and then tails: {}".format(mean_hhh))


