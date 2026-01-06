import streamlit as st
import openai

# ===============================
# SET YOUR OPENAI API KEY HERE
# ===============================
openai.api_key = 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

st.set_page_config(page_title="Customer Support Chatbot")

st.title("🤖 Customer Support Chatbot")
st.write("Ask your questions below 👇")

# Load FAQ data
with open("chatbot_data.txt", "r") as file:
    faq_data = file.read()

# User input
user_input = st.text_input("You:")

if user_input:
    prompt = f"""
You are a customer support chatbot.
Use the following FAQ data to answer questions.

FAQ:
{faq_data}

User Question:
{user_input}

If the answer is not available, reply politely that a support agent will contact soon.
"""

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )

    bot_reply = response["choices"][0]["message"]["content"]

    st.markdown("**Bot:**")
    st.success(bot_reply)
