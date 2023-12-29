
# Tsunami Study 1750-2023

# Import the necessary libraries.
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
print('Libraries imported successfully')

# Create a pandas data frame from TSV file
file=r'Tsunami(1750-present).tsv'
df=pd.read_csv(file, sep='\t')
df.info()

# Insights
# 
# Size and Structure: The DataFrame contains 2393 entries, each representing a record, and has 51 columns. Each column represents a different attribute or feature of the data.
# 
# Missing Data: There's a significant amount of missing data in several columns. For example, columns like 'Hr', 'Mn', 'Sec', 'Earthquake Magnitude', 'Focal Depth (km)', and 'Vol' have a large number of null values. This suggests that for many records, specific details like the exact time of the event or earthquake-related information are not available.
# 
# Data Types: The majority of the columns are of float64 type, indicating numerical data. There are also a few object-type columns ('Country', 'Area', 'Location Name'), which are likely categorical or textual data.
# 
# Specific Columns with High Nullity:
# 
# 'Unnamed: 0' and 'More Info' columns have all null values, which means these columns might not be useful for analysis.
# 'Focal Depth (km)' and 'Vol' have very few non-null entries, suggesting that these features are only relevant for a small subset of the data (possibly specific types of events).
# 
# Geographical Information: The dataset includes geographical data, such as 'Country', 'Area', 'Region', 'Latitude', and 'Longitude'. However, 'Area' has a high number of null values, indicating that this specific geographical detail is often missing.
# 
# Event Timing: The columns 'Year', 'Mo', 'Dy', 'Hr', 'Mn', and 'Sec' are intended to provide the exact timing of the events. However, as you move from 'Year' to 'Sec', the number of non-null entries decreases, suggesting that finer details of the timing (like hours, minutes, and seconds) are often not recorded.

# View the first 5 rows
pd.set_option('display.max_columns', None)
df.head()

# View the last 5 rows 
df.tail()
# From the head and tail methods we can see how the last 5 entries have far less NaN entries. This is likely due to better data acquisition techniques in more modern times.

# Look at the unique values in each column
df.nunique()

# Unique Identifiers: 
# The 'Id' column has 2391 unique values, almost one per entry, suggesting it likely serves as a primary identifier for each record. he 'Unnamed: 0' and 'More Info' columns have 0 unique values, reinforcing the earlier observation that they may not be useful for analysis.
# 
# Temporal Data:
# 'Year' has 266 unique values, indicating a wide range of years covered in the dataset.
# 'Mo', 'Dy', 'Hr', 'Mn', and 'Sec' have the maximum number of unique values possible for months, days, hours, minutes, and seconds, respectively. This suggests a detailed recording of event timings where available.
# 
# Geographical and Event Specifics:
# The dataset covers events in 112 different countries and 880 unique location names, indicating a broad geographical scope.
# There are 23 unique regions and 32 areas, though the lower count of unique areas suggests less granularity or more missing data in this field.
# 
# Tsunami Characteristics:
# The 'Earthquake Magnitude' and 'Focal Depth (km)' fields have 52 and 103 unique values, respectively, offering detailed insights into the seismic aspects of the events where applicable.
# 'Maximum Water Height (m)' has 240 unique values, providing a diverse range of tsunami heights.
# 
# Impact Metrics:
# 'Deaths', 'Missing', 'Injuries', 'Damage ($Mil)', 'Houses Destroyed', and 'Houses Damaged' show varied numbers of unique values, indicating a wide range of impacts from different events.
# 
# Descriptions and Intensity:
# Description columns (like 'Death Description', 'Damage Description') mostly have 4 unique values, likely representing categorical levels of impact.'Tsunami Intensity' has 32 unique values, offering a nuanced view of the severity of tsunami events.

# We look at the % of missing values.
(df.isnull().sum()/(len(df)))*100

# By looking at the percentage of missing values we can start to make some assumptions about columns that could potentially be dropped. There are for example many colums with missing value percantages in the high ninties. Many of these will need to be dropped as there are not enough entries to draw any valuable insights from. Some however like "damage" and "deaths" will be interesting to look at to get an idea of the most devastating events.

# Drop unnecessary columns
col_drop = [
'Unnamed: 0',
'Id',
'Hr',
'Mn',
'Sec',
'Vol',
'More Info',
'Tsunami Magnitude (Abe)',
'Warn Status',
'Missing',
'Missing Description',
'Injuries',
'Injuries Description',
'Houses Destroyed',
'Houses Destroyed Description',
'Houses Damaged',
'Houses Damaged Description',
'Total Deaths',
'Total Death Description',
'Total Missing',
'Total Missing Description',
'Total Injuries',
'Total Injuries Description',
'Total Damage ($Mil)',
'Total Damage Description',
'Total Houses Destroyed',
'Total Houses Destroyed Description',
'Total Houses Damaged',
'Total Houses Damaged Description'
]

