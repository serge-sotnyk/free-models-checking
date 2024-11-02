import litellm
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()
# litellm.set_verbose = True

MODELS_TO_TEST = [
    # github
    "github/gpt-4o",
    "github/gpt-4o-mini",
    "github/Meta-Llama-3.1-405B-Instruct",
    # groq
    "groq/llama-3.1-70b-versatile",
    "groq/mixtral-8x7b-32768",
    # sambanova
    "sambanova/Meta-Llama-3.1-70B-Instruct",
    "sambanova/Meta-Llama-3.1-405B-Instruct",
    # cerebras
    "cerebras/llama3.1-70b",
    "cerebras/llama3.1-8b",
    # openrouter
    "openrouter/microsoft/phi-3-medium-128k-instruct:free",
    "openrouter/google/gemini-pro-1.5-exp",
    "openrouter/google/gemini-flash-1.5-exp",
    "openrouter/meta-llama/llama-3.1-405b-instruct:free",
    "openrouter/nousresearch/hermes-3-llama-3.1-405b:free"
    # google
    "gemini/gemini-1.5-pro-exp-0827",
    "gemini/gemini-1.5-flash-exp-0827",
]


# This function is not really used, but we use such definition to check if it called by the model
def multiply(a: int, b: int) -> int:
    """Multiply two numbers."""
    return a * b


def load_text_for_summarization() -> str:
    """Load text from file for summarization test"""
    with open("text_4_summarizing.txt", "r", encoding="utf-8") as file:
        return file.read()


def test_summarization(model_name: str, text: str) -> dict:
    """Test model's summarization capabilities"""
    try:
        messages = [
            {
                "role": "user",
                "content": f"Please summarize the following text in 3-5 sentences:"
                           f"\n\n{text}\n\n"
                           f"Summary:"
            }
        ]

        response = litellm.completion(
            model=model_name,
            messages=messages,
        )

        return {
            "success": True,
            "summary": response.choices[0].message.content
        }
    except Exception as e:
        return {
            "success": False,
            "error": str(e)
        }


def test_tool_usage(model_name: str) -> dict:
    """Test model's ability to use tools"""
    try:
        messages = [
            {
                "role": "user",
                "content": "Solve this mathematical expression: 1234568789 * 9878654321\n"
                           "Show your work and use the `multiply` tool to compute the result."
            }
        ]

        tools = [
            {
                "type": "function",
                "function": {
                    "name": "multiply",
                    "description": "Multiply two numbers",
                    "parameters": {
                        "type": "object",
                        "properties": {
                            "a": {"type": "integer"},
                            "b": {"type": "integer"}
                        },
                        "required": ["a", "b"]
                    }
                }
            }
        ]

        response = litellm.completion(
            model=model_name,
            messages=messages,
            tools=tools,
        )

        return {
            "success": True,
            "result": str(response)
        }
    except Exception as e:
        return {
            "success": False,
            "error": str(e)
        }


def test_single_model(model_id: str, text: str) -> dict:
    """Run all tests for a single model and return results"""
    try:
        return {
            "model_id": model_id,
            "summarization": test_summarization(model_id, text),
            "tool_usage": test_tool_usage(model_id),
            "success": True,
        }
    except Exception as e:
        return {
            "error": str(e),
            "success": False
        }


def print_model_results(result: dict):
    """Print results for a single model"""
    print(f"\nModel: {result['model_id']}")
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
    results = []
    text = load_text_for_summarization()

    for model_id in MODELS_TO_TEST:
        print(f"\nTesting {model_id}...")

        results.append(test_single_model(model_id, text))

    # Print results
    for res in results:
        print(f"\n=== Results for {res['model_id']} ===")
        print_model_results(res)


if __name__ == "__main__":
    main()
