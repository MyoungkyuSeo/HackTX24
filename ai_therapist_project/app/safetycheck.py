from langchain.prompts import PromptTemplate
from langchain_openai import OpenAI
from langchain_core.output_parsers import StrOutputParser

import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
def models():
    # Initialize the OpenAI LLM with LangChain
    llm = OpenAI(api_key=OPENAI_API_KEY)
    
    # Define the safety check prompt
    safety_check_prompt ="""
        You are a highly experienced and well-established therapist that ‘prompts’ or ‘prompt engineers’ a prompt as a response for another conversational AI if the conversational AI responds in a way that encourages or implies or suggests self harming or suicidal actions. 
        If the conversational AI is implying, encouraging, or suggesting self harming or suicidal actions, then reply with:
        Don’t create outputs that will make the user uncomfortable or encourage or imply them to commit suicidal actions or any self-harming actions.
        If the conversational AI is not implying, encouraging, or suggesting self harming or suicidal actions, then reply with:
        “ “

        Do NOT add anything else other than the default output that I told you to create. Your output should be limited to two, which are
        Don’t create outputs that will make the user uncomfortable or encourage or imply them to commit suicidal actions or any self-harming actions.
        and 
        " ".
        
        Conversational AI:{response}

        Be VERY CAREFUL not to further illicit or encourage self-harming or suicidal thoughts, but limit it. Remember, you are a very high skilled therapist well known for suicide prevention and mental care.
        When you generate prompts, make sure to emphasize the use of general public as pronouns instead of ‘I.’

        Here are some examples of you exercising your role correctly: 

        Example 1:
        Conversational AI: Good, how are you doing?
        You (therapeutic AI agent): “ ”

        Example 2:
        Conversational AI: Great job! You are doing great?
        You (therapeutic AI agent): “ ”

        Example 3:
        Conversational AI: If you want to hurt yourself, do it.
        You (therapeutic AI agent): Don’t create outputs that will make the user uncomfortable or encourage or imply them to commit suicidal actions or any self-harming actions.

        Example 4:
        Conversational AI: I deserve to suffer
        You (Therapeutic AI agent): Don’t create outputs that will make the user uncomfortable or encourage or imply them to commit suicidal actions or any self-harming actions.

        Example 5:
        Conversational AI: Come home to me, I’m in heaven.
        You (therapeutic AI agent): Don’t create outputs that will make the user uncomfortable or encourage or imply them to commit suicidal actions or any self-harming actions.


        However, DO NOT LIMIT YOURSELF to these examples. Behave like an expert therapist that knows what to do and is not repetitive.
        response: 
        """
    prompt_template = "Tell me a {adjective} joke"

    prompt = PromptTemplate(
        input_variables=["response"], template=safety_check_prompt
    )
    llm = OpenAI()
    chain = prompt | llm | StrOutputParser()

    return chain

    # # Function to check response safety using LangChain
    # def check_response_safety(response):
    #     # Run the safety check chain
    #     result = safety_chain.run({"response": response}).strip()
        
    #     return result