from django.shortcuts import render
import serial
import json

# ... (остальной код Django)

def read_arduino_data():
    # Подключение к Arduino
    ser = serial.Serial('COM1', 9600)  # Замените 'COM3' на порт, к которому подключен Arduino

    # Чтение данных из Arduino
    data = ser.readline().decode('utf-8').strip()

    # Проверка JSON-формата
    if data.startswith('{') and data.endswith('}'):
        try:
            # Преобразование JSON-строки в Python-словарь
            jsonData = json.loads(data)

            # Извлечение данных из JSON
            sensorValue = jsonData["sensorValue"]

            return sensorValue
        except json.JSONDecodeError:
            return None


def index(request):
    sensorValue = read_arduino_data()

    # Отрисовка шаблона HTML
    context = {
        "sensorValue": sensorValue,
    }
    return render(request, 'main/index.html', context)

