# Viikkoraportti 3

Viikolla kolme pääsin hiomaan ohjelmaa. Muokkasin ehtoja joidenka perusteella ohjelma arvioi ja tein niistä logaritmiset jotta pisteytys toimii myös laattojen arvojen noustessa suureksi. Algoritmi myös tallentaa jokaisen uuden laskun välimuistiin jotta mahdollisia toistoja vältetään. Tämä nopeuttaa algoritmia huomattavasti etenkin tilanteissa jossa oli paljon mahdollisuuksia. Koodia muokattiin nyt parhaan mukaan välttämään mitään toistoja, kaikki laskut yitetään tehdä yhden kerran ja uudelleenkäyttää saatuja arvoja.

Koodin lisäämisen lisäksi kirjoitin kommentit jokaiseen fuktioon siitä mitä ne tekevät ja kirjoitin yksikkötestejä. Niitä on nyt 2 lisädokumenttia, test_algorithm jossa on perus siirto ja bonus laskuja ja sitten test_evaluation missä on suurempia koko taulun arviointeja sekä parhaan siirron laskuja. Koodi on nyt myös tarkistettu pylintillä, joka antoi noin 9 arvosanan joten parannuksen varaa siinä vielä olisi. 

Opiskelin viikkoa varten miten välimuisti kannattaa toteuttaa ja sen kanssa oli alunperin aika paljon vaikeuksia. Myös logaritmisten laskujen kirjoittaminen heurestiselle funktiolle oli aika hankalaa ja vaati tutkimusta aiheesta. Ongelmia oli taas import vikojen kanssa, pylint valittaa import ongelmista jotka nyt kommentoin pois. Samoin unittest aiheutti vaikeuksia importtien kanssa ja jouduin muokkaamaan tasks.py tiedoston kutsua. 

Seuraavalle viikolle vielä viimestelen pylint korjauksia, tutkin saanko ohjelman nopeutettua jotenkin ja aloitan uuden algortimitn eli minmax algoritmin tekemisen todennäköisesti. Samalla muutama unittesti lisää jotta kattavuus olisi 100%.

## Tuntikirjanpito

| Päivä | Käytetty aika | Kuvaus |
|-------|------------|------------|
| 15.9   |     2h      | Arviontikriteerien lisäys|
| 16.9  |     2.5h      | Arviontikriteerien muokkaus log2|
| 19.9   |     4h      | Välimuisti, kommentoimista, pylint korjailua |
| 20.9   |     5h      | Unittestit, koodin siistimistä, testiraportti|
| Yhteensä   |     13.5h      |  |
