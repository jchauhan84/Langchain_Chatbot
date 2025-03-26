from langchain_openai import ChatOpenAI
from langchain_core.prompt import ChatPromptTemplate
from langchain_core.output_parser import StrOutputParser

import streamlit as st
import os
from dotenv import load_dotenv