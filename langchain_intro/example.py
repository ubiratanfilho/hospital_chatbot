from chatbot import review_chain

question = """Has anyone complained about
           communication with the hospital staff?"""
print(review_chain.invoke(question))