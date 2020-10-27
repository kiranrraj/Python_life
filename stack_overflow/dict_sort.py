soccer = {
    1: {"England": 2, "Poland": 3},
    2: {"Italy": 2, "Sweeden": 0},
    3: {"Spain": 2, "Belgium": 2}
}

res = {key: dict(sorted(val.items(), key=lambda ele: ele[1]))
       for key, val in soccer.items()}
print(res)
