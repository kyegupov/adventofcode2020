trans=dict(F='0',B='1',R='1',L='0')
res = 0
sids = set()
for l in open('input.txt').read().splitlines():
    r = ''.join([trans[c] for c in l[:7]])
    rr = int(r,base=2)
    c = ''.join([trans[c] for c in l[7:]])
    cc = int(c,base=2)

    sid = rr*8+cc
    if sid > res:
        res = sid
    sids.add(sid)

for l in range(1024):
    if not l in sids and (l-1) in sids and (l+1) in sids:
        print(l)