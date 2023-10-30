## Question 1

number = input("Please choose the number")


def draw_squares(n):
    n = int(number)

    for i in range(n):
        print("*" * n)


##draw_squares(number)


## Question 2

def draw_triangles(n):
    n = int(number)
    for i in range(n):
        print("*" * (i + 1))


## draw_triangles(number)

## Question 3

def drawTringles2(n):
    n = int(number)
    for i in range(n, 0, -1):
        print("*" * i)


## drawTringles2(number)

## Question 4

def jumMaximum(list):
    max_number = max(list)
    x = max(list)
    list.remove(x)
    list.insert(0, x)
    return list


## print(jumMaximum([1, 2, 3, 4]))

## Question 5

def doublelist(list):
    my_new_list = [i * 2 for i in list]
    return my_new_list


##print(doublelist([1,2,3,4,5]))

## Question 6

def sublistInRange(list, min, max):
    modified_list = []
    for i in range(len(list)):
        if list[i] >= min and list[i] <= max:
            modified_list.append(list[i])

    return modified_list


## print(sublistInRange([1, 2, 3, 4, 5, 6], 3, 5))

## Question 7

def drawParallelogram(n):
    n = int(number)
    for i in range(n):
        print(i * " " + ("*" * n))


## drawParallelogram(number)


## Question 8


# def countLessThan(list, max):