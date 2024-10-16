import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from utilities.template import PROMPT_VALIDATION, SONG_CREATION, ADD_META_DATA
from langgraph.graph import MessagesState
from langchain_core.output_parsers import StrOutputParser
from langgraph.graph import StateGraph, START, END
from langchain_openai import ChatOpenAI
from typing import Literal
import requests

llm_deterministic = ChatOpenAI(model="gpt-4o-2024-08-06", temperature=0)
llm_creative = ChatOpenAI(model="gpt-4o-2024-08-06", temperature=0.6)

def add_meta_data(state: MessagesState):
    chain = (
        ADD_META_DATA
        | llm_creative
        | StrOutputParser()
    )
    return {
        "messages": [
            chain.invoke(
                {"song": state["messages"][-1]}
            ) 
        ]
    }

def song_creation(state: MessagesState):
    song = str(state["messages"][-1])
    token = os.environ("SUNO_API_KEY")

    response = requests.post(
        "https://api.aimlapi.com/v2/generate/audio/suno-ai/clip",
        headers={
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json",
        },
        json={
            "prompt": song,
            "tags": "desi pop",
            "title": "Test",
        },
    )

    response.raise_for_status()
    data = response.json()
    clip_ids = data["clip_ids"]

    return {
        "messages": [clip_ids]
    }


def lyric_creation(state: MessagesState):
    chain = (
        SONG_CREATION
        | llm_creative
        | StrOutputParser()
    )
    return {
        "messages": [
            chain.invoke(
                {"description": state["messages"][:-1]}
            ) 
        ]
    }

def prompt_validation(state: MessagesState):
    chain = (
        PROMPT_VALIDATION
        | llm_deterministic
        | StrOutputParser()
    )
    return {
        "messages": [
            chain.invoke(
                {"input": state["messages"]}
            ) 
        ]
    }

def valid_input_check(state) -> Literal["lyric_creation","__end__"]:
    if state["messages"][-1].content == "Yes":
        return "lyric_creation"
    return "__end__"

# Define a new graph
workflow = StateGraph(MessagesState)
workflow.add_node("prompt_validation", prompt_validation)
workflow.add_node("lyric_creation", lyric_creation)
workflow.add_node("add_meta_data", add_meta_data)
workflow.add_node("song_creation", song_creation)


# add edges
workflow.add_edge(START, "prompt_validation")
workflow.add_conditional_edges("prompt_validation", valid_input_check)
workflow.add_edge("lyric_creation", "add_meta_data")
workflow.add_edge("add_meta_data", "song_creation")
workflow.add_edge("song_creation", END)

# Compile
graph = workflow.compile()
