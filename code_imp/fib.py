# 动态规划详解
## M1: w/o memory
step = [0, 0, 0]
mem_dict = {1:1, 2:1, }

def fib(N, step):
    step[0] = step[0] + 1

    if (N==1 or N==2):
        step[1] = step[1] + 1
        return 1
    else:
        step[2] = step[2] + 1
        return fib(N-1, step) + fib(N-2, step)

print(fib(30, step))
print(step)

## M2: w/ memory
step = [0, 0, 0]
mem_dict = {1:1, 2:1, }

def fib(N, step):
    step[0] = step[0] + 1

    if (N==1 or N==2):
        step[1] = step[1] + 1
        return 1
    else:
        step[2] = step[2] + 1
        return find(N, step)

def find(N, step):
    if (N in mem_dict):
        return mem_dict[N]
    else:
        mem_dict[N] = fib(N-1, step) + fib(N-2, step)
        return fib(N-1, step) + fib(N-2, step)

print(fib(30, step))
print(step)
print(mem_dict)
