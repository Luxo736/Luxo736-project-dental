file_name = "obsidian123-artefact-cleandata.csv"
file = open(file_name)

artefacts = []

for line in file:

    values=line.split(",")

    artefact = values[3]
    artefacts.append(artefact)

    print(values[0])
    print('---')

print(artefacts)
