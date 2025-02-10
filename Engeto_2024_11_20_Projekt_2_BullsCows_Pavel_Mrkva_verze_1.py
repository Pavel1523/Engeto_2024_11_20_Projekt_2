# projekt_2.py: druhý projekt do Engeto Online Python Akademie, verze 1
# Bulls & Cows
# author: Ing. Pavel Mrkva
# email: pavel.mrkva@seznam.cz


import time
import random


def gen_cisla():
    """Vygeneruje 4-mistne cislo bez opakovani cislic a s nenulovym zacatkem."""
    prvni = random.choice(range(1, 10))  # rrvni cislo nesmi byt nula
    dalsi = random.sample(range(10), 3)  # zbytek cisla
    while prvni in dalsi:
        dalsi = random.sample(
            range(10), 3
        )  # znovu vybereme, pokud by se opakovalo
    return str(prvni) + "".join(map(str, dalsi))


def pocitani_byku_a_krav(cislo_pc, cislo_hrac):
    """Spocita mnozstvi byku a krav."""
    bull = 0
    cow = 0
    for c, d in zip(cislo_pc, cislo_hrac):
        if c == d:
            bull += 1
    for e in cislo_hrac:
        if e in cislo_pc:
            cow = cow + 1
    cow = cow - bull
    return bull, cow


def mnozna_cisla(**kwargs):
    """Vraci mnozna cisla podstatnych jmen podle prirazeneho mnozstvi."""
    vysledky = []
    for klic, hodnota in kwargs.items():
        if hodnota == 1:
            vysledky.append(klic)  # jednotne cislo
        else:
            # Pokud slovo konci na 's', 'x', 'z' nebo 'ch', 'sh'

            if klic.endswith(("s", "x", "z")) or klic.endswith(("ch", "sh")):
                vysledky.append(klic + "es")  # mnozne cislo
            # Pokud slovo konci na 'y', ale před 'y' je samohláska (a, e, i, o, u)

            elif klic.endswith("y") and klic[-2] in "aeiou":
                vysledky.append(klic + "s")  # mnozne cislo
            # Pokud slovo konci na 'y' a před 'y' je souhlaska, změníme 'y' na 'ies'

            elif klic.endswith("y"):
                vysledky.append(klic + "ies")  # mnozne cislo
            # Ve vsech ostatnich pripadech pridame jen 's'

            else:
                vysledky.append(klic + "s")  # mnozne cislo
    return vysledky if len(vysledky) > 1 else vysledky[0]


def prevod_sec_min(cas):
    minuta = int(cas // 60)
    vterina = round(cas % 60)
    return minuta, vterina


def bulls_and_cows():
    hledane_cislo = gen_cisla()  # viz popis funkce
    pokus_max = 20  # maximalni pocet pokusu k uhodnuti generovaneho cisla
    att = mnozna_cisla(attempt=pokus_max)  # viz popis funkce

    print(
        f"Hi there!\n"
        f"Let's play a 'Bulls and Cows' game.\n"
        f"{'-' * 85}\n"
        f"Rules:\n"
        f"   Enter your 4-digit number.\n"
        f"   All digits in your number must be unique and the number doesn't start with 'zero'.\n"
        f"   You have a maximum of {pokus_max} {att} in one game.\n"
        f"{'-' * 85}\n"
        f"I've generated my 4-digit number right now.\n"
        f"Now it's your turn.\n"
        f"Enter a number.\n"
        f"{'=' * 85}"
    )

    cas_zahajeni = time.time()

    pokus = 0
    while pokus < pokus_max:  # start procedury hadani generovaneho cisla
        pokus += 1
        pokus_rest = pokus_max - pokus
        jed_1 = mnozna_cisla(attempt=pokus_rest)

        user_volba = input("Enter a number: ")  # volba cisla uzivatelem
        if not (
            user_volba.isdigit()
            and len(user_volba) == 4
            and len(set(user_volba)) == 4
            and user_volba[0] != "0"
        ):  # Kontrola, zda je vstup platny - ciselne znaky na vstupu, 4 cisla na vstupu, 4 unikatni cisla na vstupu, na zacatku neni nula
            print(
                f"Wrong number!\nIt must be a 4-digit number with unique digits that cannot start with a 'zero'."
            )
            print(
                f"There are still {pokus_max - pokus} {jed_1} left.\n{'-' * 85}"
            )
            continue
        print("Your enter is:  ", user_volba)

        bulls, cows = pocitani_byku_a_krav(hledane_cislo, user_volba)

        jed_2, jed_3 = mnozna_cisla(bull=bulls, cow=cows)
        print(
            f"Result:{' ' *10}{jed_2}: {bulls}, {jed_3}: {cows}\n"
            f"There are still {pokus_max - pokus} {jed_1} left.\n"
            f"{'-' * 85}"
        )

        if bulls == 4:  # uzivatel uhodnul cislo
            print(
                f"Congratulations!\nYou have guessed the secret number '{hledane_cislo}' in {pokus} {jed_1}."
            )
            break
    if pokus == pokus_max and bulls < 4:  # uzivatel neuhodnul cislo
        print(
            f"All attempts are used up!\n"
            f"The secret number was: {hledane_cislo}."
        )
    cas_ukonceni = time.time()
    doba_hry = cas_ukonceni - cas_zahajeni
    minute, second = prevod_sec_min(doba_hry)
    print(f"Game time:{' ' * 7}{minute} min. and {second} sec..")
    print(f"{'-' * 85}")


if __name__ == "__main__":
    # zahajeni hry

    bulls_and_cows()