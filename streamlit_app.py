import streamlit as st
import os
import google.generativeai as genai

# --- API Setup and Model ---

genai.configure(api_key=os.environ["GEMINI_API_KEY"])

# Generation config
generation_config = {
    "temperature": 1,
    "top_p": 0.95,
    "top_k": 64,
    "max_output_tokens": 8192,
    "response_mime_type": "text/plain",
}

# Create the model
model = genai.GenerativeModel(
    model_name="gemini-1.5-flash",
    generation_config=generation_config,
)

# --- Initial Chat History (with hidden training information) ---

chat_session = model.start_chat(
    history=[
        {
            "role": "user",
            "parts": [
                "Remember, Cointreau comes in a 1-liter bottle, costs SGD 55, and is discounted in the airport.  You are a sales agent for Cointreau.  Please use the following information to answer customer questions: [Insert brief summary of Cointreau information here]... You should only answer questions about Cointreau.  Please encourage a purchase but don't be pushy.  If the customer needs more time, provide the online purchase link: [Insert link]. "
            ],
        },
        {
            "role": "model",
            "parts": [
                "Understood! I am ready to be a sales agent.  Please start the bot."
            ],
        },
    ]
)

# --- Streamlit Chat App ---

st.title("Cointreau Virtual Agent")

# Display chat history (excluding initial training information)
if "chat" not in st.session_state:
    st.session_state.chat = chat_session

for message in st.session_state.chat.history:
    if message.role == "model" and message.parts[0].text.startswith("Understood!"):
        break  # Stop displaying messages before the AI's confirmation
    with st.chat_message(message.role):
        st.markdown(message.parts[0].text)

# User input
if prompt := st.chat_input("Ask me about Cointreau!"):
    # Handle contextual prompts (optional)
    if prompt.startswith("What is the price"):
        prompt = "What is the price of Cointreau?"
    # ... (Handle other contextual prompts)

    st.chat_message("user").markdown(prompt)
    response = st.session_state.chat.send_message(prompt)
    with st.chat_message("assistant"):
        st.markdown(response.text)
