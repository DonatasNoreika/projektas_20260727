import pendulum

print("Hello world")
metai = int(input("Metai: "))
menuo = int(input("Mėnuo: "))
diena = int(input("Diena: "))
data = pendulum.date(metai, menuo, diena)
delta = data.diff(pendulum.today())
print("Nuo įvestos dienos praėjo:")
print("Metų:", delta.in_years())
print("Dienų:", delta.in_days())
print("Sekundžių:", delta.in_seconds())