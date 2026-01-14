class Solution:
    def separateSquares(self, squares: List[List[int]]) -> float:
        events = []
        S = set()
        for x, y, l in squares:
            events.append((y, 1, x, x + l))
            events.append((y + l, -1, x, x + l))
            S.add(x)
            S.add(x + l)
        events.sort()
        S = sorted(S)
        id = {x: i for i, x in enumerate(S)}
        L = len(S) - 1
        count = [0] * (4 * L)
        length = [0] * (4 * L)

        def update(node, l, r, ql, qr, val):
            if qr <= l or r <= ql:
                return
            if ql <= l and r <= qr:
                count[node] += val
            else:
                mid = (l + r) // 2
                update(node * 2, l, mid, ql, qr, val)
                update(node * 2 + 1, mid, r, ql, qr, val)
            if count[node] > 0:
                length[node] = S[r] - S[l]
            else:
                length[node] = (
                    length[node * 2] + length[node * 2 + 1]
                    if l + 1 < r else 0)

        z = events[0][0]
        net = 0
        slabs = []
        for y, typ, x1, x2 in events:
            dy = y - z
            if dy > 0:
                area = dy * length[1]
                slabs.append((z, y, length[1], area))
                net += area
            update(1, 0, L, id[x1], id[x2], typ)
            z = y
        n2 = net / 2
        res = 0
        for y1, y2, width, area in slabs:
            if res + area >= n2:
                return y1 + (n2 - res) / width
            res += area
        return z