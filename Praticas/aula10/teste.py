lst = [7, 8, 3, 4, 6, 5]
txt = ["philips", "bell", "dog"]


print([x+2 for x in lst if x<6],max(len(s) for s in txt),{s:len(s) for s in txt if s[0]<'d'},[s[0]+str(x) for x in lst[:2] for s in txt[:2]],sep='\n')

