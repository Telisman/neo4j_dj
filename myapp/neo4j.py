from neo4j import GraphDatabase

uri = "bolt://localhost:7687"
username = "Django_app"
password = "opke1987"

driver = GraphDatabase.driver(uri, auth=(username, password))
