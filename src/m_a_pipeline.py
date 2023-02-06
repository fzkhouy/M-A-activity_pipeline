""" Transforming pipeline process"""
import json
from config import SLEAK_INTERACTIONS_PATH, SLEAK_PROFILES_PATH, RESULT_PATH
from datetime import datetime


def create_node(profile):
    """
    A function that create nodes based on one profile element
    :param profile: dict
    :return node: dict
    """
    return {
        "type": "node",
        "id": profile["source"]["id"],
        "labels": [profile["name"]],
        "properties": {},
    }


def create_link(interaction):
    """
    A function that create links based on interactions between companies
    :param interaction:
    :return:
    """
    return {
        "id": interaction["source"]["dealId"],
        "type": "relationship",
        "labels": [interaction["status"]],
        "properties": {},
        "start": interaction["subject"],
        "end": interaction["object"],
    }


def companies_interactions(f_profiles, f_interactions):
    """A function that takes two json files
    (companies information and their interactions )
    and returns a json graph model
    create_node and create_links"""
    with open(f_profiles) as profiles:
        sleak_profiles = json.load(profiles)
    with open(f_interactions) as interactions:
        sleak_interactions = json.load(interactions)
    sleak_model_graph = list(map(create_node, sleak_profiles)) + list(
        map(create_link, sleak_interactions)
    )
    # save the file with tracking date
    with open(f"{RESULT_PATH}/sleak_model_{datetime.now()}.json", "w") as final:
        json.dump(sleak_model_graph, final, indent=4)


if __name__ == "__main__":
    companies_interactions(SLEAK_PROFILES_PATH, SLEAK_INTERACTIONS_PATH)
