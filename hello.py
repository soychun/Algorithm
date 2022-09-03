def Ro(rc):
    rc_ = copy.deepcopy(rc)
    rc__ = copy.deepcopy(rc)
    for i in range(len(rc)):
        if i > 0:
            rc[i][len(rc_[0]) - 1] = rc_[i - 1][len(rc_[0]) - 1]
        if i < (len(rc) - 1):
            rc[i][0] = rc_[i + 1][0]
    for i in range(len(rc[0])):
        if i > 0:
            rc[0][i] = rc__[0][i - 1]
        if i < (len(rc[0]) - 1):
            rc[len(rc_) - 1][i] = rc__[len(rc_) - 1][i + 1]