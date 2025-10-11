# Toteutusdokumentti

## 2048 Peli
Ohjelma on rakennettu 2048 nimisen pelin ympärille. Peli koostuu 4x4 ruudukosta, johon satunnaisesti syntyy laatta. Pelaaja voi vuorollaan siirtää kaikki laatat haluamaansa suuntaa (vasemmalle, oikealle, ylös tai alas). Tällöin saman arvoiset laatat yhdistyvät osutessaan toisiinsa ja muodostavat uuden laatan, jonka arvo on kaksinkertainen alkuperäisestä laatasta. Pelaajan siirron jälkeen peli luo yhden uuden laatan satunnaiseen tyhjään ruutuun. Uuden laatan arvo on 90% todennäköisyydellä 2 ja 10% todennäköisytydellä 4. Kunten pelin nimestä voi arvata pelin tavoite on saavuttaa laatta jonka arvo on 2048. Pelissä on myös pistesysteemi. Yhdistämällä laatat, pelaaja saa laattojen kokonaisumman verran pisteitä. Esim yhdistämällä kaksi 32 arvoista laattaa pelaaja saa 64 pistettä. Peli loppuu kun ruudukko on täynnä, ja mikään pelaajan tekemä siirto ei vapauta enään tilaa uudelle ruudulle. 

## Ohjelman yleisrakenne
2048-expectimax algortimin tavoite on pelata 2048 peliä mahdollisimman hyvin. Ohjelma simuloi kaikki pelaajan mahdolliset 4 suuntavalintaa. Sen jälkeen jokaiselle suunnalle ohjelma testaa jokaisen tyhjän laatan kohdalle luoda uusi laatta ja arvioi millainen pelitilanne saataisiin aikaa. Ohjelma tekee näin 4 pelaajan siirron verran, jonka jälkeen se vertaa kaikki mahdollisia lopputuloksia (joita on noin 100,000-2,000,000 riippuen tyhjien laattojen ja mahdollisten siirtosuuntien määrästä) ja valitsee niistä sen millä on suurin "pisteytys" pelilaudan arvolle. Pisteytys määrittyy useasta tekijästä: tyhjien laattojen määrästä, onko isoin laatta kulmassa, onko laudalla samankokoiset laatat lähekkäin, mahdolliset yhdistykset seuraavalla siirrolla sekä "S" muotoinen rata isoimmasta laatasta pienimpään. Kaikki nämä tekijät antavat arvon pelilaudalle, ja jokaisen siirron kohdalle myös tulee todennäköisyyslasku laattojen eri arvomahdollisuudelle (2 tai 4) jota huomioiden ohjelma kykenee laskemaan mikä siirto tuo parhaan tuloksen suurimmalla todennäköisyydellä. Ohjelma suorittaa algoritmin valitseman siirron ja sen jälkeen algoritmi lähtee uudelleen pyörimään laskemaan seuraavaa siirtoa. 

## Aika ja tilavaativuudet
Yhden siirron laskeminen vie pahimmassa tapauksessa $O((n*(2E))^d)$ jossa,
- $n$ = Mahdolliset siirrot solmussa $(n \leq 4)$
- $E$ = Tyjät laatat $(0 \leq E \leq 15)$
- $d$ = Syvyys - 1

Jokaisen siirron laskemiseen jokaisessa syvyydessä jouduaan laskemaan siirrot kerrottuna tyhjillä ruuduilla mihin uusi laatta voi tulla. Nämä tyhjät ruudut on kerrottava kahdella kun mahdollisia laattoja on 2 ja 4. Koko kaava kasvaa potentiaalisesti syvyyden verran kun jokaiselle alkuperäiselle mahdollisuudelle lasketaan uudelleen kaikki mahdollisuudet. Pahimmissa tapauksessa aikavaativuus syvyydellä 4 on $O((4*30)^4)$.

Tilavaativuus ohjelmalle on $O(d)$ jossa $d$ on syvyys, sillä ohjelma tallentaa vain yhden polun kerrallaan. 

## Suorituskyky

Algoritmin suorituskykyä testattiin syvyydellä 4 (4 pelaajan siirtoa ja 3 tyhjän laatan simulointia per siirto) käyttäen seuraavaa testiruudukkoa:
\
[ 0, 0, 8, 0] 
\
[32, 16, 0, 0]
\
[6, 0, 2, 256]
\
[6, 256, 512, 0]
\
Testissä ajettiin 100 peliä eri cache-toteutuksilla mittaamaan välimuistin vaikutusta suorituskykyyn:

| Cache-toteutus | Kokonaisaika | Keskiaika per siirto | Parannus |
|---------------|--------------|----------------------|----------|
| Ei cachea | 4128.3 s | 41.3 s | - |
| Max-solmu cache | 595.8 s | 6.0 s | 85.6\% |
| Chance-solmu cache | 615.9 s | 6.2 s | 85.1\% |
| Molemmat cachet erikseen | 501.0 s | 5.0 s | 87.9\% |
| Yhdistetty cache | 489.3 s | 4.9 s | 88.1\% |

Tuloksista näkee että välimuistin käyttö on kriittistä ohjelman suoritusnopeudelle. Yhden thtenäisen välimuistin ylläpitäminen osottautui nopeimmaksi. Yhteisen välimuistin tunnuksen alussa on 0 tai 1 merkitsemään onko se max vai chance solmu. Tämä on melkein **8.4** kertaa nopeampi kuin ilman välimuistia. Välimuistin hyöty myös kasvaa syvyyden kasvaessa, sillä osumien määrä nousee. Algoritmi hyötyy välimuistista erityisesti silloin, kun samaan pelitilaan päädytään useita eri reittejä pitkin rekursiivisessa hakupuussa. Tämä on yleistä 2048-pelissä, etenkin hakusyvyyden noustessa.


## Puutteet ja parannusehdotukset
Ohjelman pystyis nopeuttamaan arvioimalla tyhjien laattojen vaikutusarvon ja ohittamalla ne laattat joissa tulevalla laatalla olisi pieni vaikutus. Tämä nopeuttaisi ohjelmaa etenkin alkuvaiheessa. 

## Laajojen kielimallinen käyttö
Laajojen kielimalleja tuli käytettyä aivan alussa saamaan ideaa miten tälläistä projektia kannattaa lähestyä ja mistä olisi järkevintä aloittaa. Sen lisäksi sitä tuli käytettyä import ongelmien ratkaisemiseen kun importit eivät suostuneet toimimaa. Käytin Claude Sonnet 4 mallia (https://claude.ai/).

## Lähteet
- https://www.cs.columbia.edu/~sedwards/classes/2020/4995-fall/reports/Minimax.pdf
- https://www.cs.uml.edu/ecg/uploads/AIfall14/vignesh_gayas_2048_project.pdf
- https://en.wikipedia.org/wiki/Expectiminimax
