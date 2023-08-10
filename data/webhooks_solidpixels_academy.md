<p>Webhooks | solidpixels academy</p>
<p>Menu</p>
<p>cs en</p>
<p>BlogVše Inspirace Návody Případové studie Rozhovory OborySlužby Gastronomie Hotely Ambasadoři NápovědaZačínáme se solidpixels Základní bloky Pokročilé bloky Design Funkce Nastavení webu Inovace Video návody</p>
<p>Vyhledávání</p>
<p>Začít zdarma</p>
<p>cs en</p>
<p>Integrace
Webhooks
5 minutObsah článku</p>
<p>Propojení dat s dalšími aplikacemi
Založení webhooku
Přehled záznamů a událostí
Bezpečnost</p>
<p>Propojení dat s dalšími aplikacemi
Webhooks přinášejí možnost propojit platformu solidpixels s dalšími aplikacemi. Díky tomu můžete v reálném čase reagovat na události, které na vašem webu nastanou, např. zákazník vytvoří objednávku nebo se registruje k newsletteru. Webhooks vám umožní odesílat data z vašeho webu do dalších aplikací a automatizovat mnoho procesů, které byste tradičně dělali ručně.</p>
<p>Založení webhooku
Webhook je webová adresa (URL), kterou si můžete v administraci nastavit a systém podle zvolených pravidel na tuto adresu odesílá zprávy / data. V nastavení webhooku si stanovíte URL adresu, formát dat a událost, na kterou se data odešlou. O zbytek se postará systém sám. </p>
<p>Na záložce Nastavení &gt; Webhooks klikněte na tlačítko „Nový záznam“.  
Vyplňte název webhooku, např. „Registrace zákazníka do CRM“.
Vyberte formát data. V nabídce jsou varianty JSON, Form a Query (více o formátech níže).
Zvolte typ záznamu a událost, na kterou se má webhook zavolat. Např. chcete na registraci k newsletteru rovnou zákazníka přidat do svého CRM. Pak zvolíte typ záznamu „Data z formuláře“ a událost „Vytvoření záznamu“.
Klikněte na tlačítko „Uložit“.
Data se nezačnou odesílat okamžitě, jakmile budete připraveni na spuštění přepněte webhook do stavu „Aktivní“.</p>
<p>Správné nastavení záznamu si můžete ověřit kliknutím na tlačítko Poslat testovací požadavek, které ověří, že založený webhook v cílové aplikaci existuje. </p>
<p>Jak zvolit správný formát dat?
Všechno závisí na aplikaci, do které chcete data odesílat. Solidpixels podporuje nejrozšířenější formáty, tedy JSON a formulářová data. </p>
<p>JSON</p>
<p>JSON je velmi rozšířený formát dat, který se snadno dále strojově  zpracovává. Pokud ho vaše cílová aplikace podporuje, doporučujeme jej použít.</p>
<p>Form</p>
<p>Formát „Form“ představuje stejný formát, jakým se odesílají formuláře.</p>
<p>Query</p>
<p>V některých okrajových případech se vám může hodit webhook ve formátu „Query“, ve kterém jsou data přibalená do samotné URL adresy, např. https://domain.com/123456?Customer=Martin.</p>
<p>Přehled záznamů a událostí
Následující přehled ukazuje, na které typy záznamů a událostí můžete integrovat další aplikace. Nabídka se může lišit v závislosti na dostupných modulech ve vašem plánu.
Výběrem typu záznamu se omezí události pouze pro zvolený typ. Stejně funguje omezení pomocí události. Díky tomu můžete automatizovat pouze konkrétní akce na webu, např. vytvoření objednávky v e-shopu nebo odeslání poptávkového formuláře. </p>
<p>Typy záznamů</p>
<p>Název modulu
Typ záznamu</p>
<p>Články
Článek</p>
<p>Kategorie</p>
<p>Autoři článků</p>
<p>Události
Událost</p>
<p>Osoba</p>
<p>Eshop
Objednávka</p>
<p>Produkty</p>
<p>Kategorie</p>
<p>Ostatní
Data z formulářů</p>
<p>Získané kontakty</p>
<p>Události</p>
<p>Název události</p>
<p>Vytvoření záznamu
Událost se spustí při vytvoření záznamu v CMS nebo přes formulář na webu.</p>
<p>Změna záznamu
Událost se spustí, pokud dojde k opětovnému uložení záznamu.</p>
<p>Smazání záznamu
Uživatel smaže záznam v administraci.</p>
<p>Publikace LB
Událost se sputí při publikaci záznamu s Layout Builderem.</p>
<p>Bezpečnost
Všechna data se standardně posílají přes zabezpečený protokol HTTPS. Pro velmi pokročilé je tu navíc možnost přidat další vrtsvu zabezpečení skrze bezpečnostní klíč.
Klíč slouží k „podepsání“ požadavku, který je odesílán z vašeho webu. Stejný klíč je pak nutné použit k ověření na straně serveru, že je přijatá zpráva autentická.</p>
<p>Klíč získáte v detailu webhooku v administraci.
Bezpečnostní klíč je použit k vytvoření otisku dat a tento otisk je poslán v hlavičce X-Solidpixels-Security požadavku.
Otisk dat (hash) je vytvořen metodou HMAC  algoritmem sha256.</p>
<p>Témata nápovědy</p>
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