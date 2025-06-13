# 🎬 AutoReel – Where Movies Meet Machines

**AutoReel** explores the fascinating intersection of vehicles and cinema through data analysis, machine learning, and interactive visual storytelling. By examining how cars appear across movie genres and decades, it uncovers cultural trends, recommends films based on car models, and uses machine learning to predict genres from vehicle data. AutoReel isn’t just about stats — it’s about storytelling through the lens of cars on screen.

---

## ❗️Problem Statement

Cars have long played iconic roles in movies — from James Bond’s Aston Martin to the DeLorean in *Back to the Future*. Yet there is no easy way to **analyze**, **visualize**, or **predict** the relationship between cars and cinema. With thousands of films and vehicles intertwined across genres and decades, industry professionals, researchers, and fans lack a tool to extract meaningful insights from this rich cultural dataset.

> 🎥 *Film marketers and automotive advertisers spend billions annually*, but often miss data-driven opportunities to pair vehicles with audiences.
>  
> 🧠 *A McKinsey report notes that 76% of consumers say a car's brand image matters — much of which is shaped by pop culture and media appearances.*

---

## 🚀 Project Overview

AutoReel is an interactive Python-based platform that blends **machine learning**, **data visualization**, and **recommendation systems** to:
- Discover which vehicles dominate film eras and genres.
- Recommend movies based on car models (and vice versa).
- Predict film genres using vehicle data (e.g., model, brand, year).
- Showcase insights through an intuitive Dash web app.

---

## 🧠 Technical Overview

### 🔍 Features

#### 📈 Trend Analysis
- Identifies the **most popular vehicles** featured in movies by **decade**.
- Uncovers **correlations** between **vehicle types** and **movie genres**.

#### 📊 Interactive Visualizations
- Uses **Plotly** to build interactive graphs exploring car usage in films.
- Employs **Folium** for geospatial insights (if location data exists).

#### 🎯 Recommendation System
- **Movie-to-Car Mapping**: Suggests cars featured in selected films.
- **Car-to-Movie Mapping**: Recommends movies that include specific car models.

#### 🤖 Machine Learning Models
- Trains a **Random Forest Classifier** to predict **movie genres** based on car features (model, brand, year).
- Encodes categorical variables and evaluates model **accuracy** and **reliability**.

#### 🌐 Interactive Dashboard
- Built using **Dash**, featuring:
  - Dropdowns to explore trends by car model or movie.
  - Dynamic decade-wise bar charts.
  - Real-time updates based on user selections.

---

## 🛠️ Programming Insights

| Component              | Tech Used                          |
|------------------------|------------------------------------|
| Dashboard              | Dash, Flask                        |
| Visualization          | Plotly, Folium (if geospatial)     |
| Machine Learning       | Scikit-Learn (Random Forest)       |
| Data Handling          | Pandas, NumPy, Matplotlib          |
| Web Framework          | Flask (to serve Dash)              |

### ML Pipeline
- Categorical encoding of car data (brand, model, year).
- Train/test split for genre prediction model.
- Performance evaluation via **accuracy** and **confusion matrix**.

---

## 🎯 Key Applications

- **🎥 Data Exploration**: Uncover trends in how cars appear across movie history.
- **📽️ Personalized Insights**: Recommend movies based on users' favorite vehicles.
- **📊 Industry Analysis**: Help **filmmakers**, **auto advertisers**, and **product placement strategists** understand the cinematic influence of cars.
- **🎮 Fan Engagement**: Entertain movie lovers and car enthusiasts with intelligent trivia and predictions.

---

## 🧑‍💻 Target Audience

- Film analysts and entertainment marketers  
- Automotive brands exploring cinematic trends  
- Data science students and researchers  
- Movie buffs and car lovers alike  

---

## 🌟 Why AutoReel Matters

AutoReel brings together creative storytelling and technical rigor to give a new lens on how transportation shapes our on-screen experiences. It not only entertains but **informs future strategies** in both the **film** and **automotive** industries — where cultural relevance drives perception and profit.

---

## 📝 License

MIT License – Free to use, modify, and build upon with attribution.

---

## 🤝 Contribute

Have ideas for new features or better models? Open an issue or submit a pull request!
