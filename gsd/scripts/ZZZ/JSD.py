import math

# 注意其中对0的特殊处理
def JSD(P, Q):
    M = [0.5 * (pp + qq) for pp, qq in zip(P, Q)]
    if 0 in M:
        raise ValueError
    KLD_PM = sum(pp * math.log(pp / mm) for (pp, mm) in zip(P, M) if pp != 0)
    KLD_QM = sum(qq * math.log(qq / mm) for (qq, mm) in zip(Q, M) if qq != 0)
    return 0.5 * KLD_PM + 0.5 * KLD_QM

P = [2,3,4,1,1]
Q = [3,3,2,1,0]

print JSD(P, Q)