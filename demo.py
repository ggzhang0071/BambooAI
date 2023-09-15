# Run in a loop remembering the conversation history
import pandas as pd
from bambooai import BambooAI

df = pd.read_csv('./examples/test_activity_data.csv')
bamboo = BambooAI(df)
bamboo.pd_agent_converse()