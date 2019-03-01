from torch import nn,optim
from Case.minst import read_img
import torch
from torch.autograd import Variable
import numpy as np


class CNN(nn.Module):
    def __init__(self):
        super(CNN, self).__init__()
        self.layer1 = nn.Sequential(
            nn.Conv2d(1, 25, 3),
            nn.BatchNorm2d(25),
            nn.ReLU(inplace=True)
        )
        self.layer2 = nn.Sequential(
            nn.MaxPool2d(kernel_size=2, stride=2)
        )

        self.layer3 = nn.Sequential(
            nn.Conv2d(25, 50, kernel_size=3),
            nn.BatchNorm2d(50),
            nn.ReLU(inplace=True)
        )

        self.layer4 = nn.Sequential(
            nn.MaxPool2d(kernel_size=2, stride=2)
        )

        self.fc = nn.Sequential(
            nn.Linear(50 * 5 * 5, 1024),
            nn.ReLU(inplace=True),
            nn.Linear(1024, 128),
            nn.ReLU(inplace=True),
            nn.Linear(128, 10)
        )

    def forward(self, x):
        x = x.view(1, 1, 28, 28)
        print()
        x = self.layer1(x)
        x = self.layer2(x)
        x = self.layer3(x)
        x = self.layer4(x)
        x = x.view(x.size(0), -1)
        x = self.fc(x)
        return x


batch_size = 64
learning_rate = 0.02
num_epoches = 20


if __name__ == '__main__':
    train_images = read_img.load_train_images()
    train_labels = read_img.load_train_labels()
    test_images = read_img.load_test_images()
    test_labels = read_img.load_test_labels()
    train_images = train_images.astype(np.float32)
    train_labels = train_labels.astype(np.int64)
    test_images = test_images.astype(np.float32)
    test_labels = test_labels.astype(np.int64)
    train_images = torch.from_numpy(train_images)
    train_labels = torch.from_numpy(train_labels)
    test_images = torch.from_numpy(test_images)
    test_labels = torch.from_numpy(test_labels)
    model = CNN()
    if torch.cuda.is_available():
        model = model.cuda()
    criterion = nn.CrossEntropyLoss()
    optimizer = optim.SGD(model.parameters(), lr=learning_rate)


    step = 0
    for i in range(train_images.shape[0]):
        img = train_images[i]
        label = train_labels[i]
        img = Variable(img)
        label = Variable(label)
        out = model(img)
        loss = criterion(out, label)
        print_loss = loss.data.item()

        optimizer.zero_grad()
        loss.backward()
        optimizer.step()
        step+=1
        if step%50==0:
            print('step: {}, loss: {:.4}'.format(step, loss.data.item()))

    model.eval()
    eval_loss = 0
    eval_acc = 0
    for i in range(test_images.shape[0]):
        img = test_images[i]
        label = train_labels[i]
        # img = img.view(img.size(0), -1)
        img = Variable(img)
        out = model(img)
        loss = criterion(out, label)
        eval_loss += loss.data.item()*label.size(0)
        _, pred = torch.max(out, 1)
        num_correct = (pred == label).sum()
        eval_acc += num_correct.item()
    print('Test Loss: {:.6f}, Acc: {:.6f}'.format(
        eval_loss / (test_images.shape[0]),
        eval_acc / (test_images.shape[0])
    ))
