# 2048-Pelin algoritmi

Tämä on 2048 Pelille expectimax algoritmi

## Dokumentaatio
- [Määrittelydokumentti](https://github.com/BorisVer/algo-harjoitustyo/blob/main/dokumentaatio/maarittelydokumentti.md)
- [Testausdokumentti](https://github.com/BorisVer/algo-harjoitustyo/blob/main/dokumentaatio/testausraportti.md)
- [Toteutusdokumentti](https://github.com/BorisVer/algo-harjoitustyo/blob/main/dokumentaatio/toteutusdokumentti.md)

## Viikkoraportti
- [Viikko 1](https://github.com/BorisVer/algo-harjoitustyo/blob/main/dokumentaatio/viikkoraportit/viikkoraportti1.md)
- [Viikko 2](https://github.com/BorisVer/algo-harjoitustyo/blob/main/dokumentaatio/viikkoraportit/viikkoraportti2.md)
- [Viikko 3](https://github.com/BorisVer/algo-harjoitustyo/blob/main/dokumentaatio/viikkoraportit/viikkoraportti3.md)
- [Viikko 4](https://github.com/BorisVer/algo-harjoitustyo/blob/main/dokumentaatio/viikkoraportit/viikkoraportti4.md)

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

### Testien suoritus
   ```bash
   poetry run invoke test
   ```

### Pylintin suoritus
   ```bash
   poetry run invoke lint
   ```


### Coverage raportin luonti
   ```bash
   poetry run invoke coverage-report
   ```
Raportti ilmestyy *htmlcov* hakemustoon
