# Viikkoraportti 2

Tällä viikolla pääsin ohjelmoimaan itse algoritmia. Aloiten tekemällä yksinkertaisen algoritmin joka kykeni valitsemaan parhaan siirron vertailemalla mikä lopputulos sai eniten pisteitä. Siitä sitten pikkuhiljaa lisäsin kriteereitä pisteytykselle. Nyt algoritmi pisteyttää laudan tilan katsomalla tyhjien lautojen määrää, sitä onko isoin laatta kulmassa ja siitä sitten tarkistetaan vierustoverit että jokainen on edellistä pienempi. Ohjelma myös katsoo muualla lautaa onko kahta saman arvoista vierekkäin. Viimeisenä ehtona ohjelma rankaisee algoritmiä jos keskiruuduissa on iso laatta.

Viikolla eniten aikaa meni ohjelman vikojen korjaamiseen. Suuri vika oli alkuperäisen koodin alaisin siirto ei tehnyt täsyin sitä mitä piti, joka aiheutti että visuaalinen peli oli lievästi eri kuin se minkä algoritmi sai. Tämän tyylisiä ongelmia tuli useita ohjelmoinnin aikana. Sen takia tein toisen vertailu komponentin sovellukseen joka myös tulostaa kaiken tiedon jotta voin helpommin tarkistaa että sovellus ja visuaalinen palaute jakavat samaa tietoa.

Opin kuinka monimutkaista on tehdä heurestinen funktio tälläiselle algoritmille. Myös tuli muistutettua että pitää muistaa tarkistaa useammin asioiden toimivuutta eikä vain olettaa asioiden toimivan. Tällä hetkellä alogitmi saa kohtuullisia tuloksia, saavuttaa melkein joka kerta laatan 1028 ja aina välillä 2048. 

Seuraava vaihe on testien kirjoittelua algoritmille ja testin luominen joka vertaa näkyvää pelilautaa ja algoritmin pelilautaa kun siinä jotakin ongelmia välillä. Sen lisäksi on lisättävä ehtoja jonka perusteella algorimti laskee pelilaudan tilan arvon. Myös koodin siistiminen ja dokumentoiminen olisi tavoite tulevalle viikolle. Jos aikaa riittää olisi hyvä kirjoittaa jokin silmukka joka pyörittää algoritmia useita kertoja ja palauttaa tulokset jotta kertoimien hienosäätö olisi helpompaa.


## Tuntikirjanpito

| Päivä | Käytetty aika | Kuvaus |
|-------|------------|------------|
| 9.9   |     1.5h      | Algoritmin alkeiversion luonti|
| 11.9  |     3h      | Algoritmin testaus ja päivittäminen |
| 12.9   |     5h      | Ongelmien etsimistä ja niiden korjaamista, kaikki tuntui hajoavan |
| 13.9   |     6h      | Algoritmill ehtojen lisäämistä, testaamista ja kertoimien muokkausta |
| Yhteensä   |     15.5h      |  |
