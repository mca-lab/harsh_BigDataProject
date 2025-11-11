import argparse
import os
import kagglehub
from kagglehub import KaggleDatasetAdapter

def fetch_data(dataset: str, out_dir: str, file_name: str = ""):
    os.makedirs(out_dir, exist_ok=True)
    print(f"Downloading dataset '{dataset}' via KaggleHub...")

    # Load dataset as pandas DataFrame
    df = kagglehub.load_dataset(
        KaggleDatasetAdapter.PANDAS,
        dataset,
        file_name
    )

    print(f"✅ Dataset downloaded. Shape: {df.shape}")

    # Save as Parquet
    out_path = os.path.join(out_dir, f"{file_name[:len(file_name)-4]}.parquet")
    df.to_parquet(out_path, index=False, engine="pyarrow")

    print(f"💾 Saved raw data to {out_path}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--out-dir", default="../data/raw")
    args = parser.parse_args()

    dataset_name1 = "gvidalguiresse/playstation-sales-and-metadata-ps3ps4ps5"
    file1="PlayStation Sales and Metadata (PS3PS4PS5) (Oct 2025).csv"
    fetch_data(dataset_name1, out_dir=args.out_dir,file_name=file1)
    dataset_name2= "gregorut/videogamesales"
    file2="vgsales.csv"
    fetch_data(dataset_name2,out_dir=args.out_dir,file_name=file2)