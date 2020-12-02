from Preprocessing import data_preprocessing
from Logistic_Regression_with_equations import LogisticRegression
import numpy as np
from pathlib import Path
from mail_reciever import get_mails
from argparse import ArgumentParser


def spam_detecting(args):
    weight_dir, last, csv = args.weight_dir, args.last, args.csv
    # Initialize model
    logistic_regression = LogisticRegression()
    # Check the file if exists
    if Path(weight_dir).exists():
        print("Loading the model...")
        weights = np.load(weight_dir, allow_pickle=True)
        # load weights
        logistic_regression.theta_1, logistic_regression.theta_2 = weights[0], weights[1]
        logistic_regression.input_shape = weights[2]
    else:
        x, y = data_preprocessing(csv)
        # Training the model (learning rate can be decreased and iteration_num can be increased to improve accuracy)
        print("Training the model..")
        logistic_regression.fit(x, y, learning_rate=5, iteration_num=200)
        # Prediction
        output_predicted = logistic_regression.prediction(x)
        # Calculate accuracy
        accuracy = logistic_regression.accuracy(output_predicted, y)
        print(f"Logistic Regression accuracy: {accuracy:.4f}")
        print("Saving the model...")
        params = [logistic_regression.theta_1, logistic_regression.theta_2, x.shape[1]]
        np.save("weights/model.npy", params, allow_pickle=True)
    # Get mails
    mails = np.array((get_mails(last_num=last)))
    predictions = logistic_regression.prediction(mails)
    for mail, prediction in zip(mails, predictions):
        # For each prediction print mail and prediction
        pred = "SPAM!" if prediction is 0 else "NOT SPAM"
        print("\n", mail,"is ", pred)


if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("--last", type=int, default=5, help="How much mail will be iterated from last")
    parser.add_argument("--weight_dir", type=str, default="weights/model.npy", help="Model weight file")
    parser.add_argument("--csv", type=str, default="data/spam.csv", help="Training Data")
    args = parser.parse_args()
    print(args)

    spam_detecting(args)
