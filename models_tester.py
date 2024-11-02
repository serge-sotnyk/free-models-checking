import os

from dotenv import load_dotenv
from langchain.prompts import PromptTemplate
from langchain_core.tools import StructuredTool

# Load environment variables from .env file
load_dotenv()

# Define model configurations
MODEL_CONFIGS = {
    "groq": {
        "model_ids": [
            "llama-3.1-70b-versatile",
            # "mixtral-8x7b-32768"
        ],
        "api_key_env": "GROQ_API_KEY"
    },
    "sambanova": {
        "model_ids": [
            "Meta-Llama-3.1-70B-Instruct",
            "Meta-Llama-3.1-405B-Instruct"
        ],
        "api_key_env": "SAMBANOVA_API_KEY"
    },
    "cerebras": {
        "model_ids": [
            "llama3.1-70b",
            "llama3.1-8b",
        ],
        "api_key_env": "CEREBRAS_API_KEY"
    },
    "openrouter": {
        "model_ids": [
            "microsoft/phi-3-medium-128k-instruct:free",
            "google/gemini-pro-1.5-exp",
            "google/gemini-flash-1.5-exp",
            "meta-llama/llama-3.1-405b-instruct:free"
            "nousresearch/hermes-3-llama-3.1-405b:free"
        ],
        "api_key_env": "OPENROUTER_API_KEY"
    },
    "google": {
        "model_ids": [
            "gemini-1.5-pro-exp-0827",
            "gemini-1.5-flash-exp-0827",
        ],
        "api_key_env": "GEMINI_API_KEY"
    },
    "github": {
        "model_ids": [
            "gpt-4o",
            "gpt-4o-mini",
            "Meta-Llama-3.1-405B-Instruct",
        ],
        "api_key_env": "GITHUB_API_KEY"
    }
}


def multiply(a: int, b: int) -> int:
    """Multiply two numbers."""
    return a * b


async def amultiply(a: int, b: int) -> int:
    """Multiply two numbers."""
    return a * b


calculator = StructuredTool.from_function(func=multiply, coroutine=amultiply)


def load_text_for_summarization() -> str:
    """Load text from file for summarization test"""
    with open("text_4_summarizing.txt", "r", encoding="utf-8") as file:
        return file.read()


def create_model_instance(provider: str, model_id: str):
    """Create model instance based on provider and specific model_id"""
    config = MODEL_CONFIGS[provider]
    api_key = os.getenv(config["api_key_env"])

    if not api_key:
        raise ValueError(f"API key not found for {provider}")

    if provider == "groq":
        from langchain_groq import ChatGroq
        return ChatGroq(model=model_id)
    elif provider == "sambanova":
        from langchain_community.chat_models import ChatSambaNovaCloud
        return ChatSambaNovaCloud(model=model_id)
    elif provider == "cerebras":
        from langchain_openai import ChatOpenAI
        return ChatOpenAI(model=model_id,
                          api_key=os.getenv(config["api_key_env"]),
                          base_url="https://api.cerebras.ai/v1")
    elif provider == "openrouter":
        from langchain_openai import ChatOpenAI
        return ChatOpenAI(model=model_id,
                          api_key=os.getenv(config["api_key_env"]),
                          base_url="https://openrouter.ai/api/v1")
    elif provider == "google":
        from langchain_google_genai import ChatGoogleGenerativeAI
        return ChatGoogleGenerativeAI(model=model_id,
                                      api_key=os.getenv(config["api_key_env"]))
    elif provider == "github":
        from langchain_openai import ChatOpenAI
        return ChatOpenAI(model=model_id,
                          api_key=os.getenv(config["api_key_env"]),
                          base_url="https://models.inference.ai.azure.com")
    raise ValueError(f"Unknown provider: {provider}")


def test_summarization(model, text: str) -> dict:
    """Test model's summarization capabilities"""
    template = """Please summarize the following text in 3-5 sentences:
    
    {text}
    
    Summary:"""

    prompt = PromptTemplate(template=template, input_variables=["text"])

    try:
        response = model.invoke(prompt.format(text=text))
        return {
            "success": True,
            "summary": response.content
        }
    except Exception as e:
        return {
            "success": False,
            "error": str(e)
        }


def test_tool_usage(model) -> dict:
    """Test model's ability to use tools"""
    tools = [calculator]

    # Create a proper prompt template
    prompt = PromptTemplate(
        input_variables=["input"],
        template="""Solve this mathematical expression: {input}
        Show your work and use the calculator tool to compute the result.
        
        """
    )  # 123456789 * 987654321

    try:
        model_with_tools = model.bind_tools(tools)
        response = model_with_tools.invoke(prompt.format(input="123456789 * 987654321"))
        return {
            "success": True,
            "result": str(response),
        }
    except Exception as e:
        return {
            "success": False,
            "error": str(e)
        }


def test_single_model(provider: str, model_id: str, text: str) -> dict:
    """Run all tests for a single model and return results"""
    try:
        model = create_model_instance(provider, model_id)
        return {
            "summarization": test_summarization(model, text),
            "tool_usage": test_tool_usage(model),
            "success": True
        }
    except Exception as e:
        return {
            "error": str(e),
            "success": False
        }


def print_model_results(model_id: str, result: dict):
    """Print results for a single model"""
    print(f"\nModel: {model_id}")
    if not result.get("success"):
        print(f"Error: {result['error']}")
        return

    print("\nSummarization test:")
    if result["summarization"]["success"]:
        print(f"Summary: {result['summarization']['summary']}")
    else:
        print(f"Failed: {result['summarization']['error']}")

    print("\nTool usage test:")
    if result["tool_usage"]["success"]:
        print(f"Result: {result['tool_usage']['result']}")
    else:
        print(f"Failed: {result['tool_usage']['error']}")


def main():
    """Main testing function"""
    results = {}
    text = load_text_for_summarization()

    for provider, config in MODEL_CONFIGS.items():
        print(f"\nTesting {provider}...")
        results[provider] = {}
        
        for model_id in config["model_ids"]:
            print(f"\nTesting model: {model_id}")
            results[provider][model_id] = test_single_model(provider, model_id, text)

    # Print results
    for provider, provider_results in results.items():
        print(f"\n=== Results for {provider} ===")
        for model_id, result in provider_results.items():
            print_model_results(model_id, result)


if __name__ == "__main__":
    main()
