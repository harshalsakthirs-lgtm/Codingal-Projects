import re, random
from colorama import Fore, init
from textblob.en import suggest

init(autoreset=True)

destinations = {
    "beaches: " : ["Bali", "Maldives", "Phuket"],
    "mountains: " : ["Swiss Alps", "Rocky Mountains", "Himalayas"],
    "cities: " : ["Tokyo", "Paris", "New York"]
}

jokes = [
    "Why still programmers, not like nature? because having bug",
    "Why do the computer did go to the doctor? because it had a virus",
    "Why do travellers feel warm? because all their hot spots"
]

def normalize_input(text):
    return re.sub(r"\s+", "", text.strip().lower())

def recommend():
    print(f"{Fore.CYAN} Travel Bot: beaches or mountains or cities?")
    preference = input(f"{Fore.GREEN} You: ")
    preference = normalize_input(preference)

    if preference in destinations:
        suggestions = random.choice(destinations[preference])
        print(f"{Fore.GREEN} Travel Bot: How about {suggestions}?")
        print(f"{Fore.CYAN} Travel Bot: Did you like it: (yes/no): ")
        answer = input(f"{Fore.YELLOW} You: ").lower()

        if answer == "yes":
            print(f"{Fore.GREEN} Travel Bot: Awesome, Enjoy!")
        elif answer == "no":
            print(f"{Fore.RED} Travel Bot: Let's try another!")
            recommend()
        else:
            print(f"{Fore.RED} Sorry, I'll suggest another!")

    else:
        print(f"{Fore.RED}Travel Bot: Sorry, I not have that destinations")
    show_help()

def packing_tips():
    print(f"{Fore.CYAN}Travel Bot: Where to?: ")
    location = normalize_input(f"{Fore.YELLOW} You: ")
    print(f"{Fore.CYAN}Travel Bot: How many days?: ")
    days = input(f"{Fore.YELLOW}Travel Bot: You: ")

    print(Fore.GREEN, f"Travel Bot: Packing tips for {days} days in {location}")
    print(Fore.GREEN, f"Travel Bot: - Pack versatile cloths")
    print(Fore.GREEN, f"Tral Bot: - Bring chargers/adapters")
    print(Fore.GREEN, f"Travel Bot: - Chek the weather forecast")

def tell_joke():
     print(Fore.YELLOW + f"Travel Bot:{random.choice(jokes)}")
def show_help():
    print(Fore.MAGENTA + f"Travel Bot: \n I can:")
    print(Fore.GREEN + "Travel Bot: - Suggests travel spots: (say 'recommend')")
    print(Fore.GREEN + "- Offer packing tips (say 'packing' or 'pack')")
    print(Fore.GREEN + "- Tell a joke (say 'joke')")
    print(Fore.CYAN + "Type 'exit' or 'bye' to exit the program \n")

def chat():
    print(f"{Fore.CYAN} Hello I am Travel Bot!")
    name = input(f"{Fore.YELLOW}What is your name?: ")
    print(f"{Fore.CYAN}Hello Nice to meet you, {name}!")
    show_help()

    while True:
        user_input = input(f"{Fore.YELLOW} {name}: ")
        user_input = normalize_input(user_input)

        if "recommend" in user_input:
            recommend()
        elif "packing" in user_input or "pack" in user_input:
            packing_tips()
        elif "joke" in user_input:
            tell_joke()
        elif "help" in user_input:
            show_help()
        elif "exit" in user_input or "bye" in user_input:
            print(f"{Fore.CYAN} Safe Travel Good Bye!")
            break
        else:
            print(f"{Fore.RED} Could you rephrase")

if __name__ == "__main__":
    chat()


