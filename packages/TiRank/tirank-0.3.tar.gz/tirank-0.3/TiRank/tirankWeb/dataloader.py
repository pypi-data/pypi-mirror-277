# DataLoader classes
import numpy as np
import pandas as pd
import random, pickle, os
import torch
from torch.utils.data import Dataset, DataLoader


def view_clinical_variables_(save_path):
    # Load data
    f = open(os.path.join(save_path, 'bulk_clinical.pkl'), 'rb')
    bulk_clinical = pickle.load(f)
    f.close()

    print(bulk_clinical.columns)

    return bulk_clinical


def assign_binary_values(df, column_name):
    # transfer into dataframe
    df = pd.DataFrame(df)

    # Ensure the column exists in the DataFrame
    if column_name not in df.columns:
        raise ValueError(f"Column '{column_name}' not found in DataFrame.")

    # Step 1: Identify the unique categories in the specified column
    unique_categories = df[column_name].unique().tolist()

    # Safety check: Ensure there are only two unique categories
    if len(unique_categories) != 2:
        raise ValueError("The column does not contain exactly two unique categories.")

    # Step 2: Assign numerical values to these categories
    category_to_number = {unique_categories[0]: 0, unique_categories[1]: 1}

    # Convert the specified column in the DataFrame based on the detected categories
    df[column_name] = df[column_name].map(category_to_number)

    return df, category_to_number


def choose_clinical_variable_(save_path, bulk_clinical, mode, var_1, var_2=None):
    # selecting mode
    if mode == "Cox":
        time_col = var_1
        status_col = var_2
        bulk_clinical = bulk_clinical.loc[:, [time_col, status_col]]

        if type(bulk_clinical.iloc[1, 0] == type("a")):
            bulk_clinical[var_1] = pd.to_numeric(bulk_clinical[var_1], errors='coerce')

        if type(bulk_clinical.iloc[1, 1] == type("a")):
            bulk_clinical[var_2] = pd.to_numeric(bulk_clinical[var_2], errors='coerce')

    elif mode == "Classification":
        variable_col = var_1
        bulk_clinical = bulk_clinical.loc[:, variable_col]
        converted_df, correspondence = assign_binary_values(bulk_clinical, variable_col)
        print("Correspondence:", correspondence)
        bulk_clinical = converted_df

    elif mode == 'Regression':
        variable_col = var_1
        bulk_clinical = bulk_clinical.loc[:, variable_col]
        if type(bulk_clinical.iloc[1, 0] == type("a")):
            raise (TypeError("Chosen Variable in " + mode + " Mode was not numeric."))

    else:
        raise (TypeError("Unexpected Mode had been selected."))

    with open(os.path.join(save_path, 'bulk_clinical.pkl'), 'wb') as f:
        pickle.dump(bulk_clinical, f)
    f.close()

    return None


