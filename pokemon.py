import csv

#intialize the counter variables for each type of each generation
gen_1_psychic = 0
gen_1_ice = 0
gen_1_flying = 0
gen_1_ground = 0
gen_1_electric = 0
gen_1_normal = 0
gen_1_water = 0
gen_1_fire = 0
gen_1_fairy = 0
gen_1_rock = 0
gen_1_dark = 0
gen_1_bug = 0
gen_1_poison = 0
gen_1_ghost = 0
gen_1_fighting = 0
gen_1_dragon = 0
gen_1_grass = 0
gen_1_steel = 0

gen_2_psychic = 0
gen_2_ice = 0
gen_2_flying = 0
gen_2_ground = 0
gen_2_electric = 0
gen_2_normal = 0
gen_2_water = 0
gen_2_fire = 0
gen_2_fairy = 0
gen_2_rock = 0
gen_2_dark = 0
gen_2_bug = 0
gen_2_poison = 0
gen_2_ghost = 0
gen_2_fighting = 0
gen_2_dragon = 0
gen_2_grass = 0
gen_2_steel = 0

gen_3_psychic = 0
gen_3_ice = 0
gen_3_flying = 0
gen_3_ground = 0
gen_3_electric = 0
gen_3_normal = 0
gen_3_water = 0
gen_3_fire = 0
gen_3_fairy = 0
gen_3_rock = 0
gen_3_dark = 0
gen_3_bug = 0
gen_3_poison = 0
gen_3_ghost = 0
gen_3_fighting = 0
gen_3_dragon = 0
gen_3_grass = 0
gen_3_steel = 0

gen_4_psychic = 0
gen_4_ice = 0
gen_4_flying = 0
gen_4_ground = 0
gen_4_electric = 0
gen_4_normal = 0
gen_4_water = 0
gen_4_fire = 0
gen_4_fairy = 0
gen_4_rock = 0
gen_4_dark = 0
gen_4_bug = 0
gen_4_poison = 0
gen_4_ghost = 0
gen_4_fighting = 0
gen_4_dragon = 0
gen_4_grass = 0
gen_4_steel = 0

gen_5_psychic = 0
gen_5_ice = 0
gen_5_flying = 0
gen_5_ground = 0
gen_5_electric = 0
gen_5_normal = 0
gen_5_water = 0
gen_5_fire = 0
gen_5_fairy = 0
gen_5_rock = 0
gen_5_dark = 0
gen_5_bug = 0
gen_5_poison = 0
gen_5_ghost = 0
gen_5_fighting = 0
gen_5_dragon = 0
gen_5_grass = 0
gen_5_steel = 0

gen_6_psychic = 0
gen_6_ice = 0
gen_6_flying = 0
gen_6_ground = 0
gen_6_electric = 0
gen_6_normal = 0
gen_6_water = 0
gen_6_fire = 0
gen_6_fairy = 0
gen_6_rock = 0
gen_6_dark = 0
gen_6_bug = 0
gen_6_poison = 0
gen_6_ghost = 0
gen_6_fighting = 0
gen_6_dragon = 0
gen_6_grass = 0
gen_6_steel = 0

