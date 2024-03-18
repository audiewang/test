import PyPDF2
import openai

# Read the PDF file and extract its text content
pdf_path = "CAT_2024.pdf"
with open(pdf_path, 'rb') as file:
    pdf_reader = PyPDF2.PdfFileReader(file)
    text_content = ""
    for page_num in range(pdf_reader.numPages):
        page = pdf_reader.getPage(page_num)
        text_content += page.extractText()

# Set up OpenAI API credentials
openai.api_key = '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'

# Define the prompt for GPT
prompt = f"Document: {text_content}\n\nQuestion:"

# Generate responses from GPT
while True:
    user_input = input("Ask a question (or type 'exit' to quit): ")
    if user_input.lower() == 'exit':
        break

    # Append the user's question to the prompt
    prompt += f"\n{user_input}"

    # Generate a response from GPT
    response = openai.Completion.create(
        engine='text-davinci-003',
        prompt=prompt,
        max_tokens=100,
        temperature=0.7,
        n=1,
        stop=None
    )

    # Extract the answer from the GPT response
    answer = response.choices[0].text.strip()

    # Print the answer
    print(f"Answer: {answer}")