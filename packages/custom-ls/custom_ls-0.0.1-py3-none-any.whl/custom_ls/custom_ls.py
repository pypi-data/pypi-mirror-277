import torch


def save_decorator(func):
    def wrapper(*args, **kwargs):
        print("Saving data...")
        result = func(*args, **kwargs)
        print("Data saved.")
        return result
    return wrapper

def load_decorator(func):
    def wrapper(*args, **kwargs):
        print("Loading data...")
        result = func(*args, **kwargs)
        print("Data loaded.")
        return result
    return wrapper

@save_decorator
def save_data(data, file_path):
    torch.save(data, file_path)

@load_decorator
def load_data(file_path):
    return torch.load(file_path)

# 使用装饰器
# data = torch.tensor([1, 2, 3])
# save_data(data, "data.pt")
# loaded_data = load_data("data.pt")
# print("Loaded data:", loaded_data)

# torch.save = save_decorator(torch.save)
# torch.load = load_decorator(torch.load)
# data = torch.tensor([1, 2, 3])
# torch.save(data, "data.pt")
# loaded_data = torch.load("data.pt")
# print("Loaded data:", loaded_data)