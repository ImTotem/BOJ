users = list(map(
    lambda user: [max(map(len, user[0].replace(' ', '').split('*'))), user[1]],
    [input().rsplit(maxsplit=1) for _ in range(int(input().split()[0]))]
))

print(len(set(map(lambda x:x[0], users))))
print(*map(lambda x:f'{x[0]} {x[1]}', users), sep='\n')
