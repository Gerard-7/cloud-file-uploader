from pathlib import Path
import json
import csv

def load_config():
    with open("config.json", "r", encoding="utf-8") as f:
        return json.load(f)

def list_files(source_folder, allowed_extensions):
    files = []
    source_path = Path(source_folder)

    if not source_path.exists():
        print("Source folder not found.")
        return files

    for file in source_path.rglob("*"):
        if file.is_file():
            if not allowed_extensions or file.suffix.lower() in allowed_extensions:
                files.append(file)

    return files

def generate_manifest(files, source_folder, bucket, prefix, output_folder):
    output_path = Path(output_folder)
    output_path.mkdir(exist_ok=True)

    manifest_file = output_path / "upload_manifest.csv"

    with open(manifest_file, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["local_path", "bucket", "s3_key"])

        for file in files:
            relative_path = file.relative_to(source_folder).as_posix()
            s3_key = f"{prefix}{relative_path}"
            writer.writerow([file.as_posix(), bucket, s3_key])

    return manifest_file

def main():
    config = load_config()

    source_folder = config["source_folder"]
    output_folder = config["output_folder"]
    bucket = config["bucket_name"]
    prefix = config["prefix"]
    allowed_extensions = config["allowed_extensions"]

    print("Scanning files...")
    files = list_files(source_folder, allowed_extensions)

    print(f"Found {len(files)} files.")

    if files:
        manifest = generate_manifest(
            files,
            Path(source_fol_
