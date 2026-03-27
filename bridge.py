
import serial, requests, json, sys

# Tu puerto de la Mac
s = serial.Serial('/dev/cu.usbserial-1450', 9600, timeout=1) 
url = "https://script.google.com/macros/s/AKfycbxlswTohSbOushvUoRmDOr7gvJcstuAybyFvJ7IsEnR_v_iDhzLIEj30NNCRGieVNY1/exec"

print("Escuchando Arduino... (Ctrl+C para salir)")

while True:
    if s.in_waiting > 0: # Solo lee si hay datos esperando
        line = s.readline().decode('utf-8').strip()
        if line:
            # Imprime e inmediatamente "limpia" el buffer de pantalla
            print(f"Dato detectado: {line}", flush=True) 
            
            try:
                # Enviamos a Google, pero con un timeout corto 
                # para que Python no se quede "congelado" esperando respuesta
                requests.post(url, json={"value": line}, timeout=2)
                print(" -> Enviado a Google ✅")
            except Exception as e:
                print(f" -> Error de red: {e}")