# 🎬 CineBot: CLI Movie Recommendation System

A Python-based interactive chatbot that recommends movies based on user preferences. This project utilizes **Data Structures & Algorithms (Heaps/Priority Queues)** to efficiently rank and filter movies fetched from a public metadata API.

![Python](https://img.shields.io/badge/Python-3.x-blue?style=flat&logo=python)
![Algorithm](https://img.shields.io/badge/Algorithm-Heap%20Sort-orange?style=flat)
![Status](https://img.shields.io/badge/Status-Active-green?style=flat)

## 📖 Project Overview

CineBot is a command-line interface (CLI) tool designed to mimic a conversation with a movie expert. Users can request recommendations by specifying genres (including mixed genres like "Horror-Comedy") and preferred languages.

Unlike simple linear searches, this project implements a **Priority Queue (Heap)** to process movie popularity and ratings, ensuring the "Top K" recommendations are retrieved efficiently.

## ✨ Key Features

* **Efficient Ranking:** Uses a Min-Heap algorithm to maintain the top-rated movies efficiently without sorting the entire dataset.
* **Smart Filtering:** Supports filtering by specific genres and original languages.
* **Interactive CLI:** Features a chatbot-style interface with typing animations for a polished user experience.
* **Robust Error Handling:** Includes input validation loops and retry logic to prevent crashes during user input.
* **Graceful Fallbacks:** Handles scenarios where API data is missing or queries yield no results without breaking the application flow.

## 🛠️ Tech Stack & Concepts

* **Language:** Python 3
* **Data Structures:** Min-Heap / Priority Queue (`heapq` module)
* **External Data:** Public Movie Metadata API (e.g., TMDB/OpenWeather/etc.)
* **Libraries:** `requests`, `json`, `time`

## 🧠 How It Works

1.  **Data Fetching:** The bot queries a public API based on the user's genre or language input.
2.  **Filtering:** The raw data is parsed to ensure matches against specific criteria (e.g., excluding movies without poster paths or overview data).
3.  **Ranking (The DSA Part):**
    * The system iterates through the filtered movies.
    * It maintains a **Heap of size K** (where K is the number of recommendations requested).
    * This ensures that we only store the most relevant movies in memory, optimizing for performance.
4.  **Display:** The results are presented in a readable, formatted card style within the terminal.

## ⚠️ Known Limitations: Data Availability

Please note that this application relies entirely on **third-party public APIs** for movie metadata. While the recommendation algorithm is robust, the dataset has known gaps regarding regional cinema.

* **Regional Content (Hindi/Bengali):** The public API used often lacks extensive metadata for regional Indian cinema. Consequently, searches for Hindi or Bengali movies may return fewer results or older titles compared to Hollywood entries.
* **This is a data source limitation, not a flaw in the recommendation logic.** The system is designed to handle this gracefully by informing the user when insufficient data is found.

## 🚀 Installation & Usage

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/your-username/cinebot-recommender.git](https://github.com/your-username/cinebot-recommender.git)
    cd cinebot-recommender
    ```

2.  **Install dependencies:**
    ```bash
    pip install requests
    ```

3.  **API Key Configuration:**
    * Obtain an API Key from [The Movie DB (TMDB)](https://www.themoviedb.org/documentation/api) (or whichever provider you used).
    * Open `main.py` (or your config file) and replace the placeholder:
        ```python
        API_KEY = "YOUR_API_KEY_HERE"
        ```

4.  **Run the application:**
    ```bash
    python main.py
    ```

## 🔮 Future Improvements

* **Caching:** Implement local caching to reduce API calls for frequently searched genres.
* **Expanded Data Sources:** Integrate secondary APIs to improve coverage for regional/Indian cinema.
* **Web Interface:** Port the logic to a Flask/Django backend with a proper frontend.

## 🤝 Contributing

Contributions are welcome! If you have ideas for better data sources or algorithmic optimizations, feel free to open a Pull Request.

## 📄 License

This project is open-source and available under the MIT License.
