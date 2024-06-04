# test_generation.py
import pytest
from monsterapi.nextGenLLMClient import LLMClient, GenerateRequest


client = LLMClient()

@pytest.mark.parametrize("model,expected_behavior", [
    ("microsoft/phi-2", {
        "formatted_prompt": "Instruction: Provide a mayonnaise recipe.\nOutput:",
        "max_tokens": 128,
        "use_messages": False
    }),
    ("TinyLlama/TinyLlama-1.1B-Chat-v1.0", {
        "formatted_prompt": None,
        "max_tokens": 128,
        "use_messages": True
    }),
    ("mistralai/Mistral-7B-Instruct-v0.2", {
        "formatted_prompt": None,
        "max_tokens": 128,
        "use_messages": True
    }),
    ("HuggingFaceH4/zephyr-7b-beta", {
        "formatted_prompt": None,
        "max_tokens": 128,
        "use_messages": True
    })
    # Add more models and their expected behaviors as needed
])
def test_create_and_send_request(model, expected_behavior):
    request = create_request(model)
    response = client.generate(request)  # Send the request using the LLMClient

    assert response is not None, "Expected a response from the API, got None"

    # Additional assertions can be made here based on the expected structure of the response
    # For example, you might want to check the type of response, the presence of certain fields, etc.

def create_request(model: str) -> GenerateRequest:
    if model == "microsoft/phi-2":
        return GenerateRequest(
            model=model,
            formatted_prompt="Instruction: Provide a mayonnaise recipe.\nOutput:",
            max_tokens=128,
            n=1,
            best_of=2,
            temperature=1,
        )
    else:
        return GenerateRequest(
            model=model,
            messages=[
                {"role": "user", "content": "What is your favourite condiment?"},
                {"role": "assistant", "content": "Well, I'm quite partial to a good squeeze of fresh lemon juice. It adds just the right amount of zesty flavour to whatever I'm cooking up in the kitchen!"},
                {"role": "user", "content": "Do you have mayonnaise recipes?"}
            ],
            max_tokens=128,
            n=1,
            temperature=1,
        )
