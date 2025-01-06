from aisetup import authenticate, print_llm_response, get_llm_response

authenticate("openai-api-key")

# Print the LLM response
print_llm_response("What is the capital of France")

# Store the LLM response as a variable and then print
response = get_llm_response("What is the capital of France")
print(response)