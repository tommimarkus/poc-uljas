# Uljas code lists (koodistot) — full value reference

Generated from `input/schemas/common/uljasCodes/uljasCodes.xsd` (Uljas 26.3). **60 code lists, 1658 values.** Each `*Code` simple type is an `xsd:int`/`xsd:string` enumeration; this file lists every value with its Finnish description. The UML data models reference these lists by name as attribute types (see **Used by**); this reference is the authoritative source the `data-co` summary pointed to.

> Regenerate when `uljasCodes.xsd` changes.
>
> **Used by** counts *direct* UML class attributes typed to the code list. `—`
> means the list is referenced structurally (nested elements / deeper types),
> not that it is unused — every list here is referenced by at least one schema.

## Summary

| Code list | Values | Description | Used by |
|---|--:|---|---|
| [`asianMaksunTyyppiCode`](#asianmaksuntyyppicode) | 2 | Asian maksun tyyppi | 1 attr(s) |
| [`asianMuutoskirjauksenLaatuCode`](#asianmuutoskirjauksenlaatucode) | 28 | Asian muutoskirjauksen laatu (suluissa asian muutoskirjauksen laji, johon kyseinen laatu voidaan liittää) | 5 attr(s) |
| [`asianMuutoskirjauksenLajiCode`](#asianmuutoskirjauksenlajicode) | 4 | Asian muutoskirjauksen laji | 1 attr(s) |
| [`asianToimenpideCode`](#asiantoimenpidecode) | 1 | Asian toimenpide | 1 attr(s) |
| [`asianimiCode`](#asianimicode) | 140 | Asianimi | 4 attr(s) |
| [`esteenLajiCode`](#esteenlajicode) | 5 | Esteen laji | 1 attr(s) |
| [`esteenSeliteMuuEsteCode`](#esteenselitemuuestecode) | 7 | Esteen selite, muu este | 1 attr(s) |
| [`esteenSelitteenLaatuCode`](#esteenselitteenlaatucode) | 6 | Esteen selitteen laatu | 1 attr(s) |
| [`haadonToteutumistapaCode`](#haadontoteutumistapacode) | 5 | Häädön toteutumistapa | 1 attr(s) |
| [`korkolajiCode`](#korkolajicode) | 31 | Korkolaji | 1 attr(s) |
| [`koronMaaraytymistapaCode`](#koronmaaraytymistapacode) | 7 | Koron määräytymistapa | 6 attr(s) |
| [`maksunKertymistapaCode`](#maksunkertymistapacode) | 36 | Maksun kertymistapa | 1 attr(s) |
| [`oikaisuselitteenLajiCode`](#oikaisuselitteenlajicode) | 3 | Oikaisuselitteen laji | 1 attr(s) |
| [`saatavanimiCode`](#saatavanimicode) | 25 | Saatavanimi | 7 attr(s) |
| [`tuomioistuinCode`](#tuomioistuincode) | 176 | Tuomioistuin | 1 attr(s) |
| [`ulosotonMaksunLajiCode`](#ulosotonmaksunlajicode) | 2 | Ulosoton maksun laji | 1 attr(s) |
| [`ulosotonMaksunTarkenneCode`](#ulosotonmaksuntarkennecode) | 9 | Ulosoton maksun tarkenne | 1 attr(s) |
| [`siirronsyyCode`](#siirronsyycode) | 4 | Siirron syy | — |
| [`hakemuslajiCode`](#hakemuslajicode) | 6 | Hakemuslaji | 2 attr(s) |
| [`maksumuutoksenLaatuCode`](#maksumuutoksenlaatucode) | 3 | Maksumuutoksen laatu | — |
| [`peruutuksenLaatuCode`](#peruutuksenlaatucode) | 3 | Peruutuksen laatu | — |
| [`saatavamuutoksenLaatuCode`](#saatavamuutoksenlaatucode) | 2 | Saatavamuutoksen laatu | — |
| [`saatavanOsuudenLajiCode`](#saatavanosuudenlajicode) | 7 | Saatavan osuuden laji | 3 attr(s) |
| [`taytantoonpanotapaCode`](#taytantoonpanotapacode) | 2 | Täytäntöönpanotapa | 3 attr(s) |
| [`viivastyskoronLajiCode`](#viivastyskoronlajicode) | 31 | Viivästyskoron laji | 5 attr(s) |
| [`asianLiitetiedonLajiCode`](#asianliitetiedonlajicode) | 22 | Asian liitetiedon laji | 3 attr(s) |
| [`asianLisatiedonlajiCode`](#asianlisatiedonlajicode) | 31 | Asian lisätiedon laji | 1 attr(s) |
| [`henkilolajiCode`](#henkilolajicode) | 2 | Henkilölaji | 4 attr(s) |
| [`henkilotyyppiCode`](#henkilotyyppicode) | 10 | Henkilötyyppi | 4 attr(s) |
| [`kieliCode`](#kielicode) | 2 | Kieli | 2 attr(s) |
| [`kuntaCode`](#kuntacode) | 456 | Kunta | — |
| [`liitteenSaapumistapaCode`](#liitteensaapumistapacode) | 2 | Liitteen saapumistapa | 2 attr(s) |
| [`maaCode`](#maacode) | 255 | Maa | 2 attr(s) |
| [`kyllaEiCode`](#kyllaeicode) | 2 | Kyllä/Ei koodisto | 17 attr(s) |
| [`paatosLiitteenaCode`](#paatosliitteenacode) | 4 | Päätös liitteenä (= Tp-perusteen liitteen laji) | 4 attr(s) |
| [`sukupuoliCode`](#sukupuolicode) | 2 | Sukupuoli | 2 attr(s) |
| [`tietolahdeCode`](#tietolahdecode) | 2 | Tietolähde | 2 attr(s) |
| [`taytantoonpanoperusteenMaaraaikaCode`](#taytantoonpanoperusteenmaaraaikacode) | 2 | Täytäntöönpanoperusteen määräaika | 6 attr(s) |
| [`täytäntöönpanotapaCode`](#täytäntöönpanotapacode) | 3 | Täytäntöönpanotapa | — |
| [`valtakirjanLajiCode`](#valtakirjanlajicode) | 2 | Valtakirjan laji | — |
| [`valtuutuksenLaajuusCode`](#valtuutuksenlaajuuscode) | 2 | Valtuutuksen laajuus | — |
| [`valuuttaCode`](#valuuttacode) | 181 | Valuutta | 5 attr(s) |
| [`velallisenLisatiedonLajiCode`](#velallisenlisatiedonlajicode) | 15 | Velallisen lisätiedon laji | 1 attr(s) |
| [`velallistilityksenTyyppiCode`](#velallistilityksentyyppicode) | 3 | Velallistilityksen tyyppi | 1 attr(s) |
| [`asianVelallisenTilaCode`](#asianvelallisentilacode) | 9 | Asian velallisen tila | 1 attr(s) |
| [`henkilonRooliCode`](#henkilonroolicode) | 8 | Henkilön rooli | 1 attr(s) |
| [`siirtoilmoituksenLajiCode`](#siirtoilmoituksenlajicode) | 3 | Siirtoilmoituksen laji | — |
| [`ulosmittauksenLajiCode`](#ulosmittauksenlajicode) | 16 | Ulosmittauksen laji | — |
| [`tunnistautumismenetelmaCode`](#tunnistautumismenetelmacode) | 3 | Tunnistautumismenetelmä | — |
| [`maksukiellonPidatyksenLajiCode`](#maksukiellonpidatyksenlajicode) | 5 | Maksukiellon pidätyksen laji | 1 attr(s) |
| [`maksukiellonVoimassaolonLajiCode`](#maksukiellonvoimassaolonlajicode) | 3 | Maksukiellon voimassaolon laji | 1 attr(s) |
| [`maksukiellonPeruuttaminenCode`](#maksukiellonperuuttaminencode) | 9 | Maksukiellon peruuttaminen | 1 attr(s) |
| [`velallisenToimenpideCode`](#velallisentoimenpidecode) | 22 | Velallisen toimenpide | — |
| [`paaomasaatavannimiCode`](#paaomasaatavannimicode) | 5 | Pääomasaatavan nimi | — |
| [`muutoksenTilaCode`](#muutoksentilacode) | 4 | Sähköisen muutoksen tila | 1 attr(s) |
| [`ulosottorekisterinTulosteenLajiCode`](#ulosottorekisterintulosteenlajicode) | 9 | Ulosottorekisterin tulosteen laji | — |
| [`vapaakuukausipaatoksenPerusteCode`](#vapaakuukausipaatoksenperustecode) | 10 | Vapaakuukausipäätöksen peruste | — |
| [`rajoittamispaatoksenPerusteCode`](#rajoittamispaatoksenperustecode) | 4 | Rajoittamispäätöksen peruste | — |
| [`kuluttajaluottolainSopimuskoodiCode`](#kuluttajaluottolainsopimuskoodicode) | 3 | Kuluttajaluottolain mukainen sopimus | 2 attr(s) |
| [`taytantoonpanoperusteenMuutosTyyppiCode`](#taytantoonpanoperusteenmuutostyyppicode) | 2 | Täytäntöönpanoperusteen muutoksen tyyppi | 1 attr(s) |

### asianMaksunTyyppiCode

**2 values** · base `int` · Asian maksun tyyppi

*Used by:* `maksu.asianMaksunTyyppi`

| Value | Description |
|---|---|
| `1` | Osasuoritus |
| `2` | Loppusuoritus |

### asianMuutoskirjauksenLaatuCode

**28 values** · base `int` · Asian muutoskirjauksen laatu (suluissa asian muutoskirjauksen laji, johon kyseinen laatu voidaan liittää)

*Used by:* `peruutus.laatu`, `maksumuutos.laatu`, `saatavamuutos.laatu`, `muuMuutos.laatu`, `muutoskirjaus.laatu`

| Value | Description |
|---|---|
| `1` | Maksettu (Peruutus) |
| `2` | Kuittaus (Peruutus) |
| `3` | Muu syy (Peruutus) |
| `4` | Maksettu (Maksumuutos) |
| `5` | Kuittaus (Maksumuutos) |
| `6` | Muu syy (Maksumuutos) |
| `7` | Saatavaosien muutos (Saatavamuutos) |
| `13` | Elatuksen kohteen muutos (Elatuksen kohteen muutos) |
| `17` | Kiirehtimiskirje (Tiedustelu tai pyyntö) |
| `18` | Lykkäys (Tiedustelu tai pyyntö) |
| `19` | Muu syy (Tiedustelu tai pyyntö) |
| `20` | Hakijan viitetietomuutos (Muu muutos) |
| `21` | Muu asian muutos (Muu muutos) |
| `22` | Täytäntöönpanoperusteen muutos (Muu muutos) |
| `23` | Tilityksen muutos (Muu muutos) |
| `24` | Tilimuutos (Muu muutos) |
| `25` | Asian hakijamuutos (Muu muutos) |
| `26` | Asian asiamiesmuutos (Muu muutos) |
| `27` | Valtakirjamuutos (Muu muutos) |
| `28` | Asian velallismuutos (Muu muutos) |
| `29` | Passiiviperintäpyyntö (Muu muutos) |
| `31` | Tp-tavan muutos (Muu muutos) |
| `32` | Lainvoimaisuuden muutos (Muu muutos) |
| `33` | Päivämäärien tai vanhentumisen muutos (Muu muutos) |
| `34` | Sakkotuomion sisältömuutos (Muu muutos) |
| `35` | Tp-keskeytys (Muu muutos) |
| `36` | Aiheeton maksuunpano (Peruutus) |
| `37` | Saatavien vanhentumisen muutos (Saatavamuutos) |

### asianMuutoskirjauksenLajiCode

**4 values** · base `int` · Asian muutoskirjauksen laji

*Used by:* `muutoskirjaus.laji`

| Value | Description |
|---|---|
| `1` | Peruutus |
| `2` | Maksumuutos |
| `3` | Saatavamuutos |
| `7` | Muu muutos |

### asianToimenpideCode

**1 values** · base `int` · Asian toimenpide

*Used by:* `toimenpide.asianToimenpide`

| Value | Description |
|---|---|
| `6` | Asian tilitys |

### asianimiCode

**140 values** · base `int` · Asianimi

*Used by:* `asiaTiedotTypeV0.asiaNimi`, `asia.asianimi`, `asia.asianimi`, `asia.asiaNimi`

| Value | Description |
|---|---|
| `1` | Ennakkovero |
| `2` | Jäännosvero (luonnolliset henkilöt) |
| `3` | Jäännösvero (lähdevero) |
| `4` | Yhteisöjen ennakkovero |
| `5` | Yhteisöjen jäännösvero |
| `6` | Yhteisöjen ennakonpidätys |
| `7` | Ennakonpidätys |
| `8` | Työnantajan sosiaaliturvamaksu |
| `9` | Ennakonpidätys koroista ja osuuksista |
| `10` | Puun myyntitulon ennakonpidätys |
| `11` | Metsänhoitomaksu |
| `12` | Kiinteistövero |
| `13` | Perintö- ja lahjavero |
| `14` | Lähdevero |
| `15` | Korkotulon lähdevero |
| `16` | Arpajaisvero |
| `17` | Varainsiirtovero |
| `18` | Autovero (verottajan maksuunpanema) |
| `19` | Vakuutusmaksuvero |
| `20` | Arvonlisävero |
| `21` | Ajoneuvovero (verottajan maksuunpanema) |
| `22` | Leimavero |
| `23` | Leimavero leimaverokoneella kertyvä |
| `24` | TyEL-vakuutusmaksut |
| `25` | YEL-vakuutusmaksut |
| `26` | MYEL- ja MATA-vakuutusmaksut |
| `27` | LEL-vakuutusmaksut |
| `28` | MEL-vakuutusmaksut |
| `29` | TaEL-vakuutusmaksut |
| `30` | Lakisääteiset tapaturmavakuutusmaksut |
| `31` | Työttömyysvakuutusmaksut |
| `32` | Muu työnantajan lakisääteinen maksu |
| `33` | Verottajan asianimiä |
| `34` | Liikennevakuutukset ja hyvikemaksut |
| `35` | Yhdistelmävakuutusmaksut |
| `36` | Muut  vahinkovakuutusmaksut |
| `37` | Sosiaali- ja terveyspalvelumaksuasiat |
| `38` | Sairaala- ja muut laitoshoitomaksut |
| `39` | Terveyskeskusmaksut |
| `40` | Hammashoitomaksut |
| `41` | Lastenpäivähoitomaksut |
| `42` | Kotipalvelumaksut |
| `43` | Muut sosiaali- ja terveyspalvelumaksut |
| `44` | Maanparannuslainat |
| `45` | Metsänparannuslainat |
| `46` | Kolttalainat |
| `47` | Peruskuivatuslainat |
| `48` | Muut valtion avustus- tai laina-asiat |
| `49` | Valtion asuntolainat |
| `50` | Pysäköintivirhemaksut |
| `51` | Julkisen liikenteen tarkastusmaksut |
| `52` | Ylikuormamaksut |
| `53` | Verottajan asianimiä |
| `54` | Televisiomaksut |
| `55` | Muut telehallintokeskuksen maksut |
| `56` | Polttoainemaksu / dieselvero (AKE) |
| `57` | Ajoneuvovero (AKE) |
| `58` | Tullimaksut |
| `59` | Tuomioistuinten maksut |
| `60` | Oikeudenkäynti- ja oikeusapumaksut |
| `61` | Ulosoton maksut |
| `62` | Kiinteistötoimitusmaksut |
| `63` | Ajoneuvon siirtomaksut |
| `64` | Jätehuoltomaksut |
| `65` | Vesi- ja jätevesijärjestelmän maksut |
| `66` | Oppilaitosmaksut |
| `67` | Koiraverot ja muut koiriin liittyvät maksut |
| `68` | Kuljetusmaksut |
| `69` | Tiehoitomaksut |
| `70` | Nuohousmaksut |
| `71` | Muut julkisoikeudelliset maksut |
| `72` | Opintolainat |
| `73` | Rikesakot |
| `74` | Rangaistusmääräyssakot |
| `75` | Rangaistusmääräyssakkojen korotukset |
| `76` | Järjestyssääntörikkomus |
| `77` | Uhkasakot |
| `78` | Tuomiolauselmasakot |
| `79` | Pohjoismaiset sakot |
| `80` | Yhteisösakko |
| `81` | Kurinpitosakot |
| `82` | Muuntorangaistukset |
| `83` | Tuomiolauselmasaatavat |
| `84` | Rangaistusmääräyssaatavat |
| `85` | Pohjoismaiset saatavat |
| `86` | Rikosvahinkokorvaukset |
| `87` | Rahamääräiset menettämisseuraamukset |
| `88` | Kuulutusrekisteriasiat |
| `89` | Elatusapusaatavat |
| `90` | Pohjoismaiset elatusapusaatavat |
| `91` | Muut elatusapuasiat |
| `92` | Velkakirjasaatavat |
| `93` | Verottajan asianimiä |
| `94` | Vuokrasaatavat |
| `95` | Osamaksukauppasaatavat |
| `96` | Palkkasaatavat |
| `97` | Palkkaturvasaatavat |
| `98` | Riita-asioihin liittyvät vahingonkorvaussaatavat |
| `99` | Rikosasioihin liittyvät vahingonkorvaussaatavat |
| `100` | Lainhakusaatavat |
| `101` | Maksamismääräyssaatavat |
| `102` | Velkajärjestelysaatavat |
| `103` | Välitystuomiosaatavat |
| `104` | Konkurssituomiosaatavat |
| `105` | Häätö, asuinhuoneisto |
| `106` | Häätö, muu huoneisto |
| `107` | Virka-apuasiasaatava |
| `108` | Muut yksityisoikeudelliset saatavat |
| `110` | Osamaksukauppalain mukaiset asiat |
| `111` | Turvaamistoimenpideasiat |
| `112` | Lapsiasioiden täytäntöönpano |
| `113` | Irtaimen luovutuspäätökset |
| `114` | Muut toimenpideasiat |
| `115` | Muut veroasiat |
| `116` | Perintäkulut |
| `117` | Rikosas. Liit. Vah.korv., uo-maksullinen |
| `118` | Autovero (AKE) |
| `119` | Laiminlyöntimaksu |
| `120` | EU-sakot |
| `121` | EU-saamiset |
| `122` | Virka-apu |
| `123` | Ulkomainen ulosottoperuste |
| `124` | Ulkomaiset turvaamistoimipäätökset |
| `125` | Jäädyttämisasiat |
| `126` | Tulli (EU-tulli) |
| `127` | Pakoteasiat |
| `128` | Rikosuhrimaksu |
| `129` | Sakkomääräys |
| `130` | Tuomioistuimen tiedonhankintapyyntö |
| `131` | Eurooppalainen tilivarojen turvaamismääräys |
| `132` | Liikenteenharjoittajan seuraamusmaksu |
| `133` | Tilaajavastuulain mukainen laiminlyöntimaksu |
| `134` | Seuraamusmaksu yht. kalastuspolitiikan vastaisesta teosta |
| `135` | Rikkomusmaksu yht. kalastuspolitiikan vastaisesta teosta |
| `136` | Alkoholilain mukainen seuraamusmaksu |
| `137` | Liikennevirhemaksut |
| `138` | Tuontivalvonnan seuraamusmaksu |
| `139` | Ajoneuvolain mukainen seuraamusmaksu |
| `140` | Seuraamusmaksu |
| `141` | Tapaturmat ja ammattitaudit (takaisinperintäpäätös) |

### esteenLajiCode

**5 values** · base `int` · Esteen laji

*Used by:* `este.laji`

| Value | Description |
|---|---|
| `1` | Varattomuuseste |
| `2` | Varattomuus- ja tuntemattomuuseste |
| `3` | Muu este |
| `4` | Suppean ulosoton este |
| `5` | Suppean ulosoton este ja tuntemattomuuseste |

### esteenSeliteMuuEsteCode

**7 values** · base `int` · Esteen selite, muu este

*Used by:* `este.muuSelite`

| Value | Description |
|---|---|
| `1` | Vahvistettu velkajärjestely / velkasaneeraus |
| `2` | Konkurssi |
| `3` | Haastettu muuntorangaistusmenettelyyn |
| `4` | Passitettu |
| `5` | Vastaajaa ei tavoitettu |
| `6` | Muu muu este |
| `7` | Ulosottoperuste  vanhentunut velallisen osalta |

### esteenSelitteenLaatuCode

**6 values** · base `int` · Esteen selitteen laatu

*Used by:* `este.selitteenLaatu`

| Value | Description |
|---|---|
| `1` | Velallinen ei saa veronpalautusta |
| `2` | Ei jako-osuutta toistuvaistulon ulosmittauksessa |
| `3` | Ei ulosmittauskelpoista tuloa tai omaisuutta |
| `4` | Velallisen yhteenlasketut tulot eivät ylitä suojaosuutta |
| `5` | Etuoikeutettua saatavaa ulosotossa |
| `6` | Muu |

### haadonToteutumistapaCode

**5 values** · base `int` · Häädön toteutumistapa

*Used by:* `haato.toteutusTapa`

| Value | Description |
|---|---|
| `1` | Vastaaja muuttanut |
| `2` | Häädetty |
| `3` | Hakija peruuttanut |
| `4` | Lukkoseppähäätö |
| `5` | Muu |

### korkolajiCode

**31 values** · base `int` · Korkolaji

*Used by:* `viivastyskorko.korkoLaji`

| Value | Description |
|---|---|
| `1` | Aktia säästöpankki Oyj, primekorko |
| `2` | Svenska Handelsbanken Ab (publ), primekorko |
| `3` | Nordea Pankki Oyj, primekorko / Merita Pankki Oyj, primekorko |
| `4` | Osuuspankkiryhmä (OKO), primekorko |
| `5` | Sampo Pankki Oyj, primekorko / Leonia pankki Oyj, primekorko |
| `6` | Säästöpankit, viitekorko |
| `7` | Ålandsbanken Abp, primekorko |
| `8` | Peruskorko |
| `9` | Ministeriön vahvistama viitekorko |
| `10` | Euribor 1 kk |
| `11` | Euribor 3 kk |
| `12` | Euribor 6 kk |
| `13` | Euribor 9 kk |
| `14` | Euribor 12 kk |
| `15` | Veron viivästyskorko |
| `16` | EKP + marginaali / Euroopan keskuspankin viitekorko |
| `17` | EKP, Euroopan keskuspankin viitekorko |
| `18` | Tapiola Pankki Oy |
| `19` | EQ Pankki Oy |
| `20` | Euribor 365, 1kk |
| `21` | Euribor 365, 3kk |
| `22` | Euribor 365, 6kk |
| `23` | Euribor 365, 9kk |
| `24` | Euribor 365, 12kk |
| `25` | Paikallisosuuspankit |
| `26` | SEB Gyllenberg Private Bank Oy |
| `27` | Hypo-konserni |
| `28` | S-Pankki |
| `29` | EKP + 8 / Euroopan keskuspankin viitekorko |
| `31` | TF Bank, primekorko |
| `32` | Perintöveron viivästyskorko |

### koronMaaraytymistapaCode

**7 values** · base `int` · Koron määräytymistapa

*Used by:* `viivastyskorkoTypeV1.maaraytymistapa`, `viivastyskorkoTypeV0.maaraytymistapa`, `viivastysKorko.maaraytymistapa`, `viivastysKorko.maaraytymistapa`, `viivastysKorkoType.maaraytymistapa`, `viivastyskorko.maaraytymisTapa`

| Value | Description |
|---|---|
| `1` | Korkolain 4 § 1 mom. mukaan |
| `2` | Korkolain 4 § 2 mom. mukaan |
| `3` | Korkolain 4 § 2 mom. mukaan, vähintään korko |
| `4` | Korkolain 4 § 2 mom. kulutusluotto |
| `5` | Korkolain 4 a § 1 mom. mukaan |
| `6` | Korkolain 4 a § 2 mom. mukaan |
| `7` | Korkolain 4 a § 2 mom. mukaan, vähintään korko |

### maksunKertymistapaCode

**36 values** · base `int` · Maksun kertymistapa

*Used by:* `maksu.kertymistapa`

| Value | Description |
|---|---|
| `1` | Määrittelemätön |
| `2` | Kehotusmaksu |
| `3` | Käteismaksu |
| `4` | Maksusuunnitelmamaksu |
| `5` | Palkan/etuuden ulosmittaus |
| `6` | Eläkkeen ulosmittaus |
| `7` | Veronpalautuksen ulosmittaus |
| `8` | Elinkeinotulon/saatavan ulosmittaus |
| `9` | Muu ulosmittaus |
| `10` | Huutokauppa |
| `11` | Reskontralaskun maksu |
| `12` | Pankkitilin ulosmittaus |
| `13` | Tuoton ulosmittaus |
| `14` | Saatavan ulosmittaus |
| `15` | Asunto-osakkeiden julkinen huutokauppa |
| `16` | Ulosottomiehen toimittama asunto-osakkeiden vapaa myynti |
| `17` | Asunto-osakkeiden vapaa yksityismyynti |
| `18` | Kiinteistön julkinen huutokauppa |
| `19` | Ulosottomiehen toimittama kiinteistön vapaa myynti |
| `20` | Kiinteistön vapaa yksityismyynti |
| `21` | Muun irtaimen julkinen huutokauppa |
| `22` | Ulosottomiehen toimittama muun irtaimen vapaa myynti |
| `23` | Muun irtaimen vapaa yksityismyynti |
| `24` | Yksityisen toimittama asunto-osakkeiden huutokauppa |
| `25` | Yksityisen toimittama kiinteistön huutokauppa |
| `26` | Yksityisen toimittama muun irtaimen huutokauppa |
| `27` | Muulla ulosmittauksella kertynyt |
| `28` | Takaisinmaksu |
| `29` | Vakuus |
| `30` | Takavarikko |
| `31` | Asunto-osakkeiden nettihuutokauppa |
| `32` | Kiinteistön nettihuutokauppa |
| `33` | Muun irtaimen nettihuutokauppa |
| `34` | Ulosottomiehen toimittama asunto-osakkeiden välittäjämyynti |
| `35` | Ulosottomiehen toimittama kiinteistön välittäjämyynti |
| `36` | Ulosottomiehen toimittama muun irtaimen välittäjämyynti |

### oikaisuselitteenLajiCode

**3 values** · base `int` · Oikaisuselitteen laji

*Used by:* `oikaisuselite.laji`

| Value | Description |
|---|---|
| `1` | Saatavan ulosmittaus |
| `2` | Ennakonpidätys |
| `3` | Muu laji |

### saatavanimiCode

**25 values** · base `int` · Saatavanimi

*Used by:* `saatavanPerustiedotTypeV0.saatavanimi`, `saatava.saatavanimi`, `maksumuutoksenSaatava.saatavaNimi`, `saatava.saatavaNimi`, `saatavanPerustiedotType.saatavanimi`, `saatava.saatavanimi`, `maksunosuus.saatavaNimi`

| Value | Description |
|---|---|
| `1` | Korkosaatava |
| `2` | Pääoma |
| `3` | Vahingonkorvaus |
| `4` | Kulut |
| `5` | Oikeudenkäyntikulut |
| `6` | Aikaisemmat täytäntöönpanokulut |
| `7` | Muu saatava |
| `8` | Elatusapu |
| `9` | Veronlisäys |
| `10` | Viivästyskorkoa vastaava korko |
| `11` | Maksamattoman ennakon viivästyskorko |
| `12` | Veronkorotus |
| `13` | Vero |
| `14` | Maksettava yhteisökorko |
| `15` | Takaisinperittävä yhteisökorko |
| `16` | Maksunlykkäyskorko |
| `17` | Jäämämaksu |
| `18` | Viivästyskorko |
| `19` | Elatustuki |
| `20` | Elatuskorko |
| `21` | Luottokustannukset (ei luoton korko) |
| `22` | Perintäkulut |
| `23` | Muut kulut |
| `51` | Korkojäämä. Ei saa lähettää ulosottoon, mutta voi tulla ulosotosta. |
| `52` | Juokseva viivästyskorko. Ei saa lähettää ulosottoon, mutta voi tulla ulosotosta. |

### tuomioistuinCode

**176 values** · base `int` · Tuomioistuin

*Used by:* `taytantoonpanonPeruste.tuomioistuin`

| Value | Description |
|---|---|
| `1` | Korkein oikeus |
| `16` | Helsingin hovioikeus |
| `17` | Itä-Suomen hovioikeus |
| `18` | Turun hovioikeus |
| `19` | Vaasan hovioikeus |
| `20` | Kouvolan hovioikeus |
| `21` | Rovaniemen hovioikeus |
| `100` | Ahvenanmaan tuomiokunta |
| `101` | Alavuden tuomiokunta |
| `102` | Espoon tuomiokunta |
| `103` | Euran tuomiokunta |
| `104` | Haapajärven tuomiokunta |
| `105` | Halikon tuomiokunta |
| `106` | Hauhon tuomiokunta |
| `107` | Heinolan tuomiokunta |
| `108` | Vantaan tuomiokunta |
| `109` | Hollolan tuomiokunta |
| `110` | Hyvinkään tuomiokunta |
| `111` | Oulujoen tuomiokunta |
| `112` | Iitin tuomiokunta |
| `113` | Iisalmen tuomiokunta |
| `114` | Ikaalisten tuomiokunta |
| `115` | Ilmajoen tuomiokunta |
| `116` | Ilomantsin tuomiokunta |
| `117` | Imatran tuomiokunta |
| `118` | Janakkalan tuomiokunta |
| `119` | Juvan tuomiokunta |
| `120` | Jyväskylän tuomiokunta |
| `121` | Jämsän tuomiokunta |
| `122` | Kajaanin tuomiokunta |
| `123` | Kauhajoen tuomiokunta |
| `124` | Kauhavan tuomiokunta |
| `125` | Kemijärven tuomiokunta |
| `126` | Loviisan tuomiokunta |
| `127` | Kiteen tuomiokunta |
| `128` | Kokemäen tuomiokunta |
| `129` | Korsholman tuomiokunta |
| `130` | Kuopion tuomiokunta |
| `131` | Kuusamon tuomiokunta |
| `132` | Kymin tuomiokunta |
| `133` | Kyrön tuomiokunta |
| `134` | Lappeen tuomiokunta |
| `135` | Lapin tuomiokunta |
| `136` | Lapuan tuomiokunta |
| `137` | Liperin tuomiokunta |
| `138` | Lohjan tuomiokunta |
| `139` | Lohtajan tuomiokunta |
| `140` | Loimaan tuomiokunta |
| `141` | Mikkelin tuomiokunta |
| `142` | Muhoksen tuomiokunta |
| `143` | Orimattilan tuomiokunta |
| `145` | Nilsiän tuomiokunta |
| `146` | Närpiön tuomiokunta |
| `148` | Paraisten tuomiokunta |
| `149` | Pieksämäen tuomiokunta |
| `150` | Pielaveden tuomiokunta |
| `151` | Pielisjärven tuomiokunta |
| `152` | Pietarsaaren tuomiokunta |
| `153` | Piikkiön tuomiokunta |
| `154` | Pirkkalan tuomiokunta |
| `155` | Porvoon tuomiokunta |
| `156` | Raaseporin tuomiokunta |
| `157` | Rantasalmen tuomiokunta |
| `158` | Rovaniemen tuomiokunta |
| `159` | Ruoveden tuomiokunta |
| `160` | Saarijärven tuomiokunta |
| `161` | Ylivieskan tuomiokunta |
| `162` | Suonenjoen tuomiokunta |
| `163` | Tammelan tuomiokunta |
| `164` | Toijalan tuomiokunta |
| `165` | Tornion tuomiokunta |
| `166` | Tuusulan tuomiokunta |
| `167` | Tyrvään tuomiokunta |
| `168` | Ulvilan tuomiokunta |
| `169` | Valkealan tuomiokunta |
| `170` | Varkauden tuomiokunta |
| `171` | Vehmaan tuomiokunta |
| `172` | Viitasaaren tuomiokunta |
| `500` | Haminan raastuvanoikeus |
| `501` | Hangon raastuvanoikeus |
| `502` | Heinolan raastuvanoikeus |
| `503` | Helsingin raastuvanoikeus |
| `504` | Hämeenlinnan raastuvanoikeus |
| `505` | Iisalmen raastuvanoikeus |
| `506` | Joensuun raastuvanoikeus |
| `507` | Jyväskylän raastuvanoikeus |
| `508` | Kajaanin raastuvanoikeus |
| `510` | Kemin raastuvanoikeus |
| `511` | Kokkolan raastuvanoikeus |
| `512` | Kotkan raastuvanoikeus |
| `514` | Kuopion raastuvanoikeus |
| `515` | Lahden raastuvanoikeus |
| `516` | Lappeenrannan raastuvanoikeus |
| `519` | Mikkelin raastuvanoikeus |
| `520` | Naantalin raastuvanoikeus |
| `521` | Oulun raastuvanoikeus |
| `522` | Pietarsaaren raastuvanoikeus |
| `523` | Porin raastuvanoikeus |
| `524` | Porvoon raastuvanoikeus |
| `525` | Raahen raastuvanoikeus |
| `526` | Rauman raastuvanoikeus |
| `527` | Savonlinnan raastuvanoikeus |
| `529` | Tampereen raastuvanoikeus |
| `530` | Tornion raastuvanoikeus |
| `531` | Turun raastuvanoikeus |
| `533` | Uudenkaupungin raastuvanoikeus |
| `534` | Vaasan raastuvanooikeus |
| `701` | Alavuden käräjäoikeus |
| `702` | Espoon käräjäoikeus |
| `703` | Forssan käräjäoikeus |
| `704` | Haapajärven käräjäoikeus |
| `705` | Heinolan käräjäoikeus |
| `706` | Helsingin käräjäoikeus |
| `707` | Hyvinkään käräjäoikeus, ent. Hyvinkään ja Riihimäen käräjäoikeudet |
| `708` | Kanta-Hämeen käräjäoikeus, ent. Hämeenlinnan ja Forssa-Loimaan käräjäoikeudet |
| `709` | Iisalmen käräjäoikeus |
| `711` | Ikaalisten käräjäoikeus |
| `712` | Imatran käräjäoikeus |
| `713` | Pohjois-Karjalan käräjäoikeus, ent. Joensuun ja Nurmeksen käräjäoikeudet |
| `714` | Juvan käräjäoikeus |
| `715` | Keski-Suomen käräjäoikeus, ent. Jyväskylän, Jämsän ja Äänekosken käräjäoikeudet |
| `716` | Jämsän käräjäoikeus |
| `717` | Kainuun käräjäoikeus, ent. Kajaanin käräjäoikeus |
| `718` | Kauhajoen käräjäoikeus |
| `719` | Kauhavan käräjäoikeus |
| `720` | Kemijärven käräjäoikeus |
| `721` | Kemin käräjäoikeus |
| `722` | Kokemäen käräjäoikeus |
| `723` | Keski-Pohjanmaan käräjäoikeus, ent. Kokkolan käräjäoikeus |
| `724` | Kotkan käräjäoikeus |
| `725` | Kymenlaakson käräjäoikeus, ent. Kouvolan ja Kotkan käräjäoikeudet |
| `726` | Pohjois-Savon käräjäoikeus, ent. Kuopion, Iisalmen ja Varkauden käräjäoikeudet |
| `727` | Kuusamon käräjäoikeus |
| `728` | Kyrönmaan käräjäoikeus |
| `729` | Päijät-Hämeen käräjäoikeus, ent. Lahden käräjäoikeus |
| `730` | Lapin käräjäoikeus, ent. Lapin, Kemijärven ja Rovaniemen käräjäoikeudet |
| `731` | Etelä-Karjalan käräjäoikeus, ent. Lappeenrannan käräjäoikeus |
| `732` | Lapuan käräjäoikeus |
| `733` | Lohjan käräjäoikeus |
| `734` | Loimaan käräjäoikeus |
| `735` | Loviisan käräjäoikeus |
| `736` | Etelä-Savon käräjäoikeus, ent. Mikkelin, Pieksämäen ja Savonlinnan käräjäoikeudet |
| `737` | Mustasaaren käräjäoikeus |
| `738` | Vakka-Suomen käräjäoikeus |
| `739` | Nilsiän käräjäoikeus |
| `740` | Nurmeksen käräjäoikeus |
| `741` | Orimattilan käräjäoikeus |
| `742` | Oulun käräjäoikeus, ent. Oulun ja Kuusamon käräjäoikeudet |
| `743` | Paraisten käräjäoikeus |
| `744` | Pieksämäen käräjäoikeus |
| `745` | Pietarsaaren käräjäoikeus |
| `747` | Satakunnan käräjäoikeus, ent. Porin ja Rauman käräjäoikeudet |
| `748` | Itä-Uudenmaan käräjäoikeus, ent. Porvoon käräjäoikeus |
| `749` | Raahen käräjäoikeus |
| `750` | Länsi-Uudenmaan käräjäoikeus, ent. Raaseporin ja Lohjan käräjäoikeudet |
| `751` | Rauman käräjäoikeus |
| `752` | Riihimäen käräjäoikeus |
| `753` | Rovaniemen käräjäoikeus |
| `755` | Salon käräjäoikeus |
| `756` | Savonlinnan käräjäoikeus |
| `757` | Etelä-Pohjanmaan käräjäoikeus, ent. Seinäjoen, Kauhajoen ja Kauhavan käräjäoikeudet |
| `758` | Pirkanmaan käräjäoikeus, ent. Tampereen, Ikaalisen ja Toijalan käräjäoikeudet |
| `759` | Toijalan käräjäoikeus |
| `760` | Tornion käräjäoikeus |
| `761` | Varsinais-Suomen käräjäoikeus, ent. Turun, Paraisen, Salon ja Vakka-Suomen käräjäoikeudet |
| `762` | Turunseudun käräjäoikeus |
| `763` | Tuusulan käräjäoikeus |
| `764` | Pohjanmaan käräjäoikeus, ent. Vaasan ja Mustasaaren käräjäoikeudet |
| `765` | Vammalan käräjäoikeus |
| `766` | Vantaan käräjäoikeus |
| `767` | Varkauden käräjäoikeus |
| `768` | Ylivieska-Raahen käräjäoikeus, ent. Ylivieskan ja Raahen käräjäoikeudet |
| `769` | Ålands tingsrätt |
| `770` | Äänekosken käräjäoikeus |
| `771` | Kemi-Tornion käräjäoikeus, ent. Kemin käräjäoikeus |
| `772` | Forssa-Loimaan käräjäoikeus |

### ulosotonMaksunLajiCode

**2 values** · base `int` · Ulosoton maksun laji

*Used by:* `ulosotonmaksu.laji`

| Value | Description |
|---|---|
| `3` | Täytäntöönpanokulut |
| `6` | Tiedoksiantomaksu |

### ulosotonMaksunTarkenneCode

**9 values** · base `int` · Ulosoton maksun tarkenne

*Used by:* `ulosotonmaksu.tarkenne`

| Value | Description |
|---|---|
| `1` | Normaali käsittelymaksu |
| `2` | Suppean ulosoton käsittelymaksu |
| `3` | Passiiviperinnän käsittelymaksu |
| `4` | Asuinhuoneiston häätö |
| `5` | Liikehuoneiston häätö |
| `10` | Tilitysarvo enintään X € |
| `11` | Tilitysarvo ylittää X € |
| `12` | Turvaamistoimet |
| `13` | Muut |

### siirronsyyCode

**4 values** · base `int` · Siirron syy

| Value | Description |
|---|---|
| `1` | Osoite |
| `2` | Omaisuus |
| `3` | Erikoisperintä |
| `4` | Muu |

### hakemuslajiCode

**6 values** · base `int` · Hakemuslaji

*Used by:* `sahkoinenHakija.hakemusLaji`, `sahkoinenHakija.hakemusLaji`

| Value | Description |
|---|---|
| `1` | Verot |
| `2` | Muut julkisoikeudelliset asiat |
| `3` | Sakot |
| `4` | Elatusapuasiat |
| `5` | Muut yksityisoikeudelliset perintäasiat |
| `6` | Muut yksityisoikeudelliset toimenpideasiat |

### maksumuutoksenLaatuCode

**3 values** · base `int` · Maksumuutoksen laatu

| Value | Description |
|---|---|
| `4` | Maksettu |
| `5` | Kuittaus |
| `6` | Muu syy |

### peruutuksenLaatuCode

**3 values** · base `int` · Peruutuksen laatu

| Value | Description |
|---|---|
| `1` | Maksettu |
| `2` | Kuittaus |
| `3` | Muu syy |

### saatavamuutoksenLaatuCode

**2 values** · base `int` · Saatavamuutoksen laatu

| Value | Description |
|---|---|
| `7` | Saatavaosien muutos/Pääomasaatavamuutos |
| `37` | Saatavien vanhentumisen muutos |

### saatavanOsuudenLajiCode

**7 values** · base `int` · Saatavan osuuden laji

*Used by:* `osuus.laji`, `saatava.osuudenLaji`, `saatavanOsuusType.laji`

| Value | Description |
|---|---|
| `1` | Täysimääräinen osuus |
| `2` | Rahamääräinen osuus |
| `3` | Rahamääräinen maksimiosuus |
| `4` | Rahamääräinen osuus pelkästään pääomaan |
| `5` | Yhteisvastuullinen osuus |
| `6` | Saatavakokonaisuuden rahamääräinen osuus |
| `7` | Saatavakokonaisuuden rahamääräinen maksimiosuus |

### taytantoonpanotapaCode

**2 values** · base `int` · Täytäntöönpanotapa

*Used by:* `velallinen.taytantoonpanotapa`, `muuMuutos.taytantoonpanoTapa`, `velallinenType.taytantoonpanotapa`

| Value | Description |
|---|---|
| `1` | Normaali ulosotto |
| `2` | Suppea ulosotto |

### viivastyskoronLajiCode

**31 values** · base `int` · Viivästyskoron laji

*Used by:* `viivastyskorkoTypeV1.laji`, `viivastyskorkoTypeV0.laji`, `viivastysKorko.laji`, `viivastysKorko.laji`, `viivastysKorkoType.laji`

| Value | Description |
|---|---|
| `1` | Aktia säästöpankki Oyj, primekorko |
| `2` | Svenska Handelsbanken Ab (publ), primekorko |
| `3` | Nordea Pankki Oyj, primekorko |
| `4` | Osuuspankkiryhmä (OKO), primekorko |
| `5` | Sampo pankki Oyj, primekorko |
| `6` | Säästöpankit, viitekorko |
| `7` | Ålandsbanken Åbp, primerkorko |
| `8` | Peruskorko |
| `9` | Ministeriön vahvistama viitekorko |
| `10` | Euribor, 1 kk |
| `11` | Euribor, 3 kk |
| `12` | Euribor, 6 kk |
| `13` | Euribor, 9 kk |
| `14` | Euribor, 12 kk |
| `15` | Veron viivästyskorko |
| `16` | Euroopan keskuspankin viitekorko |
| `17` | EKP, Euroopan keskuspankin viitekorko |
| `18` | Tapiola Pankki Oy |
| `19` | EQ Pankki Oy |
| `20` | Euribor 365, 1kk |
| `21` | Euribor 365, 3kk |
| `22` | Euribor 365, 6kk |
| `23` | Euribor 365, 9kk |
| `24` | Euribor 365, 12kk |
| `25` | Paikallisosuuspankit |
| `26` | SEB Gyllenberg Private Bank Oy |
| `27` | Hypo-konserni |
| `28` | S-Pankki |
| `29` | EKP + 8 / Euroopan keskuspankin viitekorko |
| `31` | TF Bank, primekorko |
| `32` | Perintöveron viivästyskorko |

### asianLiitetiedonLajiCode

**22 values** · base `int` · Asian liitetiedon laji

*Used by:* `liitetieto.laji`, `liitetieto.laji`, `liitetietoType.laji`

| Value | Description |
|---|---|
| `1` | Ulosottoperuste |
| `2` | Saamistodiste (juokseva). Juokseva velkakirja, joka on palautettava. |
| `3` | Valtakirja |
| `5` | Hakemuksen täydennys |
| `6` | Ulosottoasiaa koskeva muu asiakirja. Ei enää käytössä, korvataan lajilla 22: 'Muu hakemuksen liite' |
| `11` | Kuittauspyyntö |
| `12` | Lainvoimaisuustodistus |
| `15` | Osamaksusopimuksen laskelma |
| `16` | Osamaksusopimus |
| `17` | Muu osamaksutilityksen asiakirja |
| `19` | Siirtokirja |
| `21` | Kv-muutokset |
| `22` | Muu hakemuksen liite. Korvaa lajin 6: 'Ulosottoasiaa koskeva muu asiakirja' |
| `23` | Muutos |
| `24` | Peruutus |
| `25` | Tp-tavan muutos |
| `26` | Ruotsinkieliset muutokset |
| `28` | Osamaksukauppalain mukainen tilityspyyntö |
| `29` | TP-keskeytys/akordi |
| `31` | Saamistodiste (muu). Tavallinen velkakirja / sähköisesti allekirjoitettu velkakirja. |
| `33` | Pohjapiirros |
| `34` | Osakekirja |

### asianLisatiedonlajiCode

**31 values** · base `int` · Asian lisätiedon laji

*Used by:* `lisatietoType.laji`

| Value | Description |
|---|---|
| `3` | Lyhennystiedot |
| `4` | Sekalainen |
| `5` | Sama saatava eri päätös |
| `8` | Palkkasaatava erittely |
| `9` | Asian siirtomerkinnät |
| `17` | Vakuutuksen tiedot |
| `18` | Ajoneuvon tiedot |
| `19` | Maksuunpanon pvm |
| `20` | Maksun erittely |
| `21` | Kausi / viite |
| `22` | Maksumääräyksen pvm |
| `23` | Virheen paikka ja laatu |
| `25` | Kiinteistö |
| `26` | Pantti |
| `28` | Alkuperäinen viitetieto |
| `32` | Tekoaika / tapahtumapäivä |
| `38` | Vanhentumisen katkeamispäivä |
| `41` | Alkuperäinen velkoja |
| `43` | Aiempi uo-asianro |
| `44` | Asianimi |
| `45` | Maksuunpanoerittely |
| `46` | Saatavan siirto |
| `47` | Useita täytäntöönpanoperusteita |
| `49` | Viesti täytäntöönpanijalle |
| `50` | Häädön osoite ja huoltoyhtiö |
| `51` | Häädön Yhteyshenkilö |
| `52` | Lupapyyntö: arvoton tai vähäarvoinen omaisuus |
| `54` | Realisointipyyntö |
| `57` | Velkanumero/avoin saldo |
| `58` | Avoin saldo |
| `60` | Huoneistoa koskeva lisätieto |

### henkilolajiCode

**2 values** · base `int` · Henkilölaji

*Used by:* `velallinen.laji`, `hakija.laji`, `velkojaType.laji`, `velallinenType.laji`

| Value | Description |
|---|---|
| `1` | Luonnollinen henkilö |
| `2` | Juridinen henkilö |

### henkilotyyppiCode

**10 values** · base `int` · Henkilötyyppi

*Used by:* `velallinen.tyyppi`, `hakija.tyyppi`, `velkojaType.tyyppi`, `velallinenType.tyyppi`

| Value | Description |
|---|---|
| `1` | Luonnollinen henkilö |
| `2` | Elinkeinon harjoittaja |
| `3` | Osakeyhtiö |
| `4` | Valtio tai valtion laitos |
| `5` | Kunta, kuntayhtymä tai seurakunta |
| `6` | Kommandiittiyhtiö |
| `7` | Rekisteröity yhdistys |
| `8` | Säätiö |
| `9` | Kuolinpesä |
| `10` | Muu oikeushenkilö |

### kieliCode

**2 values** · base `int` · Kieli

*Used by:* `velallinen.kieli`, `hakija.kieli`

| Value | Description |
|---|---|
| `1` | Suomi |
| `2` | Ruotsi |

### kuntaCode

**456 values** · base `int` · Kunta

| Value | Description |
|---|---|
| `4` | Alahärmä |
| `5` | Alajärvi |
| `6` | Alastaro |
| `9` | Alavieska |
| `10` | Alavus |
| `15` | Artjärvi |
| `16` | Asikkala |
| `17` | Askainen |
| `18` | Askola |
| `19` | Aura |
| `20` | Akaa |
| `35` | Brändö |
| `40` | Dragsfjärd |
| `43` | Eckerö |
| `44` | Elimäki |
| `45` | Eno |
| `46` | Enonkoski |
| `47` | Enontekiö |
| `49` | Espoo |
| `50` | Eura |
| `51` | Eurajoki |
| `52` | Evijärvi |
| `60` | Finström |
| `61` | Forssa |
| `62` | Föglö |
| `65` | Geta |
| `69` | Haapajärvi |
| `71` | Haapavesi |
| `72` | Hailuoto |
| `73` | Halikko |
| `74` | Halsua |
| `75` | Hamina |
| `76` | Hammarland |
| `77` | Hankasalmi |
| `78` | Hanko |
| `79` | Harjavalta |
| `81` | Hartola |
| `82` | Hattula |
| `83` | Hauho |
| `84` | Haukipudas |
| `85` | Haukivuori |
| `86` | Hausjärvi |
| `90` | Heinävesi |
| `91` | Helsinki |
| `92` | Vantaa |
| `95` | Himanka |
| `97` | Hirvensalmi |
| `98` | Hollola |
| `99` | Honkajoki |
| `101` | Houtskari |
| `102` | Huittinen |
| `103` | Humppila |
| `105` | Hyrynsalmi |
| `106` | Hyvinkää |
| `108` | Hämeenkyrö |
| `109` | Hämeenlinna |
| `111` | Heinola |
| `139` | Ii |
| `140` | Iisalmi |
| `142` | Iitti |
| `143` | Ikaalinen |
| `145` | Ilmajoki |
| `146` | Ilomantsi |
| `148` | Inari |
| `149` | Inkoo |
| `150` | Iniö |
| `151` | Isojoki |
| `152` | Isokyrö |
| `153` | Imatra |
| `163` | Jaala |
| `164` | Jalasjärvi |
| `165` | Janakkala |
| `167` | Joensuu |
| `169` | Jokioinen |
| `170` | Jomala |
| `171` | Joroinen |
| `172` | Joutsa |
| `173` | Joutseno |
| `174` | Juankoski |
| `175` | Jurva |
| `176` | Juuka |
| `177` | Juupajoki |
| `178` | Juva |
| `179` | Jyväskylä |
| `180` | Jyväskylän mlk |
| `181` | Jämijärvi |
| `182` | Jämsä |
| `183` | Jämsänkoski |
| `186` | Järvenpää |
| `198` | Ei kotikuntaa Suomessa |
| `199` | Tuntematon |
| `200` | Ulkomaat |
| `202` | Kaarina |
| `204` | Kaavi |
| `205` | Kajaani |
| `208` | Kalajoki |
| `210` | Kalvola |
| `211` | Kangasala |
| `212` | Kangaslampi |
| `213` | Kangasniemi |
| `214` | Kankaanpää |
| `216` | Kannonkoski |
| `217` | Kannus |
| `218` | Karijoki |
| `219` | Karinainen |
| `220` | Karjaa |
| `223` | Karjalohja |
| `224` | Karkkila |
| `226` | Karstula |
| `227` | Karttula |
| `230` | Karvia |
| `231` | Kaskinen |
| `232` | Kauhajoki |
| `233` | Kauhava |
| `235` | Kauniainen |
| `236` | Kaustinen |
| `239` | Keitele |
| `240` | Kemi |
| `241` | Keminmaa |
| `243` | Kemiö |
| `244` | Kempele |
| `245` | Kerava |
| `246` | Kerimäki |
| `247` | Kestilä |
| `248` | Kesälahti |
| `249` | Keuruu |
| `250` | Kihniö |
| `251` | Kiihtelysvaara |
| `252` | Kiikala |
| `254` | Kiikoinen |
| `255` | Kiiminki |
| `256` | Kinnula |
| `257` | Kirkkonummi |
| `259` | Kisko |
| `260` | Kitee |
| `261` | Kittilä |
| `262` | Kiukainen |
| `263` | Kiuruvesi |
| `265` | Kivijärvi |
| `266` | Kodisjoki |
| `271` | Kokemäki |
| `272` | Kokkola |
| `273` | Kolari |
| `275` | Konnevesi |
| `276` | Kontiolahti |
| `277` | Korpilahti |
| `279` | Korppoo |
| `280` | Korsnäs |
| `281` | Kortesjärvi |
| `283` | Hämeenkoski |
| `284` | Koski Tl |
| `285` | Kotka |
| `286` | Kouvola |
| `287` | Kristiinankaupunki |
| `288` | Kruunupyy |
| `289` | Kuhmalahti |
| `290` | Kuhmo |
| `291` | Kuhmoinen |
| `292` | Kuivaniemi |
| `293` | Kullaa |
| `295` | Kumlinge |
| `297` | Kuopio |
| `300` | Kuortane |
| `301` | Kurikka |
| `303` | Kuru |
| `304` | Kustavi |
| `305` | Kuusamo |
| `306` | Kuusankoski |
| `308` | Kuusjoki |
| `309` | Outokumpu |
| `310` | Kylmäkoski |
| `312` | Kyyjärvi |
| `315` | Kälviä |
| `316` | Kärkölä |
| `317` | Kärsämäki |
| `318` | Kökar |
| `319` | Köyliö |
| `320` | Kemijärvi |
| `322` | Kemiönsaari |
| `398` | Lahti |
| `399` | Laihia |
| `400` | Laitila |
| `401` | Lammi |
| `402` | Lapinlahti |
| `403` | Lappajärvi |
| `405` | Lappeenranta |
| `406` | Lappi |
| `407` | Lapinjärvi |
| `408` | Lapua |
| `410` | Laukaa |
| `413` | Lavia |
| `414` | Lehtimäki |
| `415` | Leivonmäki |
| `416` | Lemi |
| `417` | Lemland |
| `418` | Lempäälä |
| `419` | Lemu |
| `420` | Leppävirta |
| `421` | Lestijärvi |
| `422` | Lieksa |
| `423` | Lieto |
| `424` | Liljendal |
| `425` | Liminka |
| `426` | Liperi |
| `429` | Lohtaja |
| `430` | Loimaa |
| `431` | Loimaan kunta |
| `433` | Loppi |
| `434` | Loviisa |
| `435` | Luhanka |
| `436` | Lumijoki |
| `438` | Lumparland |
| `439` | Luopioinen |
| `440` | Luoto |
| `441` | Luumäki |
| `442` | Luvia |
| `443` | Längelmäki |
| `444` | Lohja |
| `475` | Maalahti |
| `476` | Maaninka |
| `478` | Maarianhamina |
| `479` | Maksamaa |
| `480` | Marttila |
| `481` | Masku |
| `482` | Mellilä |
| `483` | Merijärvi |
| `484` | Merikarvia |
| `485` | Merimasku |
| `489` | Miehikkälä |
| `490` | Mietoinen |
| `491` | Mikkeli |
| `493` | Mouhijärvi |
| `494` | Muhos |
| `495` | Multia |
| `498` | Muonio |
| `499` | Mustasaari |
| `500` | Muurame |
| `501` | Muurla |
| `503` | Mynämäki |
| `504` | Myrskylä |
| `505` | Mäntsälä |
| `506` | Mänttä |
| `507` | Mäntyharju |
| `508` | Mänttä-Vilppula |
| `529` | Naantali |
| `531` | Nakkila |
| `532` | Nastola |
| `533` | Nauvo |
| `534` | Nilsiä |
| `535` | Nivala |
| `536` | Nokia |
| `537` | Noormarkku |
| `538` | Nousiainen |
| `540` | Nummi-Pusula |
| `541` | Nurmes |
| `543` | Nurmijärvi |
| `544` | Nurmo |
| `545` | Närpiö |
| `559` | Oravainen |
| `560` | Orimattila |
| `561` | Oripää |
| `562` | Orivesi |
| `563` | Oulainen |
| `564` | Oulu |
| `567` | Oulunsalo |
| `573` | Parainen |
| `576` | Padasjoki |
| `577` | Paimio |
| `578` | Paltamo |
| `580` | Parikkala |
| `581` | Parkano |
| `582` | Pattijoki |
| `583` | Pelkosenniemi |
| `584` | Perho |
| `585` | Pernaja |
| `586` | Perniö |
| `587` | Pertteli |
| `588` | Pertunmaa |
| `589` | Peräseinäjoki |
| `592` | Petäjävesi |
| `593` | Pieksämäki |
| `595` | Pielavesi |
| `598` | Pietarsaari |
| `599` | Pedersören kunta |
| `601` | Pihtipudas |
| `602` | Piikkiö |
| `603` | Piippola |
| `604` | Pirkkala |
| `606` | Pohja |
| `607` | Polvijärvi |
| `608` | Pomarkku |
| `609` | Pori |
| `611` | Pornainen |
| `614` | Posio |
| `615` | Pudasjärvi |
| `616` | Pukkila |
| `617` | Pulkkila |
| `618` | Punkaharju |
| `619` | Punkalaidun |
| `620` | Puolanka |
| `623` | Puumala |
| `624` | Pyhtää |
| `625` | Pyhäjoki |
| `626` | Pyhäjärvi |
| `630` | Pyhäntä |
| `631` | Pyhäranta |
| `632` | Pyhäselkä |
| `633` | Pylkönmäki |
| `635` | Pälkäne |
| `636` | Pöytyä |
| `638` | Porvoo |
| `640` | Pieksänmaa |
| `678` | Raahe |
| `680` | Raisio |
| `681` | Rantasalmi |
| `682` | Rantsila |
| `683` | Ranua |
| `684` | Rauma |
| `686` | Rautalampi |
| `687` | Rautavaara |
| `689` | Rautjärvi |
| `691` | Reisjärvi |
| `692` | Renko |
| `694` | Riihimäki |
| `696` | Ristiina |
| `697` | Ristijärvi |
| `698` | Rovaniemi |
| `699` | Rovaniemen mlk |
| `700` | Ruokolahti |
| `701` | Ruotsinpyhtää |
| `702` | Ruovesi |
| `704` | Rusko |
| `705` | Rymättylä |
| `707` | Rääkkylä |
| `708` | Ruukki |
| `710` | Raasepori |
| `728` | Saari |
| `729` | Saarijärvi |
| `730` | Sahalahti |
| `732` | Salla |
| `734` | Salo |
| `736` | Saltvik |
| `737` | Sammatti |
| `738` | Sauvo |
| `739` | Savitaipale |
| `740` | Savonlinna |
| `741` | Savonranta |
| `742` | Savukoski |
| `743` | Seinäjoki |
| `746` | Sievi |
| `747` | Siikainen |
| `748` | Siikajoki |
| `749` | Siilinjärvi |
| `751` | Simo |
| `753` | Sipoo |
| `754` | Anjalankoski |
| `755` | Siuntio |
| `758` | Sodankylä |
| `759` | Soini |
| `761` | Somero |
| `762` | Sonkajärvi |
| `765` | Sotkamo |
| `766` | Sottunga |
| `768` | Sulkava |
| `770` | Sumiainen |
| `771` | Sund |
| `772` | Suodenniemi |
| `774` | Suolahti |
| `775` | Suomenniemi |
| `776` | Suomusjärvi |
| `777` | Suomussalmi |
| `778` | Suonenjoki |
| `781` | Sysmä |
| `783` | Säkylä |
| `784` | Särkisalo |
| `785` | Vaala |
| `790` | Sastamala |
| `791` | Siikalatva |
| `831` | Taipalsaari |
| `832` | Taivalkoski |
| `833` | Taivassalo |
| `834` | Tammela |
| `835` | Tammisaari |
| `837` | Tampere |
| `838` | Tarvasjoki |
| `844` | Tervo |
| `845` | Tervola |
| `846` | Teuva |
| `848` | Tohmajärvi |
| `849` | Toholampi |
| `850` | Toivakka |
| `851` | Tornio |
| `853` | Turku |
| `854` | Pello |
| `855` | Tuulos |
| `856` | Tuupovaara |
| `857` | Tuusniemi |
| `858` | Tuusula |
| `859` | Tyrnävä |
| `863` | Töysä |
| `864` | Toijala |
| `885` | Ullava |
| `886` | Ulvila |
| `887` | Urjala |
| `889` | Utajärvi |
| `890` | Utsjoki |
| `891` | Uukuniemi |
| `892` | Uurainen |
| `893` | Uusikaarlepyy |
| `895` | Uusikaupunki |
| `905` | Vaasa |
| `906` | Vahto |
| `908` | Valkeakoski |
| `909` | Valkeala |
| `911` | Valtimo |
| `912` | Vammala |
| `913` | Vampula |
| `915` | Varkaus |
| `916` | Varpaisjärvi |
| `917` | Vehkalahti |
| `918` | Vehmaa |
| `919` | Vehmersalmi |
| `920` | Velkua |
| `921` | Vesanto |
| `922` | Vesilahti |
| `923` | Västanfjärd |
| `924` | Veteli |
| `925` | Vieremä |
| `926` | Vihanti |
| `927` | Vihti |
| `928` | Viiala |
| `931` | Viitasaari |
| `932` | Viljakkala |
| `933` | Vilppula |
| `934` | Vimpeli |
| `935` | Virolahti |
| `936` | Virrat |
| `940` | Vuolijoki |
| `941` | Vårdö |
| `942` | Vähäkyrö |
| `943` | Värtsilä |
| `944` | Vöyri |
| `971` | Ylihärmä |
| `972` | Yli-Ii |
| `973` | Ylikiiminki |
| `975` | Ylistaro |
| `976` | Ylitornio |
| `977` | Ylivieska |
| `978` | Ylämaa |
| `979` | Yläne |
| `980` | Ylöjärvi |
| `981` | Ypäjä |
| `988` | Äetsä |
| `989` | Ähtäri |
| `992` | Äänekoski |
| `945` | Vöyri-Maksamaa |

### liitteenSaapumistapaCode

**2 values** · base `int` · Liitteen saapumistapa

*Used by:* `liitetieto.saapumistapa`, `liitetietoType.saapumistapa`

| Value | Description |
|---|---|
| `1` | Manuaalinen |
| `2` | Sähköinen |

### maaCode

**255 values** · base `int` · Maa

*Used by:* `osoiteType.maa`, `osoiteType.maa`

| Value | Description |
|---|---|
| `1` | Suomi |
| `2` | Ruotsi |
| `3` | Norja |
| `4` | Tanska |
| `5` | Islanti |
| `10` | Irlanti |
| `11` | Yhdistynyt kuningaskunta |
| `20` | Alankomaat |
| `21` | Belgia |
| `22` | Itävalta |
| `23` | Liechtenstein |
| `24` | Luxemburg |
| `25` | Saksa |
| `26` | Monaco |
| `27` | Ranska |
| `28` | Sveitsi |
| `40` | Albania |
| `41` | Andorra |
| `42` | Espanja |
| `43` | Italia |
| `45` | Kreikka |
| `46` | Malta |
| `47` | Portugali |
| `48` | San Marino |
| `49` | Vatikaani |
| `50` | Kroatia |
| `51` | Slovenia |
| `52` | Bosnia ja Hertsegovina |
| `53` | Pohjois-Makedonia |
| `54` | Jugoslavian liittotasavalta |
| `60` | Bulgaria |
| `62` | Puola |
| `63` | Romania |
| `65` | Unkari |
| `66` | Slovakia |
| `67` | Tsekki |
| `71` | Viro |
| `72` | Latvia |
| `73` | Liettua |
| `100` | Benin |
| `101` | Gambia |
| `102` | Ghana |
| `103` | Guinea |
| `104` | Liberia |
| `105` | Mali |
| `106` | Mauritania |
| `107` | Niger |
| `108` | Nigeria |
| `109` | Norsunluurannikko |
| `110` | Senegal |
| `111` | Sierra Leone |
| `112` | Togo |
| `113` | Burkina Faso |
| `114` | Guinea-Bissau |
| `115` | Kap Verde |
| `120` | Burundi |
| `121` | Etiopia |
| `122` | Kenia |
| `123` | Madagaskar |
| `124` | Malawi |
| `125` | Mauritius |
| `126` | Zimbabwe |
| `127` | Ruanda |
| `128` | Sambia |
| `129` | Somalia |
| `130` | Tansania |
| `131` | Uganda |
| `132` | Mosambik |
| `133` | Komorit |
| `134` | Seychellit |
| `135` | Djibouti |
| `136` | Eritrea |
| `140` | Algeria |
| `141` | Libya |
| `142` | Marokko |
| `143` | Sudan |
| `144` | Tunisia |
| `145` | Egypti |
| `160` | Gabon |
| `161` | Kamerun |
| `162` | Keski-Afrikan tasavalta |
| `163` | Kongo (Kongo-Kinshasa) |
| `164` | Kongo (Kongo-Brazzaville) |
| `165` | Päiväntasaajan Guinea |
| `166` | Tsad |
| `167` | Angola |
| `168` | São Tomé ja Príncipe |
| `180` | Etelä-Afrikka |
| `181` | Botswana |
| `182` | Lesotho |
| `183` | Eswatini |
| `194` | Namibia |
| `210` | Kanada |
| `220` | Yhdysvallat (USA) |
| `300` | Bolivia |
| `301` | Brasilia |
| `302` | Ecuador |
| `303` | Guyana |
| `304` | Kolumbia |
| `305` | Peru |
| `306` | Venezuela |
| `307` | Suriname |
| `320` | Costa Rica |
| `321` | Guatemala |
| `322` | Honduras |
| `323` | Meksiko |
| `324` | Nicaragua |
| `325` | Panama |
| `326` | El Salvador |
| `340` | Argentiina |
| `341` | Chile |
| `342` | Paraguay |
| `343` | Uruguay |
| `360` | Barbados |
| `361` | Dominikaaninen tasavalta |
| `362` | Haiti |
| `363` | Jamaika |
| `364` | Kuuba |
| `365` | Trinidad ja Tobago |
| `366` | Bahama |
| `367` | Grenada |
| `368` | Dominica |
| `369` | Saint Lucia |
| `370` | Saint Vincent ja Grenadiinit |
| `381` | Antigua ja Barbuda |
| `383` | Belize |
| `393` | Saint Kitts ja Nevis |
| `400` | Kiina |
| `410` | Mongolia |
| `430` | Japani |
| `450` | Korean tasavalta (Etelä-Korea) |
| `452` | Korean demokraattinen kansantasavalta (Pohjois-Korea) |
| `500` | Afganistan |
| `501` | Bhutan |
| `502` | Sri Lanka |
| `503` | Intia |
| `504` | Iran |
| `505` | Malediivit |
| `506` | Nepal |
| `507` | Pakistan |
| `508` | Bangladesh |
| `530` | Myanmar |
| `532` | Filippiinit |
| `533` | Indonesia |
| `534` | Kambodza |
| `535` | Laos |
| `536` | Malesia |
| `537` | Vietnam |
| `538` | Singapore |
| `539` | Thaimaa |
| `560` | Bahrain |
| `562` | Irak |
| `563` | Israel |
| `565` | Jordania |
| `566` | Qatar |
| `567` | Kuwait |
| `568` | Kypros |
| `569` | Libanon |
| `570` | Oman |
| `571` | Saudi-Arabia |
| `572` | Syyria |
| `573` | Turkki |
| `574` | Arabiemiirikunnat |
| `575` | Jemen |
| `591` | Brunei |
| `600` | Australia |
| `610` | Uusi-Seelanti |
| `611` | Papua-Uusi-Guinea |
| `620` | Salomonsaaret |
| `650` | Fidzi |
| `651` | Samoa |
| `652` | Nauru |
| `653` | Tonga |
| `654` | Tuvalu |
| `655` | Kiribati |
| `686` | Vanuatu |
| `693` | Marshallinsaaret |
| `701` | Venäjä |
| `702` | Armenia |
| `703` | Azerbaidzan |
| `704` | Kazakstan |
| `705` | Kirgisia |
| `706` | Moldova |
| `707` | Tadzikistan |
| `708` | Turkmenistan |
| `709` | Ukraina |
| `710` | Uzbekistan |
| `711` | Valko-Venäjä |
| `712` | Georgia |
| `713` | Antarktis |
| `714` | Amerikan Samoa |
| `715` | Bermuda |
| `716` | Bouvet'nsaari |
| `717` | Brittiläinen Intian valtameren alue |
| `718` | Brittiläiset Neitsytsaaret |
| `719` | Joulusaari |
| `720` | Kookossaaret |
| `721` | Mayotte |
| `722` | Cookinsaaret |
| `723` | Färsaaret |
| `724` | Falklandinsaaret |
| `725` | Etelä-Georgia ja Eteläiset Sandwichsaaret |
| `726` | Ahvenanmaa |
| `727` | Ranskan Guayana |
| `728` | Ranskan Polynesia |
| `729` | Ranskan eteläiset alueet |
| `730` | Palestiinan valtio |
| `731` | Gibraltar |
| `732` | Grönlanti |
| `733` | Guadeloupe |
| `734` | Guam |
| `735` | Heard ja McDonaldinsaaret |
| `736` | Hongkong |
| `737` | Macao |
| `738` | Martinique |
| `739` | Montserrat |
| `740` | Curaçao |
| `741` | Aruba |
| `742` | Sint Maarten (Alankomaiden osa) |
| `743` | Bonaire, Sint Eustatius ja Saba |
| `744` | Uusi-Kaledonia |
| `745` | Niue |
| `746` | Norfolkinsaari |
| `747` | Pohjois-Mariaanit |
| `748` | Yhdysvaltain pienet erillissaaret |
| `749` | Mikronesia |
| `750` | Palau |
| `751` | Pitcairn |
| `752` | Itä-Timor |
| `753` | Puerto Rico |
| `754` | Réunion |
| `755` | Saint Barthélemy |
| `756` | Saint Helena |
| `757` | Anguilla |
| `758` | Saint Martin (Ranskan osa) |
| `759` | Saint-Pierre ja Miquelon |
| `760` | Etelä-Sudan |
| `761` | Länsi-Sahara |
| `762` | Svalbard ja Jan Mayen |
| `763` | Tokelau |
| `764` | Turks- ja Caicossaaret |
| `765` | Jersey |
| `766` | Yhdysvaltain Neitsytsaaret |
| `767` | Wallis ja Futuna |
| `991` | Valtioton |
| `997` | Ei vielä selvitetty |
| `998` | Tieto selväkielisenä |
| `999` | Tuntematon |
| `1000` | Kosovo |
| `1001` | Serbia |
| `1002` | Caymansaaret |
| `1003` | Montenegro |
| `1004` | Guernsey |
| `1005` | Mansaari |
| `1006` | Taiwan |

### kyllaEiCode

**2 values** · base `int` · Kyllä/Ei koodisto

*Used by:* `osoiteType.luovutuskielto`, `hakemus.saatavatMuuttuneet`, `asia.passiiviperintapyynto`, `tuomionSisalto.haastekielto`, `viivastysKorko.valvonta`, `viivastysKorko.korkokatto10prosenttia`, `viivastysKorko.korkokattoEKP15`, `velallinen.eiLainvoimainen`, `velallinen.tiedoksiantopyynto`, `elatusasia.viivastyskorkoPyydetty`, `maksumuutos.poikkeavaKohd`, `muuMuutos.passiiviperintapyynto` … (+5)

| Value | Description |
|---|---|
| `1` | Kyllä |
| `2` | Ei |

### paatosLiitteenaCode

**4 values** · base `int` · Päätös liitteenä (= Tp-perusteen liitteen laji)

*Used by:* `taytantoonpanonPerusteTypeV1.paatosLiitteena`, `taytantoonpanonPeruste.paatosLiitteena`, `taytantoonpanonPeruste.paatosLiitteena`, `taytantoonpanonPerusteType.paatosLiitteena`

| Value | Description |
|---|---|
| `1` | Sähköinen |
| `2` | Paperilla |
| `3` | Tuomiorekisteri |
| `4` | AIPA |

### sukupuoliCode

**2 values** · base `int` · Sukupuoli

*Used by:* `velallinen.sukupuoli`, `hakija.sukupuoli`

| Value | Description |
|---|---|
| `1` | Nainen |
| `2` | Mies |

### tietolahdeCode

**2 values** · base `int` · Tietolähde

*Used by:* `hennimiType.tietolahde`, `osoiteType.osoitteenTietolahde`

| Value | Description |
|---|---|
| `1` | Hakija |
| `6` | Muu |

### taytantoonpanoperusteenMaaraaikaCode

**2 values** · base `int` · Täytäntöönpanoperusteen määräaika

*Used by:* `taytantoonpanonPerusteTypeV0.maaraaika`, `taytantoonpanonPerusteTypeV1.maaraaika`, `maaraaika.maaraaikaVuosiKdi`, `taytantoonpanonPeruste.maaraaika`, `taytantoonpanonPerusteType.maaraaika`, `taytantoonpanoperuste.maaraaika`

| Value | Description |
|---|---|
| `1` | 15 vuotta |
| `2` | 20 vuotta |

### täytäntöönpanotapaCode

**3 values** · base `int` · Täytäntöönpanotapa

| Value | Description |
|---|---|
| `1` | Normaali ulosotto |
| `2` | Suppea ulosotto |
| `3` | Vain veronpalautusperintä |

### valtakirjanLajiCode

**2 values** · base `int` · Valtakirjan laji

| Value | Description |
|---|---|
| `1` | Tilitysvaltakirja |
| `2` | Muu valtakirja |

### valtuutuksenLaajuusCode

**2 values** · base `int` · Valtuutuksen laajuus

| Value | Description |
|---|---|
| `1` | Asiakohtainen |
| `2` | Hakijakohtainen |

### valuuttaCode

**181 values** · base `int` · Valuutta

*Used by:* `saatavanPerustiedotTypeV0.valuutta`, `saatava.valuutta`, `elatusasia.valuutta`, `saatavanPerustiedotType.valuutta`, `elatusasiaType.valuutta`

| Value | Description |
|---|---|
| `1` | Itävallan shillinki |
| `2` | Belgian frangi |
| `3` | Kanadan dollari |
| `4` | Sveitsin frangi |
| `5` | Kyproksen punta |
| `6` | Tsekin koruna |
| `7` | Saksan markka |
| `8` | Tanskan kruunu |
| `9` | Viron kruunu |
| `10` | Espanjan peseta |
| `11` | Euro |
| `12` | Suomen markka |
| `13` | Ranskan frangi |
| `14` | Iso-Britannian punta |
| `15` | Kreikan drakma |
| `16` | Unkarin forintti |
| `17` | Irlannin punta |
| `18` | Islannin kruunu |
| `19` | Italian liira |
| `20` | Japanin jeni |
| `21` | Liettuan liti |
| `22` | Latvian lati |
| `23` | Maltan liira |
| `24` | Hollannin gulden |
| `25` | Norjan kruunu |
| `26` | Puolan zloty |
| `27` | Portugalin escudo |
| `28` | Venäjän rupla |
| `29` | Ruotsin kruunu |
| `30` | Singaporen dollari |
| `31` | Slovakian koruna |
| `32` | Turkin liira |
| `33` | USAn dollari |
| `34` | Etelä-Afrikan randi |
| `35` | Arabiemiirikuntien dirhami |
| `36` | AFA |
| `37` | afgaani |
| `38` | lek |
| `39` | dram |
| `40` | Alankomaiden Antillien guldeni |
| `41` | kwanza |
| `42` | Argentiinan peso |
| `43` | Australian dollari |
| `44` | Aruban guldeni |
| `45` | Azerbaidžanin manat |
| `46` | Bosnian vaihdettava markka |
| `47` | Barbadosin dollari |
| `48` | taka |
| `49` | leva |
| `50` | Bahrainin dinaari |
| `51` | Burundin frangi |
| `52` | Bermudan dollari |
| `53` | Brunein dollari |
| `54` | boliviano |
| `55` | real |
| `56` | Bahaman dollari |
| `57` | ngultrum |
| `58` | pula |
| `59` | Valko-Venäjän rupla |
| `60` | Belizen dollari |
| `61` | Kongon frangi |
| `62` | Chilen peso |
| `63` | juan renminbi |
| `64` | Kolumbian peso |
| `65` | Costa Rican colon |
| `66` | Kuuban peso |
| `67` | Kap Verden escudo |
| `68` | Djiboutin frangi |
| `69` | Dominikaanisen tasavallan peso |
| `70` | Algerian dinaari |
| `71` | Egyptin punta |
| `72` | nakfa |
| `73` | Etiopian birr |
| `74` | Fidžin dollari |
| `75` | Falklandinsaarten punta |
| `76` | lari |
| `77` | cedi |
| `78` | Gibraltarin punta |
| `79` | dalasi |
| `80` | Guinean frangi |
| `81` | quetzal |
| `82` | Guyanan dollari |
| `83` | Hongkongin dollari |
| `84` | lempira |
| `85` | kuna |
| `86` | gourde |
| `87` | Indonesian rupia |
| `88` | uusi sekeli |
| `89` | Intian rupia |
| `90` | Irakin dinaari |
| `91` | Iranin rial |
| `92` | Jamaikan dollari |
| `93` | Jordanian dinaari |
| `94` | Kenian šillinki |
| `95` | som |
| `96` | riel |
| `97` | Komorien frangi |
| `98` | KOR |
| `99` | KOX |
| `100` | Pohjois-Korean won |
| `101` | Etelä-Korean won |
| `102` | Kuwaitin dinaari |
| `103` | Caymansaarten dollari |
| `104` | tenge |
| `105` | kip |
| `106` | Libanonin punta |
| `107` | Sri Lankan rupia |
| `108` | Liberian dollari |
| `109` | loti |
| `110` | Luxemburgin f |
| `111` | Libyan dinaari |
| `112` | Marokon dirhami |
| `113` | Moldovan leu |
| `114` | Madagaskarin frangi |
| `115` | denar |
| `116` | kyat |
| `117` | tugrik |
| `118` | pataca |
| `119` | ouguija |
| `120` | Mauritiuksen rupia |
| `121` | Malawin kwacha |
| `122` | rufiyaa |
| `123` | Meksikon peso |
| `124` | ringgit |
| `125` | metical |
| `126` | Namibian dollari |
| `127` | naira |
| `128` | cordoba |
| `129` | Nepalin rupia |
| `130` | Uuden-Seelannin dollari |
| `131` | Omanin rial |
| `132` | PAB |
| `133` | uusi sol |
| `134` | kina |
| `135` | Filippiinien peso |
| `136` | Pakistanin rupia |
| `137` | guarani |
| `138` | Qatarin rial |
| `139` | Romanian leu |
| `140` | Ruandan frangi |
| `141` | Saudi-Arabian rial |
| `142` | Salomonsaarten dollari |
| `143` | Seychellien rupia |
| `144` | Sudanin dinaari |
| `145` | St. Helenan punta |
| `146` | tolar |
| `147` | leone |
| `148` | Somalian šillinki |
| `149` | Surinamin guldeni |
| `150` | dobra |
| `151` | SVC |
| `152` | Syyrian punta |
| `153` | lilangeni |
| `154` | baht |
| `155` | somoni |
| `156` | Turkmenistanin manat |
| `157` | Tunisian dinaari |
| `158` | pa'anga |
| `159` | Trinidadin ja Tobagon dollari |
| `160` | uusi Taiwanin dollari |
| `161` | Tansanian šillinki |
| `162` | grivna |
| `163` | UBF |
| `164` | Ugandan šillinki |
| `165` | Uruguayn peso |
| `166` | sum |
| `167` | bolivar |
| `168` | dong |
| `169` | tala |
| `170` | vatu |
| `171` | CFA-frangi BEAC |
| `172` | XAU |
| `173` | Itä-Karibian dollari |
| `174` | XDR |
| `175` | CFA-frangi BCEAO |
| `176` | XYP |
| `177` | CFP-frangi |
| `178` | Jemenin rial |
| `179` | dinaari (Serbiassa) |
| `180` | Sambian kwacha |
| `181` | Zimbabwen dollari |

### velallisenLisatiedonLajiCode

**15 values** · base `int` · Velallisen lisätiedon laji

*Used by:* `velallisenLisatietoType.laji`

| Value | Description |
|---|---|
| `1` | Ammatti |
| `2` | Holhooja |
| `3` | Huollettavat |
| `4` | Konkurssipesänhoitaja |
| `5` | Kuolinpesänhoitaja |
| `6` | Omaisuus (varallisuus) |
| `7` | Puhelinnumero |
| `8` | Sekalainen |
| `9` | Siviilisääty |
| `10` | Tilikausi |
| `11` | Verottajan ilmoittama työnantaja/Työnantaja (osoite, tunnus, palkkasumma = verottajan ilm. asian lisätieto) |
| `12` | Yhtiömuoto |
| `13` | Verottajan ilmoittama lainatieto |
| `14` | Verottajan ilmoittama asianhoitaja |
| `15` | Poissaolo |

### velallistilityksenTyyppiCode

**3 values** · base `int` · Velallistilityksen tyyppi

*Used by:* `velalliserittely.velallistilityksenTyyppi`

| Value | Description |
|---|---|
| `1` | Peruutettuna |
| `2` | Esteellisenä |
| `3` | Maksettuna |

### asianVelallisenTilaCode

**9 values** · base `int` · Asian velallisen tila

*Used by:* `velalliserittely.asianVelallisenTila`

| Value | Description |
|---|---|
| `1` | Kirjattavana |
| `4` | Täytäntöönpanossa |
| `5` | Tilitettävänä maksettuna |
| `6` | Tilitettävänä peruutettuna |
| `8` | Tilitettävänä esteellisenä |
| `9` | Valmiina maksettuna |
| `10` | Valmiina peruutettuna |
| `11` | Valmiina esteellisenä |
| `12` | Siirrettynä passiiviperintään |

### henkilonRooliCode

**8 values** · base `int` · Henkilön rooli

*Used by:* `vastaanottaja.rooli`

| Value | Description |
|---|---|
| `1` | Velallinen |
| `2` | Hakija |
| `3` | Asiamies |
| `4` | Toimeentuloetuuden maksaja |
| `5` | Veronpalautuksen maksaja |
| `6` | Maksukiellon saaja |
| `7` | Varattomuustietojen vastaanottaja |
| `8` | Muu ulosoton asiakas |

### siirtoilmoituksenLajiCode

**3 values** · base `int` · Siirtoilmoituksen laji

| Value | Description |
|---|---|
| `1` | Asian siirto |
| `2` | Asian siirto päävelallisen siirrossa |
| `3` | Velallisen siirto |

### ulosmittauksenLajiCode

**16 values** · base `int` · Ulosmittauksen laji

| Value | Description |
|---|---|
| `1` | Kiinteistö |
| `2` | Määräala |
| `3` | Laitos |
| `4` | Erityinen oikeus |
| `5` | Asunto-osake |
| `6` | Ajoneuvo |
| `7` | Arvo-osuus |
| `8` | Kuolinpesän osuus |
| `9` | Muu omaisuuden ulosmittaus |
| `10` | Irtain |
| `11` | Saatava |
| `12` | Palkka |
| `13` | Eläke |
| `14` | Elinkeinotulo |
| `15` | Toimeentuloetuus |
| `16` | Veronpalautus |

### tunnistautumismenetelmaCode

**3 values** · base `int` · Tunnistautumismenetelmä

| Value | Description |
|---|---|
| `1` | VETUMA |
| `2` | Yhteisötunnistautuminen |
| `3` | KATSO |

### maksukiellonPidatyksenLajiCode

**5 values** · base `int` · Maksukiellon pidätyksen laji

*Used by:* `maksukieltoTaiMuutos.pidatyksenLaji`

| Value | Description |
|---|---|
| `1` | Normaalipidätys |
| `2` | Pidätys vähintään |
| `3` | Pidätys enintään |
| `4` | Kertapidätys |
| `5` | Normaalipidätys + elatusapu |

### maksukiellonVoimassaolonLajiCode

**3 values** · base `int` · Maksukiellon voimassaolon laji

*Used by:* `maksukieltoTaiMuutos.voimassaolonLaji`

| Value | Description |
|---|---|
| `1` | Toistaiseksi |
| `2` | Lakkaa kun kertapidätys tilitetään virastolle |
| `3` | Voimassaolon päättymispäivä tiedetään |

### maksukiellonPeruuttaminenCode

**9 values** · base `int` · Maksukiellon peruuttaminen

*Used by:* `palautuksenTiedot.palautuksenSyy`

| Value | Description |
|---|---|
| `1` | Ei käytössä |
| `2` | Ei käytössä |
| `3` | Ei käytössä |
| `4` | Ei käytössä |
| `5` | Muu syy |
| `6` | Velallinen ei ole ollut palveluksessamme |
| `7` | Velallinen ei ole enää palveluksessamme |
| `8` | Velallinen ei saa meiltä eläkettä/päivärahaa |
| `9` | Velallisen palkka/eläke/muu toistuvaistulo ei nouse yli suojaosuuden |

### velallisenToimenpideCode

**22 values** · base `int` · Velallisen toimenpide

| Value | Description |
|---|---|
| `1` | Kehotus |
| `2` | Maksusuunnitelma |
| `3` | Palkan tai etuuden ulosmittaus |
| `4` | Veronpalautuksen ulosmittaus |
| `5` | Maksukielto |
| `6` | Este |
| `7` | Velkajärjestely |
| `8` | Yrityssaneeraus |
| `9` | Siirto |
| `10` | Omaisuuden ulosmittaus |
| `11` | Haaste muuntomenettelyyn |
| `12` | Vapaakuukausipäätös |
| `13` | Vapautus toistuvaistulon taulukkomaksusta |
| `14` | Elinkeinotulon ulosmittaus |
| `15` | Ulosmittauksen määrän rajoittamispäätös |
| `16` | Ulosmittauksen lykkäyspäätös |
| `17` | Omaisuuden takavarikko |
| `18` | Itseoikaisu |
| `19` | Muu toimenpide |
| `20` | Velallisen vastuun vaihto |
| `21` | Myynti |
| `22` | Valitus |

### paaomasaatavannimiCode

**5 values** · base `int` · Pääomasaatavan nimi

| Value | Description |
|---|---|
| `1` | Saaminen |
| `2` | Sakko |
| `3` | Sakon korotus |
| `4` | Muunnetut sakot |
| `5` | Rikesakko |

### muutoksenTilaCode

**4 values** · base `int` · Sähköisen muutoksen tila

*Used by:* `muutos.muutoksenTila`

| Value | Description |
|---|---|
| `1` | Sovellusvirhe |
| `2` | Hyväksytty |
| `3` | Hylätty |
| `4` | Selvityksessä |

### ulosottorekisterinTulosteenLajiCode

**9 values** · base `int` · Ulosottorekisterin tulosteen laji

| Value | Description |
|---|---|
| `1` | Todistus ulosottorekisteristä |
| `2` | Todistus ulosottorekisteristä 4v |
| `3` | Tuloste rekisteripyynnöistä |
| `4` | Asianosaistuloste asiakohtainen |
| `5` | Asianosaistuloste velalliskohtainen |
| `6` | Varattomuustodistus ilman vireillapanoa |
| `7` | Määräaikaisilmoitus |
| `8` | Asianosaistuloste velalliskohtainen taannehtivalle päivälle |
| `9` | Henkilötietotuloste |

### vapaakuukausipaatoksenPerusteCode

**10 values** · base `int` · Vapaakuukausipäätöksen peruste

| Value | Description |
|---|---|
| `1` | Asumis- ja elinkustannukset |
| `2` | Erityinen syy |
| `3` | Elatusapu |
| `4` | Alle vuosi |
| `5` | Enintään |
| `6` | Alhaiset kustannukset |
| `7` | Muut kustannukset |
| `8` | Erityinen syy |
| `9` | Elatusapu |
| `10` | Muu syy |

### rajoittamispaatoksenPerusteCode

**4 values** · base `int` · Rajoittamispäätöksen peruste

| Value | Description |
|---|---|
| `1` | Sairaus |
| `2` | Työttömyys |
| `3` | Maksettava elatusapu |
| `4` | Erityinen syy |

### kuluttajaluottolainSopimuskoodiCode

**3 values** · base `int` · Kuluttajaluottolain mukainen sopimus

*Used by:* `viivastyskorkoTypeV1.kuluttajaluottolainSopimuskoodi`, `viivastysKorko.kuluttajaluottosopimusTehtyKdi`

| Value | Description |
|---|---|
| `1` | Sopimus tehty ennen 1.2.2010 |
| `2` | Sopimus tehty 1.2.2010 - 31.8.2019 |
| `3` | Sopimus tehty 1.9.2019 tai myöhemmin |

### taytantoonpanoperusteenMuutosTyyppiCode

**2 values** · base `int` · Täytäntöönpanoperusteen muutoksen tyyppi

*Used by:* `taytantoonpanonPerusteenMuutos.tyyppi`

| Value | Description |
|---|---|
| `1` | Lisäys |
| `2` | Muutos |
