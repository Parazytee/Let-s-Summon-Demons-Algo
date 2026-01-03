
from scipy.special import comb


# might require precalculating all these to optimise the final product
def D_DiceTotal(n: int, s: int, T: int):
    # pdf
    highLimit: float = int((T-n)/s)

    subtotal = 0
    for k in range(0, highLimit+1):
        combinatory = comb(n, k)
        mclauren = comb(T-s*k-1, n-1)
        subtotal += combinatory*mclauren*(-1)**k

    return subtotal*(1/s)**n


def F_DiceTotal(n: int, s: int, T: int):
    # cdf
    if n < 0 or s < 0 or T < 0 or T < n:
        return 0

    if T > n*s:
        return 1

    subtotal = 0
    for k in range(n, T+1):
        subtotal += D_DiceTotal(n, s, k)
    return subtotal
