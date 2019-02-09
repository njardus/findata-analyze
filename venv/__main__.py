import os
import pandas as pd
from loguru import logger

debugging = True
logging = True

source_data_path = "..\\data\\"
write_data_path = "..\\analysed\\"

def init():
    logger.info("Initializing.")

def getlistofgiles(folder):
    directories = os.listdir(folder)

if __name__ == "__main__":
    logger.info("Main function started.")

    init()

    logger.info("Step 1: Get a list of files in the folder.")

    filenames = getlistofgiles(data_path)

    if debugging:
        logger.debug(f"{filenames}")

    logger.info("Step 2: Iterate through the files")

    for csvfile in filenames:
        logger.info("Step 1a: Open the file in read only mode")
        if debugging:
            logger.debug(f"Filename: {csvfile}")
        original_data = pd.read_csv(source_data_path + csvfile)

        if debugging:
            logger.debug(original_data["Date"])
            logger.debug(original_data["Open"])
            logger.debug(original_data["High"])
            logger.debug(original_data["Low"])
            logger.debug(original_data["Close"])
            logger.debug(original_data["Volume"])









        newfilename =  write_data_path + "analysis-" + csvfile
        if debugging:
            logger.debug(f"Save the results to {newfilename}")
        new_data.to_csv(newfilename, encoding='utf-8')