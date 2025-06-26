from datasets import load_dataset

dataset = load_dataset("facebook/hateful_memes", split="train")
print(dataset[0])
