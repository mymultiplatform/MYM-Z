import requests
import tkinter as tk
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from bs4 import BeautifulSoup
import time
import numpy as np
import cv2
import pyttsx3
import os
import moviepy.editor as mpe
import platform
import json
import discord
from discord import Webhook, RequestsWebhookAdapter
import praw  # Reddit API
from googleapiclient.discovery import build  # YouTube API
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import tweepy  # Twitter API

# Constants and Global Variables
REMOTE_SERVICES = ['Discord', 'Remote PC', 'iPhone Remote']
MEDIA_TYPES = ['TEXT', 'IMAGE', 'VIDEO', 'AUDIO']
VPN_LOCATIONS = {'USA': 'VPN_USA', 'MEXICO': 'VPN_MEXICO'}
REVENUE_SOURCES = ['Bank', 'Paypal', 'BTC']
LIMITATIONS = {'Spam': 'Limit Spam Frequency', 'User': 'User Specific Limits'}
UNSPLASH_API_URL = "https://source.unsplash.com/random/640x480/?"
DISCORD_WEBHOOK_URL = "YOUR_DISCORD_WEBHOOK_URL"  # Replace with your actual Discord webhook URL
REDDIT_CLIENT_ID = "YOUR_REDDIT_CLIENT_ID"  # Replace with your Reddit API credentials
REDDIT_CLIENT_SECRET = "YOUR_REDDIT_CLIENT_SECRET"
REDDIT_USER_AGENT = "YOUR_REDDIT_USER_AGENT"
YOUTUBE_API_KEY = "YOUR_YOUTUBE_API_KEY"  # Replace with your YouTube API key
INSTAGRAM_USERNAME = "YOUR_INSTAGRAM_USERNAME"  # Replace with your Instagram username
INSTAGRAM_PASSWORD = "YOUR_INSTAGRAM_PASSWORD"  # Replace with your Instagram password
TWITTER_API_KEY = "YOUR_TWITTER_API_KEY"  # Replace with your Twitter API credentials
TWITTER_API_SECRET = "YOUR_TWITTER_API_SECRET"
TWITTER_ACCESS_TOKEN = "YOUR_TWITTER_ACCESS_TOKEN"
TWITTER_ACCESS_SECRET = "YOUR_TWITTER_ACCESS_SECRET"

# Media Generation and Management
class MediaBuilder:
    def __init__(self):
        self.media_content = []

    def build_media(self, media_type: str, content: str):
        if media_type in MEDIA_TYPES:
            self.media_content.append({'type': media_type, 'content': content})
            print(f"Media of type {media_type} built successfully.")
        else:
            print("Unsupported media type.")

    def deploy_media(self):
        for media in self.media_content:
            print(f"Deploying media: {media}")
        self.media_content.clear()

