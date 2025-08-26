file = open("Students.txt", "w")
file.write("Name: Saahir\nSurname: Dharamsi\nFavourite Subject: Music\nFavourite animal: Snake")
file.close()

file = open("Students.txt", "r")
print(file.read())

file = open("Students.txt", "a")
file.write("\n\nName: John\nSurname: Colt\nFavourite Subject: PE\nFavourite animal: Tiger")
file.close()

file = open("Students.txt", "r")
print(file.read())