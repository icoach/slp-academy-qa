<p>Responzivní třídy | solidpixels academy</p>
<p>Menu</p>
<p>cs en</p>
<p>BlogVše Inspirace Návody Případové studie Rozhovory OborySlužby Gastronomie Hotely Ambasadoři NápovědaZačínáme se solidpixels Základní bloky Pokročilé bloky Design Funkce Nastavení webu Inovace Video návody</p>
<p>Vyhledávání</p>
<p>Začít zdarma</p>
<p>cs en</p>
<p>Návody
Responzivní třídy
9 minutObsah článku</p>
<p>Skrývání obsahu podle rozlišení
Obsah pro určitý typ zařízení
Otočení obsahu sekce na mobilu
Galerie a výpisy
Zalomení vnořeného gridu
Zarovnání textu
Formuláře
Sekce s preferovaným sloupcem
Dřívější "rozbití" gridu</p>
<p>Responzivní třídy jsou určené k menším zásahům do obsahu, za účelem dosažení lepšího zobrazení na různých typech zařízení. Třídy se aplikují v pokročilém nastavní sekcí nebo bloků.
Skrývání obsahu pro určitý typ zařízení (2.51+)
Jsou situace, kdy chcete zobrazit speciální obsah pouze na určitém typu zařízení. Za tímto účelem jsou v připravené následující třídy, které toto omezení umožňují:</p>
<p>Název třídy
Popis</p>
<p>hide-sm
skryje obsah na rozlišení do 719px</p>
<p>hide-md
skryje obsah od 720px - 860px</p>
<p>hide-ml
skryje obsah od 860px - 992px</p>
<p>hide-lg
skryje obsah od 993px - 1200px</p>
<p>hide-xl
skryje obsah od 1201px - 1440px</p>
<p>hide-xxl
skryje obsah od 1441px - 1800px</p>
<p>hide-hg
skryje obsah na rozlišení od 1801px</p>
<p>hide-nav-sm
skryje obsah na rozlišeních s mobilní hlavičkou</p>
<p>hide-nav-lg
skryje obsah na rozlišeních s desktopovou hlavičkou</p>
<p>V administraci se obsah zobrazí vždy aby jej bylo možné editovat, správné použití třídy je tedy vidět až na frontendu.
Pozn. pro vývojáře: u tříd zmíněných výše se používají breakpointy @screen-md, @screen-lg a jejich "max" varianty.</p>
<p>Tip: Třída se nemusí nutně používat pouze na sekce
Třídu lze použít na sekce i samotné bloky.</p>
<p>Pozor!
Duplikací obsahu můžete porušit některé SEO pravidla – například dva nadpisy H1 na stránce. Třídy je dobré používat tak, aby obsah nebyl duplikován.
Zobrazení obsahu pro určitý typ zařízení
Jsou situace, kdy chcete zobrazit speciální obsah pouze na určitém typu zařízení. Za tímto účelem jsou v připravené následující třídy, které toto omezení umožňují:</p>
<p>Od verze 2.51 prosím používejte třídy pro skrývání obsahu z našeptávače tříd.</p>
<p>Název třídy
Popis</p>
<p>only-mobile
zobrazí obsah pouze na mobilu</p>
<p>only-mobile-tablet
zobrazí obsah pouze na mobilu a tabletu</p>
<p>only-tablet
zobrazí obsah pouze na tabletu</p>
<p>only-tablet-desktop
zobrazí obsah pouze na tabletu a desktopu</p>
<p>only-desktop
zobrazí obsah pouze na desktopu</p>
<p>Třídy lze použít na sekce i na běžné bloky. Zobrazení obsahu se určuje podle rozlišení, nikoliv podle zařízení na kterém se na web koukáme, může nastat situace kdy například tablet má větší rozlišení než je běžné a bude brán jako desktop a zobrazí se mu obsah pro desktop.
V administraci se obsah zobrazí vždy, správné použití třídy je tedy vidět až na frontendu.
Pozn. pro vývojáře: u tříd zmíněných výše se používají breakpointy @screen-md, @screen-lg a jejich "max" varianty.</p>
<p>Tip: Třída se nemusí nutně používat pouze na sekce
Třídu lze použít na sekce i samotné bloky.</p>
<p>Pozor!
Duplikací obsahu můžete porušit některé SEO pravidla – například dva nadpisy H1 na stránce. Třídy je dobré používat tak, aby obsah nebyl duplikován.
Změna pořadí prvků na mobilu
Na mobilu občas potřebujeme vyměnit pořadí prvků v layoutu který máme na desktopu/tabletu. Například na webu používáme layout "cik-cak" kdy měníme pořadí obrázku a textu mezi sekcemi/řádky.  Na mobilu kde je lineární layout (vše pod sebou) by se ale zobrazil "obrázek, text, text,obrázek" což nechceme. Můžeme tedy použít třídy, only-mobile a only-tablet-desktop, mnohem lepší řešení je ale použít grid třídy které se vloží na sekci.</p>
<p>Název třídy
Popis</p>
<p>grid-reverse
zobrazí obsah každého řádku obráceně</p>
<p>grid-reverse-even
zobrazí obsah každého sudého řádku obráceně</p>
<p>grid-reverse-odd
zobrazí obsah každého lichého řádku obráceně</p>
<p>Pozn. pro vývojáře: u tříd zmíněných výše se používají breakpointy @layout-breakpoint-max
Výpisy a galerie na mobilu a tabletu (2.31+) 
Pro galerii a výpisy jsou připravené třídy díky kterým lze určit počet položek na řádek, defaultně se na mobilu zobrazí jedna položka na řádek a to není vždy chtěné, proto máme tyto třídy díky kterým lze určit počet položek na různých zařízeních:</p>
<p>Pro mobil (defaultně do 480px):</p>
<p>Název třídy
Popis</p>
<p>grid-sm-2
dvě položky na řádek</p>
<p>grid-sm-3
tři položky na řádek</p>
<p>grid-sm-4
čtyři položky na řádek</p>
<p>Pro větší mobil a užší tablet (defaultně od 481px do 640px): </p>
<p>Název třídy
Popis</p>
<p>grid-md-2
dvě položky na řádek</p>
<p>grid-md-3
tři položky na řádek</p>
<p>grid-md-4
čtyři položky na řádek</p>
<p>Pro tablet (defaultně od 641px do 992px):  </p>
<p>Název třídy
Popis</p>
<p>grid-lg-2
dvě položky na řádek</p>
<p>grid-lg-3
tři položky na řádek</p>
<p>grid-lg-4
čtyři položky na řádek</p>
<p>Pozn. pro vývojáře: u tříd zmíněných výše se používají breakpointy @screen-sm, @screen-md, @screen-lg a jejich "max" varianty </p>
<p>Tip: Třídy lze kombinovat!
Třídy lze mezi sebou kombinovat, lze tedy nastavit třídu jak pro mobil, větší mobil tak pro tablet.
Např: grid-sm-2 grid-md-4 =&gt; mobil 2 fotky, velký mobil 4 fotky
Zalomení vnořeného gridu
Na malých obrazovkách je někdy třeba zalomit sloupce ve vnořeném gridu. Pro toto máme speciální třídy:</p>
<p>Název třídy
Popis</p>
<p>nested-grid-column-mobile
Zalomí sloupce ve vnořeném gridu pod sebe. Platí v rozmezí 0 - @screen-md (720 px)</p>
<p>Zarovnání textu
Třídy pro případ, kdy potřebuji změnit zarování textu pro menší breakpointy.</p>
<p>Název třídy
Popis</p>
<p>align-sm-X
X = right, center, left. Platí v rozmezí 0 - @screen-md (720 px)</p>
<p>align-md-X
X = right, center, left. Platí v rozmezí @screen-md – @screen-lg (720 px - 993 px)</p>
<p>Příklad: Položku mám na desktopu zarovnanou doprava, ale na telefonu potřebuji zarovnání na střed. Lze tedy použít třídu align-sm-center.
Formuláře 
Formuláře od verze 2.30 hlídají, aby měla jejich políčka dostatečné rozměry. Pokud by byl formulář vložený do úzkého gridu a ještě by měl dva sloupce, snadno by docházelo ke špatnému zobrazení na front-endu. Proto jsou nově k dispozici třídy, které vynutí zobrazení v gridu vedle sebe, přestože jsou políčka užší, než dovoluje náš systém. </p>
<p>Pro tablet (defaultně od 641px do 992px):  </p>
<p>Název třídy
Popis</p>
<p>form-md-force-grid
vynutí zobrazení ve sloupcích, přestože je políčko užší</p>
<p>Pro desktop (defaultně od 992px):  </p>
<p>Název třídy
Popis</p>
<p>form-lg-force-grid
vynutí zobrazení ve sloupcích, přestože je políčko užší</p>
<p>Sekce s preferovaným sloupcem (2.34)
V některých případech (většinou sekce obrázek/text) chceme preferovat jeden sloupec aby se např. text nadpisu na menších rozlišeních nezalamoval po jednom slově. Pro tyto účely nám slouží třídy grid-prefer</p>
<p>Pro tablet a menší displaye (defaultně od 641px do 861px):  </p>
<p>Název třídy
Popis</p>
<p>grid-prefer-first
preferuje první sloupec řádku</p>
<p>grid-prefer-last
preferuje poslední sloupec řádku</p>
<p>Dřívější "rozbití" gridu (2.34)
Může se stát že "sestavený grid", většinou při použití více sloupců vedle sebe nevypadá hezky na menších rozlišeních a chceme aby základní grid přestal fungovat již dříve. K tomu nám slouží třída grid-only-ml. Třída se nastavuje na sekci, a "rozbíjí" základní grid na rozlišeních nižších než je 861px</p>
<p>Podpora
 Inspirace
Nápověda
Inovace
Videonávody
 Produkty a řešení
 Digitalizace služebWebové stránkyLanding pagesKariérní stránky Získejte zdarma náš měsíční newsletter s tipy pro lepší web. Přidejte se k více jak 7 000 lidí.</p>
<p>E-mail*</p>
<p>Odeslat</p>
<p>Vyzkoušejte solidpixels zdarma</p>
<p>Tento web běží na solidpixels.</p>