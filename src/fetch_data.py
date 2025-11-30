import argparse
import os
import kagglehub
from kagglehub import KaggleDatasetAdapter


def fetch_data(dataset: str, out_dir: str, file_name: str) -> None:
    os.makedirs(out_dir, exist_ok=True)
    print(f"\nDownloading dataset '{dataset}' via KaggleHub...")

    # Use the new API: dataset_load
    df = kagglehub.dataset_load(
        KaggleDatasetAdapter.PANDAS,
        dataset,
        file_name,
    )

    print(f"✅ Dataset downloaded. Shape: {df.shape}")

    # Build output path with safe base name
    base_name, _ = os.path.splitext(file_name)
    out_path = os.path.join(out_dir, f"{base_name}.csv")

    df.to_csv(out_path, index=False)
    print(f"💾 Saved raw data to {out_path}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--out-dir", default="data/raw")
    args = parser.parse_args()

    dataset_name1 = "gvidalguiresse/playstation-sales-and-metadata-ps3ps4ps5"
    file1 = "PlayStation Sales and Metadata (PS3PS4PS5) (Oct 2025).csv"
    fetch_data(dataset_name1, out_dir=args.out_dir, file_name=file1)

    dataset_name2 = "jahnavipaliwal/video-game-reviews-and-ratings"
    file2 = "video_game_reviews.csv"
    fetch_data(dataset_name2, out_dir=args.out_dir, file_name=file2)
