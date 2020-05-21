g = {'교대': {'동대문운동장': 34.0, '사당': 7.0, '충무로': 18.0},
 '동대문운동장': {'교대': 34.0, '을지로3가': 3.0, '충무로': 2.0},
 '사당': {'교대': 7.0, '서울역': 16.0, '신도림': 17.0},
 '서울역': {'사당': 16.0, '시청': 2.0, '신도림': 17.0, '충무로': 5.0},
 '시청': {'서울역': 2.0, '신도림': 23.0, '을지로3가': 4.0},
 '신도림': {'사당': 17.0, '서울역': 17.0, '시청': 23.0},
 '을지로3가': {'동대문운동장': 3.0, '시청': 4.0, '충무로': 1.0},
 '충무로': {'교대': 18.0, '동대문운동장': 2.0, '서울역': 5.0, '을지로3가': 1.0}}

nodes = {source for source in g}
nodes.update({dest for destinations in g.values() for dest in destinations})
print(nodes)

n_nodes = len(nodes)
n_edges = sum((len(destinations) for destinations in g.values()))
print('n_nodes = {}, n_edges = {}'.format(n_nodes, n_edges))
# n_nodes = 8, n_edges = 26

max_cost =  max(w for nw in g.values() for w in nw.values())
init_cost = n_nodes * (max_cost + 1)
print('max_cost = {}, init_cost = {}'.format(max_cost, init_cost))
# max_cost = 34.0 init_cost = 280.0

def initialize(start):
  cost = {node: (0 if node == start else init_cost) for node in nodes}
  return cost


cost = initialize('시청')


def update(cost):
 changed = False
 for from_, to_weight in g.items():
   for to_, weight in to_weight.items():
    if cost[to_] > cost[from_] + weight:
     before = cost[to_]
     after = cost[from_] + weight
     cost[to_] = after
     changed = True
     print('{} -> {} : {} -> {}'.format(from_, to_, before, after))
 return cost, changed

cost = initialize('시청')
cost, changed = update(cost)


def ford(start, destination):
 cost = initialize(start)
 for _ in range(n_nodes):
  cost, changed = update(cost)
  if not changed:
   break
 return cost

ford('시청', '사당')['사당']


def path_finder(start, dest, cost):
 immatures = [[start]]
 mature = []
 for _ in range(n_nodes):
  immatures_ = []
  for path in immatures:
   last = path[-1]
   for adjacent, c in g[last].items():
    if cost[adjacent] == cost[last] + c:
     if adjacent == dest:
      mature.append([p for p in path] + [adjacent])
     else:
      immatures_.append([p for p in path] + [adjacent])
  immatures = immatures_
 return mature


path_finder('시청', '사당', cost)

#https://lovit.github.io/nlp/graph/2018/08/21/ford_for_shortestpath/ 발최