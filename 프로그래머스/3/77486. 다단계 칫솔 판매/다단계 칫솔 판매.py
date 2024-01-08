def solution(enroll, referral, seller, amount):
    answer = {i:0 for i in enroll}
    
    graph = {u:v for u, v in zip(enroll, referral)}
    graph['-'] = ''
    
    for child, a in zip(seller, amount):
        cost = a * 100
        parent = graph[child]
        while child != "-" and cost:
            answer[child] += cost - cost // 10
            cost //= 10
            if parent == '-': break
            child, parent = parent, graph[parent]
    
    return [answer[i] for i in enroll]