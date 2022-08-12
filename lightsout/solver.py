def brute_force(G):
    count = 1 << G.n
    S = []

    while(count > 0):
        G.reset()

        for i in range(0, G.n):
            if (count & (1 << i) != 0):
                G.press(G.V[i])

        if (G.check()):
            S.append(G.X)

        count = count - 1

    return S
