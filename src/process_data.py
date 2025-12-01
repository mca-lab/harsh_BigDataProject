from pyspark.sql import SparkSession
from pyspark.sql.functions import col
from pyspark.ml.feature import Imputer
import os
import shutil
import glob


def get_numeric_columns(df):
    numeric_types = {"int", "bigint", "double", "float", "long", "short"}
    return [name for name, dtype in df.dtypes if dtype in numeric_types]


def fill_missing_with_mean(df):
    numeric_cols = get_numeric_columns(df)

    if not numeric_cols:
        return df

    imputer = (
        Imputer()
        .setInputCols(numeric_cols)
        .setOutputCols(numeric_cols)
        .setStrategy("mean")
    )

    return imputer.fit(df).transform(df)


def convert_float_to_int(df):
    for col_name, col_type in df.dtypes:
        if col_type in ("double", "float"):
            df = df.withColumn(col_name, col(col_name).cast("int"))
    return df


def save_single_csv(df, output_path):
    tmp_dir = output_path + "_temp"

    # ensure temp folder is clean
    if os.path.exists(tmp_dir):
        shutil.rmtree(tmp_dir)

    # write single CSV file
    df.coalesce(1).write.mode("overwrite").option("header", True).csv(tmp_dir)

    # find the generated CSV file
    part_file = glob.glob(os.path.join(tmp_dir, "part-*.csv"))[0]

    # remove old output file if exists
    if os.path.exists(output_path):
        os.remove(output_path)

    # move and rename
    shutil.move(part_file, output_path)

    # clean temp folder
    shutil.rmtree(tmp_dir)


def clean_csv(spark, input_path):
    df = (
        spark.read
        .option("header", True)
        .option("inferSchema", True)
        .csv(input_path)
    )

    df = fill_missing_with_mean(df)
    df = convert_float_to_int(df)

    # extract filename
    base = os.path.basename(input_path)          # example: file.csv
    name_no_ext = os.path.splitext(base)[0]      # example: file

    output_path = f"data/processed/{name_no_ext}.csv"

    save_single_csv(df, output_path)

    print(f"✔ Saved processed CSV file to: {output_path}")


def main():
    spark = (
        SparkSession.builder
        .appName("CleanDataMeanInt")
        .getOrCreate()
    )

    clean_csv(spark, "data/raw/PlayStation Sales and Metadata (PS3PS4PS5) (Oct 2025).csv")
    clean_csv(spark, "data/raw/video_game_reviews.csv")

    spark.stop()


if __name__ == "__main__":
    main()
