<p>Přesměrování | solidpixels academy</p>
<p>Menu</p>
<p>cs en</p>
<p>BlogVše Inspirace Návody Případové studie Rozhovory OborySlužby Gastronomie Hotely Ambasadoři NápovědaZačínáme se solidpixels Základní bloky Pokročilé bloky Design Funkce Nastavení webu Inovace Video návody</p>
<p>Vyhledávání</p>
<p>Začít zdarma</p>
<p>cs en</p>
<p>Nastavení webu
Přesměrování
6 minutObsah článku</p>
<p>Funkce přesměrování
Jak nastavit přesměrování
Příklad přesměrování
Import přesměrování
Přesměrování celé domény</p>
<p>Přesměrování (redirecty) slouží k převedení uživatele a vyhledávače z již neexistujících URL adres na nové URL adresy tak, aby se jim nezobrazila chybová stránka 404.
Nastavit přesměrování je vhodné zejména při spuštění nového webu, při smazání stránky, změně url adresy stránky nebo i třeba blogového článku.
Jak nastavit přesměrování</p>
<p>Pro přesměrování je potřeba vytvořit seznam starých URL adres a jejich namapování na nové URL adresy. V hlavní navigaci vyberte Nastavení a poté sekci Přesměrování.</p>
<p>Původní url – původní adresa webu
Nová url – nová adresa, kam má být uživatel přesměrován
HTTP kód – tzv. stavový kód HTTP:</p>
<p>300 – Multiple Choices: požadovaný obsah je na více místech, je třeba specifikovat požadavek
301 – Moved permanently: trvalé přesunutí aktuálního i budoucího obsahu na jinou adresu
302 – Moved temporarily: dočasné přesunutí obsahu na jinou adresu (např. sezónní nabídky)
303 – See Other: požadovaný obsah je k nalezení na jiné adrese
307 – Temporary Redirect: dočasné přesunutí stránky na jinou adresu</p>
<p>Původní i nová adresa musí obsahovat na začátku "https://www", i přesto, že původní web běžel jen na http nebo bez www na začátku domény. 
Přesměrování musí směřovat na neexistující adresu, která zobrazí chybovou stránku 404.</p>
<p>Tip: Přesměrovat můžete i nefunkční soubory ke stažení Přesměrování je funkční i na adresy souborů ke stažení. Můžete tak přesměrovat adresy, pod kterými si uživatelé mohli stahovat např. vaše výroční zprávy v PDF.https://www.domena.cz/files/nazev.pdf -&gt;https://www.nova-domena.cz/stranka
Příklad přesměrováníPokud chcete uživatele přesměrovat ze staré adresy např. http://www.domena.cz/stary-kontakt na novou adresu https://www.domena.cz/novy-kontakt. Vyplníte formulář následovně:Původní url: https://www.domena.cz/stary-kontaktNová url: https://www.domena.cz/novy-kontaktHTTP kód: "code- 301"URL adresa pro přesměrování může obsahovat tyto znaky [0-9a-zA-Z_./-?=]. Jedná se tedy o čísla, písmena, podtržítko (_), tečku (.), lomítko (/), pomlčku (-), otazník (?), rovná se (=). Další speciální znaky nejsou podporovány.Import přesměrování
V případě potřeby nastavit více přesměrování najednou můžete využít import pomocí XLSX tabulky. </p>
<p>V databázi "Přesměrování" mějte založené alespoň jedno aktivní přesměrování.
Vpravém horním rohu nad tabulkou zvolte "Hromadné akce" a vyberte možnost "Export".
V nabídce výběru exportovaných sloupce nechte výchozí výběr a potvrďte tlačítkem "Export".
Do počítače se vám stáhne soubor export-cms_redirects.xlsx, který obsahuje jednotlivé sloupce a nyní stačí doplnit vaše přesměrování jako nové řádky
Vyplně tyto sloupce: "Nová URL", "Původní URL" a "HTTP Kód" (pro přesměrování je správně hodnota 301). Hodnoty ostatních sloupců se doplní při importu automaticky.
Pro import vyberte "Hromadné akce" -&gt; "Import" soubor do tabulky nahrajete.
V posledním kroku potvrďte import přes tlačítko "Provést import".</p>
<p>Přesměrování na úrovni celé domény
Přesměrování je možno nastavit i na úrovni domén nebo subdomén. Toto přesměrování se provede jako první, poté se provede přesměrování v rámci cílové domény.
Důležitou podmínkou je, že zdrojová doména musí být nasměrována na náš server.
Např.: http://www.domena.cz/clanek-puvodni na novou adresu https://www.nova-domena.cz/clanek-novy.</p>
<p>Přesměrování na úrovni domény http://www.domena.cz -&gt; https://www.nova-domena.cz
Přesměrování v rámci nové domény (přesměrování na úrovni domény již proběhlo) https://www.nova-domena.cz/clanek-puvodni -&gt; https://www.nova-domena.cz/clanek-novy</p>
<p>Přesměrování mezi doménami doporučujeme vyřešit přímo u vaše registrátora domény. Tak budete mít vždy di případné další změny plněno pod kontrolou. 
V případě potřeby nás prosím kontaktujte.</p>
<p>Tip: Přesměrování stejnojmené stránky mezi různými doménami
Pokud je provedeno přesměrování na úrovni domény, toto přesměrování není nutno v administraci nastavovat, část URL za doménou se přenáší automaticky.
https://www.domena.cz/stranka -&gt;
https://www.nova-domena.cz/stranka
Témata nápovědy</p>
<p>Začínáme se solidpixels</p>
<p>Začněte se solidpixels</p>
<p>Práce se stránkami a strukturou webu</p>
<p>Tvorba obsahu pomocí bloků</p>
<p>Video: jak funguje layout builder </p>
<p>Video návody: začínáme tvořit web se solidpixels</p>
<p>Základní bloky</p>
<p>Blok Harmonika</p>
<p>Blok Tlačítko</p>
<p>Blok Box</p>
<p>Blok Citace</p>
<p>Blok Dělící čára</p>
<p>Pokročilé bloky</p>
<p>Blok Newsletter</p>
<p>Blok Kód</p>
<p>Blok Ceník</p>
<p>Blok Formulář</p>
<p>Blok Ikony sítí</p>
<p>Design</p>
<p>Jak nahrát vlastní font na web</p>
<p>Výběr vhodného designu</p>
<p>Jak připravit grafický návrh pro solidpixels</p>
<p>Přizpůsobte si design</p>
<p>Nastavení webu</p>
<p>Nastavení cookie lišty</p>
<p>Rozšířené možnosti nastavení hlavičky webu</p>
<p>Napojení Seznam Webmaster</p>
<p>Návod pro nastavení účtu pro Google reCAPTCHA</p>
<p>Měření konverze pro formuláře pomocí Google Analytics</p>
<p>Funkce</p>
<p>Spotlight</p>
<p>Uživatelská zóna</p>
<p>Dokupování prémiových funkcí</p>
<p>Vytvoření a správa blogu</p>
<p>Tvorba a strukturování obsahu pomocí sekcí</p>
<p>E-shop</p>
<p>Proces napojení brány přes GP Webpay</p>
<p>Proces napojení brány přes Gopay</p>
<p>Proces napojení brány přes ComGate</p>
<p>Práce s objednávkami</p>
<p>Napojení platební brány na E-shop</p>
<p>Účet a platby</p>
<p>Fakturace a platby</p>
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