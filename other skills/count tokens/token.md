# Token: 
- Tokens are the basic units of data processed by LLMs. In the context of text, a token can be a word, part of a word (subword), or even a character — depending on the tokenization process.
- 在大型語言模型（LLM）中，「token」代表模型可以理解和生成的最小意義單位，是 LLM 進行處理的最小單元。
- Tokenization是將輸入和輸出文本分割成可以由 LLM 模型處理的較小單元的過程
- 根據所使用的"Tokenization"方法，token 可以表示單詞、單詞的一部分，甚至只表示字符。採用的方案由模型的類型和大小決定
- token 被賦予數值或標識符，並按序列或向量排列，並被輸入或從模型中輸出，是模型的語言構件。
- 模型理解這些 token 之間的統計關係，並擅長於 token 的接龍。
- token 作為原始文本數據和 LLM 可以使用的數字表示之間的橋樑。LLM 使用 token 來確保文本的連貫性和一致性，有效地處理各種任務，如寫作、翻譯和回答查詢。

### protocols:
- download the tokenizer model (according to the model you want to use)
- select the json file that you want to count tokens in.
- run token_counter.py
