import torch
from torch import nn
from torch.utils.data import DataLoader
from torchvision import datasets, transforms, models
from matplotlib import pyplot as plt
from matplotlib import ticker
from tqdm import tqdm
import warnings
warnings.filterwarnings("ignore")


def train(dataloader, model, loss_fn, optimizer):
    size = len(dataloader.dataset)
    num_batches = len(dataloader)
    train_loss,correct = 0, 0
    model.train()
    for batch, (X, y) in enumerate(tqdm(dataloader)):
        X, y = X.to(device), y.to(device)
        pred=model(X)
        loss=loss_fn(pred,y)
        correct+=(pred.argmax(1) == y).type(torch.float).sum().item()
        
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()
        train_loss += loss.item()
        loss,current = loss.item(),batch * len(X)
            
    train_loss /= num_batches
    correct /= size
    train_Avg_loss.append(train_loss)
    train_Accuracy.append(100*correct)
    print(f"training Accuracy: {(100*correct):>0.1f}")


def test(dataloader, model, loss_fn):
    size = len(dataloader.dataset)
    num_batches = len(dataloader)
    model.eval()
    test_loss, correct = 0, 0
    with torch.no_grad():
        for X,y in tqdm(dataloader):
            X, y = X.to(device), y.to(device)
            pred = model(X)
            test_loss += loss_fn(pred,y).item()
            correct += (pred.argmax(1) == y).type(torch.float).sum().item()
    test_loss /= num_batches
    correct /= size
    
    test_Avg_loss.append(test_loss)
    test_Accuracy.append(100*correct)
    
    print(f"Test Accuracy: {(100*correct):>0.2f}%, Test Avg loss: {test_loss:>8f}\n")


transform1 = transforms.Compose([transforms.Resize((128, 128)),
                               transforms.RandomHorizontalFlip(p=0.5),
                               transforms.ToTensor(),
                               transforms.Normalize(0, 1)])

transform2 = transforms.Compose([transforms.Resize((128, 128)),
                               transforms.ToTensor(),
                               transforms.Normalize(0, 1)])

if __name__ == '__main__':
    training_data = datasets.ImageFolder(r'./dataset/train', transform=transform1)
    test_data = datasets.ImageFolder(r'./dataset/test', transform=transform2)
    train_dataloader = DataLoader(training_data, batch_size=32, shuffle=True)
    test_dataloader = DataLoader(test_data, batch_size=32, shuffle=False)
    
    for X,y in test_dataloader:
        print(f"Shape of X [N, C, H, W]: {X.shape}")
        print(f"Shape of y: {y.shape} {y.dtype}")
        break
    
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    print(f"Using device: {device}")
    loss_fn = nn.CrossEntropyLoss()
    learning_rate = 1e-4
    
    model = models.resnet18()
    model.to(device)
    
    optimizer = torch.optim.Adam(model.parameters(), lr=learning_rate)
    scheduler = torch.optim.lr_scheduler.StepLR(optimizer,step_size=10, gamma=0.8)
    
    train_Accuracy = []
    train_Avg_loss = []
    test_Accuracy = []
    test_Avg_loss = []
    
    epochs = 20
    for epoch in range(epochs):
        print(f"epoch{epoch+1}")
        train(train_dataloader, model, loss_fn,optimizer)
        scheduler.step()
        test(test_dataloader, model, loss_fn)
    torch.save(model, "model.pth")
    print('Done')
    