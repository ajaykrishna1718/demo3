#run the file to generate a csv file.
import tabula
import pandas as pd


pdf_path = "bank_statement.pdf"    
#the value of pdf_path must the location of the pdf file from which you want to extract the tables



tables = tabula.read_pdf(pdf_path, pages='all', multiple_tables=True)
    
# Ensure all tables have the same column names as the first table
if tables:
    first_table_columns = tables[0].columns
    num_columns = len(first_table_columns)

    for table in tables:
        if len(table.columns) < num_columns:
            # Add missing columns with NaN values
            for _ in range(num_columns - len(table.columns)):
                table[f'Unnamed: {len(table.columns)}'] = pd.NA
        elif len(table.columns) > num_columns:
            # Trim extra columns
            table = table.iloc[:, :num_columns]

        table.columns = first_table_columns

    # Combine all tables into a single DataFrame
    combined_tables = pd.concat(tables, ignore_index=True)

    # Save the combined tables as a single CSV file
    combined_csv_file = "combined_tables.csv"
    combined_tables.to_csv(combined_csv_file, index=False)
    print(f"All tables saved as {combined_csv_file}")
else:
    print("No tables found in the PDF.")