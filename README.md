## Autors
- **Vārds:** Ēriks Stovba  
- **Studenta ID:** 241RDB351  
- **Kurss:** DE0008 Datu un struktūra

# homework-organizer
Mājasdarbu pārvaldnieks

# Mājasdarbu organizators
## Projekta mērķis

Izveidot konsoles lietotni Python valodā, kas ļauj studentiem pārvaldīt mājasdarbus: pievienot, apskatīt, dzēst un arhivēt uzdevumus pēc termiņa. 
Projekts automatizē ikdienas uzdevumu sekošanu un termiņu pārvaldību.

## Izmantotās Python bibliotēkas
- `datetime` – termiņu salīdzināšanai
- `os` – failu pārbaudei un darbībām ar failiem
- `colorama` – krāsainam teksta izvadei konsolē

> Lai izmantotu `colorama`, nepieciešams:
pip install colorama

## Galvenās funkcijas
- Pievienot jaunu mājasdarbu
- Parādīt visus aktīvos uzdevumus (kārtoti pēc termiņa)
- Dzēst uzdevumu pēc izvēles
- Automātiski arhivēt nokavētos uzdevumus
- Apskatīt arhīvu
- Krāsaina termiņu norāde (sarkans/dzeltens/zaļš)

## Lietošanas instrukcija
1. Palaist `main.py` ar Python 3:
python main.py
2. Sekot izvēlnei:
   - 1 – pievienot uzdevumu
   - 2 – apskatīt aktīvos
   - 3 – dzēst
   - 4 – iziet
   - 5 – apskatīt arhīvu

## Datu glabāšana
- Aktīvie uzdevumi → `tasks.txt`
- Arhīvs (nokavētie) → `archive.txt`

