# Examination vecka 41 – Automation och integration

**Student:** Farideh Dehghannejad  

**Företag:** Novatrix AB

## Syfte

En felanmälan ska registreras i SharePoint och automatiskt ge information till ansvarig förvaltare.

## Val av lösning

Jag valde Power Automate eftersom lösningen redan använder Microsoft 365. Power Automate kan kopplas direkt till SharePoint, Outlook och Teams och kräver ingen separat kodtjänst. Lärarens förtydligande tillåter denna lösning.

## Arbetsflöde

1. En felanmälan registreras i SharePoint-listan **Felanmälan**.

2. Flödet startar när ett nytt objekt skapas i listan.

3. Ett e-postmeddelande skickas till fältet **Ansvarig Email**. Meddelandet innehåller rubrik, beskrivning och prioritet.

4. Ett meddelande publiceras i Teams-kanalen **Skötsel** i teamet **Dunderhem Förvaltning**.

## Test

Jag skapade testärenden och kontrollerade att meddelanden kom fram i Teams och Outlook.

## Byta anslutet konto

Öppna flödet i Power Automate. Välj **Ändra anslutningsreferens** vid SharePoint-, Outlook- eller Teams-anslutningen. Välj ett behörigt Microsoft 365-konto, logga in på nytt och spara flödet. Kör sedan ett test för att kontrollera anslutningen.

