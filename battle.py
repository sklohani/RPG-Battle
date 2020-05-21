from classes.main import person, bcolors
from classes.magic import spell
from classes.inventory import item

# Create Black Magic
fire = spell("Fire", 10, 100, "black")
thunder = spell("Thunder", 12, 120, "black")
blizzard = spell("Blizzard", 14, 150, "black")
meteor = spell("Meteor", 20, 200, "black")
quake = spell("Quake", 12, 140, "black")

# Create White Magic
cure = spell("Cure", 12, 150, "white")
relieve = spell("Relieve", 18, 200, "white")

# Create Items
potion = item("Potion", "potion", "Heals by 50 HP", 50)
hi_potion = item("Hi-Potion", "potion", "Heals by 100 HP", 100)
su_potion = item("Super-Potion", "potion", "Heals by 500 HP", 500)
elixir = item("Elixir", "elixir", "Fully restores HP/MP of one party member", 9999)
mg_elixir = item("Mega-Potion", "elixir", "Fully restores party's HP/MP", 9999)

grenade = item("Grenade", "attack", "Deals 500 Damage", 500)

player_spells = [fire, thunder, blizzard, meteor, cure, relieve]
player_items = [potion, hi_potion, su_potion, elixir, mg_elixir, grenade]
# Instantiate Person
player = person(400, 65, 60, 35, player_spells, player_items)
enemy = person(1200, 65, 60, 25, [], [])

print(bcolors.FAIL + "An Enemy Attacked!" + bcolors.ENDC)


running = True
i = 0
while running:
    print(bcolors.OKBLUE + bcolors.BOLD + "====================" + bcolors.ENDC)
    player.choose_action()
    choice = input("Choose Action : ")
    index = int(choice) - 1

    if index == 0:
        dmg = player.damage()
        enemy.take_damage(dmg)
        print("You attack to Enemy for", dmg, "points damage!")
    elif index == 1:
        player.choose_magic()
        print("\nChoose '0' to Go Back!")
        magic_choice = int(input("Choose your Action : "))-1

        if magic_choice == -1:
            continue
        # magic_dmg = player.spell_damage(magic_choice)
        # spell = player.get_spell_name(magic_choice)
        # cost = int(player.get_spell_cost(magic_choice))

        spell = player.magic[magic_choice]
        magic_dmg = spell.generate_damage()

        current_mp = player.get_mp()

        if spell.cost > current_mp:
            print(bcolors.FAIL + bcolors.BOLD + "\nYou are low in MP!\n" + bcolors.ENDC)
            continue
        player.reduce_mp(spell.cost)

        if spell.type == "white":
            player.heal(magic_dmg)
            print(bcolors.OKGREEN + "\n", spell.name, "heals for", str(magic_dmg), "HP" + bcolors.ENDC)
        elif spell.type == "black":
            enemy.take_damage(magic_dmg)
            print(bcolors.OKBLUE + bcolors.BOLD + "\n", "You got reduced for", spell.name, "for", str(magic_dmg), "points of damage\n" + bcolors.ENDC)
    elif index == 2:
        player.choose_item()
        print("\nChoose '0' to Go Back!")
        item_choice = int(input("Choose Item : "))- 1
        
        if item_choice == -1:
            continue

        item = player.item[item_choice]
        if item.type == "potion":
            player.heal(item.property)
            print(bcolors.OKGREEN + "\n", item.name, "heals for", str(item.property), "HP" + bcolors.ENDC)
    else:
        print("NOT a valid input!")
        break
    enemy_choice = 1
    enemy_dmg = enemy.damage()
    player.take_damage(enemy_dmg)
    print("Enemy attack to you for", enemy_dmg, "points damage!")

    print(bcolors.OKBLUE + bcolors.BOLD + "--------------------" + bcolors.ENDC)

    print("Enemy HP : ", bcolors.FAIL + str(enemy.get_hp()) + "/" + str(enemy.get_max_hp()) + bcolors.ENDC)
    print("Player HP : ", bcolors.OKGREEN + str(player.get_hp()) + "/" + str(player.get_max_hp()) + bcolors.ENDC)
    print("Player MP : ", bcolors.OKBLUE + str(player.get_mp()) + "/" + str(player.get_max_mp()) + bcolors.ENDC)
    if enemy.get_hp() == 0:
        print(bcolors.OKGREEN + bcolors.BOLD + "You Won!" + bcolors.ENDC)
        running = False
    elif player.get_hp() == 0:
        print(bcolors.FAIL + bcolors.BOLD + "You Lost!" + bcolors.ENDC)
        running = False
