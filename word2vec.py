import csv

c = 0
openq = -1
biglist = []
tinylist = []
s = ""

newfile = open('songs.csv', 'w', newline='')

c += 1

with open('songdata.csv', 'r') as file:
    writer = csv.writer(newfile)
    for line in file:
        # if len(tinylist) > 0:
        #     print(tinylist)
        line = line.strip()
        line += ', '

        # print(line)

        if openq == 1:
            s += line
            c += 1

        elif openq == -1 and c > 0 and len(s) > 1:
            tinylist.append(s)
            # biglist.append(tinylist)
            writer.writerow(tinylist)
            tinylist = []
            s = ""


        if '"' in line and len(line) == 3:
            # print(line)
            openq *= -1

        if 'html' in line:
            author = line.split(',')[0]
            name = line.split(',')[1]
            tinylist.append(author)
            tinylist.append(name)



# print(biglist[12900])
# print(len(biglist))