# def generate_val_(save_path, validation_proportion=0.15, mode=None):
#     f = open(os.path.join(save_path, 'bulk_exp.pkl'), 'rb')
#     bulkExp = pickle.load(f)
#     f.close()
#
#     f = open(os.path.join(save_path, 'bulk_clinical.pkl'), 'rb')
#     bulkClinical = pickle.load(f)
#     f.close()
#
#     # Load data
#     bulkExp, bulkClinical
#     # Transpose bulkExp so that samples are rows
#     bulkExp_transposed = bulkExp.T
#
#     # Concatenate bulkExp and bulkClinical
#     combined = pd.concat([bulkExp_transposed, bulkClinical], axis=1)
#
#     # Split the combined dataframe
#     random.seed(619)
#     num_val = int(combined.shape[0] * validation_proportion)
#     validx = random.sample(range(combined.shape[0]), num_val)
#
#     combined_val = combined.iloc[validx,]
#     mask = ~combined.index.isin(combined_val.index)
#     combined_train = combined[mask]
#
#     if mode == "Classification":
#         # Separate the training and validation sets back into bulkExp and bulkClinical
#         bulkExp_train = combined_train.iloc[:, :-1].T
#         bulkClinical_train = combined_train.iloc[:, -1]
#
#         bulkExp_val = combined_val.iloc[:, :-1].T
#         bulkClinical_val = combined_val.iloc[:, -1]
#
#     elif mode == "Cox":
#         # Separate the training and validation sets back into bulkExp and bulkClinical
#         bulkExp_train = combined_train.iloc[:, :-2].T
#         bulkClinical_train = combined_train.iloc[:, -2:]
#
#         bulkExp_val = combined_val.iloc[:, :-2].T
#         bulkClinical_val = combined_val.iloc[:, -2:]
#
#         ## save
#     savePath_splitData = os.path.join(save_path, "split_data")
#     if not os.path.exists(savePath_splitData):
#         os.makedirs(savePath_splitData, exist_ok=True)
#
#     with open(os.path.join(savePath_splitData, 'bulkExp_train.pkl'), 'wb') as f:
#         pickle.dump(pd.DataFrame(bulkExp_train), f)  ## training bulk clinical info matrix
#     f.close()
#
#     with open(os.path.join(savePath_splitData, 'bulkExp_val.pkl'), 'wb') as f:
#         pickle.dump(pd.DataFrame(bulkExp_val), f)  ## validating bulk clinical info matrix
#     f.close()
#
#     with open(os.path.join(savePath_splitData, 'bulkClinical_train.pkl'), 'wb') as f:
#         pickle.dump(pd.DataFrame(bulkClinical_train), f)  ## training bulk clinical info matrix
#     f.close()
#
#     with open(os.path.join(savePath_splitData, 'bulkClinical_val.pkl'), 'wb') as f:
#         pickle.dump(pd.DataFrame(bulkClinical_val), f)  ## validating bulk clinical info matrix
#     f.close()
#
#     return None


def generate_val_(save_path, validation_proportion=0.15, mode=None):
    f = open(os.path.join(save_path, 'bulk_exp.pkl'), 'rb')
    bulkExp = pickle.load(f)
    f.close()

    f = open(os.path.join(save_path, 'bulk_clinical.pkl'), 'rb')
    bulkClinical = pickle.load(f)
    f.close()

    # Load data
    bulkExp, bulkClinical
    # Transpose bulkExp so that samples are rows
    bulkExp_transposed = bulkExp.T

    # Concatenate bulkExp and bulkClinical
    combined = pd.concat([bulkExp_transposed, bulkClinical], axis=1)

    # Split the combined dataframe
    random.seed(619)
    num_val = int(combined.shape[0] * validation_proportion)
    validx = random.sample(range(combined.shape[0]), num_val)

    combined_val = combined.iloc[validx,]
    mask = ~combined.index.isin(combined_val.index)
    combined_train = combined[mask]

    if mode == "Classification":
        # if mode == "Bionomial":
        # Separate the training and validation sets back into bulkExp and bulkClinical
        bulkExp_train = combined_train.iloc[:, :-1].T
        bulkClinical_train = combined_train.iloc[:, -1]

        bulkExp_val = combined_val.iloc[:, :-1].T
        bulkClinical_val = combined_val.iloc[:, -1]

    elif mode == "Cox":
        # Separate the training and validation sets back into bulkExp and bulkClinical
        bulkExp_train = combined_train.iloc[:, :-2].T
        bulkClinical_train = combined_train.iloc[:, -2:]

        bulkExp_val = combined_val.iloc[:, :-2].T
        bulkClinical_val = combined_val.iloc[:, -2:]

    elif mode == "Regression":
        # Separate the training and validation sets back into bulkExp and bulkClinical
        bulkExp_train = combined_train.iloc[:, :-1].T
        bulkClinical_train = combined_train.iloc[:, -1]

        bulkExp_val = combined_val.iloc[:, :-1].T
        bulkClinical_val = combined_val.iloc[:, -1]

        ## save
    savePath_splitData = os.path.join(save_path, "split_data")
    if not os.path.exists(savePath_splitData):
        os.makedirs(savePath_splitData, exist_ok=True)

    with open(os.path.join(savePath_splitData, 'bulkExp_train.pkl'), 'wb') as f:
        pickle.dump(pd.DataFrame(bulkExp_train), f)  ## training bulk clinical info matrix
    f.close()

    with open(os.path.join(savePath_splitData, 'bulkExp_val.pkl'), 'wb') as f:
        pickle.dump(pd.DataFrame(bulkExp_val), f)  ## validating bulk clinical info matrix
    f.close()

    with open(os.path.join(savePath_splitData, 'bulkClinical_train.pkl'), 'wb') as f:
        pickle.dump(pd.DataFrame(bulkClinical_train), f)  ## training bulk clinical info matrix
    f.close()

    with open(os.path.join(savePath_splitData, 'bulkClinical_val.pkl'), 'wb') as f:
        pickle.dump(pd.DataFrame(bulkClinical_val), f)  ## validating bulk clinical info matrix
    f.close()

    return None


