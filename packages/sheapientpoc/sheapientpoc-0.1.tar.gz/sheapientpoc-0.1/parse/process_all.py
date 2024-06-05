import os
import json
import time
import argparse
from datetime import datetime
from tqdm import tqdm

from kph.src.config.config import config
from kph.src.parse.summarize import summarize_case_study


def process_all(
    input_path, summaries_path, error_path, redo_or_continue, model_name="gpt-4"
):

    docs_not_processed = []

    # Initialize or continue from the existing setup
    if redo_or_continue == "REDO":
        if os.path.exists(summaries_path):
            # Archive the existing output path with a timestamp
            timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
            archived_path = f"{summaries_path}-archived-{timestamp}"
            os.rename(summaries_path, archived_path)
            print(f"Renamed existing {summaries_path} to {archived_path}")

        # Create new directories
        os.makedirs(summaries_path, exist_ok=True)
        os.makedirs(error_path, exist_ok=True)

    elif redo_or_continue == "CONTINUE":
        print(f"Continuing from {summaries_path}...")
        os.makedirs(error_path, exist_ok=True)
        if not os.path.exists(summaries_path):
            os.makedirs(summaries_path, exist_ok=True)

    # Prepare the file list, excluding already processed files if continuing
    file_list = sorted(
        [
            filename
            for filename in os.listdir(input_path)
            if filename.endswith((".pdf", ".pptx"))
        ]
    )
    if redo_or_continue == "CONTINUE":
        existing_summaries = set(os.listdir(summaries_path))
        file_list = [
            filename
            for filename in file_list
            if f"{filename}.json" not in existing_summaries
        ]

        print(f"Files already processed: {len(existing_summaries)}")
        print(f"Files remaining to process: {len(file_list)}")

    total_files = len(file_list)

    # Process files with a progress bar
    with tqdm(total=total_files, desc="Processing Files") as pbar:
        for filename in file_list:
            full_path = os.path.join(input_path, filename)
            pbar.set_description(f"Processing {filename}...")

            retries = 5
            success = False
            for attempt in range(retries):
                try:
                    doc, response = summarize_case_study(
                        filename=full_path, model_name=model_name
                    )
                    if doc:
                        with open(
                            os.path.join(summaries_path, filename + ".json"), "w"
                        ) as f:
                            json.dump(doc, f, indent=6)
                        success = True
                        pbar.update(1)
                        break
                except Exception as e:
                    print(f"Error processing {full_path}: {e}")
                    if attempt < retries - 1:
                        delay = (attempt + 1) * 5  # Incremental delay
                        print(
                            f"Retrying {full_path} after {delay} seconds (Attempt {attempt + 1}/{retries})..."
                        )
                        time.sleep(delay)

            if not success:
                print(f"Failed to process {full_path} after {retries} attempts.")
                docs_not_processed.append(full_path)

    print(f"Processed {total_files - len(docs_not_processed)} files successfully.")

    # Save the list of unprocessed documents
    with open(os.path.join(error_path, "docs_not_processed.txt"), "w") as error_file:
        error_file.write("\n".join(docs_not_processed))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Process documents for case studies")
    parser.add_argument(
        "--input_path",
        default=config.paths.input_path,
        help="Directory containing the documents to process",
    )
    parser.add_argument(
        "--summaries_path",
        default=config.paths.summaries_path,
        help="Directory where processed documents will be saved",
    )
    parser.add_argument(
        "--error_path",
        default=config.paths.error_path,
        help="Directory where errors will be logged",
    )
    parser.add_argument(
        "--redo_or_continue",
        choices=["REDO", "CONTINUE"],
        default=config.process_all_behavior.redo_or_continue,
        help="Specify 'REDO' to start over or 'CONTINUE' to keep existing files",
    )
    parser.add_argument(
        "--model_name",
        choices=[
            "gpt-4",
            "mixtral-8x7b-32768",
            "gpt-4-turbo",
            "gpt-4-0125-preview",
            "gpt-35-turbo-16k",
            "meta-llama/Meta-Llama-3-70B-Instruct",
            "mistralai/Mixtral-8x22B-Instruct-v0.1",
        ],
        default=config.llm_models.summarization_model,
        help="Specify the model to use for summarization",
    )

    args = parser.parse_args()

    process_all(
        args.input_path,
        args.summaries_path,
        args.error_path,
        args.redo_or_continue.upper(),
        args.model_name,
    )
