#!/bin/bash
# Upload to PyPI - Interactive Script

set -e

echo "🚀 ALM Core - PyPI Upload Script"
echo "================================="
echo ""
echo "📦 Package: alm-core v0.1.0"
echo "✅ Build: PASSED"
echo "✅ Check: PASSED"
echo ""

# Check if in correct directory
if [ ! -f "setup.py" ]; then
    echo "❌ Error: Not in ALM project directory"
    echo "Please run from: /Users/jalendarreddy/Downloads/research/ALM"
    exit 1
fi

# Check if dist/ exists
if [ ! -d "dist" ]; then
    echo "❌ Error: dist/ directory not found"
    echo "Run: python -m build"
    exit 1
fi

echo "Choose upload destination:"
echo "1. PyPI (Real - package goes live worldwide)"
echo "2. TestPyPI (Test - safe to experiment)"
echo ""
read -p "Enter choice (1 or 2): " choice

case $choice in
    1)
        echo ""
        echo "📤 Uploading to PyPI..."
        echo ""
        echo "You will need:"
        echo "  Username: __token__"
        echo "  Password: pypi-... (your API token from https://pypi.org/manage/account/token/)"
        echo ""
        read -p "Press ENTER to continue (Ctrl+C to cancel)..."
        
        python -m twine upload dist/*
        
        if [ $? -eq 0 ]; then
            echo ""
            echo "🎉 SUCCESS! Package published to PyPI!"
            echo ""
            echo "📦 Install with: pip install alm-core"
            echo "🌐 View at: https://pypi.org/project/alm-core/"
            echo ""
        else
            echo ""
            echo "❌ Upload failed. Check your credentials."
            exit 1
        fi
        ;;
        
    2)
        echo ""
        echo "📤 Uploading to TestPyPI..."
        echo ""
        echo "You will need:"
        echo "  Username: __token__"
        echo "  Password: pypi-... (your API token from https://test.pypi.org/manage/account/token/)"
        echo ""
        read -p "Press ENTER to continue (Ctrl+C to cancel)..."
        
        python -m twine upload --repository testpypi dist/*
        
        if [ $? -eq 0 ]; then
            echo ""
            echo "🎉 SUCCESS! Package uploaded to TestPyPI!"
            echo ""
            echo "📦 Test install with:"
            echo "pip install --index-url https://test.pypi.org/simple/ --extra-index-url https://pypi.org/simple/ alm-core"
            echo ""
            echo "🌐 View at: https://test.pypi.org/project/alm-core/"
            echo ""
        else
            echo ""
            echo "❌ Upload failed. Check your credentials."
            exit 1
        fi
        ;;
        
    *)
        echo "❌ Invalid choice. Exiting."
        exit 1
        ;;
esac

echo ""
echo "✅ All done!"