def transform_test_exp_(train_exp, test_exp):
    # Initialize a new DataFrame to store the transformed test data
    transformed_test_exp = pd.DataFrame(index=test_exp.columns)

    # Iterate over the columns in the train_exp DataFrame
    for column in train_exp.columns:
        # Parse the column name to get the two gene names
        geneA, geneB = column.split('__')

        # Check if both genes are present in the test_exp
        if geneA in test_exp.index and geneB in test_exp.index:
            # Perform the comparison for each sample in test_exp and assign the values to the new DataFrame
            transformed_test_exp[column] = (test_exp.loc[geneA] > test_exp.loc[geneB]).astype(int) * 2 - 1

            # Handle cases where geneA == geneB by assigning 0
            transformed_test_exp.loc[:, column][test_exp.loc[geneA]
                                                == test_exp.loc[geneB]] = 0
        else:
            # If one or both genes are not present, assign 0 for all samples
            transformed_test_exp[column] = 0

    # Transpose the DataFrame to match the structure of train_exp
    # transformed_test_exp = transformed_test_exp.transpose()

    return transformed_test_exp


class BulkDataset(Dataset):
    def __init__(self, df_Xa, df_cli, mode='Cox'):
        self.mode = mode

        if mode == 'Cox':
            self.Xa = torch.tensor(df_Xa.values, dtype=torch.float32)

            # Handle 'Cox' type: df_cli is expected to be a DataFrame with columns ['t', 'e']
            self.t = torch.tensor(df_cli.iloc[:, 0].values, dtype=torch.float32)
            self.e = torch.tensor(df_cli.iloc[:, 1].values, dtype=torch.float32)

        elif mode == 'Classification':
            self.Xa = torch.tensor(df_Xa.values, dtype=torch.float32)

            # Handle 'Classification' type: df_cli is expected to be a Series/1D array with group labels
            self.label = torch.tensor(df_cli.iloc[:, 0].values, dtype=torch.long)

        elif mode == 'Regression':
            self.Xa = torch.tensor(df_Xa.values, dtype=torch.float32)

            # Handle 'Regression' type: df_cli is expected to be a Series/1D array with continuous values
            self.label = torch.tensor(df_cli.iloc[:, 0].values, dtype=torch.float32)

        else:
            raise ValueError(f"Unsupported mode: {self.mode}")

    def __len__(self):
        return len(self.Xa)

    def __getitem__(self, idx):
        if self.mode == 'Cox':
            return self.Xa[idx], self.t[idx], self.e[idx]
        else:
            return self.Xa[idx], self.label[idx]


class STDataset(Dataset):
    def __init__(self, df_Xc):
        self.Xc = torch.tensor(df_Xc.values, dtype=torch.float32)

    def __len__(self):
        return len(self.Xc)

    def __getitem__(self, idx):
        return self.Xc[idx], idx


