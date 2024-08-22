import os
import shutil
import zipfile


class reg:

    def replace(
            file:str, 
            extract:str
        ) -> None:
        try:
            shutil.move(file, extract)
        except Exception as e:
            return e
        
    def write(path:str):...
    @staticmethod
    def zip(
            path:str, 
            extract:str,
            all:bool=False
        ) -> None:
        """
        zip file.
        :param path: path to zip
        :param extract: path to extract
        :return: None
        """
        if not os.path.exists(path):
            return FileNotFoundError("File not found")
        elif not os.path.exists(extract):
            os.makedirs(extract)
        elif zipfile.is_zipfile(path):
            return ValueError("File already zipped")
        try:
            with zipfile.ZipFile(path, 'w') as zipObj:
                zipObj.write(extract)
        except Exception as e:
            return e
        
    @staticmethod
    def unzip(path:str, extract:str) -> None:
        """
        unzip file.
        :param path: path to zip
        :param extract: path to extract
        :return: None
        """
        if not os.path.exists(path):
            return FileNotFoundError("File not found")
        elif not os.path.exists(extract):
            os.makedirs(extract)
        elif zipfile.is_zipfile(path):
            return ValueError("File already zipped")
        try:
            with zipfile.ZipFile(path, 'w') as zipObj:
                zipObj.extractall(extract)
        except Exception as e:
            return e

    
