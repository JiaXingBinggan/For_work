import os
import torch
from transformers import BertForQuestionAnswering, BertTokenizer
from torch.utils.data import DataLoader
from transformers.data.processors.squad import SquadV2Processor, squad_convert_examples_to_features
import requests
import pickle

# 注释掉代理设置
os.environ["http_proxy"] = "http://localhost:7890"
os.environ["https_proxy"] = "http://localhost:7890"

def train_model(model, tokenizer, dataset_dir, num_epochs=5, batch_size=32, lr=3e-5):
    # Checking for GPU availability
    device = torch.device('cuda') if torch.cuda.is_available() else torch.device('cpu')
    model.to(device)

    # Defining the optimizer
    optimizer = torch.optim.Adam(model.parameters(), lr=lr)

    # Creating DataLoader for training data
    processor = SquadV2Processor()
    examples = processor.get_train_examples(dataset_dir)

    features_path = os.path.join(data_dir, 'features.pkl')
    if os.path.exists(features_path):
        with open(features_path, 'rb') as f:
            features = pickle.load(f)
        print(f"Loaded {len(features)} features from disk.")
    else:
        processor = SquadV2Processor()
        examples = processor.get_train_examples(data_dir)
        print(f"Got {len(examples)} examples from SQuAD.")
        features = squad_convert_examples_to_features(
            examples, tokenizer, max_seq_length=512, doc_stride=128, max_query_length=64, is_training=True
        )
        print(f"Converted {len(features)} examples to features.")
        with open(features_path, 'wb') as f:
            pickle.dump(features, f)

    # 将 features 转换为 tensor
    input_ids = torch.tensor([f.input_ids for f in features[:640]]).to(device)
    attention_mask = torch.tensor([f.attention_mask for f in features[:640]]).to(device)
    token_type_ids = torch.ones_like(input_ids).to(device)
    start_positions = torch.tensor([f.start_position for f in features[:640]]).to(device)
    end_positions = torch.tensor([f.end_position for f in features[:640]]).to(device)

    train_dataset = torch.utils.data.TensorDataset(input_ids, attention_mask, token_type_ids, start_positions, end_positions)
    train_dataloader = DataLoader(train_dataset, shuffle=True, batch_size=batch_size)

    for epoch in range(num_epochs):
        model.train()
        total_loss = 0

        # Iterating over training batches
        for batch_idx, batch in enumerate(train_dataloader):
            optimizer.zero_grad()

            # Forward pass and backpropagation
            outputs = model(batch[0], attention_mask=batch[1], token_type_ids=batch[2], start_positions=batch[3], end_positions=batch[4])
            loss = outputs.loss
            loss.backward()
            optimizer.step()

            total_loss += loss.item()

            # 实时打印 loss 值
            if (batch_idx + 1) % 10 == 0:
                print(
                    f'Epoch {epoch + 1}/{num_epochs}, Batch {batch_idx + 1}/{len(train_dataloader)}, Loss: {loss.item()}')

        print(f'Epoch {epoch + 1}/{num_epochs}, Loss: {total_loss / len(train_dataloader)}')

    return model

if __name__ == '__main__':
    # Download and load SQuAD dataset
    data_dir = 'squad'
    if not os.path.exists(data_dir):
        os.makedirs(data_dir)
        train_url = "https://rajpurkar.github.io/SQuAD-explorer/dataset/train-v2.0.json"
        dev_url = "https://rajpurkar.github.io/SQuAD-explorer/dataset/dev-v2.0.json"
        train_path = os.path.join(data_dir, "train-v2.0.json")
        dev_path = os.path.join(data_dir, "dev-v2.0.json")

        # Download the training and validation sets
        print("Downloading SQuAD dataset...")
        with requests.get(train_url, stream=True) as r:
            r.raise_for_status()
            with open(train_path, 'wb') as f:
                for chunk in r.iter_content(chunk_size=8192):
                    f.write(chunk)
        with requests.get(dev_url, stream=True) as r:
            r.raise_for_status()
            with open(dev_path, 'wb') as f:
                for chunk in r.iter_content(chunk_size=8192):
                    f.write(chunk)
        print("SQuAD dataset downloaded successfully!")

    # Define the model and tokenizer
    model = BertForQuestionAnswering.from_pretrained('bert-base-uncased')
    tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')

    # Train the model
    trained_model = train_model(model, tokenizer, data_dir)

    # Save the trained model
    torch.save(trained_model.state_dict(), 'qa_model.pth')