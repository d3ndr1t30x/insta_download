import instaloader
import os
from pathlib import Path  # Corrected import

# Define the path to the Downloads folder
downloads_path = Path.home() / "Downloads"

# Initialize Instaloader
loader = instaloader.Instaloader()

def download_post(post_url, folder_name):
    try:
        # Extract the shortcode from the post URL
        shortcode = post_url.strip('/').split('/')[-1]

        # Define a directory for the post download with the user's folder name
        post_folder = downloads_path / folder_name
        post_folder.mkdir(exist_ok=True)

        # Load the post
        post = instaloader.Post.from_shortcode(loader.context, shortcode)

        # Save images
        for i, image in enumerate(post.get_sidecar_nodes(), start=1):
            loader.download_pic(filename=str(post_folder / f"image_{i}.jpeg"), url=image.display_url, mtime=post.date)

        # Save caption and comments
        with open(post_folder / "post_details.txt", "w", encoding="utf-8") as f:
            f.write("Caption:\n" + (post.caption or "No caption") + "\n\n")
            f.write("Comments:\n")
            for comment in post.get_comments():
                f.write(f"{comment.owner.username}: {comment.text}\n")

        print(f"Post saved to {post_folder}")  # Corrected indentation
    except Exception as e:
        print("An error occurred:", e)

# Example usage
post_url = input("Enter the Instagram post URL: ")
folder_name = input("Enter the folder name to save the post: ")
download_post(post_url, folder_name)  # Corrected function name
