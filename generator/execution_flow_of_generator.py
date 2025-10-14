def count_up_to(max):
    current = 1
    while current <= max:
        print(f"Before yield current {current} and max {max}")
        yield max
        print(f"After yield current {current} and max {max}")
        current += 1

count = count_up_to(5)
next(count)
print("One yield iteration end")
next(count)
print("Tow yield iteration end")

        