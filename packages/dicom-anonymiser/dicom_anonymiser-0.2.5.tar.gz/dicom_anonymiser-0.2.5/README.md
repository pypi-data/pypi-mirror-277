# DICOM Anonymisation Tool

This tool is designed to either:

1. Anonymise a single DICOM file, or
2. Anonymise a directory (recursively) of DICOM files

Anonymised files may be saved to a different directory, and may be renamed with `_anon` suffix.

The script has a default list of tags to anonymise, but the user may point to a custom list.

```
usage: main.py [-h] [-t TAGFILE] [-i] source destination

Anonymise DICOM images

positional arguments:
  source                location of dicom file or folder to anonymise
  destination           Destination folder to save anonymised images

optional arguments:
  -h, --help            show this help message and exit
  -t TAGFILE, --tagfile TAGFILE
                        path to custom tags file
  -i, --intact          Leave filenames unchanged
```


## Installation

1. Install python3.8+
2. Create a virtual env where you want to install:

    ```
    $> python3 -m venv dicom_anon
    ```

3. Activate the environment

    ```
    $> source dicom_anon/bin/activate
    ```

4. Install the package with pip

     ```
    $> pip install dcm_anon
     ```

5. Having the environment activated, run from the terminal with the help flag to show the above usage info

     ```
     $> anonymise --help
     ```

6. Each anonymisation run will generate a log file placed in the environment's package directory:

     ```
     dicom_anon/lib/python3.x/site-packages/dicom_anonymiser/logs/
     ```
     
7. Default location of tags file
     
     ```
     dicom_anonymiser/lib/python3.x/site-packages/dcm_anon/tags/
     ```    

8. If you want to use your own tags, you can specify them in

     ```
     dicom_anonymiser/lib/python3.x/site-packages/dcm_anon/tags/user_tags.csv
     ```  

## Usage

1. Always activate the environment

   ```
   $> source dicom_anon/bin/activate
   ```

2. Single file

   ```
   anonymise "/Users/me/dcm/original/a_file.dcm" "/Users/me/Desktop/anonymised/"
   ```
   
3. Folder

   ```
   anonymise "/Users/me/dcm/original/" "/Users/me/Desktop/anonymised/"
   ```

4. Using a custom list of tags

   ```
   anonymise "/Users/me/dcm/original/" "/Users/me/Desktop/anonymised/" -t "/path/to/user_tags.csv"
   ```

5. Keep same filenames (will overwrite if destination directory is same as source)

   ```
   anonymise "/Users/me/dcm/original/" "/Users/me/Desktop/anonymised/" -i
   ```
