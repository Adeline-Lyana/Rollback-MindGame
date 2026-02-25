from story import forest_scene
from dialogues import shadow_intro
from health import Player
from rollback import GameState

player_name = input("Enter your name: ")
player = Player(player_name)

game = GameState()
score = 0

current_scene = "forest"
game.save_state((current_scene, player.health, score))

while True:

    if current_scene == "forest":
        print("\n🌲 You are alone in a dark forest.")
        print("You hear whispers around you...")
        print("1. Follow the whisper")
        print("2. Stay still")
        print("Type 'rollback' to go back")

    elif current_scene == "whisper":
        print("\n👁️ The whisper leads you to a shadow figure.")
        print("1. Talk to it")
        print("2. Run away")
        print("Type 'rollback' to go back")

    elif current_scene == "stay":
        print("\n😨 The ground cracks beneath you!")
        print("You fall into a trap.")
        player.damage(20)
        current_scene = "forest"
        continue

    choice = input("Your choice: ")

    if choice == "1":
        if current_scene == "forest":
            current_scene = "whisper"
            score += 10

        elif current_scene == "whisper":
            print("\n🧠 The shadow tests your mind.")
            answer = input("What is 5 + 3? ")
            if answer == "8":
                print("Correct! You gained power.")
                score += 20
            else:
                print("Wrong! The shadow attacks you.")
                player.damage(30)

    elif choice == "2":
        if current_scene == "forest":
            current_scene = "stay"

        elif current_scene == "whisper":
            print("You escaped safely.")
            current_scene = "forest"

    elif choice.lower() == "rollback":
        previous = game.rollback()
        if previous:
            current_scene, player.health, score = previous
            print("⏪ Rolled back!")

    else:
        print("Invalid choice.")

    game.save_state((current_scene, player.health, score))

    print(f"❤️ Health: {player.health} | ⭐ Score: {score}")

    if not player.is_alive():
        print("\n💀 You have fallen. Game Over!")
        break

    if score >= 30:
        print("\n🏆 You conquered the shadow mind. YOU WIN!")
        break