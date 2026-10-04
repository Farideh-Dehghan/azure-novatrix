# Vecka 40 – Uppgift 7: Virtualiseringsnivåer

**Student:** Farideh Dehghannejad  

**Kurs:** Microsoft Azure  

**Företag:** Novatrix AB  

## Syfte

Syftet med uppgiften är att undersöka och jämföra tre olika virtualiseringsnivåer: virtuell maskin, container och serverless.

Novatrix kundtjänst har tidigare körts på en virtuell maskin. I den här uppgiften ska mottagningen av kundärenden köras på en alternativ nivå.

## Vald lösning

Jag har valt att använda Azure Functions och serverless. Funktionen ska ta emot ett kundärende via en HTTP-förfrågan och returnera ett svar.

Azure Functions valdes eftersom lösningen är lämplig för en mindre funktion som endast behöver köras när ett nytt ärende skickas in.

## Plan

1. Skapa en Azure Function.

2. Konfigurera en HTTP-trigger.

3. Lägga in kod för att ta emot kundärenden.

4. Testa funktionen.

5. Dokumentera resultatet med bilder.

6. Jämföra VM, containers och serverless.

## Filer

Kod, testresultat och dokumentation läggs till i den här mappen under arbetets gång.

