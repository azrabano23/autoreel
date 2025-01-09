from flask import Flask, render_template, request, redirect, url_for
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import io
import base64
from forms import CarFilterForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'

data = pd.read_csv('processed_germany_auto_data.csv')

def setup_plot():
    sns.set(style="whitegrid")  

def generate_color_palette(n):
    return sns.color_palette("husl", n) 

@app.route('/', methods=['GET', 'POST'])
def index():
    form = CarFilterForm()
    years = sorted(data['Year'].unique())
    form.start_year.choices = [(year, year) for year in years]
    form.end_year.choices = [(year, year) for year in years]
    form.brands.choices = [(brand, brand) for brand in sorted(data['Brand'].unique())]
    form.fuel_types.choices = [(fuel, fuel) for fuel in sorted(data['Fuel Type'].unique())]

    if form.validate_on_submit():
        return redirect(url_for('dashboard',
                                start_year=form.start_year.data,
                                end_year=form.end_year.data,
                                brands=form.brands.data,
                                fuel_types=form.fuel_types.data,
                                visualization=form.visualization.data))
    return render_template('index.html', form=form)

@app.route('/dashboard')
def dashboard():
    start_year = request.args.get('start_year', type=int)
    end_year = request.args.get('end_year', type=int)
    brands = request.args.getlist('brands')
    fuel_types = request.args.getlist('fuel_types')
    visualization = request.args.get('visualization')
    filtered_data = data[(data['Year'] >= start_year) & (data['Year'] <= end_year)]
    if brands:
        filtered_data = filtered_data[filtered_data['Brand'].isin(brands)]
    if fuel_types:
        filtered_data = filtered_data[filtered_data['Fuel Type'].isin(fuel_types)]
    img = io.BytesIO()
    setup_plot()
    plt.figure(figsize=(12, 8))
    if visualization == 'price_trend':
        sns.lineplot(data=filtered_data, x='Year', y='Price', hue='Brand', palette=generate_color_palette(len(brands)), marker='o', ci=None)
        plt.title('Average Car Price Trend by Year')
        plt.xlabel('Year')
        plt.ylabel('Average Price (€)')
        plt.legend(title='Brand')
    elif visualization == 'brand_popularity':
        sns.countplot(data=filtered_data, x='Brand', palette=generate_color_palette(len(brands)))
        plt.title('Popularity of Car Brands')
        plt.xlabel('Brand')
        plt.ylabel('Number of Cars')
        plt.xticks(rotation=45)
    elif visualization == 'fuel_efficiency':
        sns.lineplot(data=filtered_data, x='Year', y='Fuel Consumption (L/100km)', hue='Fuel Type', palette=generate_color_palette(len(fuel_types)), marker='o', ci=None)
        plt.title('Fuel Efficiency Trend Over Time')
        plt.xlabel('Year')
        plt.ylabel('Average Fuel Consumption (L/100km)')
        plt.legend(title='Fuel Type')
    elif visualization == 'price_distribution':
        sns.boxplot(x='Fuel Type', y='Price', data=filtered_data, palette=generate_color_palette(len(fuel_types)))
        plt.title('Price Distribution by Fuel Type')
        plt.xlabel('Fuel Type')
        plt.ylabel('Price (€)')
    elif visualization == 'mileage_price':
        sns.scatterplot(data=filtered_data, x='Mileage', y='Price', hue='Brand', palette=generate_color_palette(len(brands)), alpha=0.6)
        plt.title('Mileage vs Price')
        plt.xlabel('Mileage (km)')
        plt.ylabel('Price (€)')
        plt.legend(title='Brand')

    plt.grid(True)
    plt.tight_layout()
    plt.savefig(img, format='png')
    img.seek(0)
    plot_url = base64.b64encode(img.getvalue()).decode('utf8')
    plt.close()
    return render_template('dashboard.html', plot_url=plot_url)

if __name__ == '__main__':
    app.run(debug=True)
