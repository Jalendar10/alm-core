# 🔐 Trusted Publisher Setup for PyPI

**Trusted Publishers** is the modern, secure way to publish to PyPI using GitHub Actions **without API tokens**. It uses OpenID Connect (OIDC) for authentication.

## ✅ Benefits

- 🔒 **More Secure**: No API tokens to manage or leak
- 🤖 **Automatic**: Publishes on every release automatically
- 🎯 **Simple**: No credentials needed in GitHub secrets
- ✨ **Free**: No cost, works for all PyPI users

## 📋 Setup Instructions

### Step 1: Configure Trusted Publisher on PyPI

You need to do this **BEFORE** your first publish using GitHub Actions.

#### Option A: For New Package (First Time Publishing)

1. Go to: **https://pypi.org/manage/account/publishing/**

2. Click **"Add a new pending publisher"**

3. Fill in the form:
   - **PyPI Project Name**: `alm-core`
   - **Owner**: `Jalendar10` (your GitHub username)
   - **Repository name**: `alm-core`
   - **Workflow name**: `publish-to-pypi.yml`
   - **Environment name**: `pypi` (optional but recommended)

4. Click **"Add"**

5. The publisher will be "pending" until first successful publish

#### Option B: For Existing Package (Already Published)

1. Go to your project: **https://pypi.org/manage/project/alm-core/settings/publishing/**

2. Click **"Add a new publisher"**

3. Fill in the same form as above

4. Click **"Add"**

### Step 2: Configure GitHub Environment (Recommended)

This adds an extra layer of protection.

1. Go to: **https://github.com/Jalendar10/alm-core/settings/environments**

2. Click **"New environment"**

3. Name: `pypi`

4. **Configure protection rules** (optional but recommended):
   - ✅ **Required reviewers**: Add yourself or trusted maintainers
   - ✅ **Wait timer**: 0 minutes (or add delay for extra safety)
   - ✅ **Deployment branches**: Only `main` branch

5. Click **"Save protection rules"**

6. Repeat for `testpypi` environment (for testing)

### Step 3: Create a GitHub Release

The workflow triggers automatically on new releases:

#### Using GitHub Web Interface:

1. Go to: **https://github.com/Jalendar10/alm-core/releases/new**

2. Fill in:
   - **Tag version**: `v0.1.0` (create new tag)
   - **Release title**: `v0.1.0 - Initial Release`
   - **Description**: 
     ```markdown
     ## 🎉 First Release of ALM Core!
     
     Agent Language Model (ALM) - A deterministic, policy-driven architecture for robust AI agents.
     
     ### Features
     - Constitutional Policy Engine
     - Data Airlock with PII protection
     - BDI Deterministic Controller
     - Multi-LLM support (OpenAI, Anthropic, local)
     - Browser and desktop automation tools
     - Deep research capabilities
     
     ### Installation
     ```bash
     pip install alm-core
     ```
     
     See the [README](https://github.com/Jalendar10/alm-core) for full documentation.
     ```

3. Click **"Publish release"**

4. GitHub Actions will automatically:
   - Build the package
   - Publish to PyPI
   - Update the release with build artifacts

#### Using Git Command Line:

```bash
cd /Users/jalendarreddy/Downloads/research/ALM

# Create and push a tag
git tag -a v0.1.0 -m "Release version 0.1.0"
git push origin v0.1.0

# Then create release on GitHub web interface
# Or use GitHub CLI:
gh release create v0.1.0 --title "v0.1.0 - Initial Release" --notes "First release of ALM Core"
```

### Step 4: Manual Publish (Alternative)

You can also trigger the workflow manually for testing:

1. Go to: **https://github.com/Jalendar10/alm-core/actions**

2. Click on **"Publish to PyPI"** workflow

3. Click **"Run workflow"** button

4. Select branch: `main`

5. Click **"Run workflow"**

6. This will publish to **TestPyPI** (safe for testing)

## 📁 Files Created

### `.github/workflows/publish-to-pypi.yml`
Main publishing workflow with:
- **Build job**: Creates wheel and source distribution
- **Publish to PyPI**: Automatic on release
- **Publish to TestPyPI**: Manual trigger for testing

### `.github/workflows/test.yml`
Testing workflow that runs on:
- Every push to `main`
- Every pull request
- Tests on Python 3.8-3.12
- Tests on Linux, Windows, macOS

## 🔄 Publishing Workflow

