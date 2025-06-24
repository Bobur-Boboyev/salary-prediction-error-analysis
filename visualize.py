import matplotlib.pyplot as plt
from predict import prediction, make_prediction, MSE, MAE, data

x = data[:,0]
y = data[:,1]

pred2 = prediction()
def visualize_1():
    inp, pred = make_prediction()
    plt.scatter(x, y, color='red', label="True Value")
    plt.scatter(inp, pred, color='blue', label="Predicted Value")
    plt.text(inp, pred+5000, f"${pred}", ha='center', va="top")
    plt.title("Years Experience and Salary")
    plt.xlabel("Years experience")
    plt.ylabel("Salary")
    plt.show()

def visualize_error_MSE():
    plt.scatter(x, y, color='red', label="True Value")
    plt.plot(x, pred2, color='blue', label='Predicted Value')
    plt.text(max(x)*0.7, max(y)*0.6, f"MSE: {MSE()}")
    plt.title("Years Experience vs Salary")
    plt.xlabel("Years Experience")
    plt.ylabel("Salary")

    for i in range(len(x)):
        plt.plot([x[i], x[i]], [y[i], pred2[i]], color='gray', linestyle='--', linewidth=0.7)

    plt.legend()
    plt.show()

def visualize_error_MAE():
    plt.scatter(x, y, color='red', label='True value')
    plt.plot(x, pred2, color='blue', label="Predicted Value")
    plt.text(max(x)*0.7, max(y)*0.6, f"MAE: {MAE()}")
    plt.title('Years Experience vs Salary')
    plt.xlabel("Years Experience")
    plt.ylabel("Salary")

    for i in range(len(x)):
        plt.plot([x[i], x[i]], [y[i], pred2[i]], color='gray', linestyle="--", linewidth=0.7)

    plt.legend()
    plt.show()