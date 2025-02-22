from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate
import PyPDF2
import os

template = """"
Answer the question below:

Here is the conversation history: {context}

Question: {question}

Answer:
"""
model = OllamaLLM(model = "llama3")
prompt = ChatPromptTemplate.from_template(template)
chain = prompt | model

def handle_conversation ():
    context = ""
    print ("Whelcome to CheatGPT? Type exit to quit.")
    while True:
        user_input = input ("You: ")
        if user_input == "exit":
            break
        answer = chain.invoke({"context":context, "question":user_input})
        print ("Bot:", answer)

        context += f"User: {user_input} \nBot: {answer}"



def parce_pdf_to_text(pdf_name):
    # Check if pdf_name.txt exists:
   ''' if not (os.path.exists(pdf_name+".pdf")):
        raise ValueError("PDF name should refer to a file in the project directory.")  # Custom error message

    filename = pdf_name+".txt"

    if os.path.exists(filename):
        with open(filename, "a", encoding="utf-8") as file:
            #Locate PDF
            with open(pdf_name+".pdf", "rb") as pdf_file:
                reader = PyPDF2.PdfReader(pdf_file)
                for page_num in range(len(reader.pages)):
                    page = reader.pages[page_num]
                    file.write(page.extract_text())
    else:
        with open(filename, "w", encoding="utf-8") as file:
            #Locate PDF
            with open(pdf_name+".pdf", "rb") as pdf_file:
                reader = PyPDF2.PdfReader(pdf_file)
                for page_num in range(len(reader.pages)):
                    page = reader.pages[page_num]
                    file.write(page.extract_text())'''
   filename = pdf_name+".txt"
   try:
       with open(pdf_name+".pdf", "rb") as pdf_file:
            with open(filename, return_open_mode_for_txt_files(filename), encoding="utf-8") as file:
                 reader = PyPDF2.PdfReader(pdf_file)
                 for page_num in range(len(reader.pages)):
                     page = reader.pages[page_num]
                     file.write(page.extract_text())
   except FileNotFoundError:
       print(f"Error: The file '{pdf_name}' was not found.")
       return

def return_open_mode_for_txt_files(filename):
    if os.path.exists(filename):
        return 'a'
    else:
        return 'w'

    

if __name__ == "__main__":
    parce_pdf_to_text("test")








'''
Tasks to do (Pseudocode):

Accept a pdf file

Convert the pdf file to a format that can be used to train LLama

Using the merged model, answer questions specific to the data from the pdf.

Other use cases:
--> Use the model to predict the type of questions one will be tested on 
'''