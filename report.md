# Лабораторная работа №0

## Задание

Приближённо вычислить число $\pi$ с помощью [произведения Валлиса](https://ru.wikipedia.org/wiki/%D0%A4%D0%BE%D1%80%D0%BC%D1%83%D0%BB%D0%B0_%D0%92%D0%B0%D0%BB%D0%BB%D0%B8%D1%81%D0%B0):

$$ \frac{\pi}{2} = \prod_{i=1}^{\infty} \frac{4i^2}{4i^2 - 1}. $$

## Результаты вычислений

Очередной множитель произведения на Python:


```python
def wallis_multiplier(i):
    i_squared_times_4 = 4 * i * i
    return i_squared_times_4 / (i_squared_times_4 - 1)
```


При разнице последних значений произведения $\pi / 2$ менее `1e-7` вычисленное значение $\pi = 3.1411963131348553$.

![График сходимости](https://raw.githubusercontent.com/still-coding/report_demo/e2c8f4950479afde2be4b80a58be052a2af798e6/img/convergence_plot.png)

## Вывод
Произведение Валлиса сходится очень медленно, поэтому рекомендуется использовать более эффективные методы вычисления числа $\pi$.


# Список использованных источников:
1. Matplotlib cheatsheets and handouts: [Электронный ресурс]. URL: [https://matplotlib.org/cheatsheets/](https://matplotlib.org/cheatsheets/) (дата обращения 24.04.2023).
2. Markdown Cheat Sheet: [Электронный ресурс]. URL: [https://www.markdownguide.org/cheat-sheet/](https://www.markdownguide.org/cheat-sheet/) (дата обращения 24.04.2023).
3. Writing mathematical expressions: [Электронный ресурс]. URL: [https://docs.github.com/en/get-started/writing-on-github/working-with-advanced-formatting/writing-mathematical-expressions](https://docs.github.com/en/get-started/writing-on-github/working-with-advanced-formatting/writing-mathematical-expressions) (дата обращения 24.04.2023).
