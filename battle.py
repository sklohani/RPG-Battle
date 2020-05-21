from main import person, bcolors

magic = [{"name": "fire", "cost": "10", "dmg": "100"},
         {"name": "thunder", "cost": "12", "dmg": "120"},
         {"name": "blizzard", "cost": "8", "dmg": "80"}]

player = person(400, 65, 60, 35, magic)
enemy = person(800, 65, 50, 20, magic)

print(bcolors.FAIL + bcolors.BOLD + "An Enemy Attacked!" + bcolors.ENDC)

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
        print("You attack for ", dmg, "points")
    elif index == 1:
        player.choose_magic()
        magic_choice = int(input("Choose your Action : "))-1
        magic_dmg = player.spell_damage(magic_choice)
        spell = player.get_spell_name(magic_choice)
        cost = int(player.get_spell_cost(magic_choice))
        current_mp = player.get_mp()

        if cost > current_mp:
            print(bcolors.FAIL + bcolors.BOLD + "\nYou are low in MP!\n" + bcolors.ENDC)
            continue

        player.reduce_mp(cost)
        enemy.take_damage(magic_dmg)
        print(bcolors.OKBLUE + bcolors.BOLD + "\n", "You got reduced for ", spell, "By", str(magic_dmg), "points of damage\n" + bcolors.ENDC)

    enemy_choice = 1
    enemy_dmg = enemy.damage()
    player.take_damage(enemy_dmg)
    print("Enemy attack for ", enemy_dmg, "points")

    print(bcolors.OKBLUE + bcolors.BOLD + "--------------------" + bcolors.ENDC)

    print("Enemy HP : ", bcolors.FAIL + str(enemy.get_hp()) + "/" + str(enemy.get_max_hp()) + bcolors.ENDC)
    print("Player HP : ", bcolors.OKGREEN + str(player.get_hp()) + "/" + str(player.get_max_hp()) + bcolors.ENDC)
    print("Player MP : ", bcolors.OKBLUE + str(player.get_mp()) + "/" + str(player.get_max_mp()) + bcolors.ENDC)
    if enemy.get_hp() == 0:
        print(bcolors.OKGREEN + bcolors.BOLD + "You Win!" + bcolors.ENDC)
        running = False
    elif player.get_hp() == 0:
        print(bcolors.FAIL + bcolors.BOLD + "You Lost!" + bcolors.ENDC)
        running = False
