import sympy
import matplotlib.pyplot as plt
import pandas as pd

total_visitors = 120
pizza_lovers = 65
pasta_lovers = 70
sushi_lovers = 50
pizza_pasta_lovers = 35
pizza_sushi_lovers = 25
pasta_sushi_lovers = 30

all_three_lovers_sym = sympy.Symbol('all_three_lovers')
equation = sympy.Eq(
    total_visitors,
    (pizza_lovers + pasta_lovers + sushi_lovers) -
    (pizza_pasta_lovers + pizza_sushi_lovers + pasta_sushi_lovers) +
    all_three_lovers_sym
)
solution = sympy.solve(equation, all_three_lovers_sym)
all_three_lovers = int(solution[0])

pizza_pasta_no_sushi = pizza_pasta_lovers - all_three_lovers
pizza_sushi_no_pasta = pizza_sushi_lovers - all_three_lovers
pasta_sushi_no_pizza = pasta_sushi_lovers - all_three_lovers
two_dishes = pizza_pasta_no_sushi + pizza_sushi_no_pasta + pasta_sushi_no_pizza
only_pizza_lovers = pizza_lovers - pizza_pasta_no_sushi - pizza_sushi_no_pasta - all_three_lovers
only_pasta_lovers = pasta_lovers - pizza_pasta_no_sushi - pasta_sushi_no_pizza - all_three_lovers
only_sushi_lovers = sushi_lovers - pizza_sushi_no_pasta - pasta_sushi_no_pizza - all_three_lovers
none_of_these = total_visitors - (
    only_pizza_lovers + only_pasta_lovers + only_sushi_lovers +
    two_dishes + all_three_lovers
)

data = {
    'Категория': [
        'Только\nпицца', 'Только\nпаста', 'Только\nсуши',
        'Только\n2 блюда', 'Все три\nблюда', 'Не любят\nничего'
    ],
    'Количество': [
        only_pizza_lovers,
        only_pasta_lovers,
        only_sushi_lovers,
        two_dishes,
        all_three_lovers,
        none_of_these
    ]
}
results_df = pd.DataFrame(data)

print("Результаты исследования\n")
print(f" Любят только пиццу: {only_pizza_lovers}")
print(f" Любят только пасту: {only_pasta_lovers}")
print(f" Любят только суши: {only_sushi_lovers}")
print(f" Любят только 2 блюда: {two_dishes}")
print(f" Любят все три блюда: {all_three_lovers}")
print(f" Не любят ничего: {none_of_these}\n")

plt.style.use('dark_background')

fig, ax = plt.subplots(figsize=(11, 7))
fig.canvas.manager.set_window_title('Лабораторная работа №1')

colors = ['#ff9f80', '#8ecae6', '#a9d6a9', '#fde4a4', '#b6a2de', '#999999']

bars = ax.bar(
    results_df['Категория'],
    results_df['Количество'],
    color=colors
)

ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['left'].set_color('dimgrey')
ax.spines['bottom'].set_color('dimgrey')

ax.set_title('Предпочтения посетителей ресторана', fontsize=16, pad=20, weight='bold', color='white')
ax.set_ylabel('Количество посетителей', fontsize=12, labelpad=15, color='lightgrey')

ax.set_ylim(0, results_df['Количество'].max() * 1.18)
ax.tick_params(axis='x', labelsize=11, length=0, colors='white')
ax.tick_params(axis='y', labelsize=10, colors='lightgrey')

ax.yaxis.grid(True, linestyle='--', color='gray', alpha=0.5)
ax.xaxis.grid(False)

for bar in bars:
    yval = bar.get_height()
    ax.text(
        bar.get_x() + bar.get_width()/2.0,
        yval + 0.5,
        int(yval),
        ha='center',
        va='bottom',
        fontsize=11,
        weight='bold',
        color='white' 
    )

plt.tight_layout()
plt.show()

