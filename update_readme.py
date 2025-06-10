import requests
import os

# GitHub username
USERNAME = 'imamit-b'

# GitHub API URL
API_URL = f'https://api.github.com/users/{USERNAME}'

# Fetch user data
response = requests.get(API_URL)
data = response.json()

# Extract relevant information
name = data.get('name', 'Amit Barman')
bio = data.get('bio', 'PhD Candidate, Computer Science & Engineering')
public_repos = data.get('public_repos', 0)
followers = data.get('followers', 0)
following = data.get('following', 0)
repos_url = data.get('repos_url')

# Fetch repositories
repos_response = requests.get(repos_url)
repos_data = repos_response.json()

# Generate project list
projects = []
for repo in repos_data:
    projects.append(f"- [{repo['name']}]({repo['html_url']})")

# Create README content
readme_content = f"""# {name}

{bio}  
Jadavpur University, Kolkata, India

---

## GitHub Contributions

- Public Repositories: {public_repos}
- Followers: {followers}
- Following: {following}

### Projects

{"\n".join(projects)}

---

## Connect with Me

- 📧 Email: [amitbarman811@gmail.com](mailto:amitbarman811@gmail.com)  
- 🐙 GitHub: [github.com/{USERNAME}](https://github.com/{USERNAME})  
- 💼 LinkedIn: [linkedin.com/in/amitjucse](https://linkedin.com/in/amitjucse)  

---

*Thank you for visiting my profile! Feel free to reach out for collaboration or inquiries.*
"""

# Write to README.md
with open('README.md', 'w') as f:
    f.write(readme_content)

print("README.md has been updated.")

