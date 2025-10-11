# 2048-Pelin algoritmi

Tämä on 2048 Pelille expectimax algoritmi. Peli saavuttaa suurimman osan ajasta 4096 laatan, ja ratkaisee pelin eli saavuttaa 2048 aikalailla aina. 

## Dokumentaatio
- [Määrittelydokumentti](https://github.com/BorisVer/algo-harjoitustyo/blob/main/dokumentaatio/maarittelydokumentti.md)
- [Testausdokumentti](https://github.com/BorisVer/algo-harjoitustyo/blob/main/dokumentaatio/testausraportti.md)
- [Toteutusdokumentti](https://github.com/BorisVer/algo-harjoitustyo/blob/main/dokumentaatio/toteutusdokumentti.md)

## Viikkoraportti
- [Viikko 1](https://github.com/BorisVer/algo-harjoitustyo/blob/main/dokumentaatio/viikkoraportit/viikkoraportti1.md)
- [Viikko 2](https://github.com/BorisVer/algo-harjoitustyo/blob/main/dokumentaatio/viikkoraportit/viikkoraportti2.md)
- [Viikko 3](https://github.com/BorisVer/algo-harjoitustyo/blob/main/dokumentaatio/viikkoraportit/viikkoraportti3.md)
- [Viikko 4](https://github.com/BorisVer/algo-harjoitustyo/blob/main/dokumentaatio/viikkoraportit/viikkoraportti4.md)
- [Viikko 5](https://github.com/BorisVer/algo-harjoitustyo/blob/main/dokumentaatio/viikkoraportit/viikkoraportti5.md)

## Asennus
1. Asenna riippuvuudet

   ```bash
   poetry install
   ```

2. Avaa peli

   ```bash
   poetry run invoke start
   ```

## Ohjelman suoritukset

### Pelin käynnistys
   ```bash
   poetry run invoke start
   ```
Pelin avautuessa painamalla Start Game nappia ohjelma känynnistyy tai Quit ohjelma sulkeutuu. Pelin loppuessa tulee loppunäyttö jossa painamalla Restart alkaa ohjelma uudelleen, tai Quit ohjelma sulkeutuu. 

### Testien suoritus
   ```bash
   poetry run invoke test
   ```

### Pylintin suoritus
   ```bash
   poetry run invoke lint
   ```

### Coverage suoritus
   ```bash
   poetry run invoke coverage
   ```

### Coverage raportin luonti
   ```bash
   poetry run invoke coverage-report
   ```
Raportti ilmestyy *htmlcov* hakemustoon
