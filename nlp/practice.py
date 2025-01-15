import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import Dataset,DataLoader
from torch.nn.utils.rnn import pad_sequence

data = [
    ("I love this product", 1),
    ("This is the worst thing I have ever bought", 0),
    ("Amazing quality, highly recommend it", 1),
    ("Not worth the money, really bad", 0),
    ("Great value for the price", 1),
    ("Terible experience, don't buy it", 0),
    ("He made her feel special", 1),
    ("The worst day of my life", 0),
    ("I'm stuck in traffic for 40 minutes already",0),
    ("This is the worst thing I've ever bought", 0),
    ("I was positively surprised by such great quality",1),
    ("You cook the best pasta I have ever eaten", 1),
    ("My life is the best",1),
    ("The end of the workday",1)
]

word_to_index = {"<UNK>":0}
index = 1
for sentence, _ in data:
    for word in sentence.split():
        if word not in word_to_index:
            word_to_index[word] = index
            index += 1

def encode_sentence(sentence):
    return [word_to_index.get(word, word_to_index["<UNK>"]) for word in sentence.split()]

encoded_data = [(torch.tensor(encode_sentence(sentence)), label) for sentence, label in data]

class TextDataset(Dataset):
    def __init__(self, data):
        self.data = data

    def __len__(self):
        return len(self.data)
    
    def __getitem__(self, idx):
        return self.data[idx]
    
dataset = TextDataset(encoded_data)

def collate_fn(batch):
    sentences,labels =zip(*batch)
    padded_sentences = pad_sequence(sentences, batch_first=True, padding_value=0)
    return padded_sentences, torch.tensor(labels)

dataloader = DataLoader(dataset, batch_size=2, shuffle=True, collate_fn=collate_fn)

class SentimentClassifier(nn.Module):
    def __init__(self, vocab_size, embed_dim):
        super(SentimentClassifier, self).__init__()
        self.embedding = nn.Embedding(vocab_size,embed_dim)
        self.fc = nn.Linear(embed_dim,1)

    def forward(self, x):
        x = self.embedding(x)
        x = x.mean(dim=1)
        x = self.fc(x)
        return torch.sigmoid(x)

vocab_size = len(word_to_index)
embed_dim = 10
model = SentimentClassifier(vocab_size, embed_dim)

criterion = nn.BCELoss()
optimizer = optim.Adam(model.parameters(), lr = 0.01)

print('Learnin has started...')
for epoch in range(20):
    for sentences, labels in dataloader:
        optimizer.zero_grad()
        outputs = model(sentences)
        loss = criterion(outputs.squeeze(), labels.float())
        loss.backward()
        optimizer.step()
    print(f'Epoch: {epoch + 1}, Loss: {loss.item():.4f}')

test_sentence = "Best day in my life"
encoded_test = torch.tensor(encode_sentence(test_sentence))
padded_test = pad_sequence([encoded_test], batch_first=True, padding_value=0)
prediction = model(padded_test).item()
print(f'Prediction for "{test_sentence}": {"positive" if prediction > 0.5 else "Negative"}')