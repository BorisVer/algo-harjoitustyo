# Viikkoraportti 1

Tällä viikolla päätin aiheen ja aloitin tiedon etsimisen. Sovin ohjaajan kanssa jo olemassaolvan ohjelman uudelleenkäyttöä. Viikolla suurin määrä aikaa meni edellisen projektin muokaamiseen uuteen tarkoituskeen. Tulen suorittamaan ohjelman expectimax algoritmilla. Sitä varteen pitää sekä simuloida omat siirrot että satunnais siirrot jotka johtuvat laattojen generoimisesta.  Sain aikaan hyvin yksinkertaisen pohjan algoritmille, ja silmukan joka käy läpi kaikki mahdolliset pelaajan siirrot valittuun syvyyteen.

Tällä viikolla opin enemmän ylipäätään miten tälläiset minmax algoritmit toimivat ja ymmärtämään kuinka nopeasti tälläisen ohjelman aikavaativuus nousee kun syvyyttä lisää. Vaikeuksia on hieman tuottanut täysin ymmärtämään miten lopullinen algoritmi tulee laskemaan pisteet jokaiselle tilalle, mutta oletan sen selvenevän projektin edetessä. Eniten vaikeuksia tuotti vanhan koodin muokkaaminen siihen että se oli helpossa muodossa uudelleensyöttää algoritmille, mutta se on nyt tehty.

Seuraava vaihe olisi toteuttaa silmukan osa joka käy läpi kaikki laatan generoimiset. Sen jälkeen aloitan pohtimaan ja tutkimaan miten kannattaisi kertoa ohjelmalle mitkä tilat ovat "hyvät" ja mitkä "huonot".

Tällä hetkellä ohjelma toimii käynnistämällä, painamalla start nappia ja sitten "A" näppäintä painamalla ohjelma käy läpi kaikki mahdolliset siirrot syvyydellä x (joka on määritelty game_config.py tiedostossa) ja tulostaa sen consoliin.

## Tuntikirjanpito

| Päivä | Käytetty aika | Kuvaus |
|-------|------------|------------|
| 4.8   |     2h      | Aiheen pohdinta, projektin luonti           |
| 5.8   |     3h      | Aiheen hyväskyntä ja pohjan teko |
| 6.8   |     4h      | Pohjan muokkas käytettävään muotoon, algoritmin alun kirjoitus |
| Yhteensä   |     9h      |  |
