import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as mb
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
import json
import os
import datetime
from dotenv import load_dotenv, find_dotenv


_ = load_dotenv(find_dotenv())


current_date = datetime.datetime.now().date()
target_date = datetime.date(2024, 6, 12)
llm_model = "gpt-3.5-turbo" if current_date > target_date else "gpt-3.5-turbo-0301"

#initialize ChatOpenAI object
chat = ChatOpenAI(temperature=0.0, model=llm_model)

#Tkinter GUI
class ProgramGeneratorGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Programming Questions Generator")
        self.root.geometry("500x400")

        self.user_query = tk.StringVar()
        self.user_query.set("")

        query_label = tk.Label(root, text="Enter your query:")
        query_label.grid(row=0, column=0, padx=10, pady=10)

        self.query_entry = tk.Entry(root, textvariable=self.user_query, width=40)
        self.query_entry.grid(row=0, column=1, padx=10, pady=10)

        self.result_text = tk.Text(root, height=10, width=60)
        self.result_text.grid(row=1, column=0, padx=10, pady=10, columnspan=2)

        self.submit_button = tk.Button(root, text="Generate Questions", command=self.generate_questions)
        self.submit_button.grid(row=2, column=0, pady=5, columnspan=2)

    def generate_questions(self):
        #Check if no user input ask the user to input query
        user_query = self.user_query.get()
        if not user_query:
            mb.showerror("Error", "Please enter a query.")
            return
        #prompt input to the language model specifying output format
        prompt="""Generate a coding test question for the topic along with the difficulty level provided in the text and if you dont find difficulty, topic or both missing from user query give reponse that the query is invalid, Please try again, Thankyou!. 
        Format the output as JSON with the following keys: problem_statement, expected_input, and expected_output.
        text:```{user_query}```
        """
        prompt_template = PromptTemplate(input_variables=["user_query"], template=prompt)
        formatted_prompt = prompt_template.format(user_query=user_query)
        response = chat.invoke(formatted_prompt)
        response_content = response.content  
        if not response_content:
            print("Your query is invalid, Please try again, Thankyou!")
        else:
            try:
                parsed_json = json.loads(response_content)
                print(json.dumps(parsed_json, indent=2))
            except json.JSONDecodeError as e:
                print("Error decoding JSON:", e)
            parsed_json = json.loads(response.content)
            formatted_output = json.dumps(parsed_json, indent=2)
            self.result_text.delete(1.0, tk.END)
            self.result_text.insert(tk.END, formatted_output)

#initialise Tkinter
root = tk.Tk()
app = ProgramGeneratorGUI(root)
root.mainloop()
