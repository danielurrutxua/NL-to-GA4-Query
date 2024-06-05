# app.py
import random
from query_type import query_types
from modules.query_generators import generate as generate_query_type_1

def main():
    num_pairs = 100
    pairs = []

    for _ in range(num_pairs):
        type = random.choice(query_types)
        type = 1

        if(type==1): pair = generate_query_type_1()
        #elif(type==2): pair = generate_query_type_2()

        pairs.append(pair)
    
    
    print(pairs)


if __name__ == "__main__":
    main()
