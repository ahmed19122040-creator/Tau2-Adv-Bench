# Push to Anonymous GitHub Repository

## 1. Create Anonymous GitHub Account

1. Get temp email: https://temp-mail.org or https://proton.me
2. Create GitHub account: https://github.com/join
3. Username suggestion: `neurips2026-submission`

## 2. Create Repository

1. Go to: https://github.com/new
2. Repository name: `tau2-adv-bench`
3. Description: `Code for NeurIPS 2026 Evaluations & Datasets Track submission`
4. Visibility: **Public** (required for review)
5. Click "Create repository"

## 3. Push Code

```bash
cd ~/tau2-adv-bench-anonymous

# Initialize if needed
git init
git branch -M main

# Add all files
git add .
git commit -m "Initial commit: τ²-Adversarial benchmark code"

# Add your anonymous repo as remote
git remote add origin https://github.com/YOUR-ANON-USERNAME/tau2-adv-bench.git

# Push
git push -u origin main
```

## 4. For NeurIPS Submission

In your OpenReview submission, provide:

**Code URL:** `https://github.com/YOUR-ANON-USERNAME/tau2-adv-bench`

**Installation:**
```bash
pip install git+https://github.com/YOUR-ANON-USERNAME/tau2-adv-bench.git
```

**Usage:**
```bash
tau-adversarial --model gpt-4 --domain airline --output results/
```

---

Your code is now fully anonymized and ready for submission!