#open the Pokemon data file
filename = 'Pokemon.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    #loop through each row and add to the desired counter variable depending on conditions
    for row in reader:
            if row[2] == 'Psychic':
                if row[11] == '1':
                    gen_1_psychic += 1
                if row[11] == '2':
                    gen_2_psychic += 1
                if row[11] == '3':
                    gen_3_psychic += 1
                if row[11] == '4':
                    gen_4_psychic += 1
                if row[11] == '5':
                    gen_5_psychic += 1
                if row[11] == '6':
                    gen_6_psychic += 1

            if row[2] == 'Ice':
                if row[11] == '1':
                    gen_1_ice += 1
                if row[11] == '2':
                    gen_2_ice += 1
                if row[11] == '3':
                    gen_3_ice += 1
                if row[11] == '4':
                    gen_4_ice += 1
                if row[11] == '5':
                    gen_5_ice += 1
                if row[11] == '6':
                    gen_6_ice += 1

            if row[2] == 'Flying':
                if row[11] == '1':
                    gen_1_flying += 1
                if row[11] == '2':
                    gen_2_flying += 1
                if row[11] == '3':
                    gen_3_flying += 1
                if row[11] == '4':
                    gen_4_flying += 1
                if row[11] == '5':
                    gen_5_flying += 1
                if row[11] == '6':
                    gen_6_flying += 1

            if row[2] == 'Ground':
                if row[11] == '1':
                    gen_1_ground += 1
                if row[11] == '2':
                    gen_2_ground += 1
                if row[11] == '3':
                    gen_3_ground += 1
                if row[11] == '4':
                    gen_4_ground += 1
                if row[11] == '5':
                    gen_5_ground += 1
                if row[11] == '6':
                    gen_6_ground += 1

            if row[2] == 'Electric':
                if row[11] == '1':
                    gen_1_electric += 1
                if row[11] == '2':
                    gen_2_electric += 1
                if row[11] == '3':
                    gen_3_electric += 1
                if row[11] == '4':
                    gen_4_electric += 1
                if row[11] == '5':
                    gen_5_electric += 1
                if row[11] == '6':
                    gen_6_electric += 1

            if row[2] == 'Normal':
                if row[11] == '1':
                    gen_1_normal += 1
                if row[11] == '2':
                    gen_2_normal += 1
                if row[11] == '3':
                    gen_3_normal += 1
                if row[11] == '4':
                    gen_4_normal += 1
                if row[11] == '5':
                    gen_5_normal += 1
                if row[11] == '6':
                    gen_6_normal += 1

            if row[2] == 'Water':
                if row[11] == '1':
                    gen_1_water += 1
                if row[11] == '2':
                    gen_2_water += 1
                if row[11] == '3':
                    gen_3_water += 1
                if row[11] == '4':
                    gen_4_water += 1
                if row[11] == '5':
                    gen_5_water += 1
                if row[11] == '6':
                    gen_6_water += 1

            if row[2] == 'Fire':
                if row[11] == '1':
                    gen_1_fire += 1
                if row[11] == '2':
                    gen_2_fire += 1
                if row[11] == '3':
                    gen_3_fire += 1
                if row[11] == '4':
                    gen_4_fire += 1
                if row[11] == '5':
                    gen_5_fire += 1
                if row[11] == '6':
                    gen_6_fire += 1

            if row[2] == 'Fairy':
                if row[11] == '1':
                    gen_1_fairy += 1
                if row[11] == '2':
                    gen_2_fairy += 1
                if row[11] == '3':
                    gen_3_fairy += 1
                if row[11] == '4':
                    gen_4_fairy += 1
                if row[11] == '5':
                    gen_5_fairy += 1
                if row[11] == '6':
                    gen_6_fairy += 1

            if row[2] == 'Rock':
                if row[11] == '1':
                    gen_1_rock += 1
                if row[11] == '2':
                    gen_2_rock += 1
                if row[11] == '3':
                    gen_3_rock += 1
                if row[11] == '4':
                    gen_4_rock += 1
                if row[11] == '5':
                    gen_5_rock += 1
                if row[11] == '6':
                    gen_6_rock += 1

            if row[2] == 'Dark':
                if row[11] == '1':
                    gen_1_dark += 1
                if row[11] == '2':
                    gen_2_dark += 1
                if row[11] == '3':
                    gen_3_dark += 1
                if row[11] == '4':
                    gen_4_dark += 1
                if row[11] == '5':
                    gen_5_dark += 1
                if row[11] == '6':
                    gen_6_dark += 1

            if row[2] == 'Bug':
                if row[11] == '1':
                    gen_1_bug += 1
                if row[11] == '2':
                    gen_2_bug += 1
                if row[11] == '3':
                    gen_3_bug += 1
                if row[11] == '4':
                    gen_4_bug += 1
                if row[11] == '5':
                    gen_5_bug += 1
                if row[11] == '6':
                    gen_6_bug += 1

            if row[2] == 'Poison':
                if row[11] == '1':
                    gen_1_poison += 1
                if row[11] == '2':
                    gen_2_poison += 1
                if row[11] == '3':
                    gen_3_poison += 1
                if row[11] == '4':
                    gen_4_poison += 1
                if row[11] == '5':
                    gen_5_poison += 1
                if row[11] == '6':
                    gen_6_poison += 1

            if row[2] == 'Ghost':
                if row[11] == '1':
                    gen_1_ghost += 1
                if row[11] == '2':
                    gen_2_ghost += 1
                if row[11] == '3':
                    gen_3_ghost += 1
                if row[11] == '4':
                    gen_4_ghost += 1
                if row[11] == '5':
                    gen_5_ghost += 1
                if row[11] == '6':
                    gen_6_ghost += 1

            if row[2] == 'Fighting':
                if row[11] == '1':
                    gen_1_fighting += 1
                if row[11] == '2':
                    gen_2_fighting += 1
                if row[11] == '3':
                    gen_3_fighting += 1
                if row[11] == '4':
                    gen_4_fighting += 1
                if row[11] == '5':
                    gen_5_fighting += 1
                if row[11] == '6':
                    gen_6_fighting += 1

            if row[2] == 'Dragon':
                if row[11] == '1':
                    gen_1_dragon += 1
                if row[11] == '2':
                    gen_2_dragon += 1
                if row[11] == '3':
                    gen_3_dragon += 1
                if row[11] == '4':
                    gen_4_dragon += 1
                if row[11] == '5':
                    gen_5_dragon += 1
                if row[11] == '6':
                    gen_6_dragon += 1

            if row[2] == 'Grass':
                if row[11] == '1':
                    gen_1_grass += 1
                if row[11] == '2':
                    gen_2_grass += 1
                if row[11] == '3':
                    gen_3_grass += 1
                if row[11] == '4':
                    gen_4_grass += 1
                if row[11] == '5':
                    gen_5_grass += 1
                if row[11] == '6':
                    gen_6_grass += 1

            if row[2] == 'Steel':
                if row[11] == '1':
                    gen_1_steel += 1
                if row[11] == '2':
                    gen_2_steel += 1
                if row[11] == '3':
                    gen_3_steel += 1
                if row[11] == '4':
                    gen_4_steel += 1
                if row[11] == '5':
                    gen_5_steel += 1
                if row[11] == '6':
                    gen_6_steel += 1
