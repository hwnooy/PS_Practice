from collections import deque 

def solution(bridge_length, weight, truck_weights):
    bridge = deque([0]*bridge_length)
    truck = deque(truck_weights)
    answer = 0
    cur_weight=0
    while bridge: # truck이 아니라 bridge로 
        answer+=1 #한번마다 시간 플러스 
        
        # 공간을 먼저 비워줘야 전진을 함 
        tk = bridge.popleft()
        cur_weight-=tk
        
        
        if truck:
            if cur_weight+truck[0]<=weight:
                nexttr = truck.popleft()
                bridge.append(nexttr)
                cur_weight+=nexttr

            else:
                # 맨 처음에 브릿지를 비웠으니까 빈자리라도 채워야
                bridge.append(0)

    return answer