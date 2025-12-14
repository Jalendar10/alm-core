# Publishing to PyPI - Step by Step Guide

## ✅ Package Built Successfully!

Your distribution packages are ready:
- `dist/alm_core-0.1.0-py3-none-any.whl` (31KB) - Wheel package
- `dist/alm_core-0.1.0.tar.gz` (72KB) - Source distribution

## 📋 Prerequisites

1. **PyPI Account**: Create account at https://pypi.org/account/register/
2. **API Token**: Generate at https://pypi.org/manage/account/token/
3. **Twine Installed**: ✅ Already installed

## 🚀 Option 1: Upload to Real PyPI (Recommended)

### Step 1: Create PyPI Account & API Token

1. Go to https://pypi.org/account/register/
2. Verify your email
3. Go to https://pypi.org/manage/account/token/
4. Click "Add API token"
5. Name it: `alm-core-upload`
6. Scope: "Entire account" (first time) or specific project
7. Copy the token (starts with `pypi-`)

### Step 2: Configure Credentials

Create `~/.pypirc` file:
```bash
cat > ~/.pypirc << 'EOF'
[pypi]
username = __token__
password = pypi-YOUR-API-TOKEN-HERE
EOF

chmod 600 ~/.pypirc
```

**OR** use environment variable:
```bash
export TWINE_USERNAME=__token__
export TWINE_PASSWORD=pypi-YOUR-API-TOKEN-HERE
```

### Step 3: Upload to PyPI

```bash
cd /Users/jalendarreddy/Downloads/research/ALM
python -m twine upload dist/*
```

### Step 4: Verify Upload

Visit: https://pypi.org/project/alm-core/

### Step 5: Test Installation

```bash
# In a new terminal or virtual environment
pip install alm-core

# Test import
python -c "from alm_core import AgentLanguageModel; print('✅ Package installed!')"
```

## 🧪 Option 2: Test on TestPyPI First (Safer)

### Step 1: Create TestPyPI Account

1. Go to https://test.pypi.org/account/register/
2. Verify email
3. Generate API token at https://test.pypi.org/manage/account/token/

### Step 2: Upload to TestPyPI

```bash
python -m twine upload --repository testpypi dist/*
```

Or with credentials:
```bash
python -m twine upload \
  --repository-url https://test.pypi.org/legacy/ \
  --username __token__ \
  --password pypi-YOUR-TEST-TOKEN-HERE \
  dist/*
```

### Step 3: Test Install from TestPyPI

```bash
pip install --index-url https://test.pypi.org/simple/ --extra-index-url https://pypi.org/simple/ alm-core
```

### Step 4: If Successful, Upload to Real PyPI

Follow Option 1 above.

## 📝 Quick Command Reference

### Upload to PyPI (Interactive - will ask for credentials)
```bash
python -m twine upload dist/*
```

### Upload to PyPI (with token from environment)
```bash
export TWINE_USERNAME=__token__
export TWINE_PASSWORD=pypi-YOUR-TOKEN-HERE
python -m twine upload dist/*
```

### Upload to TestPyPI
```bash
python -m twine upload --repository testpypi dist/*
```

### Check package before upload
```bash
python -m twine check dist/*
```

### Upload specific version only
```bash
python -m twine upload dist/alm_core-0.1.0*
```

## 🎯 What Happens After Upload

1. **Package Available**: Users can install with `pip install alm-core`
2. **PyPI Page**: https://pypi.org/project/alm-core/
3. **Auto Documentation**: README shown on PyPI page
4. **Search**: Package indexed in PyPI search
5. **Downloads Tracked**: Statistics available on PyPI

## 🔄 Updating Version

To publish a new version:

1. Update version in `setup.py` and `pyproject.toml`:
   ```python
   version="0.1.1"  # or 0.2.0, 1.0.0, etc.
   ```

2. Commit changes:
   ```bash
   git add setup.py pyproject.toml
   git commit -m "Bump version to 0.1.1"
   git tag v0.1.1
   git push origin main --tags
   ```

3. Rebuild and upload:
   ```bash
   rm -rf dist/ build/ *.egg-info
   python -m build
   python -m twine upload dist/*
   ```

## ⚠️ Important Notes

1. **Package Name**: `alm-core` is permanent - cannot be changed after first upload
2. **Version Numbers**: Cannot re-upload same version - must increment
3. **API Token**: Keep it secret! Never commit to Git
4. **License**: MIT license included ✅
5. **Long Description**: Uses README.md ✅

## 🛡️ Security Best Practices

1. **Use API tokens** instead of username/password
2. **Scope tokens** to specific projects when possible
3. **Store in ~/.pypirc** with `chmod 600` permissions
4. **Never commit** tokens to Git
5. **Rotate tokens** periodically
6. **Use TestPyPI** for first-time uploads

## 📊 Package Info

- **Name**: alm-core
- **Version**: 0.1.0
- **Author**: Jalendar Reddy Maligireddy
- **Email**: jalendarreddy97@gmail.com
- **License**: MIT
- **URL**: https://github.com/Jalendar10/alm-core
- **Python**: >=3.8
- **Dependencies**: 4 required, 5 optional

## ✅ Ready to Publish!

Your package is **production-ready** and built successfully. Choose:

- **TestPyPI first** (recommended for first time): Safer, can test
- **PyPI directly**: Package immediately available worldwide

After upload, users can install with:
```bash
pip install alm-core
```

And use in code:
```python
from alm_core import AgentLanguageModel, Constitution, DataAirlock

agent = AgentLanguageModel(model="gpt-4")
result = agent.execute("Write a hello world program")
```

## 🎉 Next Steps

1. Create PyPI account
2. Generate API token
3. Run: `python -m twine upload dist/*`
4. Share your package with the world! 🚀

---

**Need help?** Check PyPI documentation: https://packaging.python.org/tutorials/packaging-projects/
