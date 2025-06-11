#!/bin/bash
echo "📥 Downloading Zomato dataset via Kaggle API..."
curl -L -o ~/Downloads/zomato-eda.zip \
  https://www.kaggle.com/api/v1/datasets/download/pranavuikey/zomato-eda

echo "✅ Downloaded to ~/Downloads/zomato-eda.zip"
echo "📂 Please unzip it and place zomato.csv into the project root folder."