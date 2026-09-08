#operasi komparasi

# setiap hasil dari operasi komparasi adalah boolean

'''>,<,>=,<=,==,!=,is,is not'''

a = 4
b = 3

# lebih besar dari >
print("=== LEBIH DARI === ")
hasil = a > 3
print(a,'>',3,'=', hasil)

hasil = b > 3
print(b,'>',3,'=', hasil)

hasil = b > 2
print(b,'>',2,'=', hasil)


# KURANG DARI  <
print("=== KURANG DARI === ")
hasil = a < 3
print(a,'<',3,'=', hasil)

hasil = b < 3
print(b,'<',3,'=', hasil)

hasil = b < 2
print(b,'<',2,'=', hasil)

# KURANG DARI SAMA DENGAN <=
print("=== KURANG DARI SAMA DENGAN=== ")
hasil = a <= 3
print(a,'<=',3,'=', hasil)

hasil = b <= 3
print(b,'<=',3,'=', hasil)

hasil = b <= 2
print(b,'<=',2,'=', hasil)


# SAMA DENGAN ==
print("=== SAMA DENGAN === ")
hasil = a == 4
print(a,'==',4,'=', hasil)

hasil = b == 4
print(b,'==',4,'=', hasil)

hasil = b == 2
print(b,'==',2,'=', hasil)

# TIDAK SAMA DENGAN !=
print("=== SAMA DENGAN === ")
hasil = a != 4
print(a,'!=',4,'=', hasil)

hasil = b != 4
print(b,'!=',4,'=', hasil)

hasil = b != 2
print(b,'!=',2,'=', hasil)

#'IS' SEBAGAI KOMPARASI OBJEK IDENTITY
X = 5 #INI ADALAH ASSIGNMENT MEMBUAT OBJECT
