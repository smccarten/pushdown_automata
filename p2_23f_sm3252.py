#Name: Stephanie McCarten
#UCID: sm3252
#CS341-009

import sys;

#this function returns true if the character read is an arithmetic operator 
def is_operator(char):
    return char=='+' or char=='-' or char=='/' or char=='*'

#function for state q0
def q0(expression,n,curr,stack):
    print("\nIn state q0")
    char=expression[curr]
    print('Symbol read: ', char)
    curr+=1
    if char=='%':
        stack.append(char)
        print('Nothing popped from the stack ',char,' Pushed onto the stack\nNow in state q1')
        q1(expression,n,curr,stack)
    else:
        crash()


#function for state q1
def q1(expression,n,curr,stack):
    print('\nIn state q1')
    char=expression[curr]
    print('Symbol read: ', char)
    curr+=1
    if char!='#':
        crash()
    else:
        print('Nothing popped from the stack\nNothing pushed onto the Stack\nNow in state q2')
        q2(expression,n,curr,stack)


#function for state q2      
def q2(expression,n,curr,stack):
    print('\nIn state q2')
    if curr < n:
        char=expression[curr]
        print('Symbol read: ', char)
        curr+=1
    else:
        print('Expression rejected')
    if char.isdigit():
        print('Nothing popped from the stack\nNothing pushed onto stack\nNow in state q2')
        q2(expression,n,curr,stack)
    elif char=='.':
        print('Noting popped from the stack\nNothing pushed onto the stack\n Now in state q3')
        q3(expression,n,curr,stack)
    elif char=='(':
        stack.append(char)
        print('Nothing popped from the stack',char,'\nPushed onto the stack\nNow in state q4')
        q4(expression,n,curr,stack)
    else:
        crash()

#function for state q3
def q3(expression,n,curr,stack):
    print('\nIn state q3')
    if curr<n:
        char=expression[curr]
        print('Symbol Read ',char)
        curr+=1
    else:
        print('Expression rejected')
    if char.isdigit():
        print('Nothing popped from the stack\nNothing pushed onto stack\nNow in state q3')
        q3(expression,n,curr,stack)
    elif is_operator(char):
        print('Nothing popped from the stack\nNothing pushed onto stack\nNow in state q2')
        q2(expression,n,curr,stack)
    elif char==')':
        val=stack.pop()
        if val=='(':
            print(val,' Popped from the stack\nNothing pushed onto the stack\nNow in state q5')
            q5(expression,n,curr,stack)
        else:
            crash()
    elif char=='>':
        val=stack.pop()
        if val=='%':
            print(val,' Popped from the stack.\nNothing pushed onto the stack\nNow in state q6')
            q6(expression,n,curr,stack)
        else:
            crash()
    else:
        crash()

#function for state q4
def q4(expression,n,curr,stack):
    print('\nIn state q3')
    if curr<n:
        char=expression[curr]
        print('Symbol Read', char)
        curr+=1
    else:
        print('Expression Rejected\n')
    if char.isdigit():
        print('\nNothing popped from the stack\nNothing pushed onto stack\nNow in state q2')
        q2(expression,n,curr,stack)
    elif char=='(':
        stack.append(char)
        print('\nNothing popped from the stack',char,'\nPushed onto the stack\nNow in state q2')
        q4(expression,n,curr,stack)
    elif char=='.':
        print('\nNothing popped from the stack\nNothing pushed onto stack\nNow in state q3')
        q3(expression,n,curr,stack)
    else:
        crash()

#function for state q5
def q5(expression,n,curr,stack):
    print('\nIn state q5')
    if curr<n:
        char=expression[curr]
        print('Symbol read:', char)
        curr+=1
    else:
        print('\nExpression Rejected\n')
    if is_operator(char):
        print('Nothing popped from the stack\nNothing pushed onto stack\nNow in state q2')
        q2(expression,n,curr,stack)
    elif char=='(':
        stack.append(char)
        print('Nothing popped from the stack',char,'\nPushed onto the stack\nNow in state q4')
        q4(expression,n,curr,stack)
    elif char==')':
        val=stack.pop()
        if val=='(':
            print(val,' Popped from the stack\nNothing pushed onto the stack\nNow in state q5')
            q5(expression,n,curr,stack)
        else:
            crash
    elif char=='>':
        val=stack.pop()
        if val=='%':
            print(val,' Popped from the stack\nNothing pushed onto the satck\nNow in state q6')
            q6(expression,n,curr,stack)
        else:
            crash()
    else:
        crash()

#function for state q6
def q6(expression,n,curr,stack):
    print('\nExpression Accepted\n')

#function for crashing 
def crash():
    print("\nThe PDA crashed, expression rejected.\n")


#set up the output file where the results will be written
with open('p2_23f_sm3252_output.txt', 'w') as f:
     sys.stdout = f
     print('Project 2 for CS 341 009\nSemester: Fall 2023\nWritten by: Stephanie McCarten, sm3252\nInstructor: Marvin Nakayama, marvin@njit.edu\n')
#set read variable to true to start reading the input file
     read = True

#while read is true, we read the input file unless we encounter 'n' which indicates that we no longer want to read from the file
     while read:
        input = sys.stdin.readline().strip()
        if input == 'n':
            read = False
        else:
            expression = sys.stdin.readline().strip()
            n = len(expression) #getting length of expression and setting counter variable to zero to go through each character in the expression
            curr = 0
            stack=[] #initializing my empty stack
            print(expression)
            q0(expression,n,curr,stack)
            
            