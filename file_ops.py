import pandas as pd


def write_to_txt(fileName, linesAsArray):
    file = open(fileName, mode="w")
    for line in linesAsArray:
        if [] != line:
            value = line[1]
            if 'No Such Object currently exists at this OID' == value or 'No Such Instance currently exists at this OID' == value:
                pass
            else:
                file.write(str(line)+'\n')

def read_from_csv(fileName: str):
    reader = pd.read_csv(f"{fileName}")
    reader = reader.values.tolist()
    listed = pd.Series(reader)
    return listed.values
