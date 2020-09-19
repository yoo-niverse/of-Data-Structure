''' 스택을 이용하여 여는 괄호와 닫는 괄호의 짝이 맞는지를 확인하는 코드 '''
from collections import deque

def parentheses_checker(string):
    """주어진 문자열 인풋의 모든 괄호가 짝이 있는지 확인해주는 메소드"""
    print(f"테스트하는 문자열: {string}")
    stack = deque() # 사용할 스택 정의

    for i in range(len(string)):
        if string[i] == "(":
            stack.append(i)
        # 반복문 1 : 문자열을 처음부터 돌며 여는 괄호를 만날 때마다 stack에 해당 괄호의 index를 저장한다.

    for i in range(len(string)):
        if string[i] == ")":
            try:
                stack.pop()
            except (IndexError):
                print(f"문자열 {i} 번째 위치에 있는 닫는 괄호에 맞는 열리는 괄호가 없습니다")
        # 반복문 2 : 다시 처음부터 문자열을 돌며 닫는 괄호를 만날 때마다 stack에서 pop 연산을 수행한다.
        # 이때, stack이 비어있어 pop이 불가능하다면 맞는 여는 괄호 짝이 없는 것이므로 경고문을 출력한다.

    if stack:
        while stack:
            i = stack.pop()
            print(f'문자열 {i} 번째 위치에 있는 괄호가 닫히지 않았습니다')
        # 반복문 3 : 2번째 반복문이 수행된 후에도 stack에 요소가 남아있다면, 닫는 괄호 짝이 없는 여는 괄호들이다.
        # stack에 남는 요소들이 없을 때까지 pop을 하며 해당 data를 index로 경고문을 출력한다.

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
