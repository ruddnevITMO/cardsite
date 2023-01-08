from urllib.parse import quote
import os
import sys
import re

if __name__ == '__main__':

    if len(sys.argv) == 1:
        githubName = "ваш github ник"
        repoName = "название вашего репозитория"
        header = "заголовок вашего сайта"
    elif len(sys.argv) == 4:
        githubName = sys.argv[1]
        repoName = sys.argv[2]
        header = sys.argv[3]
    else:
        print("Неверное количество аргументов")
        sys.exit()

    obfuscateContents = True
    writeToReadme = True
    printing = False

    cards = ["0"]
    with open("cardsList.txt", encoding="utf-8") as namesFile:
        for line in namesFile:
            if line.strip() == "":
                print("Нашел пустую строку в cardsList.txt")
            else:
                cards.append(line.rstrip())
    if re.search(r'^[0-9]+\.', cards[1]):
        if cards[1][0] != "1":
            print("Неправильный список билетов в cardsList.txt! Уберите нумерацию")

    for i in range(1, len(cards)):
        if re.search(r'^[0-9]+\.', cards[i]):
            cards[i] = re.search(r"(?<=\. ).*", cards[i]).group()


    mainFiles = os.listdir("../cards")
    altFiles = os.listdir("../altCards")

    mainExt = [".none"] * len(cards)
    altExt = [".none"] * len(cards)

    countGood = 0
    for file in mainFiles:
        n = False
        n = int(re.match(r"^[0-9]+(?=\.(jpg|png|jpeg))", file).group())
        if n:
            mainExt[n] = re.search(r"\.(jpg|png|jpeg)", file).group()
            countGood += 1

    if (len(cards) - 1) != countGood:
        print("Количество билетов не сходится с количеством картинок! Поправьте, или будут пустые билеты")

    for file in altFiles:
        n = False
        n = int(re.search(r"^[0-9]+(?=\.(jpg|png|jpeg))", file).group())
        if n:
            altExt[n] = re.search(r"\.(jpg|png|jpeg)", file).group()

    if writeToReadme:
        readme = open("../README.md", "w", encoding='utf-8')


    def printWrite(*args):
        line = ' '.join([str(arg) for arg in args])
        if writeToReadme:
            readme.write(line + '\n')
        if printing:
            print(line)


    def quoteConvert(text):
        return text.lower().replace(" ", "-").replace(".", "").replace(",", "").replace("(", "").replace(")", "")


    replacements = [["о", "o"], ["М", "M"], ["е", "e"],
                    ["а", "a"], ["р", "p"], ["Т", "T"],
                    ["В", "B"], ["К", "K"], ["с", "c"],
                    ["у", "y"]]

    imageLinkTemplate = "https://raw.githubusercontent.com/" + githubName + "/" + repoName + "/main/cards/"
    linkTemplate = "https://" + githubName + ".github.io/" + repoName + "/#"
    linkToTop = linkTemplate + quote(quoteConvert(header))

    alts = [int(i[:-4]) for i in os.listdir("../altCards")]
    altsLink = "https://raw.githubusercontent.com/" + githubName + "/" + repoName + "/main/altCards/"

    # Заголовок
    printWrite("# " + header)

    # Формируем содержание
    howManyCards = len(cards) - 1
    for n in range(1, howManyCards + 1):
        name = cards[n]
        original = name

        if obfuscateContents:
            for placing in replacements:
                name = name.replace(placing[0], placing[1]).replace(placing[0].upper(), placing[1].upper())

        outputLine = "[" + name + "](" + linkTemplate + quote(quoteConvert(original) + "-" + str(n) + "-наверх") + ")"
        if n != howManyCards:  # на последней главе содержания не нужен перенос строки
            outputLine += "\\"

        printWrite(outputLine)

    # Формируем сами билеты
    for n in range(1, howManyCards + 1):


        printWrite("##", cards[n], "[" + str(n) + "] [наверх](" + linkToTop + ")")
        printWrite("![" + cards[n] + "](" + imageLinkTemplate + str(n) + mainExt[n] + ")")
        if n in alts:
            printWrite("### Альтернативный билет для ", cards[n], "[" + str(n) + "] [наверх](" + linkToTop + ")")
            printWrite("![" + cards[n] + "](" + altsLink + str(n) + altExt[n] + ")")
        printWrite("---")

