import pandas as pd
import torch
from torch import nn
from torchtext import data
import random

if torch.cuda.is_available():
    dev = "cuda:0"
    print("GPU is available.")
else:
    dev = "cpu"
device = torch.device(dev)

SEED = 32

# IPA dataset reading
df = pd.read_csv("bangla_dictionary/data/sushmitIPAData.csv", delimiter="\t", names=["ban", "ipa"])


# Section 2: Tokenization and Data Processing

def myTokenizerBAN(x):
    x = ' '.join(x)
    x = x.split(' ')
    return list(x)


def myTokenizerIPA(x):
    x = ' '.join(x)
    x = x.split(' ')
    return list(x)


SRC = data.Field(tokenize=myTokenizerBAN, batch_first=False, init_token="<sos>", eos_token="<eos>")
TARGET = data.Field(tokenize=myTokenizerIPA, batch_first=False, tokenizer_language="ipa", init_token="<sos>",
                    eos_token="<eos>")


class DataFrameDataset(data.Dataset):
    """
        This code belongs to Asif Sushmit

        Preface:
        - to point out one thing about the transformer what it could do is to enable
            training on the whole sequence at once but on really using it for translation it predicts the next word
            then it feeds the prediction into the sequence again until the model predict <eos> token (with a max length ofc)
        - I'm using adagrad because it assigns bigger updates to less frequently updated weights. so thought it could be useful for words not used a lot
        - ?????????? - HOPE VAI WILL ADD MORE.
        - ????????? - HOPE VAI WILL ADD MORE.
        - ???????? - HOPE VAI WILL ADD MORE.

        Returns:
        - translation to ipa from bangla words
    """

    def __init__(self, df, src_field, target_field, is_test=False, **kwargs):
        fields = [('ban', src_field), ('ipa', target_field)]
        examples = []
        for i, row in df.iterrows():
            ban = row.ban
            ipa = row.ipa
            examples.append(data.Example.fromlist([ban, ipa], fields))

        super().__init__(examples, fields, **kwargs)


torchdataset = DataFrameDataset(df, SRC, TARGET)

train_data, valid_data = torchdataset.split(split_ratio=0.8, random_state=random.seed(SEED))

SRC.build_vocab(train_data, min_freq=2)
TARGET.build_vocab(train_data, min_freq=2)

BATCH_SIZE = 64

train_iterator, valid_iterator = data.BucketIterator.splits(
    (train_data, valid_data),
    batch_size=BATCH_SIZE,
    device=device,
    sort=False,
    sort_within_batch=False,
    shuffle=True)


# section 3
class TranslateTransformer(nn.Module):
    def __init__(
            self,
            embedding_size,
            src_vocab_size,
            trg_vocab_size,
            src_pad_idx,
            num_heads,
            num_encoder_layers,
            num_decoder_layers,
            max_len,
    ):
        super(TranslateTransformer, self).__init__()
        self.srcEmbeddings = nn.Embedding(src_vocab_size, embedding_size)
        self.trgEmbeddings = nn.Embedding(trg_vocab_size, embedding_size)
        self.srcPositionalEmbeddings = nn.Embedding(max_len, embedding_size)
        self.trgPositionalEmbeddings = nn.Embedding(max_len, embedding_size)
        self.transformer = nn.Transformer(
            embedding_size,
            num_heads,
            num_encoder_layers,
            num_decoder_layers,
        )
        self.fc_out = nn.Linear(embedding_size, trg_vocab_size)
        self.dropout = nn.Dropout(0.1)
        self.src_pad_idx = src_pad_idx
        self.max_len = max_len

    def make_src_mask(self, src):
        src_mask = src.transpose(0, 1) == self.src_pad_idx

        return src_mask.to(device)

    def forward(self, x, trg):
        src_seq_length = x.shape[0]
        N = x.shape[1]
        trg_seq_length = trg.shape[0]
        # adding zeros is an easy way
        src_positions = (
                torch.arange(0, src_seq_length)
                .reshape(src_seq_length, 1) + torch.zeros(src_seq_length, N)
        ).to(device)

        trg_positions = (
                torch.arange(0, trg_seq_length)
                .reshape(trg_seq_length, 1) + torch.zeros(trg_seq_length, N)
        ).to(device)

        srcWords = self.dropout(self.srcEmbeddings(x.long()) + self.srcPositionalEmbeddings(src_positions.long()))
        trgWords = self.dropout(self.trgEmbeddings(trg.long()) + self.trgPositionalEmbeddings(trg_positions.long()))

        src_padding_mask = self.make_src_mask(x)
        trg_mask = self.transformer.generate_square_subsequent_mask(trg_seq_length).to(device)

        out = self.transformer(srcWords, trgWords, src_key_padding_mask=src_padding_mask, tgt_mask=trg_mask)
        out = self.fc_out(out)
        return out


# section 4
# No. of unique tokens in text
src_vocab_size = len(SRC.vocab)
# print("Size of Bangla vocabulary:", src_vocab_size)

# No. of unique tokens in label
trg_vocab_size = len(TARGET.vocab)
# print("Size of IPA vocabulary:", trg_vocab_size)

num_heads = 8
num_encoder_layers = 2
num_decoder_layers = 2

max_len = 100
embedding_size = 256
src_pad_idx = SRC.vocab.stoi["<pad>"]


class BanglaIPATranslator:

    def __init__(self, model_path):
        self.model = self.load_model(model_path)

    def load_model(self, model_path):
        model = TranslateTransformer(
            embedding_size,
            len(SRC.vocab),
            len(TARGET.vocab),
            SRC.vocab.stoi["<pad>"],
            num_heads,
            num_encoder_layers,
            num_decoder_layers,
            max_len
        ).to(device)
        model.load_state_dict(torch.load(model_path, map_location=device))
        return model

    def translate(self, sentence):
        self.model.eval()
        processed_sentence = SRC.process([myTokenizerBAN(sentence)]).to(device)
        trg = ["<sos>"]
        for _ in range(60):
            trg_indices = [TARGET.vocab.stoi[word] for word in trg]
            outputs = torch.Tensor(trg_indices).unsqueeze(1).to(device)
            outputs = self.model(processed_sentence, outputs)

            predicted_word = TARGET.vocab.itos[outputs.argmax(2)[-1:].item()]
            if predicted_word == "<unk>":
                continue
            trg.append(predicted_word)
            if predicted_word == "<eos>":
                break
        return " ".join([word for word in trg if word != "<unk>"][1:-1])


# Usage Example:
#
# model_path = "../translation_model.pth"
#
# translator = BanglaIPATranslator(model_path)
#
# # Translate a Bangla word to IPA
# translated_ipa = translator.translate("হাসপাতালের")
# print(translated_ipa)
