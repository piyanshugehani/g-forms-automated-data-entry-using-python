import pandas as pd
df = pd.read_excel('data2.xlsx')

# Drop the 'NUMBER' column
df = df.drop('NUMBER', axis=1)

# Split 'Name' column into 'First Name' and 'Last Name' columns
split_names = df['Name'].str.split(expand=True)

if len(split_names.columns) == 2:
    df[['First Name', 'Last Name']] = split_names
else:
    df['First Name'] = split_names[0]
    df['Last Name'] = None

#categorize into females
female_df = df[df['First Name'].str.contains(r'a$|i$|y$|A$|I$|Y$')]
females=female_df['Name'].tolist()
#remaining are males
male_df = df.drop(female_df.index)
males=male_df['Name'].tolist()
