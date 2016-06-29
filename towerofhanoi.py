def moveTower(height,fromPole, toPole, withPole):
    if height >= 1:
        print "    " * (3-height),"moving tower :", height, fromPole,toPole
        moveTower(height-1,fromPole,withPole,toPole)
        moveDisk(fromPole,toPole, height)
        moveTower(height-1,withPole,toPole,fromPole)

def moveDisk(fp,tp, height):
    print "    " * (4-height),"moving disk", "~"*height, "from",fp,"to",tp

moveTower(3,"A","B","C")
