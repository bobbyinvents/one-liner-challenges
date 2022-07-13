from __future__ import annotations
from beginnercodes.challenges import test


# Multiple one-liners
odds_vs_evens = lambda x: "even" if (o:=sum(int(i) for i in str(x) if int(i)%2)) < (e:=sum(int(i) for i in str(x) if not int(i)%2)) else "odd" if o > e else "equal"
odds_vs_evens = lambda x: "even" if (o:=sum(map(int, filter(lambda a: int(a)%2, str(x))))) < (e:=sum(int(i) for i in str(x) if not int(i)%2)) else "odd" if o > e else "equal"
odds_vs_evens = lambda x: "even" if (o:=(lambda y: sum(map(int, filter(lambda a: int(a)%2==y, str(x)))))(1)) < (e:=sum(int(i) for i in str(x) if not int(i)%2)) else "odd" if o > e else "equal"
odds_vs_evens = lambda x: "even" if (o:=(l:=lambda y: sum(int(i) for i in str(x) if int(i)%2==y))(1)) < (e:=l(0)) else "odd" if o > e else "equal"
odds_vs_evens = lambda x: "odd" if (o:=(l:=lambda y: sum(filter(lambda z: z%2==y, map(int, str(x)))))(1) - l(0)) > 0 else "even" if o < 0 else "equal"
odds_vs_evens = lambda x: ["equal", ["even", "odd"][(o:=sum(int(i) for i in str(x) if int(i)%2)-sum(int(i) for i in str(x) if int(i)%2==0)) > 0]][o != 0]
odds_vs_evens = lambda x: ["equal", ["even", "odd"][(o:=(l:=lambda y: sum(filter(lambda z: z%2==y, map(int, str(x)))))(1) - l(0)) > 0]][o != 0]


test(496, odds_vs_evens)  # Tell it which challenge to test against