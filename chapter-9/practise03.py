#Que 3:

for i in range(2,21):
    table=''
    for j in range(1,21):
        table += f"{i}*{j}={i*j}\n"
    with open(f'tables/{i}.txt','w') as f:
        f.write(table)
