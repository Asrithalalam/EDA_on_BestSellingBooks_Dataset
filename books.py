#import required libraries
import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt
import os
import warnings
warnings.filterwarnings("ignore")


#load the dataset
df = pd.read_csv("best-selling-books.csv")
print('\nColumns in Dataset:',df.columns)
print("Shape:", df.shape)

#Basic data
print("\nFirst 5 rows:",df.head())

print("\nLast 5 rows:",df.tail())

print("\nDataset Info:",df.info())

print("\nStatistical Summary:",df.describe())

# Check Missing Values
print("\nMissing Values:",df.isnull().sum())
print(df.isnull().sum()) #count the number of missing (null/NaN) values in each column of a DataFrame

#To handle missing values in "Genre":
df["Genre"]=df["Genre"].fillna("Unknown")
print(df.isnull().sum())

#Create visuals folder(for visualizations)
if not os.path.exists("top_selling_books_visuals"):
    os.makedirs("top_selling_books_visuals")  

#Data Visualization

#1. --Top 10 Books by Sales--
top_selling_books = df.sort_values(by="Approximate sales in millions", ascending=False).head(10)
colors = ['red', 'blue', 'green', 'orange', 'purple', 'brown', 'pink', 'gray', 'olive', 'cyan']
plt.figure()
sns.barplot( data=top_selling_books,
            x="Approximate sales in millions", 
            y="Book",
            hue = "Book",
            palette = colors)
plt.title("Top 10 Best Selling Books")
plt.xlabel("Sales (in millions)")
plt.ylabel("Book")
plt.savefig("top_selling_books_visuals/Top 10 Books by Sales.png")
plt.close()
print("Saved:Top 10 Books by Sales.png")

#2. --Sales Distribution--Analyzing How book sales are distributed across all books.
plt.figure()
sns.histplot(df["Approximate sales in millions"], bins=15,color = 'Violet') 
#bins = divide the data into intervals(range)
#KDE = Kernel Density Estimation - adds a smooth curve over the histogram
plt.title("Distribution of Book Sales")
plt.xlabel("Sales (in millions)")
plt.savefig("top_selling_books_visuals/Sales Distribution.png")
plt.close()
print("Saved:Sales Distribution.png")

#3. --Books Published Over Years--
plt.figure()
sns.histplot(df["First published"], bins=20,color='orange')
plt.title("Books Published Over Years")
plt.xlabel("Year")
plt.savefig("top_selling_books_visuals/Books Published Over Years.png")
plt.close()
print("Saved:Books Published Over Years.png")

#4. --Top 10 Sales by Genre--
sales_by_genre = df.groupby('Genre')['Approximate sales in millions'].sum().reset_index()

top_10_genres = sales_by_genre.nlargest(10, 'Approximate sales in millions')

plt.figure()
sns.barplot(data=top_10_genres, x='Genre', y='Approximate sales in millions',hue='Genre',palette='tab10',legend=False)
plt.xlabel('Genre')
plt.ylabel('Total Sales (millions)')
plt.title('Top 10 Sales by Genre')
plt.xticks(rotation=90)   #Rotates genre names vertically.
plt.savefig("top_selling_books_visuals/Top 10 Sales by Genre.png")
plt.close()
print("Saved:Top 10 Sales by Genre.png")

#5. --Revenue Trends Over Time--
df['First published'] = pd.to_datetime(df['First published'])    #Convert Year to Datetime
df = df.sort_values('First published')  #Sort by Year
plt.figure() 
plt.plot(df['First published'], df['Approximate sales in millions'], color= 'red') 
plt.xlabel('Year') 
plt.ylabel('Sales (millions)') 
plt.title('Revenue Trends Over Time') 
plt.xticks(rotation=90) 
plt.savefig("top_selling_books_visuals/Revenue Trends Over Time.png")
plt.close()
print("Saved:Revenue Trends Over Time.png")