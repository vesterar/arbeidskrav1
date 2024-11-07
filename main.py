"""
Arbeidskrav1
Enkelt program for bergening av kostnader for henholdsvis bensinbil og elbil,
samt differensen av kostnader mellom biltypene.
"""

# variabler brukt for beregning av kostnader per år.
km_year = 20000
forsikring_el = 5000
forsikring_bensin = 7500
trafikkforsikringsavgift = (8.38*365)
drivfsoff_el = (0.2*2*km_year)
drivfsoff_bensin = (1*km_year)
bom_el = (0.1*km_year)
bom_bensin = (0.3*km_year)

# kalkulering av årlige kostnader for bensin og elbil.
tot_kost_el = round(forsikring_el + trafikkforsikringsavgift + drivfsoff_el + bom_el)
tot_kost_bensin = round(forsikring_bensin + trafikkforsikringsavgift + drivfsoff_bensin + bom_bensin)
diff_bensin_el = round(tot_kost_bensin - tot_kost_el)

# Presentasjon av årlige kostnader.
print(f"Den totale årlige kostnaden for bensinbil er kr {tot_kost_bensin},-")
print(f"Den totale årlige kostnaden for elbil er kr {tot_kost_el},-")
print(f"Årlig kostnadsdifferanse mellom bensin og elbil er på kr {diff_bensin_el},-")
