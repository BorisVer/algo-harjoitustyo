# 2048-Pelin algoritmi

Tämä on 2048 Pelille algoritmi

## Dokumentaatio
- ...

## Viikkoraportti
- [Viikko 1](https://github.com/BorisVer/algo-harjoitustyo/dokumentaatio/viikkoraportit/viikkoraportti1.md)

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
