#!/usr/bin/python3
import argparse
import configparser
import functools
import os
import sys
import time
CONFIG = {}
def read_config(filename):
    if not os.path.isfile(filename):
        print(f"Could not get configuration file {filename} !")
        sys.exit("Bye...")

    # Initialize configuration file
    global CONFIG
    CONFIG = {}

    # Reads configuration file
    config = configparser.ConfigParser()
    config.read(filename)

    # Update global configuration with configuration settings
    CONFIG["global"] = {
        "years": [year.strip() for year in config.get("years", "years").split(",")],
        "chars": [char.strip() for char in config.get("specialchars", "chars").split(",")],
        "numfrom": config.getint("nums", "from"),
        "numto": config.getint("nums", "to"),
        "wcfrom": config.getint("nums", "wcfrom"),
        "wcto": config.getint("nums", "wcto"),
        "threshold": config.getint("nums", "threshold"),
    }

    # Initialize leet mode configs
    leet = functools.partial(config.get, "leet")
    letters = {"a", "i", "e", "t", "o", "s", "g", "z"}
    CONFIG["LEET"] = {letter: leet(letter) for letter in letters}

    return True

def logo():
    print(r"""
  _____                     __  __ ______ 
 / ____|                   |  \/  |  ____|
| |  __ _   _  ___  ___ ___| \  / | |__   
| | |_ | | | |/ _ \/ __/ __| |\/| |  __|  
| |__| | |_| |  __/\__ \__ \ |  | | |____ 
 \_____|\__,_|\___||___/___/_|  |_|______|

|--------------------------------------------------------------------|
| Created By: Krishna Gopal Jha                                      |
| Checkout my LinkedIn: https://www.linkedin.com/in/krishnagopaljha/ |
| Lookup at my insta: https://instagram.com/theindianpsych           |
|--------------------------------------------------------------------| 
          """)


def make_leet(x):
    for letter, leetletter in CONFIG["LEET"].items():
        x = x.replace(letter, leetletter)
    return x


def concatenation(seq, start, stop):
    for mystr in seq:
        for num in range(start, stop):
            yield mystr + str(num)


def generate_combinations(seq, start, special=""):
    for mystr in seq:
        for mystr1 in start:
            yield mystr + special + mystr1


def print_to_file(filename, unique_list_finished):
    f = open(filename, "w")
    unique_list_finished.sort()
    f.write(os.linesep.join(unique_list_finished))
    f.close()
    f = open(filename, "r")
    lines = 0
    for line in f:
        lines += 1
    f.close()
    print(
        "[+] Saving Wordlist to \033[1;32m"
        + filename
        + "\033[1;m, counting \033[1;32m"
        + str(lines)
        + " words.\033[1;m"
    )



