import os
import requests

# --- Configuration ---
# Your GitHub Personal Access Token is read from an environment variable for security.
GITHUB_TOKEN = os.getenv('GITHUB_TOKEN')

# --- Main Script ---
if not GITHUB_TOKEN:
    print("❌ Error: 'GITHUB_TOKEN' environment variable not set.")
    print("Please follow the instructions to create a token and set it up.")
    exit()

print("🚀 Starting script to make public repos private...")

# Headers for the API request, including your token for authentication
headers = {
    "Authorization": f"token {GITHUB_TOKEN}",
    "Accept": "application/vnd.github.v3+json",
}

# This will hold all of your repositories
all_repos = []
page = 1
# Loop to get all pages of repositories (GitHub gives them in batches of 100)
while True:
    # API endpoint to list your repos
    repos_url = f"https://api.github.com/user/repos?per_page=100&page={page}"
    
    response = requests.get(repos_url, headers=headers)
    
    if response.status_code != 200:
        print(f"❌ Failed to fetch repositories. GitHub said: {response.json().get('message', 'Unknown Error')}")
        exit()
        
    data = response.json()
    if not data:
        # No more repositories on this page, so we break the loop
        break
        
    all_repos.extend(data)
    page += 1

print(f"Found {len(all_repos)} total repositories in your account.")

# Filter the list to get only the public ones
public_repos = [repo for repo in all_repos if not repo['private']]

if not public_repos:
    print("✅ All good! No public repositories were found.")
    exit()

print(f"Found {len(public_repos)} public repositories. Preparing to change visibility...")
input("Press Enter to continue or CTRL+C to cancel...") # A safety check!

# Loop through each public repository and change its visibility
for repo in public_repos:
    repo_name = repo['name']
    owner = repo['owner']['login']
    
    print(f"\nAttempting to make '{repo_name}' private...")
    
    # API endpoint for a specific repository
    update_url = f"https://api.github.com/repos/{owner}/{repo_name}"
    
    # The data we want to change: set 'private' to true
    payload = {"private": True}
    
    # Make the request to update the repository
    patch_response = requests.patch(update_url, headers=headers, json=payload)
    
    if patch_response.status_code == 200:
        print(f"✅ Success! Repository '{repo_name}' is now private.")
    else:
        print(f"❌ Failed for '{repo_name}'. Status: {patch_response.status_code}")
        print(f"   Reason: {patch_response.text}")

print("\n🎉 Script finished!")
