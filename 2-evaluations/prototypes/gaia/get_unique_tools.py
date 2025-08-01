# Sample of metadata
# {'Steps': '1. Go to arxiv.org and navigate to the Advanced Search page.\n2. Enter "AI regulation" in the search box and select "All fields" from the dropdown.\n3. Enter 2022-06-01 and 2022-07-01 into the date inputs, select "Submission date (original)", and submit the search.\n4. Go through the search results to find the article that has a figure with three axes and labels on each end of the axes, titled "Fairness in Agreement With European Values: An Interdisciplinary Perspective on AI Regulation".\n5. Note the six words used as labels: deontological, egalitarian, localized, standardized, utilitarian, and consequential.\n6. Go back to arxiv.org\n7. Find "Physics and Society" and go to the page for the "Physics and Society" category.\n8. Note that the tag for this category is "physics.soc-ph".\n9. Go to the Advanced Search page.\n10. Enter "physics.soc-ph" in the search box and select "All fields" from the dropdown.\n11. Enter 2016-08-11 and 2016-08-12 into the date inputs, select "Submission date (original)", and submit the search.\n12. Search for instances of the six words in the results to find the paper titled "Phase transition from egalitarian to hierarchical societies driven by competition between cognitive and social constraints", indicating that "egalitarian" is the correct answer.', 'Number of steps': '12', 'How long did this take?': '8 minutes', 'Tools': '1. Web browser\n2. Image recognition tools (to identify and parse a figure with three axes)', 'Number of tools': '2'}

# Import libraries
import ast
import pandas as pd

# Load the csv file
eval = pd.read_csv("gaia_val.csv")

# Create a tool dict
unique_tools = {}

# Loop through rows
for index, row in eval.iterrows():

    metadata = row["Annotator Metadata"]

    metadata_dict = ast.literal_eval(metadata)

    # Extract the tools
    tools = metadata_dict["Tools"]

    # Split the tools
    tools_list = tools.split("\n")

    # Remove any bullet numbers (e.g. "1. ", "2. "
    tools_list = [tool.split(". ", 1)[-1] for tool in tools_list]

    # Trim whitespace
    tools_list = [tool.strip() for tool in tools_list]

    # Lowercase the tools
    tools_list = [tool.lower() for tool in tools_list]

    # Clean up the tool names
    for i in range(len(tools_list)):
        tools_list[i] = tools_list[i].replace("a ", "")
        tools_list[i] = tools_list[i].replace(".", "")
        tools_list[i] = tools_list[i].replace("access to ", "")
        tools_list[i] = tools_list[i].replace("(optional) ", "")
        tools_list[i] = tools_list[i].replace("no tools required", "none")
        tools_list[i] = tools_list[i].replace("google search", "search engine")
        if tools_list[i].startswith("audio"):
            tools_list[i] = "audio"
        if tools_list[i].startswith("calculator"):
            tools_list[i] = "calculator"
        if tools_list[i].startswith("computer vision"):
            tools_list[i] = "computer vision"
        if tools_list[i].startswith("excel"):
            tools_list[i] = "spreadsheet"
        if tools_list[i].startswith("file"):
            tools_list[i] = "file system"
        if tools_list[i].startswith("google sheets"):
            tools_list[i] = "spreadsheet"
        if tools_list[i].startswith("image"):
            tools_list[i] = "image recognition"
        if tools_list[i].startswith("microsoft excel"):
            tools_list[i] = "spreadsheet"
        if tools_list[i].startswith("pdf"):
            tools_list[i] = "pdf viewer"
        if tools_list[i].startswith("python"):
            tools_list[i] = "python"
        if tools_list[i].startswith("speech-to-text"):
            tools_list[i] = "speech-to-text"
        if tools_list[i].startswith("video"):
            tools_list[i] = "video"
        if tools_list[i].startswith("youtube"):
            tools_list[i] = "youtube"

    # Add to the unique tools list
    for tool in tools_list:
        if tool not in unique_tools:
            unique_tools[tool] = 1
        else:
            unique_tools[tool] += 1

# Convert to table [Tool, Count]
unique_tools = pd.DataFrame(
    list(unique_tools.items()),
    columns=['Tool', 'Count'])

# Sort the tools by name
unique_tools = unique_tools \
    .sort_values(by='Count', ascending=False) \
    .reset_index(drop=True)

# Print the unique tools
for index, row in unique_tools.iterrows():
    print(f"{row['Tool']}: {row['Count']}")

# Save the unique tools to a CSV file
unique_tools.to_csv(
    "tool-counts.csv",
    index=False,
    encoding="utf-8")
