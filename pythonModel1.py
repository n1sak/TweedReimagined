
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np


plt.style.use('default')
sns.set_palette("husl")


fig = plt.figure(figsize=(16, 12))


ax1 = plt.subplot(2, 3, 1)
food_retail_counts = [len(food_retail_mentions), len(df) - len(food_retail_mentions)]
labels = ['Mentions Food/Retail', 'No Food/Retail Mention']
colors = ['#ff7f0e', '#1f77b4']
plt.pie(food_retail_counts, labels=labels, autopct='%1.1f%%', colors=colors, startangle=90)
plt.title('Reviews Mentioning Food/Retail\
(Total: ' + str(len(df)) + ' reviews)', fontsize=12, fontweight='bold')

# mentions anything food/retail related :))
ax2 = plt.subplot(2, 3, 2)
sentiment_counts = [len(negative_food_retail_reviews), len(food_retail_mentions) - len(negative_food_retail_reviews)]
sentiment_labels = ['Negative Sentiment', 'Neutral/Positive']
colors2 = ['#d62728', '#2ca02c']
plt.pie(sentiment_counts, labels=sentiment_labels, autopct='%1.1f%%', colors=colors2, startangle=90)
plt.title('Sentiment of Food/Retail Mentions\
(' + str(len(food_retail_mentions)) + ' total mentions)', fontsize=12, fontweight='bold')

ax3 = plt.subplot(2, 3, 3)
negative_ratings = [review['rating'] for review in negative_food_retail_reviews]
rating_counts = pd.Series(negative_ratings).value_counts().sort_index()
bars = plt.bar(rating_counts.index, rating_counts.values, color='#d62728', alpha=0.7)
plt.xlabel('Star Rating')
plt.ylabel('Number of Reviews')
plt.title('Rating Distribution\
Negative Food/Retail Reviews', fontsize=12, fontweight='bold')
plt.xticks(range(1, 6))
# Add value labels on bars
for bar in bars:
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2., height + 0.1,
             str(int(height)), ha='center', va='bottom')


ax4 = plt.subplot(2, 3, 4)
# Convert dates and create timeline
df['dateCreated'] = pd.to_datetime(df['dateCreated'])
negative_indices = [review['index'] for review in negative_food_retail_reviews]
negative_dates = df.loc[negative_indices, 'dateCreated'].dt.to_period('M').value_counts().sort_index()

if len(negative_dates) > 0:
    plt.plot(negative_dates.index.astype(str), negative_dates.values, marker='o', color='#d62728', linewidth=2)
    plt.xlabel('Month')
    plt.ylabel('Number of Negative Reviews')
    plt.title('Timeline of Negative Food/Retail Reviews', fontsize=12, fontweight='bold')
    plt.xticks(rotation=45)
else:
    plt.text(0.5, 0.5, 'No date data available', ha='center', va='center', transform=ax4.transAxes)
    plt.title('Timeline of Negative Food/Retail Reviews', fontsize=12, fontweight='bold')


ax5 = plt.subplot(2, 3, 5)
# Calculate average ratings for different groups
all_reviews_avg = df['reviewRating'].mean()
food_retail_avg = np.mean([review['rating'] for review in food_retail_mentions])
negative_food_retail_avg = np.mean([review['rating'] for review in negative_food_retail_reviews])

categories = ['All Reviews', 'Food/Retail\
Mentions', 'Negative Food/\
Retail Reviews']
averages = [all_reviews_avg, food_retail_avg, negative_food_retail_avg]
colors3 = ['#1f77b4', '#ff7f0e', '#d62728']

bars = plt.bar(categories, averages, color=colors3, alpha=0.7)
plt.ylabel('Average Rating')
plt.title('Average Ratings Comparison', fontsize=12, fontweight='bold')
plt.ylim(0, 5)
# Add value labels on bars
for bar, avg in zip(bars, averages):
    plt.text(bar.get_x() + bar.get_width()/2., bar.get_height() + 0.05,
             f'{avg:.1f}', ha='center', va='bottom', fontweight='bold')

# word frequency tester for negative reviews
ax6 = plt.subplot(2, 3, 6)
# find those negative words
negative_words = []
for review in negative_food_retail_reviews:
    text = review['text'].lower()
    words = ['no food', 'limited', 'expensive', 'overpriced', 'nothing', 'hardly', 'small', 'tiny', 'minimal']
    for word in words:
        if word in text:
            negative_words.append(word)

if negative_words:
    word_counts = pd.Series(negative_words).value_counts().head(8)
    bars = plt.barh(word_counts.index, word_counts.values, color='#d62728', alpha=0.7)
    plt.xlabel('Frequency')
    plt.title('Common Negative Terms\
in Food/Retail Reviews', fontsize=12, fontweight='bold')
    for bar in bars:
        width = bar.get_width()
        plt.text(width + 0.1, bar.get_y() + bar.get_height()/2.,
                 str(int(width)), ha='left', va='center')
else:
    plt.text(0.5, 0.5, 'No common terms found', ha='center', va='center', transform=ax6.transAxes)
    plt.title('Common Negative Terms\
in Food/Retail Reviews', fontsize=12, fontweight='bold')

plt.tight_layout()
plt.show()

print("Created comprehensive visualization of food/retail review analysis")
