from datachain import DataChain
import os

LOCAL_DATASET_URI = os.path.join("file://", os.getcwd(), "sample_dataset/")
PARQUET_PATH = os.path.join("file://", os.getcwd(), "data", "dataset.parquet")
dataset_chain = DataChain.from_storage(
    LOCAL_DATASET_URI,
    update=True
)

dataset_chain.to_parquet(PARQUET_PATH)