from aisetup import authenticate, print_llm_response, get_llm_response

authenticate("eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJhcHAiLCJleHAiOjE3OTk5OTk5OTksInN1YiI6MjM1NDU2NSwiYXVkIjoiV0VCIiwiaWF0IjoxNjk0MDc2ODUxfQ.NDfHow_EkW1APQDt6D-vWjn9EByjHbTj8YJhlWUr-oE")

# Print the LLM response
print_llm_response("What is the capital of France")

# Store the LLM response as a variable and then print
response = get_llm_response("What is the capital of France")
print(response)