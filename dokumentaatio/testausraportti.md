# Testausraportti

<img width="782" height="436" alt="Screenshot from 2025-10-17 11-45-49" src="https://github.com/user-attachments/assets/f8766252-0b00-47ce-8b08-9a21c957105f" />

## Mitä on testattu ja miten

### 1. Siirtojen toimivuus ([`test_algorithm.py`](https://github.com/BorisVer/algo-harjoitustyo/blob/main/src/tests/test_algorithm.py))

**Perustoiminnot:**
Testattu että kaikki neljä siirtosuuntaa toimivat oikein yksinkertaisella pelilaudalla. Kutsuttu metodeja `move_left()`, `move_right()`, `move_up()` ja `move_down()` laudalla jossa on hajallaan muutama laatta, ja varmistettu että laatat liukuvat haluttuun suuntaan.

**Monimutkaiset yhdistymät:**
Testattu että algoritmi käsittelee oikein useita samanaikaisia yhdistymisiä ja ketjutettuja yhdistyksiä (esim. [2,2,4] → [4,4] → [8]). Testattu monimutkaisella pelilaudalla jossa on useita yhdistyviä laattapareja eri siirtosuunnissa.

**Tyhjien ruutujen suhde:**
Testattu `get_empty_ratio()` kolmella erilaisella pelilaudalla:
- Täysin tyhjä lauta → 100% (1.0)
- Täysin täysi lauta → 0% (0.0)
- Osittain täytetty lauta → 37.5% (6/16)

**Kulmabonuksen testaus:**
Testattu `get_corner_bonus()` kolmella erilaisella pelilaudalla:
- Isoin laatta yhdessä kulmassa → bonus myönnetty
- Useita isointa laattaa, joista yksi kulmassa → bonus myönnetty
- Isoin laatta keskellä lautaa → ei bonusta

**Tasaisuus ja yhdistymispotentiaali:**
Testattu `smoothness_and_merge()` monimutkaisella pelilaudalla. Varmistettu että funktio laskee oikein vierekkäisten laattojen erot (tasaisuus) ja tunnistaa mahdolliset yhdistymät ja antaa niistä bonuksen.

**Käärme-bonus:**
Testattu `get_snake_bonus()` kahdella pelilaudalla:
- Satunnainen lauta ilman käärmekuviota → bonus 0
- Lauta jossa arvot laskevat monotonisesti käärmemuodossa → oikea bonusarvo laskettu


### 2. Pelilaudan arviointi ([`test_evaluation.py`](https://github.com/BorisVer/algo-harjoitustyo/blob/main/src/tests/test_evaluation.py))
Tähän on käytetty mock-arvoja konfiguraatioparametreille jotta pelaajan muutokset `game_config.py` eivät vaikuta testeihin.

**Arviointifunktion perustestaus:**
Testattu `evaluate()` tyhjällä pelilaudalla. Varmistettu että täysin tyhjä lauta saa pelkän tyhjien ruutujen bonuksen (16.0 pistettä) ilman muita bonuksia.

**Kokonaisarvioinnin testaus:**
Testattu arviointifunktiota normaalilla pelilaudalla jossa on sekalaisia laattoja. Laskettu manuaalisesti odotettu pistemäärä joka koostuu:
- Tyhjien ruutujen bonus: 9/16 × 16.0
- Kulmabonuksen: 3.0 (isoin laatta kulmassa)
- Tasaisuusbonus: -1.17 × 5.0 (negatiivinen koska erot suuret)
- Käärme-bonus: 0.67 × 4.0
- Yhdistymisbonus: 0.125 × 5.5

Testattu että `evaluate()` palauttaa täsmälleen lasketun arvon.

**Parhaan siirron valinta:**
Testattu `get_best_move()` viidellä erilaisella pelilaudalla joissa on selkeä paras siirto:

1. **Ylös-siirto:** Lauta jossa kaksi 32-laattaa yhdistyy ylös-siirrolla
2. **Oikealle-siirto:** Lauta jossa 2048 ja kaksi 256-laattaa sijaitsevat alhaalla, oikealle siirtäminen säilyttää suuret arvot yhdessä
3. **Alas-siirto:** Lauta jossa arvot ovat järjestyksessä ylhäältä alas (2→4096), alas-siirto täyttää tyhjän rivin
4. **Vasemmalle-siirto:** Lauta jossa kolme laattaparia (2+2, 4+4, 8+8) vasemmassa reunassa, vasemmalle-siirto yhdistää kaikki
5. **Oikealle-siirto:** Lauta jossa kaksi 4-laattaa ja kaksi 2-laattaa, oikealle-siirto maksimoi yhdistymät

### 3. Pelilogiikka ([`test_game_logic.py`](https://github.com/BorisVer/algo-harjoitustyo/blob/main/src/tests/test_game_logic.py))

**Pelilaudan palautus:**
Testattu `return_board()` metodia yksinkertaisella pelilaudalla jossa on yksi rivi täynnä laattoja. Testattu että `return_board()` palauttaa oikean 2D-listan.

**Laatan generointi täydellä laudalla:**
Testattu `spawn_tile()` tilanteessa jossa pelilauta on täynnä. Varmistettu että uutta laattaa ei generoida ja metodi palauttaa `None`.

**Pelin päättymisen tunnistus:**
Testattu `game_over` tunnistaminen tilanteessa jossa ei ole mahdollisia siirtoja. Pelilaudall on laiettu vuorottelevat 2 ja 4 arvot jossa mikään siirto ei yhdistä laattoja eikä siirrä niitä. Yritetty tehdä siirto vasemmalle ja testattu että `game.game_over` muuttuu `True`.

### 4. Lisätestit
Näiden lisäksi on testejä kirjoitettu napeille ([`test_buttons.py`](https://github.com/BorisVer/algo-harjoitustyo/blob/main/src/tests/test_buttons.py)), visuaaliselle yhdistymiselle testit ([`test_merge.py`](https://github.com/BorisVer/algo-harjoitustyo/blob/main/src/tests/test_merge.py)), testaamaan että yhdistyksistä saa oikean määrän pisteitä ([`test_score.py`](https://github.com/BorisVer/algo-harjoitustyo/blob/main/src/tests/test_score.py)) ja että ennätys päivittyy ([`test_top_score.py`](https://github.com/BorisVer/algo-harjoitustyo/blob/main/src/tests/test_top_score.py))
