def accumulator():
    total = 0
    while True:
        print(f"Before yield, total={total}")
        value = yield total
        print(f"After yield, value={value}, total={total}")
        if value is None: break
        total += value

acc = accumulator()
next(acc)
acc.send(1)
acc.send(5)
acc.send(20)
acc.send(50)