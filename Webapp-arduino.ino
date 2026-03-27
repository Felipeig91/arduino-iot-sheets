// Proyecto: Sensor de Conductividad Estática para IoT
// Universidad - 2026

void setup() {
  // Inicia la comunicación serial a 9600 baudios
  // Es el "idioma" en el que hablará con el script de Python
  Serial.begin(9600);
  
  // Mensaje de depuración opcional (puedes borrarlo si quieres)
  // Serial.println("Arduino Listo"); 
}

void loop() {
  // Lee el voltaje en el pin A0 (valor entre 0 y 1023)
  int lectura = analogRead(A0);
  
  // Envía el número a la computadora por el cable USB
  // Serial.println añade un "salto de línea" al final para que Python sepa que el dato terminó
  Serial.println(lectura);
  
  // ESPERA: 1000 milisegundos = 1 segundo
  // Si lo pones más rápido (ej: 100), Google Sheets podría bloquearte por exceso de datos.
  // Si lo pones más lento (ej: 5000), la gráfica se verá muy "entrecortada".
  delay(1000); 
}