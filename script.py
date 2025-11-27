""" 
    Hal yang akan di bahas terkait basic python :

    1. Variable
    2. Tipe Data
    3. Operator
    4. if else, loop
    5. Function
"""

# Contoh Variable
x = "Bewe"

print("Hello " + x + ", apa kabar hari ini?")


# contoh loop di python
for i in range(1, 6):
    print("Perulangan ke-", i)

# Bikin perulangan bintang terbalik

n = 15
for i in range(1, n + 1):
    for j in range(i):
        print("*", end="")
    print()  # Pindah ke baris berikutnya

# Buat bintantang terbalik
n = 15
for i in range(n, 0, -1):
    for j in range(i):
        print("*", end="")
    print()  # Pindah ke baris berikutnya

# buat gambar kucing dengan bintang
n = 7
for i in range(n):
    for j in range(n):
        if (i == 0 and (j == 2 or j == 4)) or (i == 1 and (j == 1 or j == 5)) or (i == 2 and (j == 0 or j == 6)) or (i == 3 and (j == 2 or j == 4)) or (i == 4 and (j == 1 or j == 5)) or (i == 5 and (j == 0 or j == 6)) or (i == 6):
            print("*", end="")
        else:
            print(" ", end="")
    print()  # Pindah ke baris berikutnya



