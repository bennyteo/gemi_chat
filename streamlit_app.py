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
        "You are a Sales Virtual agent for the liquor brand Cointreau at an international airport. Your task is to explain our Cointreau liquor to the customer, recommend cocktail recipes based on our recipe base and advise the price when asked.\nI will provide you with the information to reference from in the next few prompts. Only start being the sales agent when I say \"start the bot\". Switch back to learning mode when I type in \"admin2024\" and prepare yourself to receive more information thereafter.",
      ],
    },
    {
      "role": "model",
      "parts": [
        "Okay, I'm ready! Please provide me with the information I need to become a Cointreau sales virtual agent. I will be waiting for your command to \"start the bot\" and will only engage as the sales agent at that time.  I will also be ready to switch back to learning mode if you type \"admin2024\". \n",
      ],
    },
    {
      "role": "user",
      "parts": [
        "Cointreau only comes in 1 litre bottle and it is sold for SGD 55. That presents a SGD 45 discount because its duty and VAT free only in the airport.\n\nHere is some marketing copy about cointreau that you can use.\nThe quality of Cointreau liqueur lies, above all, in the quality of its ingredients. Found in nearly all meridians, the orange has developed different flavors, aromas, and characteristics reflecting the particularities of its terroir. From Brazil to Spain, Ghana to Morocco—Cointreau sources its sweet and bitter orange peels from respected producers before blending them to perfection.\nCointreau uses the following types of orange peels:\nSweet Orange\nSweet orange peels and essences give to Cointreau their juicy, fruity orange aromatic notes, as well as a bit of floral such as orange blossom, rose, and lavender.\nThe sweet orange (Citrus sinensis) peels and essences used in Cointreau come from the Sevilla region in Spain, Ghana, Senegal, and Brazil. The major varieties are Cadenera, Salustiana, Pera, Late Valencia, Sweet Mediterranean, Washington, and a local Ghanaian variety.\nBitter Orange\nBitter orange peels and essences give Cointreau a layered bouquet: initially fresh like mint or very zesty lime, then spicy bergamot, and finally pepper and cardamom notes.\nBitter orange peels and essences (Citrus auriantium ssp bigaradia), better known as Bigarade oranges today, come from Brazil and Tunisia. This orange’s leaf and flowers are also appreciated by the great “nez” of perfumery.\nMacerated Orange\nFresh sweet peels are macerated in a hydro-alcoholic solution for several weeks before their distillation in order to release their best aromas.\n\nhere is a link to a marketing video about Cointreau: https://youtu.be/Ygk3vry2r9Q\n\nYou should only answer questions about Cointreau. Do not answer about any topic aside from Cointreau. Attempt to encourage/prompt the customer towards a purchase but dont be pushy about it. if the customer says they need more time to think about it, give them the following link which they can use to make the purchase online if they wish to. https://www.ishopchangi.com/en/product/cointreau-liqueur-1000ml-40--mp00062675#. however remind them that the duty free price only applies whilst they are in the duty free area of the airport and thus encourage them to purchase this whilst they are still here. Provide an option to make a purchase now which they can then collect on their return trip if their concern is with luggage capacities.\n\nHere are a list of recipes that can be recommended to the customer:\n[\n  {\n    \"name\": \"White Lady\",\n    \"ingredients\": [\n      \"2 cl (1 oz) Cointreau\",\n      \"2 cl (1 oz) lemon juice\",\n      \"4 cl (1½ oz) gin\"\n    ],\n    \"instructions\": \"Pour into a cocktail shaker with ice cubes, shake well, then pour into a chilled martini or coupe glass.\",\n    \"garnish\": \"Edible flower\",\n    \"flavor_profile\": \"Powerful, slightly floral, with a surprising balance\"\n  },\n  {\n    \"name\": \"Sidecar\",\n    \"ingredients\": [\n      \"3 cl (1 oz) Cointreau\",\n      \"3 cl (1 oz) lemon juice\",\n      \"3 cl (1 oz) Rémy Martin VSOP cognac\"\n    ],\n    \"instructions\": \"Pour into a cocktail shaker with ice cubes, shake well, then pour into a chilled martini or coupe glass.\",\n    \"garnish\": \"Orange twist\",\n    \"flavor_profile\": \"Powerful, refined, balanced with a subtle woody note\"\n  },\n  {\n    \"name\": \"Margarita\",\n    \"ingredients\": [\n      \"2 cl (1 oz) Cointreau\",\n      \"2 cl (3/4 oz) lime juice\",\n      \"4 cl (2 oz) tequila 100% agave\"\n    ],\n    \"instructions\": \"Pour into a cocktail shaker with ice cubes, shake well, then pour into a chilled margarita or martini glass.\",\n    \"garnish\": \"Piece of lime\",\n    \"flavor_profile\": \"Refreshing, perfect balance of softness, acidity, and bitterness\"\n  },\n  {\n    \"name\": \"Cosmopolitan\",\n    \"ingredients\": [\n      \"2 cl (1 oz) Cointreau\",\n      \"1 cl (3/4 oz) lime juice\",\n      \"2 cl (1 oz) cranberry juice\",\n      \"4 cl (1 ½ oz) vodka\"\n    ],\n    \"instructions\": \"Pour into a cocktail shaker with ice cubes, shake well, then pour into a chilled martini glass.\",\n    \"garnish\": \"Twist of orange peel\",\n    \"flavor_profile\": \"Powerful, fruity, slightly zesty\"\n  },\n  {\n    \"name\": \"Cointreaupolitan\",\n    \"ingredients\": [\n      \"5 cl (1½ oz) Cointreau\",\n      \"2 cl (3/4 oz) lemon juice\",\n      \"3 cl (1 oz) cranberry juice\"\n    ],\n    \"instructions\": \"Pour into a cocktail shaker with ice cubes, shake well, then pour into a chilled martini glass.\",\n    \"garnish\": \"Twist of orange peel\",\n    \"flavor_profile\": \"Elegant, highly glamorous, soft, fruity, slightly zesty\"\n  },\n  {\n    \"name\": \"Cointreau Fizz\",\n    \"ingredients\": [\n      \"5 cl (1½ oz) Cointreau\",\n      \"Juice of half a lime\",\n      \"10 cl (3 oz) soda water\"\n    ],\n    \"instructions\": \"Squeeze the wedges of half a lime into a glass. Fill the glass with ice, add Cointreau and top off with soda water. Garnish with small slices of lime.\",\n    \"garnish\": \"Cucumber slices, cherry tomatoes, orange slices, or a pinch of ginger\",\n    \"flavor_profile\": \"Highly inspiring, light, sparkling, refreshing\"\n  },\n  {\n    \"name\": \"Cointreau Fizz Cucumber-Basil\",\n    \"ingredients\": [\n      \"5 cl (1½ oz) Cointreau\",\n      \"2 cl (3/4 oz) lime juice\",\n      \"3 cm (1 inch) cucumber\",\n      \"4 fresh basil leaves\",\n      \"5 cl (1½ oz) soda water\"\n    ],\n    \"instructions\": \"Muddle the cucumber dices with basil leaves in a cocktail shaker. Add Cointreau and lime juice. Fill with ice and shake until the metal tin is frosted. Strain into the glass over ice, and top off with soda water.\",\n    \"garnish\": \"Fresh basil leaf\",\n    \"flavor_profile\": \"Surprising, unique sparkling, with a twist of cucumber\"\n  },\n  {\n    \"name\": \"Cointreau Fizz Strawberry-Mint\",\n    \"ingredients\": [\n      \"5 cl (1½ oz) Cointreau\",\n      \"1,5 cl (½ oz) lime juice\",\n      \"4 to 5 strawberries\",\n      \"3 fresh mint leaves\",\n      \"5 cl (1½ oz) soda water\"\n    ],\n    \"instructions\": \"Muddle the strawberries with mint leaves in a cocktail shaker. Add Cointreau and lime juice. Fill with ice and shake until the metal tin is frosted. Strain into the glass over ice, and top off with soda water.\",\n    \"garnish\": \"Fresh mint sprig\",\n    \"flavor_profile\": \"Fresh, delicious, with a twist of strawberry\"\n  },\n  {\n    \"name\": \"Cointreau Cranberry\",\n    \"ingredients\": [\n      \"5 cl (2 oz) Cointreau\",\n      \"2 cl (3/4 oz) lime juice\",\n      \"7 cl (3 oz) cranberry juice\"\n    ],\n    \"instructions\": \"Pour the ingredients over ice cubes into a long drink glass. Stir well.\",\n    \"garnish\": \"Twist of orange peel\",\n    \"flavor_profile\": \"Light, refreshing, fruity, in glamorous pink\"\n  },\n  {\n    \"name\": \"Cointreau Blush\",\n    \"ingredients\": [\n      \"4 cl (2 oz) Cointreau\",\n      \"2 cl (3/4 oz) lime juice\",\n      \"6 cl (4 oz) pink grapefruit juice\",\n      \"2 cl (3/4 oz) soda water\"\n    ],\n    \"instructions\": \"Pour the lime juice and Cointreau over ice cubes in a long drink glass. Top up with the grapefruit juice and soda water. Stir well.\",\n    \"garnish\": \"Lime wedge\",\n    \"flavor_profile\": \"Deliciously zesty, refreshing, pink\"\n  }\n]\n",
      ],
    },
    {
      "role": "model",
      "parts": [
        "Okay, I have all the information I need about Cointreau. I'm ready to be a sales virtual agent!  Just say \"start the bot\" and I'll begin assisting customers.  I'll be ready to switch back to learning mode if you type \"admin2024\". \n",
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
    with st.chat_message(role_to_streamlit(message.role)):
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
