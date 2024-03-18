import os
import httpx
from prefect import flow

@flow
def fetch_cat_fact():
    '''A flow that gets a cat fact'''
    return httpx.get("https://catfact.ninja/fact?max_length=140").json()["fact"]

@flow
def fetch_dog_fact():
    '''A flow that gets a dog fact'''
    return httpx.get(
        "https://dogapi.dog/api/v2/facts",
        headers={"accept": "application/json"},
    ).json()["data"][0]["attributes"]["body"]

@flow(log_prints=True)
def animal_facts():
    current_working_directory = os.getcwd()
    print(current_working_directory)

    l_files = os.listdir(current_working_directory)
    print("Printintg content of current directory")
    # Iterating over all the files
    for file in l_files:
        print (file)
 

    cat_fact = fetch_cat_fact()
    dog_fact = fetch_dog_fact()
    print(f"🐱: {cat_fact} \n🐶  : {dog_fact}")

if __name__ == "__main__":
    animal_facts()