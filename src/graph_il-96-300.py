import math
import matplotlib.pyplot as plt

# Данные о самолете
mass = 250000       # Масса самолета, кг
thrust = 627200     # Общая тяга всех двигателей, Н
Cx = 0.0510         # Коэффициент продольного сопротивления (лобовое сопротивление)
Cy = 0.746          # Коэффициент поперечного сопротивления (подъемная сила)
area = 350          # Площадь крыла, м²
density_air = 1.225 # Плотность воздуха, кг/м³
takeoff_angle = 8   # Угол подъема в градусах

# Преобразование угла в радианы
angle_rad = math.radians(takeoff_angle)

# Начальная скорость
initial_speed = 0  # м/с

# Рассчитываем силу лобового сопротивления
def drag(speed):
    return 0.5 * density_air * area * Cx * speed ** 2

# Рассчитываем подъемную силу
def lift(speed):
    return 0.5 * density_air * area * Cy * speed ** 2

# Функция ускорения
def acceleration(speed):
    g = 9.81  # Ускорение свободного падения, м/с²
    net_force = thrust - drag(speed) + lift(speed) * math.sin(angle_rad) - mass * g * math.sin(angle_rad)
    return net_force / mass

# Шаг интегрирования
dt = 0.01  # секунды

# Переменные для хранения результатов
current_time = 0
current_speed = initial_speed
current_distance = 0

# Списки для хранения данных для графика
time_data = []
distance_data = []

while current_speed < 75:  # Цикл продолжается пока скорость меньше 75 м/с
    acc = acceleration(current_speed)
    current_speed += acc * dt
    current_distance += current_speed * dt
    current_time += dt

    # Сохраняем данные для графика
    time_data.append(current_time)
    distance_data.append(current_distance)

# Округление значений
current_time = round(current_time, 2)
current_distance = round(current_distance, 2)

print(f"Скорость отрыва достигнута через {current_time} секунд.")
print(f"Пройденное расстояние составило {current_distance} метров.")

# Построение графика
plt.figure(figsize=(10, 6))
plt.plot(time_data, distance_data, label="Дистанция от времени")
plt.xlabel("Время (секунды)")
plt.ylabel("Дистанция (метры)")
plt.title("График дистанции взлета Ил-96-300")
plt.legend()
plt.grid(True)
plt.show()