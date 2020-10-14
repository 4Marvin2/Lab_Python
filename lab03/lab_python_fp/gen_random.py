import random


def gen_random(num_count, begin, end):
    for i in range(num_count):
        yield random.randint(begin, end)


def main():
    gen = gen_random(5, 1, 3)
    print(gen.__next__())
    #gen = gen_random(5, 1, 3)
    #for i in gen:
        #print(i, end=' ')


if __name__ == "__main__":
    main()
