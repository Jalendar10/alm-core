# 🚀 Publish to PyPI - Simple 3-Step Guide

## ✨ Modern Method: Trusted Publishers (Recommended)

**No API tokens needed!** GitHub Actions publishes automatically using OpenID Connect.

### Step 1: Configure PyPI Trusted Publisher

Go to: **https://pypi.org/manage/account/publishing/**

Click **"Add a new pending publisher"** and fill in:

```
PyPI Project Name:  alm-core
Owner:             Jalendar10
Repository name:   alm-core
Workflow name:     publish-to-pypi.yml
Environment name:  pypi
```

Click **"Add"**. Done! ✅

### Step 2: Create GitHub Environment (Optional but Recommended)

Go to: **https://github.com/Jalendar10/alm-core/settings/environments**

1. Click **"New environment"**
2. Name: `pypi`
3. (Optional) Add yourself as required reviewer
4. Click **"Save"**

### Step 3: Create a Release

Go to: **https://github.com/Jalendar10/alm-core/releases/new**

Fill in:
- **Tag**: `v0.1.0` (create new tag)
- **Title**: `v0.1.0 - Initial Release`
- **Description**: (Copy from below)

```markdown
## 🎉 First Release of ALM Core!

Agent Language Model (ALM) - A deterministic, policy-driven architecture for robust AI agents.

### Installation
```bash
pip install alm-core
```

### Features
- Constitutional Policy Engine with hard constraints
- Data Airlock with PII protection
- BDI Deterministic Controller
- Multi-LLM support (OpenAI, Anthropic, local)
- Browser and desktop automation tools
- Deep research capabilities

### Documentation
See the [README](https://github.com/Jalendar10/alm-core) for complete documentation.
```

Click **"Publish release"** 🎉

### What Happens Next (Automatic!)

1. ✅ GitHub Actions triggers
2. ✅ Builds package (wheel + source)
3. ✅ Runs tests
4. ✅ Publishes to PyPI
5. ✅ Package appears at: https://pypi.org/project/alm-core/
6. ✅ Anyone can install: `pip install alm-core`

**That's it!** No manual uploads, no tokens, fully automatic! 🚀

---

## 📋 Quick Checklist

- [ ] Configure Trusted Publisher on PyPI (Step 1)
- [ ] Create `pypi` environment on GitHub (Step 2)
- [ ] Create release v0.1.0 on GitHub (Step 3)
- [ ] Wait for GitHub Actions to complete (~2 min)
- [ ] Check PyPI: https://pypi.org/project/alm-core/
- [ ] Test: `pip install alm-core`
- [ ] Celebrate! 🎉

---

## 🧪 Want to Test First?

### Test on TestPyPI (Safe!)

1. Go to: **https://test.pypi.org/manage/account/publishing/**
2. Add same publisher config as above
3. Go to GitHub Actions: https://github.com/Jalendar10/alm-core/actions
4. Click **"Publish to PyPI"** workflow
5. Click **"Run workflow"** → Select `main` branch → **"Run workflow"**
6. This publishes to **TestPyPI** (safe for testing)
7. View at: https://test.pypi.org/project/alm-core/
8. Test install:
   ```bash
   pip install --index-url https://test.pypi.org/simple/ --extra-index-url https://pypi.org/simple/ alm-core
   ```

If successful, proceed to real PyPI with Step 1-3 above!

---

## 🔄 Future Updates

To publish version 0.1.1, 0.2.0, etc:

1. **Update version** in `setup.py` and `pyproject.toml`
2. **Commit**: `git commit -am "Bump version to 0.1.1"`
3. **Push**: `git push`
4. **Create release**: Tag `v0.1.1` on GitHub
5. **Done!** Auto-published

---

## 📊 Monitor Progress

Watch the workflow run:
**https://github.com/Jalendar10/alm-core/actions**

You'll see:
- 🔨 Build step
- ✅ Tests passing
- 📦 Publishing to PyPI
- 🎉 Success!

---

## ⚡ TL;DR - Ultra Quick Guide

```bash
# 1. Configure on PyPI (one-time)
Visit: https://pypi.org/manage/account/publishing/
Add: alm-core, Jalendar10, alm-core, publish-to-pypi.yml, pypi

# 2. Create GitHub Release
Visit: https://github.com/Jalendar10/alm-core/releases/new
Tag: v0.1.0
Click: Publish release

# 3. Wait ~2 minutes
GitHub Actions builds and publishes automatically

# 4. Done!
pip install alm-core
```

---

## 🆘 Troubleshooting

**Workflow fails?**
- Check you configured Trusted Publisher on PyPI first
- Verify environment name is exactly `pypi`
- Check workflow logs: https://github.com/Jalendar10/alm-core/actions

**Package not appearing on PyPI?**
- Wait a few minutes for indexing
- Check workflow completed successfully (green checkmark)
- Verify release was tagged correctly (v0.1.0)

**Need help?**
- See detailed guide: `TRUSTED_PUBLISHER_SETUP.md`
- Check PyPI docs: https://docs.pypi.org/trusted-publishers/

---

## 🎁 What You Get

After publishing, anyone worldwide can:

```bash
# Install your package
pip install alm-core

# Use it in code
from alm_core import AgentLanguageModel

agent = AgentLanguageModel(model="gpt-4")
result = agent.execute("Hello, world!")
```

**Your package will be live at:**
- 🌐 PyPI: https://pypi.org/project/alm-core/
- 📦 GitHub: https://github.com/Jalendar10/alm-core
- 📚 Docs: README shown on PyPI page

---

## ✅ Summary

**Old way (manual):**
- Generate API token
- Install twine
- Build package manually
- Upload with credentials
- Hope nothing leaks

**New way (trusted publishers):**
- Configure once on PyPI
- Create GitHub release
- Everything automatic
- Secure by design
- Zero maintenance

**You're using the new way!** 🎉

---

Ready to publish? Just follow **Step 1-2-3** above! 🚀
