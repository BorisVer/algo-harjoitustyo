# Määrittelydokumentti

Tämä projekti suoritetaan osana minun tietojenkäsittelytieteen kandidaatti tutkintoa (TKT).

Projekti suoritetaan käyttäen pääsääntöisesti python ohjelmointikieltä. Toteutan työssä algoritmin joka osaa pelata 2048 peliä optimoidusti. Käytän tähän expectimax algoritmia. Ohjelma saa syötteenä pelin tilan ja laskee siitä parhaimman mahdollisen siirron. Aika- ja tilavaativuuksia ei ole vielä pohdittu projektiin.

Harjoitustyön ydin on expectimax algoritmi. Tämä algorimti testaa jokaisen mahdollisen siirron sekä kaikki siitä johtavan tilan mahdolliset pelitilanteet johon päädytään kun pelilaudalle lisätään uusi arvo. Algoritmi laskee pelaajan määrittämän n verran siirtoja eteenpäin. Jokaisesta lopullisesta tilanteesta se vertaa sitä toisiin ja valitsee parhaan mahdollisen siirron. Se valitsee tämän märittämän heurestiikka fuktion avulla.

Projektin dokumentaatio on suomenkielellä, mutta koodin kommentit ovat englanniksi.
