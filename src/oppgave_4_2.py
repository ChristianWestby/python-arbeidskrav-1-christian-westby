import os
import shutil

def sorter_filer():
    src_dir = "Files"
    dst_dir = "SortedFiles"
    under = {
        ".txt": "txt-files",
        ".csv": "csv-files",
        ".log": "log-files",
    }

    if not os.path.exists(src_dir):
        print("Mappen 'Files' finnes ikke. Kjør oppgave 4.1 først.")
        return

    os.makedirs(dst_dir, exist_ok=True)
    for m in under.values():
        os.makedirs(os.path.join(dst_dir, m), exist_ok=True)

    flyttet = 0
    for navn in os.listdir(src_dir):
        kilde = os.path.join(src_dir, navn)
        if not os.path.isfile(kilde):
            continue  # hopper over mapper

        _, ext = os.path.splitext(navn)
        ext = ext.lower()

        if ext in under:
            målmappe = os.path.join(dst_dir, under[ext])
            dest = os.path.join(målmappe, navn)
            print(f"Flytter {navn} til {målmappe}")
            shutil.move(kilde, dest)
            flyttet += 1

    print(f"Ferdig! Flyttet {flyttet} filer til '{dst_dir}'.")
    for ext, mappenavn in under.items():
        ant = len(os.listdir(os.path.join(dst_dir, mappenavn)))
        print(f" - {mappenavn}: {ant} filer")

if __name__ == "__main__":
    sorter_filer()