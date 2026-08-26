# azure-novatrix

Microsoft Azure course – Novatrix AB  

Student: Farideh Dehghan

## Week 34 – Uppgift 1: Compute och kom igång

Azure-miljön och resursgruppen `rg-novatrix` skapades under vecka 34. En virtuell server med tillhörande nätverksresurser körs i regionen Sweden Central.

## Week 35 – Uppgift 2: IAM och identitet

### Microsoft Entra ID

Följande användare och grupper skapades:

- Användare: `Drift Novatrix`

- Användare: `Utveckling Novatrix`

- Grupp: `Novatrix-Drift`

- Grupp: `Novatrix-Utveckling`

Användarna placerades i respektive grupp för att behörigheter ska kunna hanteras via grupper i stället för individuellt.

### RBAC och least privilege

Rollerna tilldelades på resursgruppen `rg-novatrix`:

| Grupp | Azure-roll | Omfattning | Motivering |

|---|---|---|---|

| `Novatrix-Drift` | `Deltagare` (Contributor) | `rg-novatrix` | Driftteamet behöver kunna skapa, ändra och hantera resurser, men ska inte kunna tilldela behörigheter till andra. |

| `Novatrix-Utveckling` | `Läsare` (Reader) | `rg-novatrix` | Utvecklingsteamet behöver kunna se resurser och konfigurationer men inte ändra eller radera dem. |

Rollerna följer principen om least privilege eftersom varje grupp endast har den åtkomst som krävs för arbetsuppgifterna.

### Hanterad identitet

En användartilldelad hanterad identitet skapades:

- Namn: `id-novatrix-app`

- Resursgrupp: `rg-novatrix`

- Region: `Sweden Central`

- Tilldelade roller: inga

Identiteten ska senare användas av applikationen för åtkomst till lagring utan användarnamn, lösenord eller andra hemligheter i koden.

### Verifiering

Behörigheterna verifierades med funktionen **Kontrollera åtkomst** i Azure IAM:

- `Novatrix-Drift` har rollen `Deltagare`.

- `Novatrix-Utveckling` har rollen `Läsare`.

- Rollernas omfattning är resursgruppen `rg-novatrix`.

- Den hanterade identiteten har ännu ingen behörighet.

