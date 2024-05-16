text = "OZ Aj Ty v IT vzniklo v roku 2012 s cieľom motivovať a podporovať dievčatá a ženy v IT oblasti. Venuje sa práci s dievčatami od 8 rokov, cez stredné školy až po špeciálne vzdelávacie programy určené pre staršie ženy, ktorých cieľom je pomôcť im rozbehnúť kariéru v IT sfére. Intenzívne spolupracuje s IT fakultami vysokých škôl a pomáha im zvyšovať počet študentiek."

# Vytvorte slovník pre uchovanie počtu výskytov samohlások
samohlasky = {'a': 0, 'á': 0, 'A': 0, 'Á': 0, 'ä': 0, 'Ä': 0,
              'e': 0, 'é': 0, 'E': 0, 'É': 0,
              'i': 0, 'í': 0, 'I': 0, 'Í': 0,
              'o': 0, 'ó': 0, 'O': 0, 'Ó': 0, 'ô': 0,
              'u': 0, 'ú': 0, 'U': 0, 'Ú': 0,
              'y': 0, 'ý': 0,'Y': 0, 'Ý': 0}

# Prejdite cez každý znak v texte a zvýšte počet výskytov pre samohlásky
for char in text:
    if char in samohlasky:
        samohlasky[char] += 1

# Vytlačte výsledky
for samohlaska, pocet in samohlasky.items():
    print(f"{samohlaska}: {pocet}")

# Vypočítajte celkový počet samohlások
celkovy_pocet_samohlasok = sum(samohlasky.values())
print("Celkový počet samohlások:", celkovy_pocet_samohlasok)
