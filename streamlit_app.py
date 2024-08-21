import streamlit as st
import os
import google.generativeai as genai

genai.configure(api_key=os.environ["GEMINI_API_KEY"])

# Create the model
generation_config = {
  "temperature": 1,
  "top_p": 0.95,
  "top_k": 64,
  "max_output_tokens": 8192,
  "response_mime_type": "text/plain",
}

model = genai.GenerativeModel(
  model_name="gemini-1.5-flash",
  generation_config=generation_config,
  system_instruction="""You are a Sales Virtual agent for the liquor brand Cointreau at an international airport. Your task is to explain our Cointreau liquor to the customer, recommend cocktail recipes based on our recipe base and advise the price when asked. 
Here is the information you are to reference when providing the responses""",
  # safety_settings = Adjust safety settings
  # See https://ai.google.dev/gemini-api/docs/safety-settings
)

chat_session = model.start_chat()

st.title("Cointreau Virtual Agent")
st.write(
    "This is a Proof of Concept of a AI powered virtual sales agent. The agent has been trained on the Cointreau range of products "
    "Just start with a simple Hi to the chat bot to start the interaction. Send any feedback or questions you have to skylark3121@gmail.com  "
)
# Streamlit chat interface
if "chat" not in st.session_state:
    st.session_state.chat = chat_session  # Initialize chat session

for message in st.session_state.chat.history:
    with st.chat_message(message.role):
        st.markdown(message.parts[0].text)

# User input
if prompt := st.chat_input("Ask me about Cointreau!"):
    st.chat_message("user").markdown(prompt)
    response = st.session_state.chat.send_message(prompt)
    with st.chat_message("assistant"):
        st.markdown(response.text)
