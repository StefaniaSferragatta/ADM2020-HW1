n, x = map(int,input().split())
marks = []
for _ in range(x):
    items = map(float, input().split())
    marks.append(items)

for i in zip(*marks):
    average_score = sum(i)/len(i)
    print(average_score)