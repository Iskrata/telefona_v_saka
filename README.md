# Основното предназначение на този файл
  - Разглеждане на идеи и сортирането им по приоритет
  - Разглеждане на части / контролери / сензори, които са налични
  - Обсъждане и разпределяне на времето върху различните идеи
  
# Всичко налично, с което разполагаме и къде може да се използва

**Налични части**

| Бройка | Име на частта |
| ------ | ------ |
|x2| Raspberry Pi 3 Model B+|
|x2| NodeMCU (ESP8266)|
|x1| Arduino Uno|
|x1| Arduino Nano|
|x1| BeagleBone black|

**Предназначение за всяка част**
  
| Име на частта | Къде и как ще се използва |
| ------ | ------ |
|Raspberry Pi 3 Model B+| Планирано е да се работи с [mycroft](https://mycroft.ai/blog/mycroft-now-available-raspberry-pi-image/) и [custom skills](https://mycroft.ai/documentation/skills/msk/)|
|NodeMCU| Може да се ползва от приложението [Blynk](https://blynk.io/) (като не е задължително да си в същата мрежа) и да служи като изпълнител на дребни задачи на SPAS (Raspbery-то)|
|Arduino Uno/Nano |Възможно е да играят ролята на посредник от СПАС (Например да включва/изключва с гласова команда кафе машина неподдържаща WI-FI) |
| | |
| | |
    
# Идеи от тефтера на Марти

​```mermaid
graph LR
A[Hard edge] -->B(Round edge)
    B --> C{Decision}
    C -->|One| D[Result one]
    C -->|Two| E[Result two]
​```