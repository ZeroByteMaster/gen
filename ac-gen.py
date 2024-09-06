#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import random
import os

def ilolcat(prompt):
    print(prompt)
    return input()

def GCN():
    ftd = random.choice(['4', '51', '52', '53', '54', '55', '34', '37'])

    if ftd == '4' or ftd.startswith('5'):
        restd = ''.join(random.choices('0123456789', k=16 - len(ftd)))
    elif ftd.startswith('34') or ftd.startswith('37'):
        restd = ''.join(random.choices('0123456789', k=15 - len(ftd)))
    else:
        restd = ''.join(random.choices('0123456789', k=14))

    cnumber = ftd + restd
    return cnumber

def GED():
    month = random.randint(1, 12)
    day = random.randint(1, 28)
    year = random.randint(2025, 2027)
    return f"{month:02}/{day:02}/{year}"

def GCR():
    names = ["Daniel", "Julián", "Emiliano", "Juan", "Pedro", "Jose", "Antonio", "Francisco", "Luis", "Manuel", "Javier", "Carlos", "Sergio", "Raúl", "Emilio", "Brandon", "Ana", "Sofía", "Laura", "María", "Elizabeth", "Samira", "Rocio", "Gabriel", "Fernando", "Verónica", "Isabella", "Diego", "Roberto", "Valentina", "Fabián", "Lucía", "Andrés", "Carolina", "Martina", "Gonzalo", "Camila", "Tomás", "Victoria", "Matías", "Alejandra", "Maximiliano", "Valeria", "Eduardo", "Julia", "Nicolás", "Mariana", "Rafael", "Catalina", "Leandro", "Adriana", "Sebastián", "Daniela", "Facundo", "Margarita", "Lorenzo", "Abril", "Felipe", "Solange", "Benjamín", "Renata", "Pedro", "Constanza", "Ángel", "Antonia", "Gabriela", "Hugo", "René", "Paloma", "Rodrigo", "Elena", "Federico", "Juliana", "Ignacio", "Paula", "Martín", "Beatriz", "Matilde", "Francisca", "Esteban", "René", "Rosa", "Alberto", "Silvia", "Leonardo", "Natalia", "Bruno", "Valentín", "Juliana", "Gisela", "Fernando", "Cecilia", "Agustín", "Marina"]
    surnames = ["Giménez", "Fernández", "García", "López", "Martínez", "Pérez", "Sánchez", "Suárez", "Torres", "Díaz", "Gómez", "Vázquez", "Castro", "Morales", "Jiménez", "Ruiz", "Ramírez", "Herrera", "Medina", "Ortega", "Delgado", "Hernández", "Álvarez", "Navarro", "Moreno", "Guerrero", "Cabrera", "Vidal", "Mendoza", "Ponce", "Salazar", "Aguilar", "Rojas", "Sepúlveda", "Quintero", "Contreras", "Vega", "Escobar", "Soto", "Valenzuela", "Espinoza", "Muñoz", "Figueroa", "Chávez", "Rivas", "Suarez", "Montoya", "Fuentes", "Cruz", "Flores", "Martínez", "Gómez", "Franco", "Pérez", "León", "Reyes", "Vargas", "Rosales", "Campos", "Ibarra", "Guerrero"]
    name = f"{random.choice(names)} {random.choice(surnames)}"
    cnumber = GCN()
    expiryd = GED()
    cvv = ''.join(random.choices('123456789', k=3))
    
    if cnumber.startswith('4'):
        ctype = "Visa"
    elif cnumber.startswith(('51', '52', '53', '54', '55')):
        ctype = "MasterCard"
    elif cnumber.startswith(('34', '37')):
        ctype = "American Express"
    else:
        ctype = "Unknown"

    crinf = f'C. Number: {cnumber} | H. Name: {name} | CVV: {cvv} | Type: {ctype} | C. Expiry: {expiryd}'
    return crinf

def GCRs(num_crs):
    crs = []
    for _ in range(num_crs):
        crinf = GCR()
        crs.append(crinf)
    return crs

def WCTF(crs, filename):
    clines = sum(1 for _ in open(filename))
    
    with open(filename, 'a') as file:
        for i, acc_info in enumerate(crs, start=1):
            file.write(acc_info + "\n")
            if i == len(crs):
                print(f"- New card generated successfully. | File: {filename} - Line: {clines + i} \n\n")
            else:
                print(f"- New card generated successfully. | File: {filename} - Line: {clines + i} \n")

def main():
    os.system("cls" if os.name == "nt" else "clear")
    ilolcat("\nPress enter to continue ->> ")
    filename = ilolcat("Enter file name ->> ")
    if not filename.endswith(".txt"):
        print("Error: Only .txt files are supported.")
        return

    try:
        num_crs = int(ilolcat("Number of cards to generate ->> "))
        print("")
    except ValueError:
        print("Error: Please enter a valid number.")
        return
    
    if not os.path.isfile(filename):
        with open(filename, 'w') as file:
            file.write("")

    crs = GCRs(num_crs)
    WCTF(crs, filename)

if __name__ == "__main__":
    main()