def pack_data_(save_path, mode, infer_mode, batch_size=1024):
    save_path_split_data = os.path.join(save_path, "split_data")

    f = open(os.path.join(save_path, 'train_bulk_gene_pairs_mat.pkl'), 'rb')
    train_bulk_gene_pairs_mat = pickle.load(f)
    f.close()
    f = open(os.path.join(save_path, 'val_bulkExp_gene_pairs_mat.pkl'), 'rb')
    val_bulkExp_gene_pairs_mat = pickle.load(f)
    f.close()

    f = open(os.path.join(save_path_split_data, 'bulkClinical_train.pkl'), 'rb')
    bulkClinical_train = pickle.load(f)
    f.close()
    f = open(os.path.join(save_path_split_data, 'bulkClinical_val.pkl'), 'rb')
    bulkClinical_val = pickle.load(f)
    f.close()

    f = open(os.path.join(save_path, 'scAnndata.pkl'), 'rb')
    scAnndata = pickle.load(f)
    f.close()
    f = open(os.path.join(save_path, 'sc_gene_pairs_mat.pkl'), 'rb')
    sc_gene_pairs_mat = pickle.load(f)
    f.close()
    f = open(os.path.join(save_path, 'similarity_df.pkl'), 'rb')
    similarity_df = pickle.load(f)
    f.close()

    train_dataset_Bulk = BulkDataset(train_bulk_gene_pairs_mat, bulkClinical_train, mode=mode)
    val_dataset_Bulk = BulkDataset(val_bulkExp_gene_pairs_mat, bulkClinical_val, mode=mode)
    train_loader_Bulk = DataLoader(train_dataset_Bulk, batch_size=batch_size, shuffle=False)
    val_loader_Bulk = DataLoader(val_dataset_Bulk, batch_size=batch_size, shuffle=False)

    if infer_mode == "ST":
        adj_A = torch.from_numpy(similarity_df.values)
        adj_B = None
        patholabels = scAnndata.obs["patho_class"]

        train_dataset_SC = STDataset(sc_gene_pairs_mat)
        train_loader_SC = DataLoader(train_dataset_SC, batch_size=batch_size, shuffle=True)

    elif infer_mode == "SC":
        adj_A = torch.from_numpy(similarity_df.values)
        adj_B = None
        patholabels = None

        train_dataset_SC = STDataset(sc_gene_pairs_mat)
        train_loader_SC = DataLoader(train_dataset_SC, batch_size=batch_size, shuffle=True)

    else:
        raise TypeError("Unexpected infer mode !")

    savePath_data2train = os.path.join(save_path, "data2train")
    if not os.path.exists(savePath_data2train):
        os.makedirs(savePath_data2train, exist_ok=True)

    with open(os.path.join(savePath_data2train, 'train_loader_Bulk.pkl'), 'wb') as f:
        pickle.dump(train_loader_Bulk, f)
    f.close()
    with open(os.path.join(savePath_data2train, 'val_loader_Bulk.pkl'), 'wb') as f:
        pickle.dump(val_loader_Bulk, f)
    f.close()
    with open(os.path.join(savePath_data2train, 'train_loader_SC.pkl'), 'wb') as f:
        pickle.dump(train_loader_SC, f)
    f.close()

    with open(os.path.join(savePath_data2train, 'adj_A.pkl'), 'wb') as f:
        pickle.dump(adj_A, f)
    f.close()
    with open(os.path.join(savePath_data2train, 'adj_B.pkl'), 'wb') as f:
        pickle.dump(adj_B, f)
    f.close()
    with open(os.path.join(savePath_data2train, 'patholabels.pkl'), 'wb') as f:
        pickle.dump(patholabels, f)
    f.close()

    return None


def transform_test_exp(train_exp, test_exp):
    # Initialize a new DataFrame to store the transformed test data
    transformed_test_exp = pd.DataFrame(index=test_exp.columns)

    # Iterate over the columns in the train_exp DataFrame
    for column in train_exp.columns:
        # Parse the column name to get the two gene names
        geneA, geneB = column.split('__')

        # Check if both genes are present in the test_exp
        if geneA in test_exp.index and geneB in test_exp.index:
            # Perform the comparison for each sample in test_exp and assign the values to the new DataFrame
            transformed_test_exp[column] = (test_exp.loc[geneA] > test_exp.loc[geneB]).astype(int) * 2 - 1

            # Handle cases where geneA == geneB by assigning 0
            transformed_test_exp.loc[:, column][test_exp.loc[geneA]
                                                == test_exp.loc[geneB]] = 0
        else:
            # If one or both genes are not present, assign 0 for all samples
            transformed_test_exp[column] = 0

    # Transpose the DataFrame to match the structure of train_exp
    # transformed_test_exp = transformed_test_exp.transpose()

    return transformed_test_exp
