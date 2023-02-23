

semana=["lunes", "martes", "miercoles", "jueves", "vieres", "sabado", "domingo"]
num_semana = int(input ("dime un numero "))

while num_semana<1 or num_semana>7:
    print("ese numero no corresponde a ningun dia de la semana")
    num_semana = int(input ("dime un numero "))
    

print(semana[num_semana-1])