import random

ITEMS = ["leaf", "nugget", "cheese", "keyboard", "tiny hat"]

def main():
    inventory = []
    print("TimTim's Treasure Hunt")
    for turn in range(5):
        item = random.choice(ITEMS)
        inventory.append(item)
        print(f"Turn {turn + 1}: found a {item}!")
    print("Inventory:", ", ".join(inventory))
    print("Unique items:", len(set(inventory)))

if __name__ == "__main__":
    main()
