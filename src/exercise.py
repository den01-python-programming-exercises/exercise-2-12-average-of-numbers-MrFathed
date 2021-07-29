def main():
    #write your code below this line
    count = 0
    sum_of_num  = 0

    while True:
        number = int(input("Give a number:"))

        if number == 0:
            break

        count = count + 1
        sum_of_num = sum_of_num + number
    
    average = sum_of_num / count

    print("Average of numbers: " + str(average))

if __name__ == '__main__':
    main()
