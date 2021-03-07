# Data finder

## Simple Set of Apis to extract data from source, 

    current version does the following:
  
      - Read text file from the disk
      - Extract all the urls from the file
      - writes the extracted urls to a file
      
## Needs:

python 3(onwards)
      
## Usage:

```python driver.py```

## Test cases:

```python -m unittest discover```

## Open points:

  1. Currently dumping the results to file on disk (could be problmetic if data is huge)
  2. Could have refactored extract data part to make it dynamic based on user requirement (currently holding regex match for fetching urls)
  3. Could not test with GBs of text file , may be needed better testing approach
