# TCGPriceExtractor
Using public-facing api of [Unnamed TCG Website], gathers low-estimate data on prices for a trading card collection and returns total value of collection. Can also be used to craft decks. Currently only supports Yugioh cards\
\
Accepts an excel with the below table headers as input from /resources and outputs into "complete.xlsx"

| Quantity	| Name	              | Set Number	| Price	| Condition	| Edition	| Dirty |
|----------:|:--------------------|:------------|------:|:----------|:--------|:------|
| 1	        | Dimensional Barrier	| DUDE-EN048	|	      | NM	      | F	      | Y     |
| 1	        | Raigeki	            | TN19-EN010  |	      | NM    	  | L       |	N     |      


| NOTE | All columns (with headers) are required, however (OPTIONAL) fields can be left empty. |
|:---|:---|
| Quantity:     | Number of cards in collection |
| Name:         | Name of card, avoid using non-alphanumeric special characters, though the app will sanitize it anyway|
| Set Number:   | (OPTIONAL) The set the card was released. If this is left empty, will pull the cheapest copy of this card across all sets|
| Price:        | (OPTIONAL) App will calculate the price. This column is still required for internal logic. If there is a value here, and 'Dirty' column is not empty or 'N', will recalculate the price.|
| Condition:    | (OPTIONAL) DEFAULT: "LP". Condition the card is in. Acceptable inputs; "NM", "LP", "MP", "HP" for "Near Mint", "Lightly Played", "Moderately Played" and "Heavily Played" respectively.|
| Edition:      | (OPTIONAL) DEFAULT: "U". Edition the card is in. Acceptable inputs: "F", "L", "U" for "1st Edition", "Limited", and "Unlimited" respectively.|
| Dirty:        | (OPTIONAL) Flag indicating whether the card price should be recalculated. Any value other than empty or 'N' will trigger recalculation, provided there is a value in "Price" column.|
