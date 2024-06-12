# app.py
import random
from query_type import query_types
from modules.query_generators import generate_type_1
from modules.query_generators import generate_type_2
from modules.query_generators import generate_type_3
from modules.export_csv import export as export_csv

def main():
    num_pairs = 100
    pairs = []

    for _ in range(num_pairs):
        type = random.choice(query_types)
        #type = 3
        if(type==1): pair = generate_type_1()
        elif(type==2): pair = generate_type_2()
        elif(type==3): pair = generate_type_3()

        pairs.append(pair)
    export_csv(pairs)

if __name__ == "__main__":
    main()
