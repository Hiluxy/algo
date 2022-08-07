def solution(number, k):
    answer = []
    remove_num = k
    for s in number:
        if len(answer)==0:
            answer.append(s)
        elif answer[-1] < s and k>0:
            answer.pop()
            k -= 1
            answer.append(s)
            while len(answer) > 1:
                if answer[-2] < s and k>0:
                    answer.pop(-2)
                    k -= 1
                else:
                    break      
        else:
            answer.append(s)
    answer = "".join(answer)
    if len(answer) != len(number) - remove_num:
        answer = answer[:-remove_num]
    return answer
