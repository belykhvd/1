# ------------------------ DSU -------------------------------- 
def find_set(parent, v):
	if v == parent[v]:  # v is root
		return v
	parent[v] = find_set(parent, parent[v])
	return parent[v]

def union_sets(parent, rank, a, b):
	if rank[a] < rank[b]:
		a, b = b, a
	parent[b] = a
	if rank[a] == rank[b]:
		rank[a] += 1

# -------------------------- I/O ------------------------------
with open('in.txt') as f:
	n = int(f.readline())
	edge_weight = {}
	for i in range(n):
		s = list(map(int, f.readline().split()[:-1]))
		for v, w in zip(s[::2], s[1::2]):
			edge_weight[(i, v-1)] = w

# ------------------------ BorKrus ----------------------------
edges = list(sorted(edge_weight, key=lambda k:edge_weight[k]))
parent, rank = [i for i in range(n)], [0] * n
mst = []
while len(mst) != n - 1:
	v, w = edges.pop(0)
	p, q = find_set(parent, v), find_set(parent, w)
	if p != q:
		union_sets(parent, rank, p, q)
		mst.append((v, w))

# ----------------------------- I/O ----------------------------------
o = {i: [] for i in range(n)}
for v, w in mst:
	o[v].append(w)
with open('out.txt', 'w') as f:
	for i in range(n):
		f.write(' '.join(map(str, list(map(lambda x: x + 1, sorted(o[i]))) + ['0'])) + '\n')
	f.write(str(sum([edge_weight[e] for e in mst])))
