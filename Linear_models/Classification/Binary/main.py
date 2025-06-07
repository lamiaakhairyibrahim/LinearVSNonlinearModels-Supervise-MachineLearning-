from Linear_models.Classification.Binary.test_code import final
import argparse

def data(path):
    op = final(path)
    
def main():
    parser = argparse.ArgumentParser(description="enter the dataset path.")
    parser.add_argument('path', help="The path to incloude")
    args = parser.parse_args()

    try:
        data(args.path)
    except Exception as e:
        print(f"Error occurred: {e}")

if __name__ == "__main__":
    main()