# User Authentication
class UserAuthentication:
    def authenticate(self, method: str):
        print(f"Authenticating using {method}...")
        return method in ['I'M NOT A ROBOT', 'HUMAN TEST', 'IPHONE REMOTE', 'GIZMO REMOTE']

# Server and VPN Management
class ServerManager:
    def __init__(self):
        self.connected_vpn = None

    def connect_vpn(self, location: str):
        if location in VPN_LOCATIONS:
            self.connected_vpn = VPN_LOCATIONS[location]
            print(f"Connected to VPN: {self.connected_vpn}")
        else:
            print("VPN location not supported.")

    def deploy_server(self, server_type: str):
        print(f"Deploying server: {server_type}")

# Error Handling
class ErrorHandling:
    def check_errors(self):
        errors = []
        if platform.system() == "Windows":
            errors.append("Windows specific error detected")
        return errors

    def suggest_fix(self, errors):
        for error in errors:
            print(f"Suggested fix for {error}: Apply standard correction.")

# Image Generation
class ImageGenerator:
    def fetch_images(self, keywords, count=1):
        images = []
        for i in range(count):
            keyword = keywords[i % len(keywords)]
            response = requests.get(f"{UNSPLASH_API_URL}{keyword}")
            if response.status_code == 200:
                image_path = f"generated_image_{i + 1}.jpg"
                with open(image_path, 'wb') as f:
                    f.write(response.content)
                images.append(image_path)
                print(f"Image fetched successfully for keyword: {keyword}")
            else:
                print(f"Failed to fetch image for keyword: {keyword}")
        return images

# News Fetching, Text-to-Speech, Video Generation, and Social Media Upload
class NewsProcessor:
    def __init__(self):
        self.reddit = praw.Reddit(client_id=REDDIT_CLIENT_ID,
                                  client_secret=REDDIT_CLIENT_SECRET,
                                  user_agent=REDDIT_USER_AGENT)
        self.twitter_auth = tweepy.OAuthHandler(TWITTER_API_KEY, TWITTER_API_SECRET)
        self.twitter_auth.set_access_token(TWITTER_ACCESS_TOKEN, TWITTER_ACCESS_SECRET)
        self.twitter_api = tweepy.API(self.twitter_auth)

    def fetch_news(self):
        print("Fetching news from BBC...")
        try:
            driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
            driver.get("https://www.bbc.com/news")
            time.sleep(20)
            soup = BeautifulSoup(driver.page_source, "html.parser")
            articles = soup.find_all('h2', {"data-testid": "card-headline"}, limit=3)
            news = []
            for article in articles:
                title = article.text if article else "No title available."
                description = article.find_next('p').text if article.find_next('p') else "No description available."
                news.append((title, description))
                print(f"Title: {title}")
                print(f"Description: {description}")
            driver.quit()
        except Exception as e:
            print(f"Failed to fetch news: {e}")
            news = [("Error", f"Failed to fetch news: {e}")]
        
        print("Fetching news from Reddit...")
        try:
            subreddit = self.reddit.subreddit('news')
            for submission in subreddit.hot(limit=3):
                title = submission.title
                description = submission.selftext if submission.selftext else "No description available."
                news.append((title, description))
                print(f"Reddit Title: {title}")
                print(f"Reddit Description: {description}")
        except Exception as e:
            print(f"Failed to fetch news from Reddit: {e}")
            news.append(("Error", f"Failed to fetch news from Reddit: {e}"))
        
        return news

    def text_to_speech(self, news):
        engine = pyttsx3.init()
        audio_files = []
        for i, (title, description) in enumerate(news):
            text = f"{title}. {description}"
            audio_path = f"news_{i + 1}.wav"
            engine.save_to_file(text, audio_path)
            audio_files.append(audio_path)
        engine.runAndWait()
        return audio_files

    def generate_video(self, news, audio_files, images):
        fourcc = cv2.VideoWriter_fourcc(*'mp4v')
        fps = 24
        frame_size = (640, 480)
        word_duration = 14
        num_frames_per_word = fps * word_duration
        num_frames = num_frames_per_word * len(news)

        video_path = 'news_video.mp4'
        out = cv2.VideoWriter(video_path, fourcc, fps, frame_size)

        for i in range(num_frames):
            frame = np.zeros((480, 640, 3), dtype=np.uint8)
            paragraph_index = i // num_frames_per_word
            title, description = news[paragraph_index]
            text = f"{title}: {description}"
            font = cv2.FONT_HERSHEY_SIMPLEX
            font_scale = 0.7
            font_thickness = 2
            max_line_width = frame_size[0] - 40
            wrapped_text = self.wrap_text(text, font, font_scale, max_line_width)
            y0, dy = 50, 25
            for j, line in enumerate(wrapped_text):
                text_size = cv2.getTextSize(line, font, font_scale, font_thickness)[0]
                text_x = int((frame_size[0] - text_size[0]) / 2)
                text_y = y0 + j * dy
                cv2.putText(frame, line, (text_x, text_y), font, font_scale, (255, 255, 255), font_thickness, lineType=cv2.LINE_AA)
            # Overlay image if available
            if paragraph_index < len(images):
                image = cv2.imread(images[paragraph_index])
                image_resized = cv2.resize(image, frame_size)
                frame = cv2.addWeighted(frame, 0.5, image_resized, 0.5, 0)
            out.write(frame)

        out.release()
        video_clip = mpe.VideoFileClip(video_path)
        audio_clips = [mpe.AudioFileClip(audio) for audio in audio_files]
        audio_start_times = [i * word_duration for i in range(len(news))]
        final_audio = mpe.CompositeAudioClip([
            audio_clips[i].set_start(audio_start_times[i])
            for i in range(len(news))
        ])
        final_clip = video_clip.set_audio(final_audio)
        final_clip.write_videofile("final_news_video_with_audio.mp4", codec="libx264", fps=fps)

        for audio in audio_files:
            os.remove(audio)

        print("Video with synchronized audio saved successfully.")

    def upload_to_tiktok(self):
        print("Uploading videos to TikTok...")
        videos_uploaded = 0
        while videos_uploaded < 20:
            try:
                driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
                driver.get("https://www.tiktok.com/upload")
                time.sleep(10)  # Wait for page to load

                # Check if "I'm not a robot" pop-up appears
                if "I'm not a robot" in driver.page_source:
                    print("Authentication required: 'I'm not a robot'. Sending Discord notification...")
                    webhook = Webhook.from_url(DISCORD_WEBHOOK_URL, adapter=RequestsWebhookAdapter())
                    webhook.send("TikTok upload blocked by 'I'm not a robot' verification. Please authenticate using your iPhone remote.")
                    time.sleep(60)  # Wait for manual authentication

                upload_input = driver.find_element_by_css_selector("input[type='file']")
                upload_input.send_keys(os.path.abspath("final_news_video_with_audio.mp4"))
                time.sleep(5)

                post_button = driver.find_element_by_css_selector("button[type='submit']")
                post_button.click()
                time.sleep(10)  # Wait for upload to complete

                print(f"Video {videos_uploaded + 1} uploaded successfully.")
                videos_uploaded += 1
                driver.quit()

            except Exception as e:
                print(f"Failed to upload video: {e}")
                driver.quit()
                webhook = Webhook.from_url(DISCORD_WEBHOOK_URL, adapter=RequestsWebhookAdapter())
                webhook.send(f"Failed to upload video: {e}")

    def upload_to_youtube(self):
        print("Uploading videos to YouTube Shorts...")
        youtube = build('youtube', 'v3', developerKey=YOUTUBE_API_KEY)
        for i in range(20):
            try:
                request_body = {
                    'snippet': {
                        'title': f'News Update {i + 1}',
                        'description': 'Daily news update generated automatically.',
                        'tags': ['news', 'daily update', 'automated'],
                        'categoryId': '25',
                    },
                    'status': {
                        'privacyStatus': 'public',
                        'madeForKids': False,
                    }
                }

                media_file = "final_news_video_with_audio.mp4"
                request = youtube.videos().insert(
                    part="snippet,status",
                    body=request_body,
                    media_body=media_file
                )
                response = request.execute()
                print(f"Uploaded video {i + 1} to YouTube Shorts successfully. Video ID: {response['id']}")
            except Exception as e:
                print(f"Failed to upload video to YouTube Shorts: {e}")

    def upload_to_instagram(self):
        print("Uploading videos to Instagram Reels...")
        videos_uploaded = 0
        options = Options()
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
        driver.get("https://www.instagram.com")
        time.sleep(3)
        
        # Log in to Instagram
        try:
            username = driver.find_element(By.NAME, "username")
            password = driver.find_element(By.NAME, "password")
            username.send_keys(INSTAGRAM_USERNAME)
            password.send_keys(INSTAGRAM_PASSWORD)
            password.send_keys(Keys.RETURN)
            time.sleep(5)

            while videos_uploaded < 20:
                driver.get("https://www.instagram.com")
                time.sleep(5)

                # Open the Reels upload page
                driver.get("https://www.instagram.com/create/style/")
                time.sleep(5)

                # Upload video
                upload_input = driver.find_element(By.CSS_SELECTOR, "input[type='file']")
                upload_input.send_keys(os.path.abspath("final_news_video_with_audio.mp4"))
                time.sleep(5)

                # Proceed with sharing the video
                next_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Next')]")
                next_button.click()
                time.sleep(5)
                share_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Share')]")
                share_button.click()
                time.sleep(10)

                print(f"Reel {videos_uploaded + 1} uploaded successfully.")
                videos_uploaded += 1

            driver.quit()
        except Exception as e:
            print(f"Failed to upload video to Instagram Reels: {e}")
            driver.quit()

    def upload_to_twitter(self):
        print("Uploading videos to Twitter...")
        for i in range(20):
            try:
                video_path = "final_news_video_with_audio.mp4"
                status = f"Daily News Update {i + 1}: Check out the latest news! #news #dailyupdate"
                media = self.twitter_api.media_upload(video_path)
                self.twitter_api.update_status(status=status, media_ids=[media.media_id])
                print(f"Uploaded video {i + 1} to Twitter successfully.")
            except Exception as e:
                print(f"Failed to upload video to Twitter: {e}")

    def wrap_text(self, text, font, font_scale, max_width):
        words = text.split(' ')
        lines = []
        current_line = ''

        for word in words:
            test_line = current_line + word + ' '
            text_size = cv2.getTextSize(test_line, font, font_scale, 1)[0]
            if text_size[0] <= max_width:
                current_line = test_line
            else:
                lines.append(current_line)
                current_line = word + ' '

        lines.append(current_line.strip())
        return lines

# Main Control Class
class MultiPlatformController:
    def __init__(self):
        self.media_builder = MediaBuilder()
        self.auth = UserAuthentication()
        self.server_manager = ServerManager()
        self.error_handler = ErrorHandling()
        self.news_processor = NewsProcessor()
        self.image_generator = ImageGenerator()

    def deploy(self):
        print("Starting daily deployments...")
        self.media_builder.deploy_media()

    def authenticate_user(self):
        methods = ['I'M NOT A ROBOT', 'HUMAN TEST']
        for method in methods:
            if self.auth.authenticate(method):
                print(f"User authenticated with {method}.")
            else:
                print(f"Authentication failed with {method}.")

    def check_errors_and_fix(self):
        errors = self.error_handler.check_errors()
        if errors:
            print("Errors detected:", errors)
            self.error_handler.suggest_fix(errors)
        else:
            print("No errors detected.")

    def manage_news(self):
        news = self.news_processor.fetch_news()
        images = self.image_generator.fetch_images([title for title, _ in news], count=len(news))
        audio_files = self.news_processor.text_to_speech(news)
        self.news_processor.generate_video(news, audio_files, images)
        self.news_processor.upload_to_tiktok()
        self.news_processor.upload_to_youtube()
        self.news_processor.upload_to_instagram()
        self.news_processor.upload_to_twitter()

    def remote_operations(self):
        print("Executing remote operations...")

    def clone_emergency(self):
        print("Performing emergency clone...")

# GUI Setup and Control
root = tk.Tk()
root.title("Top News")
root.geometry("700x400")

news_frame = tk.Frame(root)
news_frame.pack(fill="both", expand=True)

controller = MultiPlatformController()

def display_news():
    print("Displaying news...")
    for widget in news_frame.winfo_children():
        widget.destroy()
    news_data = controller.news_processor.fetch_news()
    images = controller.image_generator.fetch_images([title for title, _ in news_data], count=len(news_data))
    audio_files = controller.news_processor.text_to_speech(news_data)
    controller.news_processor.generate_video(news_data, audio_files, images)
    controller.news_processor.upload_to_tiktok()
    controller.news_processor.upload_to_youtube()
    controller.news_processor.upload_to_instagram()
    controller.news_processor.upload_to_twitter()
    for i, (title, description) in enumerate(news_data):
        title_label = tk.Label(news_frame, text=title, font=("Arial", 14, "bold"))
        title_label.grid(row=i*2, column=0, sticky="w", padx=10, pady=5)
        desc_label = tk.Label(news_frame, text=description, wraplength=600, justify="left")
        desc_label.grid(row=i*2+1, column=0, sticky="w", padx=10, pady=5)
    print("News displayed!")

connect_button = tk.Button(root, text="Connect", command=display_news, font=("Arial", 12))
connect_button.pack(pady=20)

root.mainloop()
