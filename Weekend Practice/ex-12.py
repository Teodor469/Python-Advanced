a = input()
s = []

for element in a:
    num = int(element)
    
    if num not in s:
        s.append(num)
print(s)