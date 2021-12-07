#Script para medir la velocidad de internet:

from decimal import Decimal
import speedtest   
  
# Para manejar la consola de windows y linux creando una funcion clear(): 
from os import system, name 
  


#Funcion que limpia la pantalla: 
def borrar(): 
  
    #para Windows
    if name == 'nt': 
        _ = system('cls') 
  
    #para Linux y Mac 
    else: 
        _ = system('clear') 
  


#Tests:----------------------------------------------------
st = speedtest.Speedtest() 
  
print("-----------------------------------------------")  
print("Test en proceso: espere un momento por favor... ")  
print("-----------------------------------------------")  



#Velocidad de bajada
bajada = st.download()
bajada = str(round(bajada / 1e+6,2))


#Velocidad de subida
subida = st.upload()
subida = str(round(subida / 1e+6,2))


#Ping
ping = str(round(float(st.results.ping),2))
  
  



#Resultados--------------------------------------------
borrar()
print("-----------------------------------------------")  
print("                 Resultados"                  )
print("-----------------------------------------------")  
print("Velocidad de bajada: " + bajada + " Mbits/s")
print("Velocidad de subida: " + subida + " Mbits/s")
print("Ping: " + ping + " ms")  
print("-------------- Test finalizado ----------------") 


  
