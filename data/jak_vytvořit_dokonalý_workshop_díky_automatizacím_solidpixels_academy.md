<p>Jak vytvořit dokonalý workshop (díky automatizacím) | solidpixels academy</p>
<p>Menu</p>
<p>cs en</p>
<p>BlogVše Inspirace Návody Případové studie Rozhovory OborySlužby Gastronomie Hotely Ambasadoři NápovědaZačínáme se solidpixels Základní bloky Pokročilé bloky Design Funkce Nastavení webu Inovace Video návody</p>
<p>Vyhledávání</p>
<p>Začít zdarma</p>
<p>cs en</p>
<p>Návody, Video tipy
Jak vytvořit dokonalý workshop (díky automatizacím)
18 minutObsah článku</p>
<p>Představení automatizace
Nástroje pro automatizaci
Scénáře pro vytvoření automatizace</p>
<p>V článku s Eliškou Vyhnánkovou jste si mohli přečíst o tom, jak si díky automatizacím ušetřit práci. Úspora času ale není to jediné, co může přinést. Automatizace vám také umožní dělat lepší služby. A přesně o tom je tento článek.Na příklady webu UX Workshopy, který na solidpixels rozběhla výzkumnice Tereza Kosnarová, si ukážeme, jak si díky automatizacím nejenom ušetřit čas, ale také jak vytvořit perfektní zážitek pro zákazníka. Tereza na svém webu prodává hlavně kurzy, ale vy si můžete návod přizpůsobit i třeba pro konference, webináře nebo podobné aktivity.V článku se postupně zaměříme na přípravnou fázi, detailně popíšeme propojení jednotlivých nástrojů a přineseme také inspiraci pro vylepšení vzniklé automatizace.Představení automatizace: co bude umět, až ji vytvoříte
Příklad, který jsme pro tento článek navrhli, nepatří mezi ty nejjednodušší. Ale zároveň to není přehnaně složité a zvládne to každý, kdo se dokáže seznámit s prostředím Integromatu. Zkrátka lepší služba musí být trochu ambiciózní ;).
Co je tedy lepší služba v podání tohoto článku? Je to služba, která je přívětivá pro zákazníka. Zákazník vždy ví, co má udělat nebo očekávat. Je to služba, která myslí za zákazníka a snaží se mu vše okolo účasti na workshopu zjednodušit a zpříjemnit.
A konkrétně? Na začátku si zákazník na webu prostřednictvím formuláře objedná místo na workshopu. My pak informace o zákazníkovi uložíme do tabulky, abych mohli se zákazníkem dále pracovat. V dalším kroku vytvoříme fakturu, odkaz uložíme zpět do tabulky a pošleme fakturu zákazníkovi – s platebními údaji, aby ji mohl zaplatit.
Pak budeme kontrolovat, zda už zákazník fakturu uhradil a jakmile se tak stane, najdeme ho v databázi a informaci o zaplacené faktuře opět uložíme do databáze. V této chvíli můžeme zákazníkovi poslat také informace o tom, jak se na workshop připravit, aby si z něj odnesl maximum: odkazy na články, podklady nebo třeba jen informaci, že si nemusí brát počítač.
V den před workshopem pak zákazníkům, kteří mají workshop zaplacený, pošleme praktické informace: kde a kdy se workshop koná a jak se tam nejlépe dostavit. Tento krok by byl důležitější pro online workshopy, kde je vhodné lidi předem informovat o tom, zda si mají stáhnout software, jak s ním pracovat, že je lepší, když budou mít sluchátka a webkameru apod.
Druhý den po workshopu pak pošleme účastníkům, kteří dorazili, zprávu s poděkováním, dalšími zdroji a informacemi o dalších workshopech nebo službách.</p>
<p>TIP: Ještě než se pustíme do vlastní automatizace, popište si tímto způsobem vaši vlastní službu. Ušetří si tak několik hodin práce.Nástroje: Co budeme pro automatizaci potřebovat
Pro tvorbu automatizace budeme propojovat několik nástrojů. Vybrali jsme si ty nejvhodnější, ale často existují alternativy. Vybírat je vhodné z nástrojů, které mají přímou podporu Integromatu (který budeme využívat), ale propojit se dá jakákoliv služba, která poskytuje API nebo Webhooky.
Objednávkový formulář
Pro vytvoření objednávkového formuláře využijeme formuláře, které jsou přímo v solidpixels. Tvorba formuláře je intuitivní, a protože solidpixels podporují webhooky, je také snadné je na Integromat připojit. Pro tento konkrétní příklad jsme vytvořili tento formulář.</p>
<p>Až budete navrhovat svůj formulář, myslete na to, že v něm musí být hlavně všechny informace, které budete dál využívat. Chcete posílat upozornění před konáním workshopu? Pak musíte znát termín workshopu. Chcete firmám vystavit fakturu? Pak se hodí znát IČ.
Propojení všech nástrojů a automatizace služby
Pro tvorbu automatizace využíváme Integromat. Existují i jiné možnosti jako Zapier nebo Automate.io, ale Integromat přináší tři výhody. V první řadě jde o český startup, a proto má dobré napojení na české služby. Zároveň má funkce, které vám umožní snadno vytvářet pokročilé scénáře. A nakonec je často levnější, než konkurence. Abyste mohli postupovat podle návodu, potřebujete účet v Integromatu.</p>
<p>TIP: Pokud ještě nemáte účet v Integromatu, můžete si přes tento odkaz účet založit a získat měsíc placeného tarifu zdarma.</p>
<p>Popis práce s Integromatem v tomto článku předpokládá, že se seznámíte se základy. Nejlépe přímo v nápovědě Integromatu.
Tabulka pro evidenci objednávek
Data o zákaznících si potřebujete uložit do tabulky, abyste s nimi mohli dále pracovat. Pro spoustu automatizací se hodí Google Tabulky, které mají přímé napojení na solidpixels, ale v našem případě využijeme Airtable. Airtable je databázový software, ale nenechte se odradit – není pro programátory, ale pro koncové uživatele. Využíváme ho ze dvou důvodů: mnohem lépe se automatizuje a navíc zmenšuje riziko lidského faktoru – bude třeba složitější, abyste si omylem přepsali hodnoty v tabulce.
Pokud budete vytvářet svou automatizaci, založte si účet v Airtablu a vytvořte si podobnou tabulku té, se kterou v automatizaci pracujeme.</p>
<p>Tato tabulka za vás plní pár dalších úkolů – automaticky při vytvoření záznamu generuje identifikační číslo objednávky. to můžete využít jako variabilní symbol (sloupec Variabilní symbol).
Podle termínu workshopů vám také dopočítává cenu workshopu (sloupec Cena). Můžete to klidně řešit jinak – můžete si například vytvořit druhou tabulku s názvem „Produkty” a podle názvu produktu ve formuláři vyhledat cenu nebo termín konání.</p>
<p>Platby a faktury
Automatizace fakturace a plateb může působit složitě, ale pokud máte dobré nástroje, může to být velmi jednoduché. My jsme se rozhodli využít Fakturoid. V placené verzi vám dokáže ušetřit kus práce, tím, že za vás na vašem bankovním účtu kontroluje, zda už byla faktura zaplacena.</p>
<p>TIP: Pokud začínáte a nemáte Fakturoid, můžete ho získat s 50% slevou v rámci projektu Nakopni.to.
Komunikace se zákazníkem
V průběhu celého procesu potřebujete komunikovat se zákazníkem – ať už jde o potvrzení odeslání formuláře, potvrzení přijetí platby nebo připomenutí v den před konáním workshopu. Dokud půjde o nižší desítky e-mailů, můžete využít svůj e-mail.
Vytvoření automatizace
Celá automatizace se skládá ze čtyř scénářů:</p>
<p>Uložení informací z formuláře a odeslání faktury
Kontrola přijatých plateb a odeslání potvrzení
Odeslání připomenutí
Odeslání poděkování</p>
<p>1. Uložení informací z formuláře a odeslání faktury</p>
<p>První částí tohoto scénáře je přidání spouštěče scénáře. Chceme, aby se scénář spustil pokaždé, když někdo na webu vyplní formulář. Přesně k tomu slouží webhook – speciální webová adresa, kterou získáte získáte v Integromatu a uložíte ji do nastavení v solidpixels.</p>
<p>V Integromatu vyberte do prvního modulu (s otazníkem) aplikace „Webhooks” a přidejte nový modul, který se jmenuje „Custom Webhook”.
Klikněte na něj a přidejte nový webhook. Ten stačí pojmenovat a Integromat vám vytvoří odkaz.
Tento odkaz zkopírujte a vložte ho do nastavení webhooků v solidpixels. Pro tento krok využijte existující návod v solidpixels Academy.
Předtím, než přidáte další moduly, zkuste scénář zapnout. Pokud vyplníte testovací formulář, Integromat ho zachytí a vám se bude lépe pracovat na dalších krocích</p>
<p>Pak připojte tabulku z Airtablu.</p>
<p>Přidejte nový modul z aplikace Airtable a vyberte modul „Create a Record”.
Do příslušných sloupců namapujte údaje, které jste přes webhook obdrželi z formuláře na webu. 
Pokud spustíte scénář a znovu vyplníte formulář, měly by se vám údaje vyplnit do tabulky v Airtablu.</p>
<p>Dál se pustíme do vytvoření faktury.</p>
<p>Nejprve musíme vytvořit nový kontakt, který uvedeme na faktuře. Přidejte nový modul aplikace Fakturoid – „Create a contact”. Namapujte údaje o zákazníkovi z tabulky.
Pak přidejte druhý modul Fakturoidu, tentokrát „Create an invoice”. Do tohoto modulu napamujete zákazníka, které jsme vytvořili v Integromatu, a dál údaje o produktu z Airtablu.
Abychom mohli odeslat zákazníkovi, musíme získat veřejný odkaz na fakturu. Přidejte třetí modul Fakturoidu „Get an invoice”. Do toho stačí z předchozího modulu namapovat identifikační číslo faktury.</p>
<p>Získaný odkaz pak chceme uložit do databáze v Airtablu. V tomto případě ukládáme také číslo faktury. Oba údaje nejsou vyloženě nutné, ale je praktické, pokud máte všechny informace o objednávce v jedné tabulce a nemusíte nikde nic dohledávat.
Samotné odeslání už je pak jednoduché. Přidáte modul, který umí rozesílat e-maily – může to být Email, my jsme využili Gmail, ale klidně to může být Mailchimp, Ekomail.cz nebo jiný poskytovatel.
Do textu zprávy pak můžete mapovat jednotlivá pole ze scénáře a ta se pak budou měnit podle konkrétní objednávky. Obsah e-mailu můžete vytvořit jako obyčejný text, ale můžete přidávat i různé prvky HTML. A na vytvoření pěkného e-mailu vám stačí základ: odstavce, odkazy a třeba obrázek.</p>
<p>Tip: Pokud chcete pěknou šablonu, můžete využít editor šablon Beefree.io. Šablonu, kterou si podobně jako v solidpixels naklikáte na míru, stačí vložit do modulu E-mailu. Jednotlivé informace, které se v rámci e-mailu mění, můžete namapovat podobně jako v jiných modulech.2. Kontrola přijetí platby</p>
<p>V druhém scénáři budeme čekat na zaplacené faktury. Jakmile platba přijde, uložíme ji do tabulky a pošleme zákazníkovi potvrzení o přijetí platby a k tomu třeba nějaké praktické informace, aby se na workshop těšil a dobře se připravil. Jen připomínám – abyste nemuseli platbu označovat ručně, musíte mít ve Fakturoidu zapnuté párování plateb.</p>
<p>Nejprve potřebujeme přidat modul Fakturoidu, který bude kontrolovat, zda jsou faktury zaplacené. Jmenuje se „New event”. K tomu využijeme webhook Fakturoidu. Podívejte se do nápovědy Fakturoidu.
V druhém kroku zkontrolujeme, zda máme v tabulce zákazníka s daným číslem faktury (modul Airtable s názvem „Search Records”). Pokud ho najdeme, upravíme v tabulce stav objednávky z „Čeká na platbu” na „Zaplacená”.
Nakonec podobně jako v předchozím scénáři pošleme zákazníkovi informaci o tom, že nám platba došla. Využijeme znovu jakýkoliv modul, který umí rozesílat e-maily.</p>
<p>V tomto scénáři bychom si dovedli představit ještě další vylepšení. Např.:</p>
<p>nastavte si upozornění na mobil, že vám došla platba.
pokud zákazníka v tabulce nenajdeme, může vám systém poslat upozornění, abyste fakturu zkontrolovali.</p>
<p>3. Odeslání připomenutí</p>
<p>Den před workshopem chceme zákazníkovi poslat připomenutí. V tomto kroku za vás velkou část práce udělá Airtable. V tabulce si můžete všimnout, že jsme vytvořili několik různých pohledů („Views” najdete v nápovědě Airtablu). Views vám umožňují uložit si různé pohledy na vaše data. Každý pohled může mít například zobrazené jiné sloupce nebo můžete aplikovat filtrování řádků (podobně jako v Google Tabulkách).
Pro účely třetího a čtvrtého scénáře jsme si vytvořily dva pohledy, které filtrujeme podle data a vždy zobrazujeme jen objednávky, které odpovídají filtru.
První pohled se jmenuje „Připomenout dnes” a zobrazuje všechny objednávky na workshop, který se koná následující den. Konkrétně Airtablu říkáme: zobraz všechny objednávky, u nichž je termín workshopu zítra. 
V Integromatu pak kontrolujeme, zda se v tomto pohledu objevily nějaké objednávky, a pokud mají stav „Zaplaceno” (přišla platba), odesíláme jim upozornění.</p>
<p>Vložte tedy první modul aplikace Airtable, tentokrát „Watch records”.
Ve scénáři odfiltrujte jen objednávky, které byly zaplaceny.
Nakonec přidejte modul, který rozesílá e-maily (platí stejné informace jako v prvním scénáři).</p>
<p>4. Odeslání poděkování</p>
<p>Posledním krokem je zaslání poděkování za účast na workshopu. V tomto případě je scénář téměř identický jako předchozí, třetí scénář. Vycházíme opět z pohledu v Airtablu. Jmenuje se „Poděkovat dnes” a zobrazuje všechny objednávky, které mají termín workshop plus jeden den (tedy den po workshopu).
Abychom neposílali poděkování zákazníkům, kteří workshop nakonec nenavštívili, posíláme e-mail pouze objednávkám, které mají stav „Dokončeno”. Tento stav je vhodné nastavit manuálně, například na začátku workshopu při kontrole prezence.
V Integromatu jde o scénář, který je velmi podobný třetímu scénáři.</p>
<p>Vložte tedy první modul aplikace Airtable, opět jde o „Watch records”.
Přidejte modul, který rozesílá e-maily (platí stejné informace jako v prvním scénáři).</p>
<p>Jak by se dala automatizace ještě vylepšit?
A to je vše – máme nastavené čtyři scénáře, které vám uvolní ruce, ať už se chcete věnovat rozvoji svého podnikání, rodině nebo koníčkům. Tato automatizace navíc znamená, že dodáváte profesionálnější službu než dřív.
Někomu můžete tato automatizace stačit. Je ale jasné, že vaše služba bude trochu jiná, a tak je potřeba postupně všechno vychytat. Pro inspiraci přidáváme několik dalších podnětů, které můžete zvážit:</p>
<p>Mohli bychom vytvořit další scénář, který by upozornil jak vás, tak zákazníka, že faktura ještě nebyla zaplacena.
Pro situace, kdy by zákazník platil na poslední chvíli, můžete přidat upozornění přes sms.
Po uložení zákazníka do databáze ho můžete uložit také do newsletterové databáze, např. do Mailchimpu (nezapomeňte ale na potřebný souhlas, který musí být součástí formuláře).
Vytvořte si statistiky v Google Data Studiu: posílejte si všechny objednávky do Google Tabulky a napojte ji na Google Data Studio. Můžete si tak vytvořit pořád aktuální přehled o tom, jak se daří vašemu podnikání.
Ocenili by vaši zákazníci platby kartou? To umožňuje buď nejvyšší tarif Fakturoidu nebo třeba zmiňovaný Stripe.</p>
<p>Při vylepšování je ale potřeba zůstat nohama na zemi – automatizace by vždy měla být co nejjednodušší. Pamatujte, že čím složitější systém je, tím složitější bude na údržbu a tím spíše se něco pokazí. A myslet byste měli i na to, že se musí vyplatit.
Vyplatí se podobný postup automatizovat? Za nás ano
Celý tento proces fakticky zahrnuje pouze jediný manuální úkon – v den po ukončení workshopu změníte stav u zákazníků, kteří nakonec doopravdy přišli. Nechcete totiž posílat poděkování těm, kteří to třeba kvůli nemoci nestihli.
Odhadujeme, že by vám práce okolo tohoto workshopu mohla při patnácti účastnících zabrat klidně deset hodin. Na straně provozních nákladů se vejdeme do základního měsíčního předplatného za cca 210 Kč. Další provozní náklady, jako např. předplatné fakturačního nástroje, byste platili tak i tak. Pak také musíte počítat s časem, který pro vytvoření automatizace potřebujete. Pokud vám to zabere třicet hodin, bude se vám investice jen pomalu. Pokud to bude 5 hodin (což je u tohoto scénáře reálné), vrátí se vám to během jednoho workshopu.
U všech automatizací je tedy potřeba odhadnout, zda se vám vyplatí. Pokud si spočítáte, jak se vám v podobném případě změní ziskovost, není o čem přemýšlet. Úspora je dost významná a vy můžeme získaný čas využít na rozvoj vašich služeb nebo klidně na odpočinek.
Automatizace nešetří jen peníze
Nakonec to nemusí být jen o penězích. Jen těžko se dá vyčíslit, že nemusíte dělat práci, která vás příliš nebaví. Že sami nebo v pár lidech zvládnete práci, kterou dřív dělalo deset lidí. Že máte čas přemýšlet o svém podnikání. Nebo že si můžete odpočinout, pokud je toho na vás příliš.
Automatizace jsou v kontextu malých a středních firem poměrně nové, ale vidíme jasné uplatnění. Navíc, spoustu práci si dokážete díky solidpixels, Integromatu a třeba Airtablu usnadnit sami.
Honza Páv
honzapav.cz
 Martin Hakl
solidpixels
Další inspirace pro lepší web</p>
<p>Kompletní návod: skvělé představení služeb na webu</p>
<p>Návody</p>
<p>Naučte se představovat vaše služby na webu způsobem, který konvertuje návštěvníky v zákazníky a prezentuje vás jako respektované odborníky. </p>
<p>Jak na skvělou landing page</p>
<p>Návody</p>
<p>Jedna z největších překážek při komunikaci s dnešním uživatelem internetu je jeho roztříštěná pozornost. Důležitá sdělení je proto potřeba maximálně zjednodušit, jasně formulovat a očistit od všech zbytečných podnětů. V tom nám může skvěle pomoci landing page.</p>
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