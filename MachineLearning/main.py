"""
    Main method for running all code 
    
    Author: Eline-Elorm Nuviadenu
"""
from classification import Classification

def main():
    print("Starting classification...")
    classify = Classification()
    print("Loading models...")
    boil_fry_model = classify.load_model("./models/FryBoil_LR.sav")
    safe_unsafe_model = classify.load_model("./models/naive_bayes_modelHanan.sav")
    on_off_model = classify.load_model("./models/svm_model.sav")
    print("Processing data...")
    X_data, dataset = classify.process_data("./dataset/AfterPostFair_Dataset.csv")
    print("Making predictions...")
    classify.label_predictions(X_data, dataset, on_off_model, safe_unsafe_model, boil_fry_model)

if __name__ == '__main__':
    main()
