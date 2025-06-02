class CryptoChatbot:
    def __init__(self, name, tone, crypto_db):
        self.name = name
        self.tone = tone
        self.crypto_db = crypto_db

    def respond_to_query(self, user_query):
        user_query = user_query.lower().strip()

        if "sustainable" in user_query and "most" in user_query:
            sustainable = max(self.crypto_db, key=lambda x: self.crypto_db[x]["sustainability_score"])
            return f"♻️ {sustainable} is the most sustainable coin with a score of {self.crypto_db[sustainable]['sustainability_score'] * 10}/10!"

        if "sustainable" in user_query:
            recommend = max(self.crypto_db, key=lambda x: self.crypto_db[x]["sustainability_score"])
            return f"🌱 Invest in {recommend}! It's eco-friendly and has long-term potential!"

        if "trending" in user_query or "growth" in user_query:
            trending_coins = [name for name, data in self.crypto_db.items() if data["price_trend"] == "rising"]
            return f"📈 These coins are trending: {', '.join(trending_coins)}"

        if "long-term" in user_query:
            for name, data in self.crypto_db.items():
                if data["price_trend"] == "rising" and data["sustainability_score"] > 0.7:
                    return f"🚀 {name} is trending up and has a top-tier sustainability score!"
            return "🔍 No coin matches that exact criteria, but Cardano is a strong eco-friendly choice."

        return "🤖 Sorry, I didn't quite get that. Try asking about trends, sustainability, or best crypto to buy!"

    def start_chat(self):
        print(f"{self.name}: {self.tone}")
        while True:
            user_input = input("You: ")
            if user_input.lower() in ["exit", "quit", "end"]:
                print(f"{self.name}: Goodbye! Remember, crypto is risky—always do your own research! 🚨")
                break
            response = self.respond_to_query(user_input)
            print(f"{self.name}: {response}")


if __name__ == "__main__":
    crypto_db = {
        "Bitcoin": {
            "price_trend": "rising",
            "market_cap": "high",
            "energy_use": "high",
            "sustainability_score": 3 / 10
        },
        "Ethereum": {
            "price_trend": "stable",
            "market_cap": "high",
            "energy_use": "medium",
            "sustainability_score": 6 / 10
        },
        "Cardano": {
            "price_trend": "rising",
            "market_cap": "medium",
            "energy_use": "low",
            "sustainability_score": 8 / 10
        }
    }

    bot = CryptoChatbot(
        "CryptoBuddy",
        "🌟 Hey there! I'm CryptoBuddy, your friendly guide in the world of crypto!",
        crypto_db
    )
    bot.start_chat()
