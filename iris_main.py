# Importing all the necessary Packages. 
import pandas as pd 
import seaborn as sns
import matplotlib.pyplot as plt 

# Reading the CSV file using pandas. 
df = pd.read_csv(r"Iris.csv")

# Reading top 5 rows. 
print(df.head())

# Getting the information about the dataset.
print(df.shape)

# Gathering the information about columns and their datatype. 
print(df.info())

# Statical Computations. 
print(df.describe())

# Checking the missing values.
print(df.isnull().sum())

# Cheking the duplicate values.
data = df.drop_duplicates(subset = "Species",)
print(data)

# Checking if the dataset (species) is balanced or not.
print(df.value_counts("Species"))

# Starting with Data Visualization -
# Comparing Sepal Length and Sepal Width.
sns.scatterplot(x='SepalLengthCm', 
                y='SepalWidthCm',
                hue='Species',
                data=df, )
# Placing Legend outside the Figure
plt.legend(bbox_to_anchor=(1, 1), loc=2)
plt.show()


# Comparing Petal Length and Petal Width.
sns.scatterplot(x='PetalLengthCm', 
                y='PetalWidthCm',
                hue='Species', 
                data=df, )
# Placing Legend outside the Figure
plt.legend(bbox_to_anchor=(1, 1), loc=2)
plt.show()


# Histogram.
fig, axes = plt.subplots(2, 2, figsize=(10,10))
axes[0,0].set_title("Sepal Length")
axes[0,0].hist(df['SepalLengthCm'], bins=7)
axes[0,1].set_title("Sepal Width")
axes[0,1].hist(df['SepalWidthCm'], bins=5);
axes[1,0].set_title("Petal Length")
axes[1,0].hist(df['PetalLengthCm'], bins=6);
axes[1,1].set_title("Petal Width")
axes[1,1].hist(df['PetalWidthCm'], bins=6);
plt.show()


# Histogram with Displot Plot.
plot = sns.FacetGrid(df, hue="Species")
plot.map(sns.distplot, "SepalLengthCm").add_legend()
plot = sns.FacetGrid(df, hue="Species")
plot.map(sns.distplot, "SepalWidthCm").add_legend()
plot = sns.FacetGrid(df, hue="Species")
plot.map(sns.distplot, "PetalLengthCm").add_legend()
plot = sns.FacetGrid(df, hue="Species")
plot.map(sns.distplot, "PetalWidthCm").add_legend()
plt.show()


# Done! 