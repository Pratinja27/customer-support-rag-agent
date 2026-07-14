import uuid

import streamlit as st
from langchain_core.messages import HumanMessage

from src.graph import graph

st.set_page_config(
    page_title="GigaCorp Customer Support",
    page_icon="🤖",
    layout="wide",
)

st.title("🤖 GigaCorp Customer Support Assistant")
st.write(
    "Ask questions about shipping, returns, business hours, or service tiers."
)

# -----------------------------
# Session State
# -----------------------------

if "messages" not in st.session_state:
    st.session_state.messages = []

if "thread_id" not in st.session_state:
    st.session_state.thread_id = str(uuid.uuid4())

# -----------------------------
# Sidebar
# -----------------------------

with st.sidebar:

    st.header("Conversation")

    if st.button("🗑 Clear Conversation"):

        st.session_state.messages = []

        st.session_state.thread_id = str(uuid.uuid4())

        st.rerun()

# -----------------------------
# Display Chat
# -----------------------------

for msg in st.session_state.messages:

    with st.chat_message(msg["role"]):

        st.markdown(msg["content"])

        if msg["role"] == "assistant":

            if msg.get("sources"):

                with st.expander("📚 Sources"):

                    for source in msg["sources"]:

                        st.markdown(source)

# -----------------------------
# Chat Input
# -----------------------------

prompt = st.chat_input("Ask your question...")

if prompt:

    prompt = prompt.strip()

    if len(prompt) == 0:

        st.stop()

    st.session_state.messages.append(
        {
            "role": "user",
            "content": prompt,
        }
    )

    with st.chat_message("user"):

        st.markdown(prompt)

    with st.chat_message("assistant"):

        with st.spinner("Thinking..."):

            try:

                response = graph.invoke(

                    {
                        "question": prompt,

                        "messages": [

                            HumanMessage(
                                content=prompt
                            )

                        ],

                    },

                    config={

                        "configurable": {

                            "thread_id": st.session_state.thread_id

                        }

                    }

                )

                answer = response["answer"]

                docs = response.get(
                    "retrieved_docs",
                    [],
                )

                sources = []

                for doc in docs:

                    source = doc.metadata.get(
                        "source",
                        "Unknown"
                    )

                    preview = doc.page_content.replace(
                        "\n",
                        " "
                    )[:200]

                    sources.append(
                        f"**{source}**\n\n{preview}..."
                    )

                st.markdown(answer)

                if sources:

                    with st.expander("📚 Sources"):

                        for s in sources:

                            st.markdown(s)

                st.session_state.messages.append(

                    {

                        "role": "assistant",

                        "content": answer,

                        "sources": sources,

                    }

                )

            except Exception as e:

                st.error(str(e))