# GitHub Setup Guide for τ²-Adv-Bench

This guide will help you push your repository to GitHub and set it up properly.

---

## 📋 Prerequisites

- GitHub account (create one at https://github.com/signup if needed)
- Git installed locally (already done ✓)
- Repository initialized (already done ✓)

---

## 🚀 Step-by-Step GitHub Setup

### Step 1: Create GitHub Repository

1. Go to https://github.com/new
2. Fill in repository details:
   - **Repository name**: `tau2-adv-bench`
   - **Description**: "τ²-Adv-Bench: Adversarial Robustness Evaluation for Conversational Agents in Dual-Control Environments"
   - **Visibility**: Public (or Private if you prefer)
   - **DO NOT** initialize with README, .gitignore, or license (we already have these)

3. Click "Create repository"

### Step 2: Connect Local Repository to GitHub

GitHub will show you commands, but here's exactly what to do:

```bash
# 1. Navigate to your repository
cd ~/tau2-adv-bench

# 2. Add GitHub as remote (replace YOUR_USERNAME with your GitHub username)
git remote add origin https://github.com/YOUR_USERNAME/tau2-adv-bench.git

# 3. Verify remote was added
git remote -v

# 4. Push to GitHub
git push -u origin main
```

**Example with specific username:**
```bash
# If your GitHub username is "Ahm3dAlAli"
git remote add origin https://github.com/Ahm3dAlAli/tau2-adv-bench.git
git push -u origin main
```

### Step 3: Authenticate

When you push, GitHub will ask for authentication. You have two options:

#### Option A: GitHub CLI (Recommended)

```bash
# Install GitHub CLI (if not installed)
# macOS:
brew install gh

# Authenticate
gh auth login

# Then push
git push -u origin main
```

#### Option B: Personal Access Token

1. Go to https://github.com/settings/tokens
2. Click "Generate new token" → "Generate new token (classic)"
3. Set token name: "tau2-adv-bench"
4. Select scopes: `repo` (all sub-options)
5. Click "Generate token"
6. **Copy the token** (you won't see it again!)

When pushing, use:
- **Username**: Your GitHub username
- **Password**: The token you just copied

---

## ✅ Verify Upload

After pushing, visit:
```
https://github.com/YOUR_USERNAME/tau2-adv-bench
```

You should see:
- ✅ README.md displayed nicely
- ✅ All source files
- ✅ Paper in `paper/` folder
- ✅ Dataset in `data/domains/`

---

## 🎨 Customize Your Repository

### Add Topics/Tags

1. Go to your repository on GitHub
2. Click the ⚙️ icon next to "About"
3. Add topics:
   - `adversarial-robustness`
   - `conversational-ai`
   - `agent-safety`
   - `llm-evaluation`
   - `benchmark`
   - `neurips-2026`
   - `ai-safety`

### Add Repository Description

In the "About" section:
```
τ²-Adv-Bench: Adversarial Robustness Evaluation for Conversational Agents.
24 adversarial tasks, 5 attack strategies, comprehensive safety evaluation.
NeurIPS 2026 submission.
```

### Add Website

If you upload to Hugging Face, add:
```
https://huggingface.co/datasets/YOUR_USERNAME/tau2_adversarial
```

---

## 📝 Update README with Correct GitHub Links

After creating the repository, update these placeholders in your README:

```bash
cd ~/tau2-adv-bench

# Edit README.md and replace:
# "YOUR_USERNAME" with your actual GitHub username

# Then commit and push
git add README.md setup.py
git commit -m "docs: update GitHub links with actual username"
git push
```

---

## 🏷️ Create a Release (Optional but Recommended)

Once everything is uploaded:

```bash
# 1. Tag your current commit
git tag -a v1.0.0 -m "v1.0.0: Initial release for NeurIPS 2026 submission

- 24 adversarial tasks across 3 domains
- 5 attack strategies at 3 sophistication levels
- Comprehensive safety evaluation framework
- Full experimental results (360 evaluations)
- Research paper included"

# 2. Push tags
git push origin v1.0.0
```

Then on GitHub:
1. Go to "Releases" → "Create a new release"
2. Choose tag `v1.0.0`
3. Release title: `v1.0.0 - Initial Release`
4. Description: Copy the tag message
5. Attach paper PDF as release asset (optional)
6. Click "Publish release"

---

## 🔗 Link to τ²-Bench

Add a reference in τ²-Bench's repository:

1. Go to https://github.com/sierra-research/tau2-bench/pull/158
2. Add comment:
   ```
   Hi! I've created a standalone repository for the τ²-Adversarial
   framework: https://github.com/YOUR_USERNAME/tau2-adv-bench

   This will make it easier to maintain and use independently.
   I've also submitted this work to NeurIPS 2026 Evaluations & Datasets Track.
   ```

---

## 📊 Add GitHub Actions (Optional)

Create `.github/workflows/tests.yml`:

```yaml
name: Tests

on: [push, pull_request]

jobs:
  test:
    runs-on: ubuntu-latest
    strategy:
      matrix:
        python-version: [3.9, '3.10', 3.11]

    steps:
    - uses: actions/checkout@v3

    - name: Set up Python ${{ matrix.python-version }}
      uses: actions/setup-python@v4
      with:
        python-version: ${{ matrix.python-version }}

    - name: Install dependencies
      run: |
        python -m pip install --upgrade pip
        pip install -e .
        pip install pytest pytest-cov

    - name: Run tests
      run: |
        pytest tests/ -v --cov=tau_adversarial
```

Commit and push:
```bash
git add .github/workflows/tests.yml
git commit -m "ci: add GitHub Actions for automated testing"
git push
```

---

## 🌟 Add README Badges

Update your README.md to include status badges at the top:

```markdown
[![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Tests](https://github.com/YOUR_USERNAME/tau2-adv-bench/workflows/Tests/badge.svg)](https://github.com/YOUR_USERNAME/tau2-adv-bench/actions)
[![Paper](https://img.shields.io/badge/Paper-NeurIPS%202026-red.svg)](https://github.com/YOUR_USERNAME/tau2-adv-bench/blob/main/paper/Tau2_Adv_Bench_AgentBeats_AhmedAli.pdf)
```

---

## 📣 Promote Your Repository

After setup:

1. **Update your PR**: Add GitHub link to PR #158
2. **Share on Twitter/X**: Announce your work
3. **Add to your CV/website**: Link to the repository
4. **Update NeurIPS submission**: Include GitHub link in OpenReview

---

## 🔄 Daily Workflow

```bash
# Make changes to code
# ...

# Check status
git status

# Add changes
git add .

# Commit with descriptive message
git commit -m "feat: add new attack strategy"

# Push to GitHub
git push
```

---

## 📚 Useful Git Commands

```bash
# View commit history
git log --oneline

# Create new branch
git checkout -b feature/new-domain

# Switch branches
git checkout main

# Merge branch
git merge feature/new-domain

# Undo last commit (keep changes)
git reset --soft HEAD~1

# View changes
git diff
```

---

## 🆘 Troubleshooting

### "Permission denied (publickey)"

**Solution:** Set up SSH key or use HTTPS with token (as described above)

### "Updates were rejected"

**Solution:** Pull first, then push:
```bash
git pull origin main --rebase
git push
```

### "Large files rejected"

**Solution:** Use Git LFS for files >100MB:
```bash
# Install Git LFS
brew install git-lfs  # macOS
# or: sudo apt-get install git-lfs  # Linux

# Track large files
git lfs track "*.pdf"
git add .gitattributes
git commit -m "Add Git LFS tracking"
```

---

## ✅ Checklist

After completing this guide:

- [ ] Repository created on GitHub
- [ ] Local repo connected to GitHub
- [ ] Code pushed successfully
- [ ] README displays properly
- [ ] Topics/tags added
- [ ] Description added
- [ ] Links updated (replace YOUR_USERNAME)
- [ ] Release created (v1.0.0)
- [ ] GitHub Actions configured (optional)
- [ ] Badges added to README

---

**Your repository URL:**
```
https://github.com/YOUR_USERNAME/tau2-adv-bench
```

**Next step:** Update Hugging Face upload script with this GitHub URL!

---

For questions: ahmedaliahmedmohamed.al-ali@uzh.ch
