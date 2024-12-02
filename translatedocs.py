import os


def execute_trans(file: str):
    print(f"translate {file}")
    os.system(
        f"trans -i docs/ru/{file} -o docs/en/{file} -no-auto  -show-original N	-show-original-phonetics N	-show-prompt-message N	-show-languages N  -show-dictionary N -show-alternatives N -show-original-dictionary N -j -no-ansi	-no-bidi -no-theme -brief"
    )
    print("end")


files = ["index.md", "projectdesign.md"]

for file in files:
    execute_trans(file)
