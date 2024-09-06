from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate


model = OllamaLLM(model="llama3.1")
template = (
    "You are tasked with extracting specific information from the following text content: {dom_content}. "
    "Please follow these instructions carefully: \n\n"
    "1. **Extract Information:** Only extract the information that directly matches the provided description: {parse_description}. "
    "2. **No Extra Content:** Do not include any additional text, comments, or explanations in your response. "
    "3. **Empty Response:** If no information matches the description, return an empty string ('')."
    "4. **Direct Data Only:** Your output should contain only the data that is explicitly requested, with no other text."
)
def parse_using_llms(dom_batches: list,desc: str) -> str:
    """
    :param dom_batches: list-> list of batches of the DOM content
    :param desc: str description of the information that needs to be extracted
    :return: str extracted information
    """
    prompt = ChatPromptTemplate.from_template(template)
    chain = prompt | model
    parsed_text = []
    for i, batch in enumerate(dom_batches):
        response = chain.invoke({"dom_content": batch,"parse_description":desc})
        print(f"Batch {i+1} of {len(dom_batches)}: \n{response}")
        parsed_text.append(response)
    return "\n".join(parsed_text)