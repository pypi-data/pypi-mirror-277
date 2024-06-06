import numpy as np
def sayhello():
    print("Hello World!")

def generateData(X_train_vec):
    for i in range(len(X_train_vec)):
        if(y_train_vec[i] == True):
            for j in range(100):
            random_number = np.random.uniform(0.95, 1.1)
            test = X_train_vec[i][-1] * random_number
            test_vec = X_train_vec[i].copy()
            test_vec[-1] = test
            X_train_bsmote.append(test_vec)
            y_train_bsmote.append(True)

        else:
            X_train_bsmote.append(X_train_vec[i])
            y_train_bsmote.append(False)
    return X_train_bsmote, y_train_bsmote
