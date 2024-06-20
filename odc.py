import serial

# Konfiguracja portu szeregowego
ser = serial.Serial(
    port='COM7',       # Zmień na odpowiedni port (np. 'COM3' dla Windows, '/dev/ttyUSB0' dla Linux)
    baudrate=115200,     # Zmień na odpowiednią prędkość transmisji
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
    bytesize=serial.EIGHTBITS,
    timeout=0.1          # Czas oczekiwania na dane
)

# Wyczyszczenie pliku przed rozpoczęciem zapisu
with open('proba_2.txt', 'w') as file:
    pass  # Otwieramy i zamykamy plik w trybie pisania, co go czyści

# Inicjalizacja bufora danych
data_buffer = []  # Lista do przechowywania odebranych linijek
lines_to_collect = 7 + 7  # Liczba linijek do zebrania przed zapisem do pliku 1280 +10??
warunek = 1
print("Oczekiwanie na dane...")
while warunek:
    # Sprawdzamy, czy są dostępne dane do odczytu
    if ser.in_waiting > 0:
        # Odbieramy dane z portu szeregowego
        data = ser.readline().decode('utf-8').strip()
        print(f"{data}")
        # Dodajemy dane do bufora
        data_buffer.append(data)

        # Sprawdzamy, czy zebraliśmy wystarczającą liczbę linijek
        if len(data_buffer) >= lines_to_collect:
            warunek = 0

# Zapisujemy dane do pliku
with open('proba_2.txt', 'a') as file:
    for line in data_buffer:
        file.write(line + '\n')
    print("Dane zapisane do pliku proba_2.txt")

print("Program zakończony")