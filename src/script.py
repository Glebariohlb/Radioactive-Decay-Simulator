import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, Button

initial_N_0 = 100000 # Начальное кол-во ядер
lambda_ = 0.1        # Постоянная распада
time_steps = 50      # Кол-во шагов за N-ую единицу времени
show_theory = True   # Изначальное значение показа теоретической прямой

fig, ax = plt.subplots()
fig.set_size_inches(7.5, 5.3)
plt.subplots_adjust(bottom=0.35)

#Функция, симулирующая распад
def simulate_decay(N_0, lambda_val):
    N_current = N_0
    N_list = []
    for t in range(time_steps):
        random_numbers = np.random.rand(N_current)
        decayed = np.sum(random_numbers < lambda_val)
        N_current -= decayed
        N_list.append(N_current)
    return N_list

#Функция, создающая теоретическую прямую
def simulate_theory(N_0, lambda_val, time_steps):
    time_array = list(range(time_steps))
    theory_list = [N_0 * np.exp(-lambda_val * t) for t in time_array]
    return theory_list

time_array = list(range(time_steps))

theory_list = simulate_theory(initial_N_0, lambda_, time_steps)
N_list = simulate_decay(initial_N_0, lambda_)

line, = ax.plot(time_array, N_list, 'b-', linewidth=2) #Создание графика распада
line1, = ax.plot(time_array, theory_list, 'r--', linewidth=2) #Создание графика теоретической прямой

ax.set_xlabel('Время (шаги)')
ax.set_ylabel('Количество ядер')
ax.set_title('Моделирование радиоактивного распада')

ax.grid(True)
ax.set_ylim(0, initial_N_0)

#Слайдер, меняющий значение lambda_
slider_lambda_ax = plt.axes([0.2, 0.1, 0.65, 0.03])
lambda_slider = Slider( #Слайдер, меняющий значение lambda_
    ax=slider_lambda_ax,
    label='λ',
    valmin=0.01,
    valmax=0.5,
    valinit=lambda_,
)

#Слайдер, меняющий значение N_0 (изначального кол-ва ядер)
N_slider_ax = plt.axes([0.2, 0.05, 0.65, 0.03])
N_slider = Slider(
    ax = N_slider_ax,
    label='N₀',
    valmin=1000,
    valmax=200000,
    valinit=initial_N_0,
    valstep=100
)

theory_button_ax = plt.axes([0.35, 0.155, 0.35, 0.06])
theory_button = Button(theory_button_ax, 'Скрыть теоретическую прямую', color='lightblue')

#Функция, изменяющая значения N_0 и lambda_. Относятся к слайдерам
def update(val):
    global show_theory
    new_N_0 = N_slider.val
    new_lambda = lambda_slider.val

    new_N_list = simulate_decay(new_N_0, new_lambda)
    new_theory_list = simulate_theory(new_N_0, new_lambda, time_steps)

    line.set_ydata(new_N_list)
    line1.set_ydata(new_theory_list)

    line1.set_visible(show_theory)

    ax.set_ylim(0, new_N_0)
    fig.canvas.draw_idle()

#Функция, отвечающая за показ теоретической прямой
def toggle_theory(event):
    global show_theory
    show_theory = not show_theory

    line1.set_visible(show_theory)

    if show_theory:
        theory_button.label.set_text('Скрыть теоретическую прямую')
        theory_button.color = 'lightgreen'
    else:
        theory_button.label.set_text('Показать теоретическую прямую')
        theory_button.color = 'lightgray'

    fig.canvas.draw_idle()

lambda_slider.on_changed(update)
N_slider.on_changed(update)
theory_button.on_clicked(toggle_theory)

fig.canvas.manager.set_window_title("Radioactive Decay Simulator v1.0")

plt.show()