def interactive():

    print("\r\n[+] Provide the information about the victim to make a Wordlist")
    print("[+] You can leave blank if you are unaware of any of those information! ;)\r\n")

    profile = {}

    name = input("> First Name: ").lower()
    while len(name) == 0 or name == " " or name == "  " or name == "   ":
        print("\r\n[-] A name is required! ")
        name = input("> Name: ").lower()
    profile["name"] = str(name)

    profile["surname"] = input("> Surname: ").lower()
    profile["nick"] = input("> Nickname: ").lower()
    birthdate = input("> Birthdate (DDMMYYYY): ")
    while len(birthdate) != 0 and len(birthdate) != 8:
        print("\r\n[-] You must enter 8 digits for birthday!")
        birthdate = input("> Birthdate (DDMMYYYY): ")
    profile["birthdate"] = str(birthdate)

    print("\r\n")

    profile["wife"] = input("> Partners) name: ").lower()
    profile["wifen"] = input("> Partners) nickname: ").lower()
    wifeb = input("> Partners) birthdate (DDMMYYYY): ")
    while len(wifeb) != 0 and len(wifeb) != 8:
        print("\r\n[-] You must enter 8 digits for birthday!")
        wifeb = input("> Partners birthdate (DDMMYYYY): ")
    profile["wifeb"] = str(wifeb)
    print("\r\n")

    profile["kid"] = input("> Child's name: ").lower()
    profile["kidn"] = input("> Child's nickname: ").lower()
    kidb = input("> Child's birthdate (DDMMYYYY): ")
    while len(kidb) != 0 and len(kidb) != 8:
        print("\r\n[-] You must enter 8 digits for birthday!")
        kidb = input("> Child's birthdate (DDMMYYYY): ")
    profile["kidb"] = str(kidb)
    print("\r\n")

    profile["pet"] = input("> Pet's name: ").lower()
    profile["company"] = input("> Company name: ").lower()
    print("\r\n")

    profile["words"] = [""]
    words1 = input(
        "> Do you want to add some key words about the victim? Y/N: "
    ).lower()
    words2 = ""
    if words1 == "y":
        words2 = input(
            "> Please enter the words, separated by comma. [i.e. hacker,developer,gamer], spaces will be removed: "
        ).replace(" ", "")
    profile["words"] = words2.split(",")

    profile["spechars1"] = input(
        "> Do you want to add special chars at the end of words? Y/N: "
    ).lower()

    profile["randnum"] = input(
        "> Do you want to add some random numbers at the end of words? Y/N:"
    ).lower()
    profile["leetmode"] = input("> Leet mode? (i.e. password = p4ssw0rd) Y/N: ").lower()

    generate_wordlist_from_profile(profile)  


