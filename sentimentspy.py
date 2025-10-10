import colorama
from colorama import Fore, Style
from textblob import TextBlob

colorama.init()

print(f"{Fore.CYAN}Sentiment Spyl{Style.RESET_ALL}")

user_name = input(f"{Fore.MAGENTA}Enter your name: {Style.RESET_ALL}")
if not user_name:
    user_name = "Mystry Agent"


conversion_history = []

print(f"\n {Fore.CYAN}Welcome, {user_name}!{Style.RESET_ALL}")
print("Type the sentiment, I will anylyze the sentence with TextBlob and Show you the sentence")
print(f"{Fore.YELLOW} 'reset' {Fore.CYAN}, {Fore.YELLOW} 'history' {Fore.CYAN}, "
      f"or {Fore.YELLOW} 'exit' {Style.RESET_ALL} to quit the program.\n")

while True:
    user_input = input(f"{Fore.GREEN}>> {Style.RESET_ALL}").strip()

    if not user_input:
        print(f"{Fore.BLUE}Please enter a valid sentence.{Style.RESET_ALL}")

    if user_input.lower() == "exit":
        print(f"{Fore.CYAN}Goodbye, {user_name}!{Style.RESET_ALL}")
        break
    elif user_input.lower() == "rest":
        conversion_history.clear()
        print(f"{Fore.BLUE}History cleared.{Style.RESET_ALL}")
        continue
    elif user_input.lower() == "history":
        if not conversion_history:
            print(f"{Fore.YELLOW}No history available.{Style.RESET_ALL}")
        else:
            print(f"{Fore.CYAN}Conversion History:{Style.RESET_ALL}")
            for idx, (text, polarity, sentiment_type) in enumerate(conversion_history, start=1):
                if sentiment_type == "Positive":
                    color = Fore.GREEN
                    emoji = "😊"
                elif sentiment_type == "Negative":
                    color = Fore.RED
                    emoji = "😞"
                else:
                    color = Fore.YELLOW
                    emoji = "😐"
    continue

polarity = TextBlob(user_input).sentiment.polarity
if polarity > 0.25:
    sentiment_type = "Positive"
    color = Fore.GREEN
    emoji = "😊"
elif polarity < -0.25:
    sentiment_type = "Negative"
    color = Fore.RED
    emoji = "😞"
else:
    sentiment_type = "Neutral"
    color = Fore.YELLOW
    emoji = "😐"

conversion_history.append((user_input, polarity, sentiment_type))

print(f"{color} {emoji} {sentiment_type} sentiment detected!"
      f" (Polarity: {polarity:.2f}){Style.RESET_ALL}")