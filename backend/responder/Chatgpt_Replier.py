import os
import openai
import tiktoken
import json
import re
from globals import(
  FILENAME1, FILENAME2, FILENAME3, OPENAI_API_KEY,
  GPT_CHAT_1_INSTRUCTIONS, GPT_CHAT_2_INSTRUCTIONS, GPT_CHAT_3_INSTRUCTIONS
)
from .chatgpt import generate_text

openai.api_key = OPENAI_API_KEY
def gen_text1(prompt):
  gpt_model = "gpt-4"
  prompt = "Reply without any signature: " + prompt
  messages=[{"role": "system", "content": GPT_CHAT_1_INSTRUCTIONS}, {"role": "user", "content": prompt}]
  res = generate_text(gpt_model, messages, 0.2, 0.2)
  return res

def gen_text2(prompt):
  gpt_model = "gpt-3.5-turbo"
  prompt = "Reply without any signature: " + prompt
  messages=[{"role": "system", "content": GPT_CHAT_1_INSTRUCTIONS}, {"role": "user", "content": prompt}]
  res = generate_text(gpt_model, messages, 0.2, 0.2)
  return res

def gen_text3(prompt):
  gpt_model = "gpt-3.5-turbo"
  prompt = "Reply without any signature: " + prompt
  messages=[{"role": "system", "content": GPT_CHAT_3_INSTRUCTIONS}, {"role": "user", "content": prompt}]
  res = generate_text(gpt_model, messages, 0.2, 0.2)
  return res

def fileread(filename, names, a):
  with open(filename,"r", encoding="utf8") as f:
    d = json.load(f)
  var1 = []
  for i in range (a) :
    k = d['messages'][i]['body']

    if i%2 == 0:
      var11 = {"role": "system", "name": names[0], "content": k}
      var1.append(var11)
    else:
      var11 = {"role": "system", "name": names[1], "content": k}
      var1.append(var11)
    i += 1
  return var1