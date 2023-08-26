# report_tool

Небольшое приложение для облегчения генерации pdf версии отчётов из md файлов.

Работа тестировалась на Debian 12.

## Зависимости
* pandoc
* texlive-latex-recommended
* texlive-xetex
* texlive-lang-all
* pdftk

Установить одной командой:

```shell
sudo apt install pandoc texlive-latex-recommended texlive-xetex texlive-lang-all pdftk -y
```

Для работы необходимы файлы `head.tex` - файл с настройками форматирования и `title.tex` - файл титульного листа.

## Использование

1. Отредактируйте файл `title.tex`

2. Запустите 
```shell
./report_tool.py название_md_файла_без_расширения --toc --title
```

Например:
```shell
./report_tool.py report --toc --title
```

Аргументы `--toc` и `--title` не обязательны и отвечают за создание оглавления и титульного листа соответственно.


Если будут проблемы с отображнием символов кириллицы, выполните
```shell
fc-list :lang=ru
```
и выберите название шрифта (стоит после полного пути к файлу шрифта и первого двоеточия).
