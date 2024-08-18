!pip install google-generativeai
import google.generativeai as palm
import os

palm.configure(api_key='"YOUR API KEY"')  # Replace 'YOUR_API_KEY' with your actual API key

# Now try listing the models again
models = [m for m in palm.list_models() if 'generateText' in m.supported_generation_methods]
model = models[0].name
print(model)
# Set your input text
prompt = "tell about  ms dhoni ?"
# prompt = "What is Quantum Computing? Explain like I'm 5."

completion = palm.generate_text(
    model=model,
    prompt=prompt,
    temperature=0,
    # temperature=0 >> more deterministic results // temperature=1 >> more randomness
    max_output_tokens=100
    # maximum length of response
)

print(completion.result)
