# Uitbreiding van het basisproject

## Nieuwe functionaliteiten

### Gebruikersbeheer:

In deze uitbreiding is het nu ook mogelijk een gebruikersaccount toe te voegen. Deze heb ik gemaakt om de nieuwe functies (het hashen van wacthwoorden, en Oauth toepassing) te kunnen testen en aantonen.

### Beveiliging via gehashte wacthwoorden en Oauth

Op het nieuwe endpoint GET /users/ is zowel hashing als Oauth toegepast. Hierdoor kan je dit endpoint enkel gebruiken als je geauthenticeerd bent.

### Put endpoint voor het aanpassen van reviews

In mijn database is nu ook de mogelijkheid om een gehele review te "updaten" (PUT). Stel dat je een review hebt gegeven, maar na een bepaalde tijd wil je je mening herzien kan je gewoon doormiddel van het juiste ID te gebruiken je huidige review aanpassen.

### Test van alle GET endpoints

Door het gebruik te maken van zelfgemaakte scripts, kan ik mijn GET endpoints effectief testen en controleren of deze correct werken.

### Testen van POST /artists/ endpoint

Het POST endpoint /artists/ om een nieuwe artiest aan te maken wordt ook getest met een zelfgeschreven script.

### Testen van DELETE /artists/ endpoint

Het DELETE endpoint /artists/ om een artiest te verwijderen wordt ook getest met een zelfgeschreven script.

### Testen van het nieuwe PUT reviews/{review_id} endpoint

Het nieuwe PUT endpoint voor de reviews wordt met een uitgebreid en zelfgeschreven script uitvoerig getest.

### Testfiles automatisch runnen met github actions

Als ik een nieuwe push maak van mijn files naar deze github, dan zorg ik er met github actions voor dat al mijn tests automatisch gerunt worden door github. Wel op voorwaarde dat mijn API eerst gedeployed is op okteto. Deze tests blijven wachten tot deze echter is opgestart alvorens deze kan runnen.

## Frontend

### VUE

Zoals je kan zien is er ook een nieuwe directory aangemaakt **/reviews**, hierin zit het project van de frontend. Hierin heb ik gebruik gemaakt van VUE, een javascript framework.

### Hosting via netlify

Op onderstaande link kan je mijn gehoste frontend op netlify terugvinden. Belangrijk om weten is wel dat deze wel de actieve API nodig heeft. In de environment variabele van dit project heb ik namelijk mijn persoonlijke okteto link van de API in gedeclareerd.
**https://arnebogaerts-api-eindproject.netlify.app/**

**NOTE:** Belangrijke sidenote, aangezien mijn okteto deployment na een periode van inactiviteit in sleep mode gaat kan het voorvallen dat de frontend tijdelijk niet werkt, aangezien de api die hij gebruikt dus in sleep mode is. Daarom voorzie ik hier alvast enkele screenshots.

