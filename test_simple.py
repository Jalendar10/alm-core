"""
Simple test to verify ALM Core works locally
"""

import os
from alm_core import AgentLanguageModel

def test_basic():
    """Test basic initialization with different models."""
    
    print("\n" + "="*60)
    print("Testing ALM Core - Flexible Model Configuration")
    print("="*60 + "\n")
    
    # Test 1: Default configuration (reads from environment)
    print("Test 1: Using environment variables...")
    print(f"  OPENAI_API_KEY: {'Set' if os.environ.get('OPENAI_API_KEY') else 'Not set'}")
    print(f"  OPENAI_MODEL: {os.environ.get('OPENAI_MODEL', 'Not set (will use gpt-4)')}")
    
    if os.environ.get('OPENAI_API_KEY'):
        agent1 = AgentLanguageModel()  # Uses env vars
        print(f"✓ Agent created with model: {agent1.llm.model}")
    else:
        print("⚠ Skipping (no API key in environment)")
    
    # Test 2: Explicit model configuration
    print("\nTest 2: Explicit model configuration...")
    agent2 = AgentLanguageModel(
        api_key="dummy-key",
        llm_provider="local",
        model="gpt-3.5-turbo"
    )
    print(f"✓ Agent created with model: {agent2.llm.model}")
    
    # Test 3: Different models
    print("\nTest 3: Testing different model options...")
    models = ["gpt-4", "gpt-3.5-turbo", "gpt-4-turbo-preview"]
    
    for model in models:
        agent = AgentLanguageModel(
            api_key="dummy-key",
            llm_provider="local",
            model=model
        )
        print(f"✓ Model '{model}' configured successfully")
    
    # Test 4: Anthropic
    print("\nTest 4: Anthropic Claude models...")
    claude_models = ["claude-3-opus-20240229", "claude-3-sonnet-20240229"]
    
    try:
        for model in claude_models:
            agent = AgentLanguageModel(
                api_key="dummy-key",
                llm_provider="anthropic",
                model=model
            )
            print(f"✓ Model '{model}' configured successfully")
    except ImportError as e:
        print(f"⚠ Anthropic not installed (optional): {e}")
        print("  Install with: pip install anthropic")
    
    print("\n" + "="*60)
    print("All tests passed! ✓")
    print("="*60 + "\n")
    
    print("Usage Examples:")
    print("-" * 60)
    print("\n1. Using environment variables:")
    print("   export OPENAI_API_KEY='sk-...'")
    print("   export OPENAI_MODEL='gpt-3.5-turbo'")
    print("   agent = AgentLanguageModel()")
    
    print("\n2. Explicit configuration:")
    print("   agent = AgentLanguageModel(")
    print("       api_key='sk-...',")
    print("       model='gpt-4'")
    print("   )")
    
    print("\n3. Different providers:")
    print("   # OpenAI GPT-4")
    print("   agent = AgentLanguageModel(model='gpt-4')")
    print()
    print("   # OpenAI GPT-3.5")
    print("   agent = AgentLanguageModel(model='gpt-3.5-turbo')")
    print()
    print("   # Anthropic Claude")
    print("   agent = AgentLanguageModel(")
    print("       llm_provider='anthropic',")
    print("       model='claude-3-opus-20240229'")
    print("   )")
    print()


if __name__ == "__main__":
    test_basic()
