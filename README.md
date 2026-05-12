# Анализ резюме с HeadHunter

EDA базы резюме соискателей с hh.ru. Проект выполнен в рамках курса
по анализу данных на Python (Skillfactory).

## Что сделано

- Очистка и преобразование данных: извлечение возраста, пола, уровня
  образования, опыта работы из сырых текстовых полей
- Анализ пропусков, выбросов (правило 3σ)
- 11 интерактивных визуализаций на Plotly: распределения, box plots,
  scatter plots, зависимости зарплаты от образования, города, пола,
  возраста

## Стек

`Python` `pandas` `numpy` `matplotlib` `seaborn` `plotly`

## Графики

GitHub не рендерит iframe, поэтому визуализации доступны по ссылкам:

| № | Описание | Ссылка |
|---|----------|--------|
| 01 | Распределение по возрасту | [Открыть](https://egorchik44.github.io/Skillfactory/plotly/01_age_hist.html) |
| 02 | Распределение по опыту работы | [Открыть](https://egorchik44.github.io/Skillfactory/plotly/02_work_exp_hist.html) |
| 03 | Распределение по желаемой зарплате | [Открыть](https://egorchik44.github.io/Skillfactory/plotly/03_salary_hist.html) |
| 04 | Зарплата vs уровень образования | [Открыть](https://egorchik44.github.io/Skillfactory/plotly/04_salary_edu_bar.html) |
| 05 | Зарплата по городам | [Открыть](https://egorchik44.github.io/Skillfactory/plotly/05_salary_city_box.html) |
| 06 | Зарплата vs готовность к переезду и командировкам | [Открыть](https://egorchik44.github.io/Skillfactory/plotly/06_sal_loc_trip_box.html) |
| 07 | Зарплата vs возраст и образование | [Открыть](https://egorchik44.github.io/Skillfactory/plotly/07_salary_age_ims.html) |
| 08 | Опыт работы vs возраст | [Открыть](https://egorchik44.github.io/Skillfactory/plotly/08_work_exp_age_scat.html) |
| 09 | Резюме по полу | [Открыть](https://egorchik44.github.io/Skillfactory/plotly/09_pie.html) |
| 10 | Зарплата и возраст по полу | [Открыть](https://egorchik44.github.io/Skillfactory/plotly/10_scatter.html) |
| 11 | Распределение возрастов (−3σ / среднее / +3σ) | [Открыть](https://egorchik44.github.io/Skillfactory/plotly/11_age_distribution.html) |
