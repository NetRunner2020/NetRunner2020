import os
import mxnet as mx
from mxnet.gluon import nn, Trainer
from mxnet.gluon.loss import SoftmaxCrossEntropyLoss
from mxnet import autograd

def load_preprocessed_data(input_dir):
    """Load all preprocessed text files in input_dir and return as list."""
    data = []
    for text_file in os.listdir(input_dir):
        if text_file.endswith('_preprocessed.txt'):
            text_path = os.path.join(input_dir, text_file)
            with open(text_path, 'r', encoding='utf-8') as f:
                data.append(f.read())
    return data

def train_model(data):
    """Train a simple machine learning model on the preprocessed data."""
    # This is a simple placeholder model using MXNet's Gluon API.
    net = nn.Sequential()
    net.add(nn.Dense(128, activation='relu'))
    net.add(nn.Dense(64, activation='relu'))
    net.add(nn.Dense(2))  # Assuming binary classification (change as needed)
    net.initialize(mx.init.Xavier())

    # Training parameters (placeholders, modify based on your needs)
    batch_size = 32
    epochs = 10
    loss_fn = SoftmaxCrossEntropyLoss()
    trainer = Trainer(net.collect_params(), 'adam')

    for epoch in range(epochs):
        cumulative_loss = 0
        for i in range(0, len(data), batch_size):
            batch_data = data[i:i + batch_size]

            # Convert data to MXNet NDArrays (Placeholder logic, replace with actual data handling)
            inputs = mx.nd.array(batch_data)  # You need to transform text into features
            labels = mx.nd.array([0] * len(batch_data))  # Placeholder labels

            with autograd.record():
                outputs = net(inputs)
                loss = loss_fn(outputs, labels)
            loss.backward()
            trainer.step(batch_size)

            cumulative_loss += loss.mean().asscalar()
        print(f"Epoch {epoch+1}, Loss: {cumulative_loss/len(data)}")

if __name__ == "__main__":
    input_dir = '../data/preprocessed_data/'  # Directory containing preprocessed text
    data = load_preprocessed_data(input_dir)
    train_model(data)
    print("Model training complete.")
