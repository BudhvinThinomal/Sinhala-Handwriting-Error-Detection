import pandas as pd
import numpy as np
import joblib


def risk_detection(input_data):
    # Load the model from the h5 file
    load_model = joblib.load(
        r"E:\Study materials\IIT\4th year\FYP\Codes\sinhala_handwriting_error_detection-main\weigths\MLP_model.h5"
    )

    # Create sample input data (should have the same number of features as the model was trained on)
    title_columns = np.array(
        [
            "Q_1.1",
            "Q_1.2",
            "Q_1.3",
            "Q_2.1",
            "Q_2.2",
            "Q_2.3",
            "Q_3.1",
            "Q_3.2",
            "Q_3.3",
            "Q_4.1",
            "Q_4.2",
            "Q_4.3",
            "Q_5.1",
            "Q_5.2",
            "Q_5.3",
            "Q_6.1",
            "Q_6.2",
            "Q_6.3",
            "Q_7.1",
            "Q_7.2",
            "Q_7.3",
            "Q_8",
            "Q_8_Severity_Level",
            "Q_9",
            "Q_9_Severity_Level",
            "Q_10.1",
            "Q_10.2",
            "Q_10.3",
            "Q_11",
            "Q_12",
            "Q_13",
            "Q_14.1",
            "Q_14.2",
            "Q_14.3",
            "Q_15.1",
            "Q_15.2",
            "Q_15.3",
            "Q_16",
            "Q_16_Severity_Level",
            "Q_17.1",
            "Q_17.2",
            "Q_17.3",
            "Q_18",
            "Q_19",
            "Q_20",
            "Q_P_1",
            "Q_P_2",
            "Q_P_3",
            "Q_P_4.1",
            "Q_P_4.2",
            "Q_P_4.3",
            "Q_P_4.4",
            "Q_P_5.1.1",
            "Q_P_5.1.2",
            "Q_P_5.1.3",
            "Q_P_5.1.4",
        ]
    )

    # input_data = np.array([[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0]])
    # input_data = np.array([[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 0, 0, 0, 1]])

    # {
    #  "data": [[0, 0, 1, 0, 0, 1,  0, 0, 1,  0, 0, 1, 0, 0, 1,  0, 0, 1, 0, 0, 1, 0, 2, 0, 2, 0, 0, 0, 0, 0, 1,  0, 0, 0,  0, 1, 0,  0, 2, 0, 0, 1,  0, 0, 1, 1, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0]]
    # }

    input_data_dataset_frame = pd.DataFrame(input_data, columns=title_columns)

    # Predict output for input data
    output = load_model.predict(input_data_dataset_frame)
    # print("Name", output)
    return output
