# Create reviews.csv file for user download
import pandas as pd

data = [
    [1,"This product is amazing","positive"],
    [2,"I love this item","positive"],
    [3,"Very bad experience","negative"],
    [4,"Not worth the money","negative"],
    [5,"It is okay","neutral"],
    [6,"Excellent quality","positive"],
    [7,"Worst product ever","negative"],
    [8,"Average performance","neutral"],
    [9,"Highly recommended","positive"],
    [10,"Not satisfied","negative"],
    [11,"Good value for money","positive"],
    [12,"The product is decent","neutral"],
    [13,"Very disappointing","negative"],
    [14,"Superb build quality","positive"],
    [15,"Nothing special","neutral"]
]

df = pd.DataFrame(data, columns=["reviewId","review","sentiment"])
file_path = "/mnt/data/reviews.csv"
df.to_csv(file_path, index=False)

file_path