Monitor de Datos Biométricos / Estáticos (IoT)

🚀 ¿Qué es y para qué sirve?
Este proyecto es un sistema de Internet de las Cosas (IoT) de bajo costo diseñado para capturar señales eléctricas analógicas (como la estática del cuerpo humano o sensores resistivos) y enviarlas a la nube sin necesidad de módulos WiFi o Ethernet adicionales.

Sirve como una base para cualquier proyecto que requiera:

Telemetría en tiempo real: Ver datos de sensores desde cualquier lugar del mundo.

Registro histórico: Almacenar datos en una base de datos (Google Sheets).

Visualización Web: Generar gráficos dinámicos automáticos.

🛠️ Configuración Paso a Paso

1. Nivel Hardware (Arduino C++)
   El Arduino actúa como la unidad de adquisición de datos (Edge Device).

Conexión: Conecta un cable al pin A0.

Función: Mide el voltaje (0-5V) y lo convierte en un número (0-1023).

Código:

C++
void setup() {
Serial.begin(9600); // Abre el canal de comunicación USB
}
void loop() {
int val = analogRead(A0); // Lee la señal del pin
Serial.println(val); // Envía el dato a la PC
delay(1000); // Frecuencia de muestreo (1 segundo)
} 2. Nivel Base de Datos (Google Apps Script)
Google Sheets funciona como nuestro servidor y base de datos.

Crea una hoja nueva.

Ve a Extensiones > Apps Script.

Pega este código (asegúrate de que la función sea doPost):

JavaScript
function doPost(e) {
var sheet = SpreadsheetApp.getActiveSpreadsheet().getActiveSheet();
var data = JSON.parse(e.postData.contents);
sheet.appendRow([new Date(), data.value]); // Registra Fecha y Valor
return ContentService.createTextOutput("OK");
}
Crucial: Haz clic en Desplegar > Nueva implementación. Selecciona Aplicación Web, ejecuta como "Yo" y permite acceso a "Cualquier persona". Copia la URL generada.

3. Nivel Puente (Python)
   Python actúa como el "Gateway" que toma los datos del USB y los sube a Internet.

Instala las dependencias: pip3 install pyserial requests.

Configura el puerto correcto (ej: /dev/cu.usbserial-1450 en Mac o COM3 en Windows).

Código del puente (bridge.py):

Python
import serial, requests, json

# Configuración del puerto y URL

s = serial.Serial('/dev/cu.usbserial-1450', 9600)
url = "TU_URL_DE_GOOGLE_AQUI"

while True:
line = s.readline().decode('utf-8').strip()
if line:
print(f"Subiendo: {line}")
requests.post(url, json={"value": line})
📈 Función Principal
La función principal es el Desacoplamiento de Capas.

El Arduino no necesita saber nada de Internet (ahorra memoria y costo).

El Python se encarga de la lógica de red y seguridad.

El Google Script se encarga de la persistencia de datos y la interfaz de usuario final (Gráficos).

Instrucciones de Ejecución Rápida
Conecta el Arduino y sube el código C++.

Cierra el Monitor Serie del IDE de Arduino.

Ejecuta en terminal: python3 bridge.py.

Abre tu Google Sheet y crea un gráfico de líneas con las columnas A y B.
