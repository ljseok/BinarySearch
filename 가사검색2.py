from bisect import bisect_left, bisect_right

def count_by_range(a, left, right):
    right_val = bisect_right(a, right)
    left_val = bisect_left(a, left)
    return right_val - left_val

arr = [[]for _ in range(10001)] # 모든 단어를 길이마다 나누는 리스트
rearr = [[]for _ in range(10001)] # 모든 단어를 길이마다 뒤집어서 나누는 리스트

def solution(words, queries):
    answer = []
    for word in words:
        arr[len(word)].append(word) # 단어를 삽입
        rearr[len(word)].append(word[::-1]) # 단어를 뒤집어서 삽입

    for list in range(10001): # 정렬
        arr[list].sort()
        rearr[list].sort()

        for str in queries:

            if str[0] != '?': # 앞에 ?가 붙은 경우
                ans = count_by_range(arr[str], str.replace('?', 'a'),str.replace('?', 'z'))
            else: # 뒤에 ?가 붙은 경우
                ans = count_by_range(rearr[str], str[::-1].replace('?', 'a'), str[::-1].replace('?', 'z'))
            answer.append(ans)
        return answer