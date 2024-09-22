# Datos de entrada
"""
P = 22000  # No hay un capital inicial único
PMT = 10000  # Depósito mensual
r = 0.10  # Tasa de interés anual compuesta
n = 12  # Interés compuesto mensual
t = 1  # Periodo de 1 año
"""

P = int(input("Capital Inicial"))  
PMT = int(input("Depósito mensual")) 
r =  float(input("Tasa de interés anual compuesta (decimal)"))
n = int(input("Interés compuesto mensual"))  
t = int(input("Tiempo"))


def Calculadora_Inversion(P, PMT, r, n, t):
    # Fórmula para el monto final con interés compuesto y aportaciones periódicas
    A = P * (1 + r/n)**(n*t) + PMT * (((1 + r/n)**(n*t) - 1) / (r/n))

    print(f"Tu ingreso seria {A} Pesos en {t} año(s)")



