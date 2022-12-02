"""provides path joining functions annd module joining"""
import os
import sys

INPUT_FILE="inputtest"

def main():
  """Main Function called on Startup"""
  input_text= open(os.path.join(sys.path[0], INPUT_FILE),'r', encoding="UTF-8")
  lines = input_text.readlines()

if __name__ == "__main__":
  main()