### Automatic (Recommended):

1. **Update version** in `setup.py` and `pyproject.toml`:
   ```python
   version="0.1.1"
   ```

2. **Commit and push**:
   ```bash
   git add setup.py pyproject.toml
   git commit -m "Bump version to 0.1.1"
   git push origin main
   ```

3. **Create release on GitHub**:
   - Tag: `v0.1.1`
   - Title: `v0.1.1`
   - Description: What's new

4. **GitHub Actions automatically**:
   - ✅ Builds package
   - ✅ Publishes to PyPI
   - ✅ Creates release artifacts

5. **Done!** Package is live on PyPI

### Manual (For Testing):

1. Go to GitHub Actions
2. Select "Publish to PyPI" workflow
3. Click "Run workflow"
4. Publishes to TestPyPI for testing

## 🎯 Configuration Details

### PyPI Trusted Publisher Form

Here's exactly what to enter on PyPI:

```
PyPI Project Name: alm-core
Owner: Jalendar10
Repository name: alm-core
Workflow name: publish-to-pypi.yml
Environment name: pypi
```

### For TestPyPI (Optional Testing)

1. Go to: **https://test.pypi.org/manage/account/publishing/**
2. Same form as above
3. Use for testing before real PyPI

## 🔐 Security Features

1. **No API Tokens**: Uses OIDC, not tokens
2. **GitHub Environment Protection**: Requires approval (optional)
3. **Repository-Specific**: Only this repo can publish
4. **Workflow-Specific**: Only this workflow file can publish
5. **Branch Protection**: Can limit to `main` branch only

## ⚠️ Important Notes

1. **First-time setup**: Must configure Trusted Publisher on PyPI **BEFORE** first workflow run
2. **Pending status**: New packages show "pending" until first successful publish
3. **Environment names**: Must match exactly between PyPI config and workflow
4. **Workflow filename**: Must be exact: `publish-to-pypi.yml`

## 🧪 Testing Before Production

### Test Publish Flow:

1. Configure trusted publisher on **TestPyPI** first
2. Run workflow manually (publishes to TestPyPI)
3. Verify package at: https://test.pypi.org/project/alm-core/
4. Test install:
   ```bash
   pip install --index-url https://test.pypi.org/simple/ --extra-index-url https://pypi.org/simple/ alm-core
   ```
5. If successful, configure for real PyPI and create release

## 📊 Workflow Status

Check workflow runs at:
**https://github.com/Jalendar10/alm-core/actions**

You'll see:
- ✅ Build status
- ✅ Publish status
- 📦 Artifacts (wheel + source)
- 📝 Logs for debugging

## 🎉 Success Indicators

After successful publish:

1. **GitHub Actions**: Green checkmark ✅
2. **PyPI**: Package appears at https://pypi.org/project/alm-core/
3. **Installation works**: `pip install alm-core`
4. **Release shows artifacts**: Wheel and source files attached

## 🔄 Comparison: Old vs New Way

### Old Way (API Tokens):
```bash
# Manual process
python -m build
python -m twine upload dist/*
# Enter username: __token__
# Enter password: pypi-AgE...
```

❌ Security risk: Token can leak  
❌ Manual: Need to run commands  
❌ Maintenance: Token expires  

### New Way (Trusted Publishers):
```bash
# Just create a release on GitHub
# GitHub Actions does everything automatically
```

✅ Secure: No tokens  
✅ Automatic: No manual steps  
✅ Simple: One-time setup  

## 📖 Resources

- **PyPI Trusted Publishers Guide**: https://docs.pypi.org/trusted-publishers/
- **GitHub OIDC Documentation**: https://docs.github.com/en/actions/deployment/security-hardening-your-deployments/about-security-hardening-with-openid-connect
- **PyPA Publish Action**: https://github.com/pypa/gh-action-pypi-publish

## 🚀 Quick Start Checklist

- [ ] Push workflows to GitHub (`.github/workflows/*.yml`)
- [ ] Configure Trusted Publisher on PyPI
- [ ] Create GitHub environment `pypi` (optional but recommended)
- [ ] Create first release on GitHub (tag: `v0.1.0`)
- [ ] Watch GitHub Actions run
- [ ] Verify package on PyPI
- [ ] Test: `pip install alm-core`
- [ ] Celebrate! 🎉

---

**This is the modern, recommended way to publish Python packages!** 🔐✨
