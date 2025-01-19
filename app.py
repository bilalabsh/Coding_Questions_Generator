import os
import openai
from langchain_core.prompts import PromptTemplate
import json
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv, find_dotenv
import datetime

# langchain_implement.debug = False
# langchain_implement.verbose = False


def handle_userquestions(user_question):
    user_query=user_question
    
    return user_query
    
# user_query="generate coding test for topic strings with hard difficulty"    

def conversational_model(llm_model,user_question):
    chat=ChatOpenAI(temperature=0.0,model=llm_model)
    user_query=handle_userquestions(user_question)
    prompt="""Generate a coding test question for the topic along with the difficulty level provided in the text and if you dont find difficulty, topic or both missing from user query give reponse that the query is invalid, Please try again, Thankyou!. 
    Format the output as JSON with the following keys: problem_statement, expected_input, and expected_output.
    text:```{user_query}```
    """
    

    prompt_template = PromptTemplate(input_variables=["user_query"], template=prompt)

    #Format the prompt with the user query
    formatted_prompt = prompt_template.format(user_query=user_query)

    #Fetch response from the llm
    response = chat.invoke(formatted_prompt)

    #print
    # print(response)
    # print(response.content)
    response_content = response.content 
    if not response_content:
        print("Your query is invalid, Please try again, Thankyou!")
    else:
        try:
            parsed_json = json.loads(response_content)
            print(json.dumps(parsed_json, indent=2))
        except json.JSONDecodeError as e:
            print("Error decoding JSON:", e)

def main():
    _ = load_dotenv(find_dotenv()) # read local .env file
    openai.api_key = os.environ['OPENAI_API_KEY']
    
    #use undepreciated model
    current_date = datetime.datetime.now().date()
    target_date = datetime.date(2024, 6, 12)

    if current_date > target_date:
        llm_model = "gpt-3.5-turbo" ##Standard
    else:
        llm_model = "gpt-3.5-turbo-0301"


    user_question=input("Enter Question for topic along with difficulty level: ")
    
    conversational_model(llm_model,user_question)
    
if __name__ == "__main__":
    main()