import streamlit as st
from openai import OpenAI

st.title("ChatGPT-despedida - Carlos")

# Set OpenAI API key from Streamlit secrets
client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

# Set a default model
if "openai_model" not in st.session_state:
    st.session_state["openai_model"] = "gpt-3.5-turbo"

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Initialize additional context (e.g., previous interactions, user preferences)
if "additional_context" not in st.session_state:
    st.session_state.additional_context = "este fin de semana se celebra la despedida de Carlos. Su mote es Caratonto, le gusta el pádel que es un deporte de bujarras"

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Accept user input
if prompt := st.chat_input("What is up?"):
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    # Display user message in chat message container
    with st.chat_message("user"):
        st.markdown(prompt)

    # Prepare messages for API call including additional context
    messages_for_api = [{"role": "system", "content": st.session_state.additional_context}]
    messages_for_api.extend([
        {"role": m["role"], "content": m["content"]}
        for m in st.session_state.messages
    ])

    # Display assistant response in chat message container
    with st.chat_message("assistant"):
        stream = client.chat.completions.create(
            model=st.session_state["openai_model"],
            messages=messages_for_api,
            stream=True,
        )
        response = st.write_stream(stream)
    st.session_state.messages.append({"role": "assistant", "content": response})
