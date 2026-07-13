import streamlit as st

from src.graph import graph

st.set_page_config(
    page_title="GigaCorp Customer Support",
    page_icon="🤖",
    layout="wide"
)

st.title("🤖 GigaCorp Customer Support Assistant")
st.caption("Ask questions about shipping, returns, business hours, or service tiers.")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display previous messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Chat input
if prompt := st.chat_input("Ask your question..."):

    # Show user message
    st.session_state.messages.append(
        {"role": "user", "content": prompt}
    )

    with st.chat_message("user"):
        st.markdown(prompt)

    # Generate response
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            response = graph.invoke(
                {
                    "question": prompt
                }
            )

            answer = response["answer"]

            st.markdown(answer)

    # Save assistant message
    st.session_state.messages.append(
        {"role": "assistant", "content": answer}
    )