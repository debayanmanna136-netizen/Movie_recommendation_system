import requests
import heapq
import time
import sys

# =====================================================
# CONFIGURATION
# =====================================================

API_KEY = "YOUR_API_KEY_HERE"
API_HOST = "YOUR_API_HOST_HERE"
BASE_URL = "YOUR_API_BASE_URL_HERE"

TOP_K = 5
PAGES_TO_FETCH = 5

EXIT_COMMANDS = {"bye", "exit", "quit", "goodbye"}

# =====================================================
# GENRE & LANGUAGE MAPS
# =====================================================

GENRE_MAP = {
    "action": 28,
    "adventure": 12,
    "animation": 16,
    "comedy": 35,
    "crime": 80,
    "documentary": 99,
    "drama": 18,
    "family": 10751,
    "fantasy": 14,
    "history": 36,
    "horror": 27,
    "music": 10402,
    "mystery": 9648,
    "romance": 10749,
    "science fiction": 878,
    "thriller": 53,
    "war": 10752,
    "western": 37
}

LANGUAGE_MAP = {
    "english": "en",
    "hindi": "hi",
    "bengali": "bn",
    "tamil": "ta",
    "telugu": "te",
    "malayalam": "ml",
    "kannada": "kn",
    "marathi": "mr",
    "punjabi": "pa",
    "gujarati": "gu",

    "french": "fr",
    "spanish": "es",
    "german": "de",
    "italian": "it",
    "korean": "ko",
    "japanese": "ja",
    "chinese": "zh"
}

# =====================================================
# CHATBOT UTILITIES
# =====================================================

def bot_say(message, delay=0.02):
    """Typing animation"""
    for char in message:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()


# =====================================================
# CORE LOGIC FUNCTIONS (UNCHANGED)
# =====================================================

def get_genre_ids_from_input(user_input):
    genres = user_input.lower().split("-")
    genre_ids = []

    for genre in genres:
        if genre in GENRE_MAP:
            genre_ids.append(str(GENRE_MAP[genre]))
        else:
            return ""

    return ",".join(genre_ids)


def fetch_movies(genre_id_string):
    headers = {
        "x-rapidapi-key": API_KEY,
        "x-rapidapi-host": API_HOST
    }

    all_movies = []

    for page in range(1, PAGES_TO_FETCH + 1):
        params = {"page": page}

        if genre_id_string:
            params["with_genres"] = genre_id_string

        response = requests.get(BASE_URL, headers=headers, params=params)

        if response.status_code != 200:
            continue

        all_movies.extend(response.json().get("results", []))

    return all_movies


def filter_by_original_language(movies, language_code):
    return [
        movie for movie in movies
        if movie.get("original_language") == language_code
    ]


def rank_movies_with_heap(movies, k):
    heap = []

    for movie in movies:
        rating = movie.get("vote_average", 0)
        heapq.heappush(heap, (-rating, movie))

    top_movies = []

    for _ in range(min(k, len(heap))):
        top_movies.append(heapq.heappop(heap)[1])

    return top_movies

# =====================================================
# CHATBOT FLOW
# =====================================================

def chatbot():
    bot_say("\n🤖 Hello! I am your Movie Recommendation Bot 🎬")
    bot_say("I can suggest movies based on genre and language.\nType 'exit' to quit anytime.\n")

    bot_say(
        "📌 NOTE:\n"
        "Some regional movies may be missing due to\n"
        "limited metadata in public movie APIs.\n"
    )

    while True:
        # ------------------------------
        # GENRE INPUT LOOP
        # ------------------------------
        while True:
            user_genre = input(
                "👤 Enter genre(s) (e.g. horror-romance) or 'exit': "
            ).strip().lower()

            if user_genre in EXIT_COMMANDS:
                bot_say("👋 Goodbye! Happy watching 🍿")
                return

            genre_id_string = get_genre_ids_from_input(user_genre)

            if genre_id_string:
                break
            else:
                bot_say("❌ Unsupported genre. Please try again.\n")

        # ------------------------------
        # LANGUAGE INPUT LOOP
        # ------------------------------
        while True:
            user_language = input(
                "👤 Enter language (press Enter for English): "
            ).strip().lower()

            if user_language == "":
                language_code = "en"
                break

            if user_language in LANGUAGE_MAP:
                language_code = LANGUAGE_MAP[user_language]
                break
            else:
                bot_say("❌ Unsupported language. Please try again.\n")

        # ------------------------------
        # FETCH & RECOMMEND
        # ------------------------------
        bot_say("\n🔍 Let me find some movies for you...\n")

        movies = fetch_movies(genre_id_string)
        movies = filter_by_original_language(movies, language_code)

        if not movies:
            bot_say("⚠️ Couldn't find movies with that genre.")
            bot_say("🔄 Trying with language only...\n")

            movies = fetch_movies("")
            movies = filter_by_original_language(movies, language_code)

            if not movies:
                bot_say("❌ No movies found. Try different preferences.\n")
                continue

        ranked_movies = rank_movies_with_heap(movies, TOP_K)

        # ------------------------------
        # DISPLAY RESULTS
        # ------------------------------
        bot_say("🏆 Here are my recommendations:\n")

        for idx, movie in enumerate(ranked_movies, 1):
            title = movie.get("title", "Unknown")
            year = movie.get("release_date", "N/A")[:4]
            rating = movie.get("vote_average", "N/A")

            bot_say(f"{idx}. {title} ({year}) ⭐ {rating}")

        bot_say("\n🎯 Want more recommendations? Just ask!\n")

# =====================================================
# ENTRY POINT
# =====================================================

if __name__ == "__main__":
    chatbot()
