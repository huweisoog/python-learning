# Setting Up SSH Access for GitHub

1. **Check for existing SSH keys:**
   ```
   ls -al ~/.ssh
   ```
   Look for files named `id_rsa.pub`, `id_ecdsa.pub`, or `id_ed25519.pub`.

2. **Generate a new SSH key if needed:**
   ```
   ssh-keygen -t ed25519 -C "your_email@example.com"
   ```
   Press Enter to accept the default file location and optionally set a passphrase.

3. **Start the SSH agent:**
   ```
   eval "$(ssh-agent -s)"
   ```

4. **Add your SSH key to the agent:**
   ```
   ssh-add ~/.ssh/id_ed25519
   ```

5. **Copy your public key:**
   ```
   cat ~/.ssh/id_ed25519.pub
   ```
   Copy the output.

6. **Add the key to your GitHub account:**
   - Go to GitHub → Settings → SSH and GPG keys
   - Click "New SSH key"
   - Paste your key and give it a title

7. **Test your connection:**
   ```
   ssh -T git@github.com
   ```
   You should see a welcome message.

8. **Clone a repository using SSH:**
   ```
   git clone git@github.com:username/repository.git
   ```

9. **For existing repositories, update the remote URL:**
   ```
   git remote set-url origin git@github.com:username/repository.git
   ```

Remember to replace `your_email@example.com`, `username`, and `repository` with your actual information.