df.drop(columns=col_drop, inplace=True)

df.info()

# An explanation for the dropped columns.                                                                                                     
# 
# Dropped Column Name	                Reason                                                                                                 
# Unnamed: 0       	                Column contain no data                                                        
# Id	                                Does not provide any useful information for the analysis                              
# Hr	                                This degree of time information is not required                                              
# Mn	                                This degree of time information is not required                                                 
# Sec	                                This degree of time information is not required                                                          
# Vol	                                Source data set provides a link to information about volcanic eruption pertaining to the tsunami event.     
# More Info	                        Source data set provides a link with more information about the specific event.                     
# Tsunami Magnitude (Abe)	            99.9% missing values                                                          
# Warn Status	                        97% missing values                                                                      
# Missing	                            99.8% missing values                                                         
# Missing Description	                99.8% missing values                                                                 
# Injuries	                        96.8% missing values                                                                 
# Injuries Description	            96.3% missing values                                                                
# Houses Destroyed	                96.5% missing values                                                                      
# Houses Destroyed Description	    90.5% missing values                                                                      
# Houses Damaged	                    99.3% missing values                                                                              
# Houses Damaged Description	        97.4% missing values                                                                                         
# Total Death Description	            Total data columns will be dropped (Tsunami Only)
# Total Missing	                    Total data columns will be dropped (Tsunami Only)                                          
# Total Missing Description	        Total data columns will be dropped (Tsunami Only)                                          
# Total Injuries	                    Total data columns will be dropped (Tsunami Only)                                   
# Total Injuries Description	        Total data columns will be dropped (Tsunami Only)                                               
# Total Damage ($Mil)	                Total data columns will be dropped (Tsunami Only)                                           
# Total Damage Description	        Total data columns will be dropped (Tsunami Only)                                                           
# Total Houses Destroyed	            Total data columns will be dropped (Tsunami Only)                                                   
# Total Houses Destroyed Description	Total data columns will be dropped (Tsunami Only)                                                       
# Total Houses Damaged	            Total data columns will be dropped (Tsunami Only)                                           
# Total Houses Damaged Description	Total data columns will be dropped (Tsunami Only)                                           
# 

# Next, we will correct the data types.
float_to_int = [
    "Year",
    "Mo",
    "Dy",
    "Deposits",
    "Number of Runups",
    "Deaths" 
]

df[float_to_int] = df[float_to_int].fillna(0).astype(int)

float_to_category = [
    "Tsunami Event Validity",
    "Tsunami Cause Code",
    "Region",
    "Death Description",
    "Damage Description"
]

df[float_to_category] = df[float_to_category].astype('category')

df.info()

# Tsunami Event Validity is described as follows:
# 
# Valid values: -1 to 4
# 
# Validity of the actual tsunami occurrence is indicated by a numerical rating of the reports of that event:
# 
# -1	erroneous entry.   
# 0	event that only caused a seiche or disturbance in an inland river/lake.  
# 1	very doubtful tsunami.  
# 2	questionable tsunami.  
# 3	probable tsunami.  
# 4	definite tsunami.  
# 
# We will only keep events with values 2 and higher.
keep=[2,3,4]

df = df[df['Tsunami Event Validity'].isin(keep)]

df.info()
# Next, we'll start looking at how to deal with our missing values.

df[['Earthquake Magnitude','Focal Depth (km)','Maximum Water Height (m)','Tsunami Magnitude (Iida)', 'Tsunami Intensity']].describe()

# The missing values for columns containing data pertaining to measurements of the natural phenomena will be replaced with the median value of said columns. The median is preferred over the mean in this case as it is a robust estimate of location.
replace_with_median= [
    'Earthquake Magnitude',
    'Focal Depth (km)',
    'Maximum Water Height (m)',
    'Tsunami Magnitude (Iida)', 
    'Tsunami Intensity'
]

medians = df[replace_with_median].median()

df[replace_with_median] = df[replace_with_median].fillna(medians)

df.info()

# Next will take a look at the missing values in the "Area" column
filtered_rows = df[df['Country'].isin(['USA','CANADA'])]
pd.set_option('display.max_rows', None)
print(filtered_rows[['Area', 'Country']])

