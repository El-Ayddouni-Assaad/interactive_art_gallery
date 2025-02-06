import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

def generate_heatmap(file_path):
    df = pd.read_csv(file_path, parse_dates=["Date_Time"])
    df.set_index("Date_Time", inplace=True)
    
    x = np.linspace(0, np.pi * 2, len(df))
    wave = np.sin(x) * 5 
    df["Temperature_C"] += wave
    
    plt.figure(figsize=(12, 8))
    heatmap = sns.heatmap(df[["Temperature_C"]].T, cmap='magma', annot=False, cbar=True)
    

    for i in range(len(df)):
        if df.iloc[i]["Temperature_C"] > df["Temperature_C"].mean():
            plt.gca().add_patch(plt.Rectangle((i, 0), 1, 1, fill=None, edgecolor='yellow', linewidth=1.5, hatch='xx'))
    
    plt.title("Abstract Wave-Like Heatmap", fontsize=16, color='white')
    plt.xticks(color='white')
    plt.yticks(color='white')
    plt.gca().set_facecolor('black')
    plt.savefig("static/heatmap.png", bbox_inches='tight', facecolor='black')
    plt.close()

def generate_bar_chart(file_path):
    df = pd.read_csv(file_path, parse_dates=["Date_Time"])
    x_vals = np.arange(len(df))
    
    wave_effect = np.sin(x_vals / 3) * 2
    df["Temperature_C"] += wave_effect
    
    colors = plt.cm.plasma(np.linspace(0, 1, len(df)))
    plt.figure(figsize=(12, 8))
    bars = plt.bar(df["Date_Time"], df["Temperature_C"], color=colors, edgecolor='white', linewidth=1.5, alpha=0.7)
    
    for bar, alpha_val in zip(bars, np.linspace(0.3, 1, len(bars))):
        bar.set_alpha(alpha_val)  
        if bar.get_height() > df["Temperature_C"].mean():
            bar.set_hatch('o')  
    
    plt.xlabel("Date Time", fontsize=14, color='white')
    plt.ylabel("Temperature (°C)", fontsize=14, color='white')
    plt.title("Abstract Bar Chart with Wave Effect", fontsize=16, color='white')
    plt.xticks(rotation=45, color='white')
    plt.yticks(color='white')
    plt.gca().set_facecolor('black')
    plt.savefig("static/bar_chart.png", bbox_inches='tight', facecolor='black')
    plt.close()

if __name__ == "__main__":
    sample_file = "static/weather_data.csv"
    generate_heatmap(sample_file)
    generate_bar_chart(sample_file)

