''' 스택을 이용하여 여는 괄호와 닫는 괄호의 짝이 맞는지를 확인하는 코드 '''
from collections import deque

def parentheses_checker(string):
    """주어진 문자열 인풋의 모든 괄호가 짝이 있는지 확인해주는 메소드"""
    print(f"테스트하는 문자열: {string}")
    stack = deque() # 사용할 스택 정의

    count = 0
    num_a = num_b = 0
    for i in range(len(string)):
        count += 1
        if string[i] == "(":
            num_a += 1
            stack.append(string[i])
            stack.append(count)

        elif string[i] == ")":
            num_b += 1
            stack.append(string[i])
            stack.append(count)

    if num_a > num_b:
        print("어케")

    print (stack)

case1 = "(1+2)*(3+5)"
case2 = "((3*12)/(41-31))"
case3 = "((1+4)-(3*12)/3"
case4 = "(12-3)*(56/3))"
case5 = ")1+14)/3"
case6 = "(3+15(*3"

parentheses_checker(case1)
parentheses_checker(case2)
parentheses_checker(case3)
parentheses_checker(case4)
parentheses_checker(case5)
parentheses_checker(case6)
