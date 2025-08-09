# Bulk Repo Privacy Changer 🔒

A simple Python script to change the visibility of ALL your public GitHub repositories to **private**.

---

> ### ⚠️ **EXTREMELY IMPORTANT WARNING** ⚠️
>
> This script performs a **permanent action**. Once a repository is made private, public links will break and GitHub Pages sites will be unpublished.
>
> **Please use this with extreme caution!** It's a good idea to test it on a dummy account or repository first.
> **Also, this script doesn’t change your forked repos to private**

---

## How to Use 🚀

### 1. Prerequisites 🛠️

-   You need [Python 3](https://www.python.org/) installed.
-   Install the `requests` library:
    ```bash
    pip install requests
    ```

### 2. Get a GitHub Token 🔑

-   Go to **Settings** > **Developer settings** > **Personal access tokens** > **Tokens (classic)**.
-   Click **Generate new token**.
-   Give it a note (e.g., "Repo Privacy Script").
-   ✅ **IMPORTANT**: Check the `repo` scope. This is the only permission needed.
-   Generate the token and **copy it immediately**.

### 3. Set Environment Variable 🤫

For security, the script reads the token from an environment variable.

-   **On macOS/Linux:**
    ```bash
    export GITHUB_TOKEN="paste_your_token_here"
    ```
-   **On Windows (Command Prompt):**
    ```cmd
    setx GITHUB_TOKEN "paste_your_token_here"
    ```
    *(You'll need to restart your Command Prompt after running this.)*

### 4. Run the Script! ✨

Navigate to the script's directory and run:

```bash
python make_private.py
