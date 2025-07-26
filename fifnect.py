# Code written by @fif3x_
# Modified by ChatGPT to save and display friends and mutuals
# Script comes "as is", without warranty of any kind

import requests
import json

def get_friends(user_id):
    url = f"https://friends.roblox.com/v1/users/{user_id}/friends/"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json().get("data", [])
    else:
        print("Failed to fetch friends list. Status code:", response.status_code)
        return []

def save_to_json(data_dict, filename):
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data_dict, f, indent=2, ensure_ascii=False)

def print_list(title, key, data):
    print(f"{title}:")
    print("-" * 50)
    for item in data.get(key, []):
        name = item.get("name", "No name")
        display_name = item.get("displayName", "No display name")
        print(f"{name} (Display Name: {display_name})")
    print("-" * 50)

def main():
    user_id = input("Enter your userID: ")

    print("\nFetching your friends...")
    friends = get_friends(user_id)
    save_to_json({"friends": friends}, "friends.json")

    mutuals = []
    print("Checking for mutual friends (this may take a while)...")

    for friend in friends:
        friend_id = friend["id"]
        their_friends = get_friends(friend_id)
        if any(str(f["id"]) == user_id for f in their_friends):
            mutuals.append(friend)

    save_to_json({"mutuals": mutuals}, "mutuals.json")

    # Print both lists
    print()
    print_list("Friends", "friends", {"friends": friends})
    print_list("Mutuals", "mutuals", {"mutuals": mutuals})
    print("\nNote: the lists are saved in `friends.json` and `mutuals.json` files")

if __name__ == "__main__":
    main(
