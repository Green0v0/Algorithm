from collections import deque
import copy

def dfs(visit, start, node_dict):
    print(start, end=' ')
    visit[start] = True
    for i in sorted(list(node_dict[start])):
        if not visit[i]:
            dfs(visit, i, node_dict)

def bfs(visit, start, node_dict):
    dq = deque([start])
    while dq:
        cur_node = dq.popleft()
        print(cur_node, end=' ')
        for i in sorted(list(node_dict[cur_node])):
            if not visit[i]:
                visit[i] = True
                dq.append(i)

node_cnt, road_cnt, start = map(int, input().split())

node_dict = {i:set() for i in range(1, node_cnt+1)}
for _ in range(road_cnt):
    x, y = map(int, input().split())
    node_dict[x].add(y)
    node_dict[y].add(x)

visit = [False] * (node_cnt + 1)
visit[start] = True

dfs(copy.deepcopy(visit), start, node_dict)
print()
bfs(copy.deepcopy(visit), start, node_dict)

########################################################

from collections import deque

node_len, road_len, start = map(int, input().split())

node_graph = {i:list() for i in range(1, node_len+1)}
for _ in range(road_len):
    x, y = map(int, input().split())
    if y not in node_graph[x]:
        node_graph[x].append(y)
    if x not in node_graph[y]:
        node_graph[y].append(x)

def dfs(start, node_graph):
    visited = set()
    stack = [start]
    while stack:
        cur_node = stack.pop()
        if cur_node not in visited:
            print(cur_node, end=' ')
            node_graph[cur_node].sort(reverse=True)
            for i in node_graph[cur_node]:
                stack.append(i)
            visited.add(cur_node)

def bfs(start, node_graph):
    visited = set()
    dq = deque([start])
    while dq:
        cur_node = dq.popleft()
        if cur_node not in visited:
            print(cur_node, end=' ')
            node_graph[cur_node].sort()
            for i in node_graph[cur_node]:
                dq.append(i)
            visited.add(cur_node)

dfs(start, node_graph)
print()
bfs(start, node_graph)