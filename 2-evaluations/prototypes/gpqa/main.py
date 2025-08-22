import pandas as pd

# data = pd.read_csv("gpqa_main.csv")
data = pd.read_csv("gpqa_diamond.csv")
# data = pd.read_csv("gpqa_extended.csv")

print(f"Questions: {len(data)}")
print()

# Count the number of domains
domains = data["High-level domain"].unique()
print(f"Domains: {len(domains)}")
print()

# Count the number of questions in each domain
domain_counts = data["High-level domain"].value_counts()
print("Questions per domain:")
print(domain_counts)
print()


# Count the unique subdomains in diamond
subdomains = data["Subdomain"].unique()
print(f"Subdomains: {len(subdomains)}")
print()

# Count the number of questions in each subdomain
subdomain_counts = data["Subdomain"].value_counts()
print("Questions per subdomain:")
print(subdomain_counts)
print()

# Count the difficulty levels in diamond
difficulty_counts = data["Writer\'s Difficulty Estimate"].value_counts()
print("Difficulty levels:")
print(difficulty_counts)
print()

