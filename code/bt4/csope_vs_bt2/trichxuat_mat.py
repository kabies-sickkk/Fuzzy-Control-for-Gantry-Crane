import matplotlib.pyplot as plt

# Biểu đồ Neural Network
plt.plot(epochs, train_loss, label="Train Loss (Neural Network)", color="blue")
plt.plot(epochs, val_loss, label="Validation Loss (Neural Network)", color="green")
plt.plot(epochs, test_loss, label="Test Loss (Neural Network)", color="red")

# Biểu đồ Fuzzy Logic (giả định fuzzy_output đã được trích xuất)
fuzzy_epochs = epochs  # Giả sử fuzzy và NN cùng số epoch
fuzzy_output = [0.02 * e for e in epochs]  # Ví dụ giả định
plt.plot(fuzzy_epochs, fuzzy_output, label="Fuzzy Logic Output", color="purple", linestyle="--")

# Tùy chỉnh biểu đồ
plt.title("Comparison: Neural Network & Fuzzy Logic")
plt.xlabel("Epochs")
plt.ylabel("Loss / Output")
plt.legend()
plt.grid()
plt.show()