# The area column provides information on "the State, Province or Prefecture of the tsunami source" but it only does so for the US and Canada and enen then there are still some Nan values. We will fill these Nan values with "NA" for not applicable.
df['Area'].fillna('NA',inplace=True)
df.info()

# Next, Location Name
df[df["Location Name"].isna()]

# There is only one NaN value. Because we don't have the Location Name but we do have the Country information we will replace the missing value with "In New Zealand"
df["Location Name"].fillna("In New Zealand", inplace=True)
df.info()

# The Damage ($Mil) column missing values will be replaced with 0. Here we make the assumption that if no data was collected, the damage value is less than 1 million USD.
df.loc[:, 'Damage ($Mil)'] = df['Damage ($Mil)'].fillna(0.00)
df.info()

#We look at damage description
df[['Death Description','Damage Description']].describe()

# The death and damage description missing values will be replaced with 1 as this includes very small quantaties like "Few (~1 to 50 deaths)" and "LIMITED (roughly corresponding to less than $1 million)"
df.loc[:, ['Death Description','Damage Description']] = df[['Death Description','Damage Description']].fillna(1)
df.info()

# Let's take a look at our data frame.
df.head()

# We can see that our index is off. Let's reset it.
df.reset_index(drop=True, inplace=True)
df.head()
df.tail()

# Let's do a deeper exploration of our data
df.describe(include='all').T

#Insights
# Temporal Distribution:
# Year: The data spans from 1750 to 2023, with most events occurring around 1928, showing a historical range of over 270 years. The standard deviation of 68.83 years indicates a broad temporal spread of events.
# Month (Mo): The average month is around June (6.46), but the data spans all months. This suggests no specific monthly trend in the occurrence of these events.
# Day (Dy): The average day is mid-month (about the 15th), with complete coverage of all days in a month.
# 
# 
# Seismic Data:
# Earthquake Magnitude: Ranges from 3.7 to 9.5 with an average of around 7.07, indicating that the dataset includes moderate to extremely strong earthquakes.
# Focal Depth (km): Varies widely from 0 to 600 km, with most events having a focal depth around 28 to 31 km, indicative of shallow to intermediate depth earthquakes.
# 
# 
# Country: 
# The dataset includes events from 95 countries, with Japan being the most common location.
# Area: Has 20 unique values, but 'NA' is most frequent.
# Location Name: Shows a high degree of variability with 630 unique locations.
# 
# 
# Latitude and Longitude: 
# Cover a wide range of values, indicating a global spread of tsunami events. Still have missing values.
# 
# Impact Measures:
# Maximum Water Height (m): Varies significantly, up to 524.6 meters, pointing to the varying intensities of tsunami waves.
# Number of Runups: Has a wide range, suggesting diverse impacts on different shorelines.
# Deaths: The number of deaths varies widely, with some events causing up to 227,899 deaths, underscoring the potentially catastrophic nature of these events.
# Damage ($Mil): Economic impacts also vary greatly, with some events causing up to $220,136.6 million in damages.
# 
# 
# 

# Not satisfied with the missing values in longitude and latitude. They will be filled with the mean of other entries with the same location name.
df['Latitude'] = df.groupby('Location Name')['Latitude'].transform(lambda x: x.fillna(x.mean()))
df['Longitude'] = df.groupby('Location Name')['Longitude'].transform(lambda x: x.fillna(x.mean()))
missing_locations = df[df['Latitude'].isnull() | df['Longitude'].isnull()]['Location Name'].unique()
print("Location names with missing latitude or longitude:", missing_locations)

# Seems we still have missing values and it's due to having no data on latitude and longitude for certain locations. They will instead be filled with latitude and longitude info of entries with the same country. Any left will be filled with the median.
df['Latitude'] = df.groupby('Country')['Latitude'].transform(lambda x: x.fillna(x.mean()))
df['Longitude'] = df.groupby('Country')['Longitude'].transform(lambda x: x.fillna(x.mean()))
df.info()
median_latitude = df['Latitude'].median()
median_longitude = df['Longitude'].median()
df['Latitude'].fillna(median_latitude, inplace=True)
df['Longitude'].fillna(median_longitude, inplace=True)

# We now have only the data we need with no missing values other than the longitude and latitude and the correct data types. Let's export to csv
df.to_csv('CleanedTsunamiDataIndex', index=True)

# We now have an improved data set with no missing values. Lets separate our columns into numerical and categorical columns.
cat_cols=df.select_dtypes(include=['object', 'category']).columns
num_cols = df.select_dtypes(include=np.number).columns.tolist()
print("Categorical Variables:")
print(cat_cols)
print("Numerical Variables:")
print(num_cols)

