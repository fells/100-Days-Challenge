"""
        NAMESPACES

        LOCAL VS GLOBAL SCOPE

        Example:
        enemies = 1


        def increase_enemies():
            enemies = 2
            print(f"Enemies inside function: {enemies}")


        increase_enemies()   = 2
        print(f"Enemies outside the function: {enemies}")   = 1

        # Local scope

        def drink_potion():
            potion_strenght = 2
            print(potion_strenght)
        drink_potion()

        # global scope

        player_health = 10

        def drink_potion():
            potion_strength = 2
            print(player_health + potion_strength)
        drink_potion()
        print(player_health)


"""

# FINAL PROJECT