#add the variables into generation dictionaries.
#yes, this step is unnecessary but it made everything grouped together.
generation_1 = {
    'Psychic': gen_1_psychic,
    'Ice': gen_1_ice,
    'Flying': gen_1_flying,
    'Ground': gen_1_ground,
    'Electric': gen_1_electric,
    'Normal': gen_1_normal,
    'Water': gen_1_water,
    'Fire': gen_1_fire,
    'Fairy': gen_1_fairy,
    'Rock': gen_1_rock,
    'Dark': gen_1_dark,
    'Bug': gen_1_bug,
    'Poison': gen_1_poison,
    'Ghost': gen_1_ghost,
    'Fighting': gen_1_fighting,
    'Dragon': gen_1_dragon,
    'Grass': gen_1_grass,
    'Steel': gen_1_steel
}

generation_2 = {
    'Psychic': gen_2_psychic,
    'Ice': gen_2_ice,
    'Flying': gen_2_flying,
    'Ground': gen_2_ground,
    'Electric': gen_2_electric,
    'Normal': gen_2_normal,
    'Water': gen_2_water,
    'Fire': gen_2_fire,
    'Fairy': gen_2_fairy,
    'Rock': gen_2_rock,
    'Dark': gen_2_dark,
    'Bug': gen_2_bug,
    'Poison': gen_2_poison,
    'Ghost': gen_2_ghost,
    'Fighting': gen_2_fighting,
    'Dragon': gen_2_dragon,
    'Grass': gen_2_grass,
    'Steel': gen_2_steel
}

generation_3 = {
    'Psychic': gen_3_psychic,
    'Ice': gen_3_ice,
    'Flying': gen_3_flying,
    'Ground': gen_3_ground,
    'Electric': gen_3_electric,
    'Normal': gen_3_normal,
    'Water': gen_3_water,
    'Fire': gen_3_fire,
    'Fairy': gen_3_fairy,
    'Rock': gen_3_rock,
    'Dark': gen_3_dark,
    'Bug': gen_3_bug,
    'Poison': gen_3_poison,
    'Ghost': gen_3_ghost,
    'Fighting': gen_3_fighting,
    'Dragon': gen_3_dragon,
    'Grass': gen_3_grass,
    'Steel': gen_3_steel
}


generation_4 = {
    'Psychic': gen_4_psychic,
    'Ice': gen_4_ice,
    'Flying': gen_4_flying,
    'Ground': gen_4_ground,
    'Electric': gen_4_electric,
    'Normal': gen_4_normal,
    'Water': gen_4_water,
    'Fire': gen_4_fire,
    'Fairy': gen_4_fairy,
    'Rock': gen_4_rock,
    'Dark': gen_4_dark,
    'Bug': gen_4_bug,
    'Poison': gen_4_poison,
    'Ghost': gen_4_ghost,
    'Fighting': gen_4_fighting,
    'Dragon': gen_4_dragon,
    'Grass': gen_4_grass,
    'Steel': gen_4_steel
}

generation_5 = {
    'Psychic': gen_5_psychic,
    'Ice': gen_5_ice,
    'Flying': gen_5_flying,
    'Ground': gen_5_ground,
    'Electric': gen_5_electric,
    'Normal': gen_5_normal,
    'Water': gen_5_water,
    'Fire': gen_5_fire,
    'Fairy': gen_5_fairy,
    'Rock': gen_5_rock,
    'Dark': gen_5_dark,
    'Bug': gen_5_bug,
    'Poison': gen_5_poison,
    'Ghost': gen_5_ghost,
    'Fighting': gen_5_fighting,
    'Dragon': gen_5_dragon,
    'Grass': gen_5_grass,
    'Steel': gen_5_steel
}

generation_6 = {
    'Psychic': gen_6_psychic,
    'Ice': gen_6_ice,
    'Flying': gen_6_flying,
    'Ground': gen_6_ground,
    'Electric': gen_6_electric,
    'Normal': gen_6_normal,
    'Water': gen_6_water,
    'Fire': gen_6_fire,
    'Fairy': gen_6_fairy,
    'Rock': gen_6_rock,
    'Dark': gen_6_dark,
    'Bug': gen_6_bug,
    'Poison': gen_6_poison,
    'Ghost': gen_6_ghost,
    'Fighting': gen_6_fighting,
    'Dragon': gen_6_dragon,
    'Grass': gen_6_grass,
    'Steel': gen_6_steel
}