# Univariate analysis using Histogram and  Box Plot for numerical variables.
for col in num_cols:
    print(col)
    print('Skew :', round(df[col].skew(), 2))
    plt.figure(figsize = (15, 4))
    plt.subplot(1, 2, 1)
    df[col].hist(grid=False)
    plt.ylabel('count')
    plt.subplot(1, 2, 2)
    sns.boxplot(x=df[col])
    plt.show()
    
#Insights
# -We can see that the years span from 1750 to 2023 and it seams as though the rate of events is increasing. It will be interesting to take a closer lok at that                                                                               
# -The earthquake magnitude seams to be centered around 7 which is reasonable given that the data is only for earthquakes having caused a tsunami  
# -Focal depth and deposits seem to have significant outliers on the upper bounds                                    
# -The latitude and longitude plots seam to indicate a slight concentration in the northern and eastern hemispheres                           
# -Max water height is mostly concentrate with the 0 to 50 meter range with some significant outliers reaching 500                                 
# -Number of run-ups is mostly concentrated around 0-500 with some extreme outliers
# -The peculiarly large concentration around the median for magnitude and intensity is likely due to the way we have filled missing values for these columns using the median                                                 
# -Most events deaths seem to be well bellow 10000 and there is an extreme outlier nearing 250000
# -Damage cost are  mostly close to 0 and we have one particular extreme outlier.
# 
# 

#Count plots for categorical variables
N = 5  
# We Iterate through each categorical column
for col in cat_cols:
    
    top_categories = df[col].value_counts().nlargest(N).index
    
   
    fig, ax = plt.subplots(figsize=(8, 6))
    plt.title(f'Top {N} categories for {col}')
    sns.countplot(x=col, data=df[df[col].isin(top_categories)], color='blue', order=top_categories)

   
    total_entries = len(df[col])
    for p in ax.patches:
        percentage = f'{100 * p.get_height() / total_entries:.1f}%'
        ax.annotate(percentage, (p.get_x() + p.get_width() / 2., p.get_height()), ha='center', va='center', xytext=(0, 10), textcoords='offset points')

plt.show()
#Insights
# -Over 70% of eventas have a validity code of 3 or 4. 3 being probable tsunami 4 being definite tsunami                               
# -75% of events in the data set have a cause code of 1 which mean the tsunami was caused by an earthquake                     
# -Over 40% of events in our data set occured in the top 5 countries Japan, Indonesia, USA, Chile, and Greece. Japan being number one with 13.3%   

# Multivariate analysis 
numerical_columns = df.select_dtypes(include='number') 
correlation_matrix = numerical_columns.corr()
plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt='.2f', linewidths=0.5)
plt.title('Correlation Matrix for Numerical Columns')
plt.show()

#Insights
# Number of Runups' is highly correlated with 'Tsunami Intensity' (0.91), suggesting that as the number of waves reaching the shore increases, so does the intensity of the tsunami.
# 
# 'Deaths' are strongly correlated with 'Maximum Water Height (m)' (0.92), which is intuitive as higher tsunami waves can be more destructive and lead to higher death tolls.
# 
# Similarly, 'Deaths' show a strong correlation with 'Damage ($Mil)' (0.91), indicating that more severe tsunamis that cause higher fatalities also tend to result in more monetary damage.
# 
# The strong correlation between 'Maximum Water Height (m)' and 'Damage ($Mil)' (0.91) reinforces the understanding that taller tsunami waves are likely to cause more damage.
# 
# 'Tsunami Magnitude (Iida)' and 'Tsunami Intensity' have a significant positive correlation (0.56), which might be expected since both metrics are related to the strength of the tsunami. However, the correlation is not as strong as one might anticipate, suggesting that there are other factors at play determining the perceived intensity of a tsunami beyond its magnitude.
# 
# The lack of strong correlations between 'Latitude' and 'Longitude' with other variables could indicate that the impact of a tsunami is not strongly dependent on the location of occurrence within the dataset's geographical scope.
# 
# The low correlations between 'Earthquake Magnitude' and both 'Tsunami Magnitude (Iida)' and 'Tsunami Intensity' suggest that while earthquakes can cause tsunamis, the strength of the earthquake does not linearly translate to the strength or intensity of the tsunami. This may be due to a variety of factors including depth of the earthquake, distance from the shore, and local topography.
# 
# Time variables ('Year', 'Mo', 'Dy') do not show a significant correlation with tsunami metrics, indicating that the timing of a tsunami does not predict its magnitude, intensity, or impact.


# We will continue with data visualization in Tableau.