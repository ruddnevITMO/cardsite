## Шаблон сайта для удобной подготовки к любым предметам по билетам
> :sparkles: При добавлении билетов сайт автоматически обновляется

> :warning: Этот файл будет заменен при первом запуске генератора. Этот текст можно найти [здесь](https://github.com/ruddnevITMO/cardsite/wiki)

### Как настроить сайт:

<details open> 
<summary>Простой автоматический способ</summary>

---
1. Сделать свой репозиторий, пользуясь этим репозиторием как шаблоном

2. Через браузер добавить названия билетов в файл `cardsList.txt` построчно по порядку (можно с нумерацией вида "1. ", "2. ")

5. Добавить билеты (на один билет одна картинка) в папку `cards` называя файлы номером билета

> :warning: Все картинки в одном расширении, на ваш выбор *.png*, *.jpg*, *.jpeg*

6. Добавить альтернативные версии билетов также называя номером билета в папку `altCards` **(не обязательно)** 

3. Зайти во вкладку Actions
<img width="350" alt="image" src="https://user-images.githubusercontent.com/37450057/211227429-223ff013-d062-4b48-946a-96a4c6e7ab78.png">

4. В меню слева выбрать "Generate README.md to serve"
<img width="350" alt="image" src="https://user-images.githubusercontent.com/37450057/211227400-e75c2412-15ed-44b5-9257-d3c1585b294d.png">

5. Нажать кнопку "Run workflow"
6. В появившемся меню ввести заголовок страницы и расширение картинок
<img width="350" alt="image" src="https://user-images.githubusercontent.com/37450057/211227465-42cd40cc-8bdf-4986-a65f-ff9dc3211eb1.png">

7. Снова нажать "Run workflow"

> :warning: В дальнейшем так запускать стоит только тогда, когда собираетесь изменить заголовок или расширение файлов. Если изменять или добавлять файлы, то скрипт выполнится автоматически.

8. Перейти в настройки репозитория > Pages > Build and deployment > Branch, выбрать ***main*** вместо ***None*** и нажать ***Save*** 

9. Подождать около минуты, перезагрузить страницу, и после этого на странице появится ссылка на сайт.

> :warning: Пункты 8 и 9 нужно делать только в первый раз

10. Готово!

---
</details>

<details> 

<summary>Сложный ручной способ</summary>

---

1. Сделать свой репозиторий, пользуясь этим репозиторием как шаблоном
2. Клонировать свой репозиторий
3. Добавить названия билетов в файл `cardsList.txt` построчно по порядку (можно с нумерацией вида "1. ", "2. ")
4. Внутри `generator.py` изменить несколько переменных:

	- в `githubName` указать ваш username
	- в `repoName` указать название вашего репозитория
	- в `header` указать заголовок сайта
	- в `fileExtension` указать расширение картинок (*.png*, *.jpg*, *.jpeg*)
5. Добавить билеты (на один билет одна картинка в расширении, выбранном в пункте 4) в папку `cards` называя файлы номером билета
6. Добавить альтернативные версии билетов (формат и название как в пункте 5) в папку `altCards` **(не обязательно)** 
7. Запустить генератор сайта командой

```sh 
python3 generator.py
```

8. Выгрузить всё в удаленный репозиторий командой

```sh
git commit -am "Initial commit"
git push
```

9. Перейти в настройки репозитория > Pages > Build and deployment > Branch, выбрать ***main*** вместо ***None*** и нажать ***Save***

10. Подождать около минуты, перезагрузить страницу, и после этого на странице появится ссылка на сайт.

11. Готово!

---

</details>

