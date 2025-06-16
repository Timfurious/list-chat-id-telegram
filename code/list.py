import requests
import time

# Replace with your bot token
bot_token = input("Enter your bot token: ")

# URL to get updates
url = f'https://api.telegram.org/bot{bot_token}/getUpdates'

# Set to keep track of chat IDs
chat_ids = set()

def fetch_updates():
    response = requests.get(url)
    data = response.json()
    if data['ok']:
        updates = data['result']
        for update in updates:
            if 'message' in update:
                chat_id = update['message']['chat']['id']
                chat_ids.add(chat_id)
            else:
                print("Update does not contain a message:", update)
    else:
        print("Failed to fetch updates:", data['description'])

def main():
    while True:
        fetch_updates()
        print("List of chat IDs:")
        for chat_id in chat_ids:
            print(chat_id)
        time.sleep(5)  # Wait for 30 seconds before fetching updates again

if __name__ == '__main__':
    main()
