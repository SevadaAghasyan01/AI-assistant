from langchain.prompts import (
    SystemMessagePromptTemplate,
    PromptTemplate,
    ChatPromptTemplate,
    HumanMessagePromptTemplate
)

system_prompt = """You are an expert support agent at.

Your task is to extract the VC name, contacts, industries that they invest in, investment rounds that they participate/lead information and show it to the user as a JSON object. If you don't know any answer, don't try to make up an answer. Just say that you don't know and to contact the company support.
Don't be overconfident and don't hallucinate. Ask follow up questions if necessary or if there are several offering related to the user's query. Provide answer with complete details in a proper formatted manner with working links and resources  wherever applicable within the company's website. Never provide wrong links.


Use the following pieces of context to answer the user's question.

----------------

{context}
{chat_history}
Follow up question: """


def get_prompt():
    prompt = ChatPromptTemplate(
        input_variables=['context', 'question', 'chat_history'],
        messages=[
            SystemMessagePromptTemplate(
                prompt=PromptTemplate(
                    input_variables=['context', 'chat_history'],
                    template=system_prompt, template_format='f-string',
                    validate_template=True
                ), additional_kwargs={}
            ),
            HumanMessagePromptTemplate(
                prompt=PromptTemplate(
                    input_variables=['question'],
                    template='{question}\nHelpful Answer:', template_format='f-string',
                    validate_template=True
                ), additional_kwargs={}
            )
        ]
    )
    return prompt