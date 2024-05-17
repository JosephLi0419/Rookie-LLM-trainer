from sentencepiece import SentencePieceProcessor
import json

# Initialize SentencePieceProcessor with your model file
sp = SentencePieceProcessor(model_file="/home/yabilab/Desktop/tokenizer.model") #改成你想要用的模型的tokenizer

def tokenize(input_text):
    # Tokenize input_text using SentencePiece
    tokens = sp.EncodeAsIds(input_text) #Encoder: 对应预处理时的tokenization操作，把句子转为对应的subword或id。
    return len(tokens)

# Path to your JSON file
json_file_path = "/home/yabilab/Desktop/LLaMA-Factory-main/data/AI_conversation.json" #改成你想要計算的對話檔


# Load JSON data from file
with open(json_file_path, "r", encoding="utf-8") as file:
    json_data = json.load(file)

total_token_count = 0

# Iterate over conversations and accumulate token counts
for conversation in json_data:
    for conv in conversation["conversations"]:
        if "value" in conv:
            total_token_count += tokenize(conv["value"])

print("Total token count:", total_token_count)
