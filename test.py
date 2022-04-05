Landens = ["suriname","saodi arabie","singapore","senegal"]
Landena = ["argentinie","algeria","almeria"]
Landenb = ["belgie","belerus","bulgarie"]
landenall = []
landen = []

print("de S landen : ")
for x in Landens:
    print(x)

print("de A landen :")
for y in Landena:
    print(y)

print("de B landen : ")
for z in Landenb:
    print(z)

start = 0 
while start < 3:
    land = input("Type 3 landen in : ")
    landen.append(land)
    start += 1
    if start == 3:
        print("jouw landen zijn : ")
        for q in landen:
            print(q)

landenall.extend(Landena)
landenall.extend(Landenb)
landenall.extend(Landens)
landenall.extend(landen)

print("alle landen : ")
for p in landenall:
    print(p)
    
