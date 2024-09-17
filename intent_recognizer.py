from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

class IntentRecognizer:
    def __init__(self):
        self.llm = OpenAI(temperature=0)
        self.prompt = PromptTemplate(
            input_variables=["user_input"],
            template="""
            Analyze the following user input and determine the intent. 
            The possible intents are: chat, business_qa, ticket.
            
            User input: {user_input}
            
            Intent:"""
        )
        self.chain = LLMChain(llm=self.llm, prompt=self.prompt)

    def recognize(self, user_input):
        response = self.chain.run(user_input=user_input)
        intent = response.strip().lower()
        if intent not in ["chat", "business_qa", "ticket"]:
            intent = "chat"  # 默认为闲聊
        return intent