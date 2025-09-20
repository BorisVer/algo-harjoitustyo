# Viikkoraportti 3

Viikolla kolme pääsin hiomaan ohjelmaa. Muokkasin ehtoja joidenka perusteella ohjelma arvioi ja tein niistä logaritmiset jotta pisteytys toimii myös laattojen arvojen noustessa suureksi. Algoritmi myös tallentaa jokaisen uuden laskun välimuistiin jotta mahdollisia toistoja vältetään. Tämä nopeuttaa algoritmia huomattavasti etenkin tilanteissa jossa oli paljon mahdollisuuksia. Koodia muokattiin nyt parhaan mukaan välttämään mitään toistoja, kaikki laskut yitetään tehdä yhden kerran ja uudelleenkäyttää saatuja arvoja.

Koodin lisäämisen lisäksi kirjoitin kommentit jokaiseen fuktioon siitä mitä ne tekevät ja kirjoitin yksikkötestejä. Niitä on nyt 2 lisädokumenttia, test_algorithm jossa on perus siirto ja bonus laskuja ja sitten test_evaluation missä on suurempia koko taulun arviointeja sekä parhaan siirron laskuja. Koodi on nyt myös tarkistettu pylintillä, joka antoi noin 9 arvosanan joten parannuksen varaa siinä vielä olisi. 

Opiskelin viikkoa varten miten välimuisti kannattaa toteuttaa ja sen kanssa oli alunperin aika paljon vaikeuksia. Myös logaritmisten laskujen kirjoittaminen heurestiselle funktiolle oli aika hankalaa ja vaati tutkimusta aiheesta. Ongelmia oli taas import vikojen kanssa, pylint valittaa import ongelmista jotka nyt kommentoin pois. Samoin unittest aiheutti vaikeuksia importtien kanssa ja jouduin muokkaamaan tasks.py tiedoston kutsua. 

## Tuntikirjanpito

| Päivä | Käytetty aika | Kuvaus |
|-------|------------|------------|
| 9.9   |     1.5h      | Algoritmin alkeiversion luonti|
| 11.9  |     3h      | Algoritmin testaus ja päivittäminen |
| 12.9   |     5h      | Ongelmien etsimistä ja niiden korjaamista, kaikki tuntui hajoavan |
| 13.9   |     6h      | Algoritmill ehtojen lisäämistä, testaamista ja kertoimien muokkausta |
| Yhteensä   |     15.5h      |  |
