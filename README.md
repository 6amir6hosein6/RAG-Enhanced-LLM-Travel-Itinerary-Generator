# RAG-Enhanced-LLM-Travel-Itinerary-Generator

This project is an AI-powered travel planning system that generates personalized itineraries for cities or countries based on user preferences and real-world data. It leverages **Retrieval-Augmented Generation (RAG)** to handle destinations that are less well-known or have limited information, combining retrieved knowledge with a **Large Language Model (LLM)** to produce accurate and engaging travel plans.

The system uses **thenlper/gte-small** for embeddings and **Pinecone** for vector data storage, enabling efficient retrieval of relevant travel information. The LLM backend is powered by **HuggingFace’s H4/zephyr-7b-beta** model, ensuring high-quality, context-aware itinerary generation. RAG-based retrieval allows the tool to provide recommendations even for lesser-known locations, enhancing the user experience with rich, personalized travel insights.