Hieronder kan je een afbeelding van de hoofdpagina terugvinden. Deze geeft een CD-lijst terug met alle cd's en dus ook de bijhorende artiesten van die cd.
![afbeelding](https://github.com/ArneBogaerts/API-Development-Eindproject/assets/113974569/c8ae2297-bac4-4703-9bf2-ff77136737ea)
Vervolgens om nog een extra endpoint aan te spreken heb ik ook de reviews van een CD beschikbaar gemaakt. Als je op een album klik (zoals ik hier op het laatste album heb geklikt), dan krijg je de reviews die van dit album zijn gegeven.
![afbeelding](https://github.com/ArneBogaerts/API-Development-Eindproject/assets/113974569/5768e5c7-439a-41f7-a25e-42d0e6364061)

## De volledige API:

Onder deze screenshots, ga ik verder in detail over de nieuwe endpoints die ik ter uitbreiding van het eindproject heb gemaakt.
![afbeelding](https://github.com/ArneBogaerts/API-Development-Eindproject/assets/113974569/b6fef968-2a90-4d83-b3c6-9e207e05b688)
![afbeelding](https://github.com/ArneBogaerts/API-Development-Eindproject/assets/113974569/1335adc9-f1be-41a9-b295-0a92779b7a2c)

## ENDPOINT: GET /artists/{artist_id}/

Dit endpoint is ontworpen om gedetailleerde informatie over een specifieke artiest op te halen op basis van hun unieke ID. Het biedt een eenvoudige en directe manier om gegevens over een enkele artiest uit de database te verkrijgen.

![afbeelding](https://github.com/ArneBogaerts/API-Development-Eindproject/assets/113974569/08258e83-69c9-49db-b589-289a62de052e)

### Data ophalen:

* Bij een GET-verzoek wordt aan de hand van de meegegeven artist_id in de URL de specifieke artiest in de database gezocht.
* De artist_id is een unieke identifier die elke artiest in de database heeft.

### Response:

* De response is een JSON-object dat de details van de artiest bevat. Dit omvat typisch de id, name, en een lijst van CD's of albums geassocieerd met deze artiest, afhankelijk van hoe de relaties in de database zijn opgezet.
* Als een artiest met de opgegeven ID niet wordt gevonden, geeft de API meestal een 404-fout terug met een bericht zoals "Artist not found".

### Gebruik:

* Een artiest ophalen: Om details van een specifieke artiest op te halen, zou je een GET-verzoek sturen naar /artists/{artist_id}. Vervang {artist_id} met de werkelijke ID van de artiest die je wilt opvragen.
* Bijvoorbeeld: GET /artists/5 zal de details van de artiest met ID 5 ophalen.

## ENDPOINT: PUT /reviews/{reviews_id}/

Dit endpoint stelt gebruikers in staat om een bestaande recensie te bewerken of bij te werken op basis van de unieke ID van de recensie. Het is een cruciaal onderdeel van de API voor het beheren van de gebruikersfeedback en kwaliteitscontrole van de inhoud.

Hieronder ziet u eerst de GET-request van de review, om vervolgens het PUT-endpoint te gebruiken welke deze review aanpast om tot slot via een nieuwe GET-request de bevestiging te krijgen dat de aanpassing gedaan is.
![afbeelding](https://github.com/ArneBogaerts/API-Development-Eindproject/assets/113974569/07f234fa-3fa1-4fb5-accd-66f60ed2d7bb)
![afbeelding](https://github.com/ArneBogaerts/API-Development-Eindproject/assets/113974569/6e86ca8e-b1e7-4c5b-b18b-a8f7284e4e22)
![afbeelding](https://github.com/ArneBogaerts/API-Development-Eindproject/assets/113974569/f5721b3d-b281-40a3-82bc-42d83773200c)
![afbeelding](https://github.com/ArneBogaerts/API-Development-Eindproject/assets/113974569/0c59191d-a340-4f38-aeb4-5a497d13c596)

### Data bijwerken:

* Een PUT-verzoek naar /reviews/{review_id} vereist dat je de review_id in de URL specificeert. Dit identificeert de specifieke recensie die je wilt bijwerken.
* In de body van het verzoek stuur je de bijgewerkte gegevens mee, zoals de nieuwe beoordelingsscore en commentaar.

### Request body:

* De body van het verzoek bevat een JSON-object met de bijgewerkte velden zoals **rating** en **comment** en ook nog de **cd_id**.

### Response:

Bij een succesvolle update, zal de response meestal de bijgewerkte gegevens van de recensie terugsturen in de vorm van een JSON-object. Als de recensie met de opgegeven review_id niet wordt gevonden, zal de API een 404-fout terugsturen met een passende boodschap.

### Gebruik:

* Een recensie bijwerken: Om een recensie te bewerken, stuur je een PUT-verzoek met de nieuwe gegevens naar /reviews/{review_id}. Vervang {review_id} door de werkelijke ID van de recensie die je wilt bijwerken.
* Bijvoorbeeld: PUT /reviews/321 met een body van **{ "rating": 4.5, "comment": "Nieuwe gedachten over dit album.", "cd_id": 5 }** zal de recensie met ID 321 bijwerken.

## ENDPOINT: GET /reviews/{review_id}/

Dit endpoint is bedoeld om specifieke details van een enkele recensie op te halen aan de hand van zijn unieke ID. Het biedt een manier om individuele recensiegegevens te bekijken, wat nuttig is voor gebruikers die de details van hun eigen recensies willen zien of voor het weergeven van gedetailleerde recensie-informatie in een gebruikersinterface.

![afbeelding](https://github.com/ArneBogaerts/API-Development-Eindproject/assets/113974569/f8483570-6ce5-42bc-8ac1-76c32091ff5b)
![afbeelding](https://github.com/ArneBogaerts/API-Development-Eindproject/assets/113974569/7b57b558-cccb-4d55-84ec-0b8dcb3ff303)

### Data ophalen:

Bij een GET-verzoek wordt de review_id die in de URL is opgegeven gebruikt om de specifieke recensie in de database te lokaliseren. Deze review_id is een unieke identificator die aan elke recensie wordt toegekend.

### Response:

* De response is een JSON-object dat de details van de recensie bevat. Dit omvat gewoonlijk de id, rating, comment, en cd_id (de ID van de CD waarop de recensie betrekking heeft).
* Als er geen recensie met de opgegeven ID wordt gevonden, geeft de API meestal een 404-fout terug met een bericht zoals "Review not found".

### Gebruik:

* Een recensie ophalen: Om de details van een specifieke recensie te bekijken, verstuur je een GET-verzoek naar /reviews/{review_id}. Vervang {review_id} met de daadwerkelijke ID van de recensie die je wilt opvragen.
* Bijvoorbeeld: **GET /reviews/123** zal de details van de recensie met ID 123 ophalen.

-------------------------------------------------------------------------------------------------------------------------------------------------------------
# Basisproject:

# Thema van de API: Muziekcollectie Beheer

Deze API stelt gebruikers in staat om een digitale catalogus van cd's bij te houden. De gebruikers kunnen informatie over artiesten en cd's toevoegen, bekijken en verwijderen. Daarnaast is het mogelijk om beoordelingen (reviews) en commentaren over individuele cd's toe te voegen en te raadplegen.

## Belangrijkste Functionaliteiten:

### Artiesten Beheer:

#### Toevoegen van Artiesten:

Gebruikers kunnen nieuwe artiesten aan de database toevoegen door hun naam, genre en andere relevante details op te geven.

#### Bekijken van Artiesten:

De API biedt mogelijkheden om een lijst van alle artiesten te bekijken of om specifieke artiesten op te zoeken.

#### Verwijderen van Artiesten:

Artiesten kunnen uit de database worden verwijderd. Dit proces zorgt ervoor dat alle gerelateerde cd's en reviews ook verwijderd worden om integriteit van de data te behouden.

### CD's Beheer:

#### Toevoegen van CD's:

Gebruikers kunnen nieuwe cd's aan de catalogus toevoegen met details zoals titel, releasejaar, en de gekoppelde artiest.

#### Bekijken van CD's:

Er is een mogelijkheid om alle cd's te bekijken, of om te zoeken naar een cd op titel of via de unieke ID.

#### Verwijderen van CD's:

Wanneer een cd wordt verwijderd, worden ook automatisch de gekoppelde reviews verwijderd.

### Reviews Beheer:

#### Toevoegen van Reviews:

Gebruikers kunnen beoordelingen toevoegen aan een cd door een rating en commentaar op te geven, samen met de ID van de cd.

#### Bekijken van Reviews:

Reviews kunnen per cd bekeken worden.

## Conclusie

De API is zo ontworpen dat het eenvoudig is voor gebruikers om de informatie te beheren via een reeks van HTTP-verzoeken, waardoor het een flexibele tool is voor muziekliefhebbers of verzamelaars. De nadruk ligt op gebruiksgemak en het waarborgen van de integriteit van de gegevens bij elke bewerking.

De link naar mijn eigen gehoste API kan je hier terugvinden:
https://api-arnebogaerts.cloud.okteto.net/docs#/

Onderaan deze set foto's van mijn API, laat ik per endpoint kort zien hoe ze werken, met een korte uitleg.

![Screenshot1](https://github.com/ArneBogaerts/APIBasisproject/assets/113974569/34a35dfd-04bc-4840-a997-a64e62e2519a)
![Screenshot2](https://github.com/ArneBogaerts/APIBasisproject/assets/113974569/4538aee3-9cb1-4a08-a11e-b701a306e878)
![Screenshot3](https://github.com/ArneBogaerts/APIBasisproject/assets/113974569/c69267fe-a570-410d-bef4-58b56171aef1)

## ENDPOINT: GET /cds/

Dit endpoint haalt een lijst van CD's op uit de database. Het is ontworpen om op een handige manier toegang te geven tot de gehele collectie van CD's.

![GET cds](https://github.com/ArneBogaerts/APIBasisproject/assets/113974569/fe1b188a-ac33-4813-b93e-10c86fce2a6e)
![GET cds skiplimit](https://github.com/ArneBogaerts/APIBasisproject/assets/113974569/2fee1cd4-5f51-471b-9b5b-17f494fdd187)


### Data ophalen:

Bij een GET-verzoek wordt de database gequeryd voor CD's, waarbij de skip en limit parameters worden toegepast, als deze zijn meegegeven. Standaard slaat het 0 records over, en limiteert het resultaat tot 10 CD's. Maar deze waarden kunnen worden aangepast.

### Response:

De response is een lijst van CD's (objecten). Elk van deze objecten bevat details over deze CD, zoals zijn ID, titel en artist.

### Gebruik:

* Om de eerste  10 CD's op te halen: **GET /cds/**
* Om de volgende 10 CD's (d.w.z. CD's 11-20) op te halen: **GET /cds/?skip=10&limit=10**

## ENDPOINT: POST /cds/

Dit endpoint maakt het mogelijk om een nieuwe CD toe te voegen aan de database. Het is bedoeld om de CD-collectie uit te breiden met nieuwe items.

![POST cds](https://github.com/ArneBogaerts/APIBasisproject/assets/113974569/35f02cdd-bdfd-4060-8792-e7db80075750)
![POST cds 404](https://github.com/ArneBogaerts/APIBasisproject/assets/113974569/4176fdde-2eb6-4701-8061-c71336a719ec)

### Data toevoegen:

* Bij een POST-verzoek ontvangt het endpoint gegevens over een nieuwe CD, waaronder de titel en de naam van de artiest.
* De API zoekt eerst naar de artiest in de database. Als de artiest niet gevonden wordt, geeft het een **404-foutmelding** terug met de melding dat de artiest niet gevonden is.
* Als de artiest wel bestaat, wordt de nieuwe cd aangemaakt en aan de database toegevoegd met de meegegeven titel en de ID van de gevonden artiest.

### Request:

Het POST request moet de volgende gegevens bevatten in JSON-formaat:

* **title**: De titel van de CD.
* **artist_name**: De naam van de artiest van de CD.

### Response:

De response bevat de gegevens van de nieuw toegevoegde CD, inclusief het unieke ID dat door de database is toegekend. Dat wil zeggen de titel van het album en het album ID, alsook de gekoppelde artist met zijn ID.

## ENDPOINT: GET /artists/

Dit endpoint biedt toegang tot de lijst van artiesten in de database. Het stelt gebruikers in staat om informatie over alle geregistreerde artiesten op te halen.

![GET artists](https://github.com/ArneBogaerts/APIBasisproject/assets/113974569/0e1d3bec-1c38-4bc6-a501-6b5fc8b49f37)
![get artists skip limit](https://github.com/ArneBogaerts/APIBasisproject/assets/113974569/76f71ffc-c8a8-40fd-8f0b-b7b17667aaad)

### Data ophalen:

* Bij een GET-verzoek worden alle artiesten uit de database opgehaald, waarbij de skip en limit parameters worden toegepast. Deze parameters bepalen respectievelijk het aantal over te slagen records en het maximale aantal terug te geven records.
* Standaard worden er geen records overgeslagen (skip=0) en worden de eerste 10 artiesten teruggegeven (limit=10). Deze standaardwaarden kunnen echter door de gebruiker worden aangepast.

### Response:

* De response bestaat uit een lijst van artiesten (objecten). Elk van deze artiesten (objecten) bevatten gegevens zoals de ID en naam van de artiest.
* Deze informatie is nuttig voor gebruikers die willen weten welke artiesten in de database zijn geregistreerd.

### Gebruik:

* Om de eerste 10 artiesten op te halen: **GET /artists/**
* Om bijvoorbeeld artiesten 11-20 op te halen: **GET /artist/?skip=10&limit=10**

## ENDPOINT: POST /artist/

Dit endpoint maakt het mogelijk om een nieuwe artiest toe te voegen aan de database. Het is ontworpen om de lijst van artiesten in de database uit te breiden.

![POST artist](https://github.com/ArneBogaerts/APIBasisproject/assets/113974569/653fcbe8-1913-4a64-b367-e840e70732a1)

### Data toevoegen:

* Bij een POST-verzoek ontvangt het endpoint gegevens van een nieuwe artiest, de naam.
* Deze informatie wordt gebruikt om een nieuw artiest-object in de database aan te maken.
* Het is belangrijk dat de naam van de artiest uniek is om duplicaten in de database te voorkomen.

### Request:

Het verzoek verwacht de volgende informatie in JSON-formaat:

* **name**: De naam van de artiest.

### Response:

* De response bevat de gegevens van de nieuw toegevoegde artiest, inclusief het unieke ID dat de database zelf toekent.
* Dit bevestigd de succesvolle toevoeging van de artiest aan de database.

## ENDPOINT: POST /reviews/: 

Dit endpoint stelt gebruikers in staat om een nieuwe recensie voor een specifieke CD toe te voegen aan de database op basis van cd-id. Het is een essentieel onderdeel van de functionaliteit voor gebruikersfeedback.

![post review](https://github.com/ArneBogaerts/APIBasisproject/assets/113974569/6182b0ec-4ec5-4985-9b12-e8100c0fbe80)
![post review fout](https://github.com/ArneBogaerts/APIBasisproject/assets/113974569/bcfaa8b9-df54-403a-9efb-d7634d195e6e)

### Data toevoegen:

* Bij een POST-verzoek ontvangt het endpoint gegevens over een nieuwe recensie, waaronder de beoordeling, het commentaar en de ID van de CD waarop de review betrekking heeft.
* Het systeem controleert eerst of de gespecifieerde CD in de database bestaat. Als dit niet het geval is, wordt een 404-foutmelding teruggestuurd, wat aangeeft dat de opgegeven CD niet gevonden kan worden.
* Als de CD wel bestaat, wordt de nieuwe recensie gecreëerd en aan de database toegevoegd met de meegegeven gegevens.

### Request:

Het verzoek moet de volgende gegevens bevatten in JSON-formaat:

* **rating**: De beoordeling voor de CD met een score tot 10.
* **comment**: Een review/commentaar over de CD.
* **cd_id**: De ID van de CD waarop de recensie betrekking heeft.

### Response:

* De response bevat de gegevens van de nieuw toegevoegde recensie, inclusief het unieke ID dat aan de recensie is toegekend.
* Dit Bevestigt de succesvolle toevoeging van de recensie aan de database.

## ENDPOINT: GET /cds/{cd_id}/reviews/

Dit endpoint haalt alle recensies op die zijn gekoppeld aan een specifieke CD, geïdentificeerd door zijn ID (cd_id). Het is een nuttig hulpmiddel voor gebruikers die geïnteresseerd zijn in het lezen van feedback en beoordelingen van een bepaalde CD.

![get reviews](https://github.com/ArneBogaerts/APIBasisproject/assets/113974569/6b9ecaf6-41d0-408f-8e16-c74a3de1a2b5)

### Data ophalen:

* Bij een GET-verzoek gebruikt het endpoint de **cd_id** parameter in de URL om de overenkomstige CD in de database te identificeren.
* Vervolgens worden alle recensies die aan deze CD zijn gekoppeld opgehaald en teruggestuurd in de response.

### Response:

* De response bestaat uit een lijst van review-objecten, waarbij elk object de details bevat die je zonet hebt meegegeven zoals: beoordeling, commentaar en de ID van de review die automatisch gegenereert word.
* Deze informatie is waardevol voor gebruiker die meer willen weten over de ervaringen van bepaalde CD's van anderen die deze api gebruiken.

### Gebruik:

* Om alle recensies van een bepaalde CD te bekijken: **GET /cds/{cd_id}/reviews/**

## ENDPOINT: DELETE /cds/{cd_id}

Dit endpoint stelt gebruikers in staat om een specifieke CD uit de database te verwijderen op basis van zijn **cd_id**. Het is bedoeld voor het beheren van de CD-collectie, waaronder het verwijderen van verouderde of ongewenste items.

![DELETE CD](https://github.com/ArneBogaerts/APIBasisproject/assets/113974569/4d94b8cc-422f-452f-ac4f-620ae0f6d768)
![DELETE CD notfound](https://github.com/ArneBogaerts/APIBasisproject/assets/113974569/c49ad78a-b15d-4e43-8661-0de99b267392)

### Data verwijderen:

* Bij een DELETE-verzoek gebruikt het endpoint de cd_id parameter in de URL om de overeenkomstige CD in de database te lokaliseren.
* Als de CD wordt gevonden, wordt deze verwijderd uit de database.
* Als de CD niet wordt gevonden, geeft het endpoint een 404-foutmelding terug met **CD not found**. Dit geeft aan dat de CD niet bestaat, of al verwijderd is.

### Response:

* Er zijn geen body-parameters vereist voor dit verzoek. De actie wordt geheel gestuurd door de cd_id parameter in de URL.
* Bij succesvolle verwijdering geeft het endpoint een response terug met de gegevens van de verwijderde CD, als bevestiging van de actie.
* Bij een fout (zoals een niet-bestaande CD) geeft het de gedefinieerde foutmelding, **CD not found**, terug.

### Gebruik:

* Om een CD met een specifiek ID te verwijderen: **DELETE /cds/{cd_id}**

## ENDPOINT: DELETE /artists/{artist_id}

Dit endpoint stelt gebruikers in staat om een artiest uit de database te verwijderen op basis van het unieke **artist_id**. Het wordt gebruikt voor het beheer van de artiestengegevens in de database, waaronder het verwijderen van artiesten die niet langer relevant zijn of waarvan de gegevens niet meer kloppen. Bij het verwijderen van een artiest, worden ook gelijk alle bijhorende cd's en de daarbijhorende reviews verwijderd.

![DELETE ARTIST](https://github.com/ArneBogaerts/APIBasisproject/assets/113974569/a6326eb2-45ef-4839-b9cd-6944525df085)
![DELETE ARTIST notfound](https://github.com/ArneBogaerts/APIBasisproject/assets/113974569/97637d8b-dc8d-41a0-87cf-1f98757177c2)

### Data verwijderen:

* Bij een DELETE-verzoek gebruikt het endpoint de artist_id parameter in de URL om de overeenkomstige artiest in de database te lokaliseren.
* Als de artiest wordt gevonden, wordt deze, samen met alle bijbehorende gegevens (gerelateerde CD's en de daarbijhorende reviews), verwijderd uit de database.
* Als de artiest niet wordt gevonden, geeft het endpoint een 404-foutmelding met de boodschap **Artist not found** terug, wat aangeeft dat de artiest niet bestaat of al verwijderd is.

### Response:

* Er zijn geen body-parameters vereist voor dit verzoek. De actie wordt geheel gestuurd door de **artist_id** parameter in de URL.
* Bij succesvolle verwijdering geeft het endpoint een response terug met de gegevens van de verwijderde artiest, als bevestiging van de actie.
* Bij een fout (zoals een niet-bestaande artiest) geeft het een passende foutmelding, **Artist not found** terug.

### Gebruik:

* Om een artiest met een specifiek ID te verwijderen: **DELETE /artists/{artist_id}**

## ENDPOINT: DELETE /artists/by-name/{artist_name}

Dit endpoint stelt gebruikers in staat om een artiest uit de database te verwijderen op basis van de naam van de parameter **artist_name**. Dit is handig in situaties waar de unieke ID van de artiest niet bekend is, maar de naam wel. Bij het verwijderen van een artiest, worden ook gelijk alle bijhorende cd's en de daarbijhorende reviews verwijderd.

![DELETE ARTIST on name](https://github.com/ArneBogaerts/APIBasisproject/assets/113974569/34cd5b2a-181f-4c65-8f55-5d6dda50f3bd)
![DELETE ARTIST on name notfound](https://github.com/ArneBogaerts/APIBasisproject/assets/113974569/89a7a2c2-aa88-44e4-af72-9fc9cfba8e76)

### Data verwijderen:

* Bij een DELETE-verzoek gebruikt het endpoint de **artist_name** parameter in de URL om de overeenkomstige artiest in de database te vinden.
* Als de artiest met de opgegeven naam wordt gevonden, wordt deze verwijderd uit de database. Ook de daarbijhorende gegevens (gerelateerde CD's en de daarbijhorende reviews) worden hierdoor mee verwijderd.
* Als er geen artiest met die naam wordt gevonden, geeft het endpoint een 404-foutmelding, **Artist not found** terug, wat aangeeft dat de artiest niet bestaat onder de opgegeven naam.

### Response:

* Er zijn geen body-parameters vereist voor dit verzoek. De actie wordt gestuurd door de artist_name parameter in de URL.
* Bij succesvolle verwijdering geeft het endpoint een response terug met de gegevens van de verwijderde artiest, als bevestiging van de actie.
* Bij een foutmelding (bijvoorbeeld als de artiest niet gevonden kan worden) geeft het een passende foutmelding, **Artist not found** terug.

### Gebruik:

* Om een artiest met een specifieke naam te verwijderen: **DELETE /artists/by-name/{artist_name}**

## ENDPOINT: DELETE /cds/by-title/{cd_title}

Dit endpoint maakt het mogelijk om een CD uit de database te verwijderen op basis van de titel van de CD (cd_title). Dit is vooral handig wanneer de unieke ID van de CD niet bekend is, maar de titel wel.

![DELETE CD onname](https://github.com/ArneBogaerts/APIBasisproject/assets/113974569/89ed590a-f89e-49fc-8ecc-d860f8c65c83)
![DELETE CD onname notfound](https://github.com/ArneBogaerts/APIBasisproject/assets/113974569/25d4df59-6d9e-4358-92af-daf89e122c24)

### Data verwijderen:

* Bij een DELETE-verzoek gebruikt het endpoint de cd_title parameter in de URL om de betreffende CD in de database te zoeken.
* Als de CD met de opgegeven titel wordt gevonden, wordt deze, inclusief alle gerelateerde informatie en recensies, verwijderd uit de database.
* Als er geen CD met die titel wordt gevonden, geeft het endpoint een 404-foutmelding, **CD not found** terug, wat aangeeft dat de CD niet bestaat onder de opgegeven titel.

### Response:

* Er zijn geen body-parameters nodig voor dit verzoek. De actie wordt volledig gestuurd door de cd_title parameter in de URL.
* Bij succesvolle verwijdering geeft het endpoint een response terug met de gegevens van de verwijderde CD, ter bevestiging van de actie.
* Bij een fout (zoals het niet vinden van de CD) wordt een passende foutmelding, **CD not found** teruggestuurd.
