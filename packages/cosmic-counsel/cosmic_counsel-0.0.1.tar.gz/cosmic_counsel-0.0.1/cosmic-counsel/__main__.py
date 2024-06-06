#!/usr/bin/env python3

import argparse
import os
import torch
from threading import Thread
from transformers import (
    AutoModelForCausalLM,
    AutoTokenizer,
    TextIteratorStreamer,
    GenerationConfig,
)
import sys
import json
from .cosmic_utils import *

parent_dir_path = os.path.dirname(os.path.realpath(__file__))

parser = argparse.ArgumentParser(description="Cosmic Counsel CLI")
parser.add_argument("-q","--question", default="what is your expertise?", type=str, help="The user's question")
args = parser.parse_args()

# Initialize the system message
SYSTEM_PROMPT = "Welcome to Cosmic Counsel! How can I help you today?"

# Check if the model and tokenizer are saved in the models directory
model_exists = os.path.isfile(f'{parent_dir_path}/models/model.sav')
tokenizer_exists = os.path.isfile(f'{parent_dir_path}/models/tokenizer.sav')
model_path = os.path.join(parent_dir_path, 'models', 'model.sav')
tokenizer_path = os.path.join(parent_dir_path, 'models', 'tokenizer.sav')

# Load the model and tokenizer
if not model_exists or tokenizer_exists:
    model = load_model(model_path)
    tokenizer = load_tokenizer(tokenizer_path)
else:
    model = AutoModelForCausalLM.from_pretrained("HuggingFaceH4/zephyr-7b-beta")
    tokenizer = AutoTokenizer.from_pretrained("HuggingFaceH4/zephyr-7b-beta")
    save_model(model, model_path)
    save_tokenizer(tokenizer, tokenizer_path)

# Load the chat history
chat_history_path = os.path.join(parent_dir_path, 'data', 'chat_history.json')
chat_history = load_chat_history(chat_history_path)

# Update the system message in the chat history
update_system_message(chat_history, SYSTEM_PROMPT)

# Save the updated chat history
save_chat_history(chat_history, chat_history_path)

# Define the main function
def main():

    question = args.question

    # Load existing chat history
    chat_history_path = f"{parent_dir_path}/chat_history.json"
    chat_history = load_chat_history(chat_history_path)

    # Update or add a new 'system' message
    new_system_content = SYSTEM_PROMPT
    update_system_message(chat_history, new_system_content)

    import time
    start_time = time.time()

    generation_config = GenerationConfig(
        num_beams=1,
        early_stopping=False,
        decoder_start_token_id=0,
        eos_token_id=model.config.eos_token_id,
        pad_token_id=50256,
        temperature=0.01,
        do_sample=True
    )

    streamer = TextIteratorStreamer(
        tokenizer, skip_prompt=True, skip_special_tokens=True
    )

    generation_kwargs = {
        "streamer": streamer,
        "generation_config": generation_config,
        "max_new_tokens": 200,
    }

    relevant_hist = relevant_history(chat_history, question)

    # Assume we're adding a new user question
    new_user_message = {"role": "user", "content": question}

    relevant_hist.append(new_user_message)

    chat_history.append(new_user_message)

    save_chat_history(relevant_hist, f"{parent_dir_path}/relevant_history.json")

    inputs = tokenizer.apply_chat_template(
        relevant_hist, tokenize=True, add_generation_prompt=False, return_tensors="pt"
    ).to(model.device)

    thread = Thread(target=model.generate, args=(inputs,), kwargs=generation_kwargs)
    thread.start()

    gen_text = ""
    for new_text in streamer:
        gen_text += new_text.split("\n")[-1]
        sys.stdout.write(new_text.split("\n")[-1])
        sys.stdout.flush()

    # Append the generated response to the chat history
    chat_history.append({"role": "assistant", "content": gen_text})
    # Save the updated chat history back to the JSON file
    save_chat_history(chat_history, chat_history_path)

    end_time = time.time()
    execution_time = end_time - start_time
    print(f"\nExecution time: {execution_time} seconds")

if __name__ == "__main__":
    main()
