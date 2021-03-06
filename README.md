# Основното предназначение на този файл

- Разглеждане на идеи и сортирането им по приоритет
- Разглеждане на части / контролери / сензори, които са налични
- Обсъждане и разпределяне на времето върху различните идеи
  
## Към какво се целим

- Да измислим предназначение на крайния продукт по който ще го представим (Зависи от подтемите)

- Да се стремим да направим нещо, което го няма в Google assistant, Siri, Bixby, Alexa
  
## Всичко налично, с което разполагаме и къде може да се използва

### Налични части

| Бройка | Име на частта |
| ------ | ------ |
|x2| Raspberry Pi 3 Model B+|
|x2| NodeMCU (ESP8266)|
|x1| Arduino Uno|
|x1| Arduino Nano|
|x1| BeagleBone black|
|x2| Adaruit 0.91 Inch 128x32 |
|x1| Yeelight RGB bulb|

### Предназначение за всяка част
  
| Име на частта | Къде и как ще се използва |
| ------ | ------ |
|Raspberry Pi 3 Model B+| Планирано е да се работи с [mycroft](https://mycroft.ai/blog/mycroft-now-available-raspberry-pi-image/) и [custom skills](https://mycroft.ai/documentation/skills/msk/)|
|NodeMCU| Може да се ползва от приложението [Blynk](https://blynk.io/) (като не е задължително да си в същата мрежа) и да служи като изпълнител на дребни задачи на SPAS (Raspbery-то)|
|Arduino Uno/Nano| Възможно е да играят ролята на посредник от СПАС (Например да включва/изключва с гласова команда кафе машина неподдържаща WI-FI) |
|BeagleBone black| [BeagleBone-а също има възможнст за voice recognition](http://www.laplinker.com/2013/10/step-by-step-guide-beagle-bone-black.html), но има ограничен брой материал за него|
|Yeelight RGB bulb| Тествах управляването на крушката в [LAN](https://en.wikipedia.org/wiki/Local_area_network) с python library-то [Yeelight](https://yeelight.readthedocs.io/en/latest/). Всичко работи и е добра идея крушката да се управлява с voice recognition. Може да се направи нещо като morning routine, който да включва крушката или като засече, че си излязъл да я изключва автоматично.|

## Идеи

- Свързване на Raspberry-то с различни device-ове (Arduino, NodeMCU, Onion...)

  - Чакам Raspberry-то за да тествам как ще върви с ESP-то

- Да се направи приложение за управление на цялата конфигурация

  - Менторът ни (Николета) предложи Android Studio, като каза че не е сложно да се работи с него

- Да добавим управление чрез messenger с library-то [fbchat](https://fbchat.readthedocs.io/en/master/)

  - Вече имаме готов, тестван бот и е значително лесна комуникацията межау Python и Arduino IDE, но няма особен смисъл ако вече имаме приложение

- Възможно е свързването на някое Adafruit дисплейче, за да изписва дадените му команди, температура, час или просто [личице](https://mycroft.ai/wp-content/uploads/2017/12/Mark-1-and-Mark-2-No-logo.png)

  - Не толкова важен елемент, но ако остане време може да е ключов детайл

- Skill за правене на постове в социалните мрежи (Facebook, Instagram, Twitter)

  - Добра и оригинална идея, която според мен си заслужава време да проучим

- Възможно да се направи нещо като Security camera чрез ps3 camera-та, която сме я взели предимно за микрофона

- Горепосочената идея за Yeelight крушката (в таблицата)

- Ползване на [Google assistant SDK](https://developers.google.com/assistant/sdk/guides/library/python/) вместо Mycroft
  - Поприцип е по-лесен и известен вариант, но се свежда до готова работа и не се знае дали ще има много какво да добавим, трябва да се тества и провери. Също има възможност за [custom skills](https://developers.google.com/assistant/sdk/guides/library/python/extend/install-hardware) и [custom wakewords](https://www.hackster.io/shiva-siddharth/multiple-custom-wakewords-activation-of-google-assistant-d0c986).

## Въпроси без отгвор

- Възможно ли е Voice Recognition-а да работи на български?

  - Полезно поради факта, че темата е "Technology for everyone" тоест трябва да работи и за неговорещите английски

- Колко време ще отделим за дизайна на крайния продукт?

  - Освен идеята и функциолността ще е важно и как изглежда всичко това. Не може да го пъхнем в един кашон, трябва като крайния потребител го погледне да е красиво на вид, да не се приема като играчка.