def generate_wordlist_from_profile(profile):

    chars = CONFIG["global"]["chars"]
    years = CONFIG["global"]["years"]
    numfrom = CONFIG["global"]["numfrom"]
    numto = CONFIG["global"]["numto"]

    profile["spechars"] = []

    if profile["spechars1"] == "y":
        for spec1 in chars:
            profile["spechars"].append(spec1)
            for spec2 in chars:
                profile["spechars"].append(spec1 + spec2)
                for spec3 in chars:
                    profile["spechars"].append(spec1 + spec2 + spec3)

    print("\r\n[+] Now making a Wordlist...")

    birthdate_yy = profile["birthdate"][-2:]
    birthdate_yyy = profile["birthdate"][-3:]
    birthdate_yyyy = profile["birthdate"][-4:]
    birthdate_xd = profile["birthdate"][1:2]
    birthdate_xm = profile["birthdate"][3:4]
    birthdate_dd = profile["birthdate"][:2]
    birthdate_mm = profile["birthdate"][2:4]

    wifeb_yy = profile["wifeb"][-2:]
    wifeb_yyy = profile["wifeb"][-3:]
    wifeb_yyyy = profile["wifeb"][-4:]
    wifeb_xd = profile["wifeb"][1:2]
    wifeb_xm = profile["wifeb"][3:4]
    wifeb_dd = profile["wifeb"][:2]
    wifeb_mm = profile["wifeb"][2:4]

    kidb_yy = profile["kidb"][-2:]
    kidb_yyy = profile["kidb"][-3:]
    kidb_yyyy = profile["kidb"][-4:]
    kidb_xd = profile["kidb"][1:2]
    kidb_xm = profile["kidb"][3:4]
    kidb_dd = profile["kidb"][:2]
    kidb_mm = profile["kidb"][2:4]

    nameup = profile["name"].title()
    surnameup = profile["surname"].title()
    nickup = profile["nick"].title()
    wifeup = profile["wife"].title()
    wifenup = profile["wifen"].title()
    kidup = profile["kid"].title()
    kidnup = profile["kidn"].title()
    petup = profile["pet"].title()
    companyup = profile["company"].title()

    wordsup = []
    wordsup = list(map(str.title, profile["words"]))

    word = profile["words"] + wordsup

    # reverse a name

    rev_name = profile["name"][::-1]
    rev_nameup = nameup[::-1]
    rev_nick = profile["nick"][::-1]
    rev_nickup = nickup[::-1]
    rev_wife = profile["wife"][::-1]
    rev_wifeup = wifeup[::-1]
    rev_kid = profile["kid"][::-1]
    rev_kidup = kidup[::-1]

    reverse = [
        rev_name,
        rev_nameup,
        rev_nick,
        rev_nickup,
        rev_wife,
        rev_wifeup,
        rev_kid,
        rev_kidup,
    ]
    rev_n = [rev_name, rev_nameup, rev_nick, rev_nickup]
    rev_w = [rev_wife, rev_wifeup]
    rev_k = [rev_kid, rev_kidup]

    bds = [
        birthdate_yy,
        birthdate_yyy,
        birthdate_yyyy,
        birthdate_xd,
        birthdate_xm,
        birthdate_dd,
        birthdate_mm,
    ]

    bdss = []

    for bds1 in bds:
        bdss.append(bds1)
        for bds2 in bds:
            if bds.index(bds1) != bds.index(bds2):
                bdss.append(bds1 + bds2)
                for bds3 in bds:
                    if (
                        bds.index(bds1) != bds.index(bds2)
                        and bds.index(bds2) != bds.index(bds3)
                        and bds.index(bds1) != bds.index(bds3)
                    ):
                        bdss.append(bds1 + bds2 + bds3)

    wbds = [wifeb_yy, wifeb_yyy, wifeb_yyyy, wifeb_xd, wifeb_xm, wifeb_dd, wifeb_mm]

    wbdss = []

    for wbds1 in wbds:
        wbdss.append(wbds1)
        for wbds2 in wbds:
            if wbds.index(wbds1) != wbds.index(wbds2):
                wbdss.append(wbds1 + wbds2)
                for wbds3 in wbds:
                    if (
                        wbds.index(wbds1) != wbds.index(wbds2)
                        and wbds.index(wbds2) != wbds.index(wbds3)
                        and wbds.index(wbds1) != wbds.index(wbds3)
                    ):
                        wbdss.append(wbds1 + wbds2 + wbds3)

    kbds = [kidb_yy, kidb_yyy, kidb_yyyy, kidb_xd, kidb_xm, kidb_dd, kidb_mm]

    kbdss = []

    for kbds1 in kbds:
        kbdss.append(kbds1)
        for kbds2 in kbds:
            if kbds.index(kbds1) != kbds.index(kbds2):
                kbdss.append(kbds1 + kbds2)
                for kbds3 in kbds:
                    if (
                        kbds.index(kbds1) != kbds.index(kbds2)
                        and kbds.index(kbds2) != kbds.index(kbds3)
                        and kbds.index(kbds1) != kbds.index(kbds3)
                    ):
                        kbdss.append(kbds1 + kbds2 + kbds3)

    generate_combinationsinaac = [profile["pet"], petup, profile["company"], companyup]

    generate_combinationsina = [
        profile["name"],
        profile["surname"],
        profile["nick"],
        nameup,
        surnameup,
        nickup,
    ]

    generate_combinationsinaw = [
        profile["wife"],
        profile["wifen"],
        wifeup,
        wifenup,
        profile["surname"],
        surnameup,
    ]

    generate_combinationsinak = [
        profile["kid"],
        profile["kidn"],
        kidup,
        kidnup,
        profile["surname"],
        surnameup,
    ]

    generate_combinationsinaa = []
    for generate_combinationsina1 in generate_combinationsina:
        generate_combinationsinaa.append(generate_combinationsina1)
        for generate_combinationsina2 in generate_combinationsina:
            if generate_combinationsina.index(generate_combinationsina1) != generate_combinationsina.index(generate_combinationsina2) and generate_combinationsina.index(
                generate_combinationsina1.title()
            ) != generate_combinationsina.index(generate_combinationsina2.title()):
                generate_combinationsinaa.append(generate_combinationsina1 + generate_combinationsina2)

    generate_combinationsinaaw = []
    for generate_combinationsina1 in generate_combinationsinaw:
        generate_combinationsinaaw.append(generate_combinationsina1)
        for generate_combinationsina2 in generate_combinationsinaw:
            if generate_combinationsinaw.index(generate_combinationsina1) != generate_combinationsinaw.index(generate_combinationsina2) and generate_combinationsinaw.index(
                generate_combinationsina1.title()
            ) != generate_combinationsinaw.index(generate_combinationsina2.title()):
                generate_combinationsinaaw.append(generate_combinationsina1 + generate_combinationsina2)

    generate_combinationsinaak = []
    for generate_combinationsina1 in generate_combinationsinak:
        generate_combinationsinaak.append(generate_combinationsina1)
        for generate_combinationsina2 in generate_combinationsinak:
            if generate_combinationsinak.index(generate_combinationsina1) != generate_combinationsinak.index(generate_combinationsina2) and generate_combinationsinak.index(
                generate_combinationsina1.title()
            ) != generate_combinationsinak.index(generate_combinationsina2.title()):
                generate_combinationsinaak.append(generate_combinationsina1 + generate_combinationsina2)

    generate_combinationsi = {}
    generate_combinationsi[1] = list(generate_combinations(generate_combinationsinaa, bdss))
    generate_combinationsi[1] += list(generate_combinations(generate_combinationsinaa, bdss, "_"))
    generate_combinationsi[2] = list(generate_combinations(generate_combinationsinaaw, wbdss))
    generate_combinationsi[2] += list(generate_combinations(generate_combinationsinaaw, wbdss, "_"))
    generate_combinationsi[3] = list(generate_combinations(generate_combinationsinaak, kbdss))
    generate_combinationsi[3] += list(generate_combinations(generate_combinationsinaak, kbdss, "_"))
    generate_combinationsi[4] = list(generate_combinations(generate_combinationsinaa, years))
    generate_combinationsi[4] += list(generate_combinations(generate_combinationsinaa, years, "_"))
    generate_combinationsi[5] = list(generate_combinations(generate_combinationsinaac, years))
    generate_combinationsi[5] += list(generate_combinations(generate_combinationsinaac, years, "_"))
    generate_combinationsi[6] = list(generate_combinations(generate_combinationsinaaw, years))
    generate_combinationsi[6] += list(generate_combinations(generate_combinationsinaaw, years, "_"))
    generate_combinationsi[7] = list(generate_combinations(generate_combinationsinaak, years))
    generate_combinationsi[7] += list(generate_combinations(generate_combinationsinaak, years, "_"))
    generate_combinationsi[8] = list(generate_combinations(word, bdss))
    generate_combinationsi[8] += list(generate_combinations(word, bdss, "_"))
    generate_combinationsi[9] = list(generate_combinations(word, wbdss))
    generate_combinationsi[9] += list(generate_combinations(word, wbdss, "_"))
    generate_combinationsi[10] = list(generate_combinations(word, kbdss))
    generate_combinationsi[10] += list(generate_combinations(word, kbdss, "_"))
    generate_combinationsi[11] = list(generate_combinations(word, years))
    generate_combinationsi[11] += list(generate_combinations(word, years, "_"))
    generate_combinationsi[12] = [""]
    generate_combinationsi[13] = [""]
    generate_combinationsi[14] = [""]
    generate_combinationsi[15] = [""]
    generate_combinationsi[16] = [""]
    generate_combinationsi[21] = [""]
    if profile["randnum"] == "y":
        generate_combinationsi[12] = list(concatenation(word, numfrom, numto))
        generate_combinationsi[13] = list(concatenation(generate_combinationsinaa, numfrom, numto))
        generate_combinationsi[14] = list(concatenation(generate_combinationsinaac, numfrom, numto))
        generate_combinationsi[15] = list(concatenation(generate_combinationsinaaw, numfrom, numto))
        generate_combinationsi[16] = list(concatenation(generate_combinationsinaak, numfrom, numto))
        generate_combinationsi[21] = list(concatenation(reverse, numfrom, numto))
    generate_combinationsi[17] = list(generate_combinations(reverse, years))
    generate_combinationsi[17] += list(generate_combinations(reverse, years, "_"))
    generate_combinationsi[18] = list(generate_combinations(rev_w, wbdss))
    generate_combinationsi[18] += list(generate_combinations(rev_w, wbdss, "_"))
    generate_combinationsi[19] = list(generate_combinations(rev_k, kbdss))
    generate_combinationsi[19] += list(generate_combinations(rev_k, kbdss, "_"))
    generate_combinationsi[20] = list(generate_combinations(rev_n, bdss))
    generate_combinationsi[20] += list(generate_combinations(rev_n, bdss, "_"))
    generate_combinations001 = [""]
    generate_combinations002 = [""]
    generate_combinations003 = [""]
    generate_combinations004 = [""]
    generate_combinations005 = [""]
    generate_combinations006 = [""]
    if len(profile["spechars"]) > 0:
        generate_combinations001 = list(generate_combinations(generate_combinationsinaa, profile["spechars"]))
        generate_combinations002 = list(generate_combinations(generate_combinationsinaac, profile["spechars"]))
        generate_combinations003 = list(generate_combinations(generate_combinationsinaaw, profile["spechars"]))
        generate_combinations004 = list(generate_combinations(generate_combinationsinaak, profile["spechars"]))
        generate_combinations005 = list(generate_combinations(word, profile["spechars"]))
        generate_combinations006 = list(generate_combinations(reverse, profile["spechars"]))

    print("[+] Sorting list and removing duplicates...")

    generate_combinations_unique = {}
    for i in range(1, 22):
        generate_combinations_unique[i] = list(dict.fromkeys(generate_combinationsi[i]).keys())

    generate_combinations_unique01 = list(dict.fromkeys(generate_combinationsinaa).keys())
    generate_combinations_unique02 = list(dict.fromkeys(generate_combinationsinaac).keys())
    generate_combinations_unique03 = list(dict.fromkeys(generate_combinationsinaaw).keys())
    generate_combinations_unique04 = list(dict.fromkeys(generate_combinationsinaak).keys())
    generate_combinations_unique05 = list(dict.fromkeys(word).keys())
    generate_combinations_unique07 = list(dict.fromkeys(generate_combinations001).keys())
    generate_combinations_unique08 = list(dict.fromkeys(generate_combinations002).keys())
    generate_combinations_unique09 = list(dict.fromkeys(generate_combinations003).keys())
    generate_combinations_unique010 = list(dict.fromkeys(generate_combinations004).keys())
    generate_combinations_unique011 = list(dict.fromkeys(generate_combinations005).keys())
    generate_combinations_unique012 = list(dict.fromkeys(generate_combinations006).keys())

    uniqlist = (
        bdss
        + wbdss
        + kbdss
        + reverse
        + generate_combinations_unique01
        + generate_combinations_unique02
        + generate_combinations_unique03
        + generate_combinations_unique04
        + generate_combinations_unique05
    )

    for i in range(1, 21):
        uniqlist += generate_combinations_unique[i]

    uniqlist += (
        generate_combinations_unique07
        + generate_combinations_unique08
        + generate_combinations_unique09
        + generate_combinations_unique010
        + generate_combinations_unique011
        + generate_combinations_unique012
    )
    unique_lista = list(dict.fromkeys(uniqlist).keys())
    unique_leet = []
    if profile["leetmode"] == "y":
        for (
            x
        ) in (
            unique_lista
        ): 

            x = make_leet(x) 
            unique_leet.append(x)

    unique_list = unique_lista + unique_leet

    unique_list_finished = []
    unique_list_finished = [
        x
        for x in unique_list
        if len(x) < CONFIG["global"]["wcto"] and len(x) > CONFIG["global"]["wcfrom"]
    ]

    print_to_file(profile["name"] + ".txt", unique_list_finished)

def mkdir_if_not_exists(dire):
    if not os.path.isdir(dire):
        os.mkdir(dire)


def main():

    read_config(os.path.join(os.path.dirname(os.path.realpath(__file__)), "guessme.cfg"))

    parser = get_parser()
    args = parser.parse_args()

    if args.interactive:
        logo()
        interactive()
    else:
        parser.print_help()

def get_parser():
    parser = argparse.ArgumentParser(
        description="GuessME (guessme)\n"
    )
    
    parser.add_argument(
        "-i",
        "--interactive",
        action="store_true",
        help="Start interactive mode"
    )

    return parser


if __name__ == "__main__":
    main()