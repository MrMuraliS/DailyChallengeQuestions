import sys
import argparse

print(sys.argv)

parser = argparse.ArgumentParser()
parser.add_argument("--experiment_name", required=True, help="Name of the experiment")
parser.add_argument("--name", required=False, help="Name of the person")
parser.add_argument("--age", required=False, help="Age of the person")
# parser.add_argument('--age', required=True, help='Age of the person')
args = parser.parse_args()

experiment_name = args.experiment_name
age = args.age
name = args.name
# Your code here
print("Running experiment:", experiment_name)
print("Age:", age)

print(type(age), type(experiment_name), type(name))
