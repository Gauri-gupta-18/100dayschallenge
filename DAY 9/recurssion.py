def func(sum, i, N):
    if i > N:
        print("Answer =", sum)
        return

    func(sum + i, i + 1, N)

func(0, 1, 4)