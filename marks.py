def get(N):
    marks=[]
    for i in range(N):
        while True:
            temp=float(input(f"Enter the marks for student {i+1} : "))
            if temp<0 or temp>100:
                print("Invalid Marks, Please Enter Again")
            else:
                marks.append(temp)
                break
    return marks

def mark_with_highest_frequency(marks):
    cntemp=-1
    for i in range(len(marks)):
        cnt = -1
        temp=marks[i]
        for j in range(len(marks)):
            if marks[j]==temp:
                cnt+=1
        if cnt>cntemp:
            cntemp=cnt
    return marks[cntemp]


def avg(marks):
    sum_of_marks = sum(marks)
    average = sum_of_marks / len(marks)
    return average

def high(marks):
    max_mark = marks[0]
    for i in range(len(marks)):
        if marks[i] > max_mark:
            max_mark = marks[i]
    return max_mark

def low(marks):
    min_mark = 100
    for i in range(len(marks)):
        if marks[i] < min_mark and marks[i]!=0:
            min_mark = marks[i]
    return min_mark

def absentcount(marks):
    count=0
    for mark in marks:
        if mark==0:
            count+=1
    return count

def main():
    num = int(input("Enter the total number of students : "))
    marks = get(num)
    print("The Average Marks are {:.2f}".format(avg(marks)))
    print("Highest score ", high(marks))
    print("Lowest score ", low(marks))
    print("Total absent students ", absentcount(marks))
    print("Marks with highest frequency ", mark_with_highest_frequency(marks))

if __name__=="__main__":
    main()
