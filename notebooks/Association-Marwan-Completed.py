import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns



#-------------------------------------IMPORTING DATA--------------------------------------------


df_raw = pd.read_excel("data/online_retail.xlsx")   # reading the excel file and storing it into a dataframe 

print("Dataset shape (rows, columns):", df_raw.shape)   # verifying throigh displaying the number of rows and columns 

df_raw.head()   # verifying by displayinng the first 5 rows of the dataframe

print("Missing values per column:\n", df_raw.isnull().sum())    # summing the total number of of missing data in each column


print("\nExact duplicate rows:", df_raw.duplicated().sum())     # summing the total number of exact duplicated rows


print("Non-positive quantities:", (df_raw['Quantity'] <= 0).sum())   # summing total number of non-positive attributes


print("Cancelled invoices:", df_raw['InvoiceNo'].astype(str).str.startswith('C').sum())   

# cancelled invoices start with c so we check them to delete them by cheacking if the invoiceno contains "C" or not.

# we do all this to find a benchmark to compare our results to through out the process


#-------------------------------------PROCESSING DATA--------------------------------------------


df = df_raw.copy()  # here we copy our dataframe into a dummy dataframe so we can start processing it



df['InvoiceNo'] = df['InvoiceNo'].astype(str).str.strip()   
# forces all the invoice numbers to be strings and the strip() removes any spaces in the cell

df = df[~df['InvoiceNo'].str.startswith('C')]
# the tilda operator here works as a NOT operator so that we can select all the invoice numbers that DO NOT start with 'C'



df = df[df['Quantity'] > 0]
# this only keeps the positive value in quantities



df = df.dropna(subset=['Description'])
# here the dropna() operation removes all the rows containing missing descriptions
# and we use subset="..." so that we limit it to only checking Description and not deleting any row containgin na in any cell

df['Description'] = df['Description'].astype(str).str.strip()
# and here we use the same strip() to remove extra spaces



df = df.drop_duplicates()
# here we simply remove any exact duplicates



df = df[df['Description'] != 'POSTAGE']
# removes rows that contain PSOTAGE in the description becuase these aren't real products  


print(f"Rows before cleaning: {len(df_raw)}")
print(f"Rows after cleaning:  {len(df)}")
print(f"Total rows removed:   {len(df_raw) - len(df)}")



df['Country'].value_counts()
# I then ran this commmand to check the number of occuring countries and choose one for size control

df_germany = df[df['Country'] == 'Germany']
# then ran this command to choose the country germany only since its the second biggest yet still small 


basket = df_germany.groupby(['InvoiceNo', 'Description'])['Quantity'].sum().unstack().fillna(0)
# here we start grouping with invoiceno and description becuase these two are two reliable benchmarks for uniqueness 
# we use this to check if a customer orders the exact same product twice if so then 
# we sum them then we use unstack to change them from rows to columns and then we fill na cells with zero

basket_bool = basket > 0
# here we convert binary to true or false


basket_bool.iloc[:5, :5]

# we use this as we said before for just checking and marking a checkpoint visually



top_10_items = basket_bool.sum().sort_values(ascending=False).head(10)
# we create a variable containing how many invoices contains each product 
# and we use ascending=False so that it sorts from highest to lowest





top_10_items.plot(kind='barh', color='steelblue')
plt.title('Top 10 Most Frequent Products in Germany')
plt.xlabel('Number of Invoices (Baskets)')
plt.ylabel('Product')
plt.gca().invert_yaxis()  # inverts the y-axis so the highest product is at the top 
plt.show()

# here we specify the attributes and the names for our plot and the type and everything




basket_sizes = basket_bool.sum(axis=1)
# here we count how many unique items are in each invoice (row) using axis=1 instead of default axis=0

basket_sizes.plot(kind='hist', bins=20, color='coral', edgecolor='black')
plt.title('Distribution of Basket Sizes in Germany')
plt.xlabel('Number of Unique Items per Invoice')
plt.ylabel('Number of Invoices')
plt.show()


# Plot a histogram of basket sizes





# after that we save the boolean basket for the next team member


basket_bool.to_csv("data/basket_matrix_germany.csv")