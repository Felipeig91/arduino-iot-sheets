# Proyecto IoT: Monitor de Datos en Tiempo Real

Este proyecto captura datos analógicos de un **Arduino Uno** y los envía a una **Google Sheet** mediante un puente de **Python**, permitiendo la visualización web instantánea.

## Arquitectura
1. **Hardware:** Arduino Uno (Lectura de Pin A0).
2. **Puente:** Script de Python (Serial a HTTP POST).
3. **Base de Datos:** Google Sheets (Apps Script).
4. **Dashboard:** Gráficos dinámicos de Google.

## Cómo usar
1. Cargar el código `.ino` al Arduino.
2. Ejecutar `python3 bridge.py` en la computadora.
3. Ver los datos en el link de la Google Sheet.