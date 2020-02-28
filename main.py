

def estimate_pi(n)
    circlePoint = 0
    allPoins = 0
    for _ in range(n):
        x = random.uniform(0,1)
        y = random.uniform(0,1)
        distance = x**2 + y**2
        if distance <=1:
            circlePoint += 1
        allPoins += 1

        return 4*circlePoint/allPoins
