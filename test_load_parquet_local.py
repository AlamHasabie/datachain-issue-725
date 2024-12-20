from datachain import C, DataChain
import os

PARQUET_PATH = os.path.join("file://", os.getcwd(), "data", "dataset.parquet")
dataset = DataChain.from_parquet(PARQUET_PATH)
dataset.show()