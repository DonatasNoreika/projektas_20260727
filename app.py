import pendulum

print("Hello world")
metai = int(input("Metai: "))
menuo = int(input("Mėnuo: "))
diena = int(input("Diena: "))
data = pendulum.date(metai, menuo, diena)
