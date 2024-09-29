import requests
from bs4 import BeautifulSoup
from transformers import GPT2LMHeadModel, GPT2Tokenizer
import random
import os
from dotenv import load_dotenv
import tkinter as tk
from tkinter import messagebox, scrolledtext

# Load environment variables from .env file
load_dotenv()

# Initialize GPT-2 model and tokenizer for tweet generation
gpt2_model = GPT2LMHeadModel.from_pretrained('gpt2')
gpt2_tokenizer = GPT2Tokenizer.from_pretrained('gpt2')

# Pre-defined human-like, emotional tweet templates
REACTION_TEMPLATES = [
    "Wow, I can't believe this just happened: {tech_news}! 🚀",
    "It's crazy that {tech_news} is finally here! 🤯",
    "So sad to see {tech_news} 😢, but I guess it was coming.",
    "This is amazing! {tech_news} is going to change everything. 🌍",
    "I never thought {tech_news} would happen, but here we are. 🙌",
    "This tech just keeps getting better: {tech_news}. I’m so excited! 🔥"
]

# Function to scrape latest articles from dev.to
def scrape_dev_to():
    url = "https://dev.to"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    
    articles = []
    
    # Find articles by selecting elements based on class names
    for article in soup.find_all('a', class_='crayons-story__hidden-navigation-link'):
        title = article.get_text().strip()
        link = f"https://dev.to{article['href']}"
        articles.append({'title': title, 'link': link})
        
    return articles

# Function to scrape the content of an article given its URL
def scrape_article_content(url):
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Get the first paragraph of the article content
        content = soup.find('div', class_='crayons-article__body').find('p').get_text().strip()
        return content
    except Exception as e:
        print(f"Error scraping article content: {e}")
        return "Interesting tech article."

# Function to clean up the tech news content (remove unnecessary parts but keep relevant news)
def clean_up_content(content):
    return content.strip()

# Function to generate a GPT-2 tweet based on a prompt
def generate_gpt2_tweet(prompt):
    inputs = gpt2_tokenizer.encode(prompt, return_tensors='pt', max_length=50, truncation=True)
    outputs = gpt2_model.generate(inputs, max_length=100, num_return_sequences=1, no_repeat_ngram_size=2, do_sample=True, temperature=0.7)
    tweet = gpt2_tokenizer.decode(outputs[0], skip_special_tokens=True)
    return tweet.strip()

# Function to select a random emotional template and combine it with cleaned tech news or keyphrase
def create_emotional_tweet(tech_news):
    cleaned_news = clean_up_content(tech_news)
    template = random.choice(REACTION_TEMPLATES)
    return template.format(tech_news=cleaned_news)

# Function to add emojis to tweets
def add_emojis(tweet):
    tech_emojis = ['🤖', '🚀', '💻', '🧠', '📱', '🌐', '🔧', '💡']
    return tweet + " " + random.choice(tech_emojis)

# Function to generate tweet content from dev.to articles
def generate_tweets_from_dev_to_articles(articles):
    tweets = []
    for article in articles:
        title = article['title']
        link = article['link']
        
        # Scrape the article content
        content = scrape_article_content(link)
        
        # Create emotional tweet based on article content
        tweet = create_emotional_tweet(content)
        tweet_with_link = tweet + f" {link} #TechNews"
        tweets.append(tweet_with_link)
    return tweets

# GUI Setup using Tkinter
def create_gui():
    def fetch_dev_to_and_generate_tweets():
        try:
            articles = scrape_dev_to()
            tweets = generate_tweets_from_dev_to_articles(articles)
            tweet_output.delete(1.0, tk.END)  # Clear the output text area
            for tweet in tweets:
                tweet_output.insert(tk.END, tweet + "\n\n")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to fetch dev.to articles or generate tweets: {str(e)}")

    # Main window
    root = tk.Tk()
    root.title("Tech Tweet Generator")
    root.geometry("600x400")

    # Button to fetch dev.to articles and generate tweets
    tk.Button(root, text="Generate dev.to Tweets", command=fetch_dev_to_and_generate_tweets).pack(pady=10)

    # Output area for the generated tweets
    tk.Label(root, text="Generated Tweets:").pack()
    tweet_output = scrolledtext.ScrolledText(root, width=70, height=10)
    tweet_output.pack()

    root.mainloop()

# Start the GUI
if __name__ == "__main__":
    create_gui()
