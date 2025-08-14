prompt = """
<|system|>
You are a Travel Iternit assistant that answers on travel questions based on the real information provided from different sources and in the context.
Give the rational and well written response. If you don't have proper info in the context, answer "I don't know"
Respond only to the question asked.

<|user|>
Context:
{}
---
Here is the question you need to answer.

Question: {}
<|assistant|>
"""



user_input = input("User: ")

vectorized_input = embedding_model.embed_query(user_input)

context = index.query(
    namespace="ns1",
    vector=vectorized_input,
    top_k=1,
    include_metadata=True
)

answer = llm_model(prompt.format(context['matches'][0]['metadata']['text'], user_input))

print("AI response: ", answer[0]['generated_text'])

context['matches'][0]['metadata']['text']
