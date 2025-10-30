# src/plotter.py

"""
In this class, we are generating the final visualizations using Bokeh.
This module reads data directly from the database using sqlite3
and pandas, matching the architecture of the sample code.

This version is enhanced with a professional theme, tabs,
a 2x2 grid layout, and linked panning for more enhanced
user experience.
"""

import pandas as pd
import sqlite3
from bokeh.plotting import figure, show, output_file
from bokeh.layouts import column, gridplot
from bokeh.models import HoverTool, ColumnDataSource, Tabs, TabPanel
from bokeh.palettes import Category10_4  # A color palette for 4 items
from bokeh.io import curdoc  # To apply the theme
from .exceptions import DataLoadError

def _load_plot_data(db_name: str) -> dict:
    """Helper function to load all data needed for plotting."""
    try:
        conn = sqlite3.connect(db_name)
        data = {
            "train": pd.read_sql("SELECT * FROM train_data", conn),
            "ideal": pd.read_sql("SELECT * FROM ideal_data", conn),
            "mapped": pd.read_sql("SELECT * FROM mapped_test_results", conn)
        }
        conn.close()
        return data
    except Exception as e:
        raise DataLoadError("loading tables for plotting", e)

def generate_plots(best_matches: dict, db_name: str = "assignment_data.db"):
    """
    this class creates and saves an enhanced Bokeh HTML visualization with tabs.
    
    Args:
        best_matches (dict): The {train_col: ideal_col} mapping.
        db_name (str): The path to the database.
    """
    print("Generating enhanced Bokeh visualizations...")
    try:
        # Set a professional theme for the document
        curdoc().theme = "caliber"

        data = _load_plot_data(db_name)
        train_df = data["train"]
        ideal_df = data["ideal"]
        mapped_df = data["mapped"]

        output_file("assignment_results.html", title="Data Analysis Results")
        
        train_plots = []
        
        # --- Plots 1-4: Training vs. Ideal (in a 2x2 grid) ---
        
        # Create the first plot
        p1 = _create_train_plot(train_df, ideal_df, 'y1', best_matches['y1'], Category10_4[0])
        train_plots.append(p1)

        # Create the other 3 plots, linking their x-range to the first plot
        p2 = _create_train_plot(train_df, ideal_df, 'y2', best_matches['y2'], Category10_4[1], x_range=p1.x_range)
        train_plots.append(p2)
        
        p3 = _create_train_plot(train_df, ideal_df, 'y3', best_matches['y3'], Category10_4[2], x_range=p1.x_range)
        train_plots.append(p3)
        
        p4 = _create_train_plot(train_df, ideal_df, 'y4', best_matches['y4'], Category10_4[3], x_range=p1.x_range)
        train_plots.append(p4)

        # Arrange the 4 training plots in a 2x2 grid
        train_grid = gridplot(train_plots, ncols=2)
        
        # Create the first tab
        tab1 = TabPanel(child=train_grid, title="1. Training Function Analysis")

        # --- Plot 5: Mapped Test Data (in a separate tab) ---
        test_source = ColumnDataSource(mapped_df)
        test_tooltips = [
            ("X", "`X (test func)`{0.00}"),
            ("Y", "`Y (test func)`{0.000}"),
            ("Mapped to", "`No. of ideal func`"),
            ("Deviation (Δy)", "`Delta Y (test func)`{0.0000}")
        ]

        p_test = figure(
            title=f"Mapped Test Points ({len(mapped_df)} points)",
            width=1200, height=500, tools=["pan,wheel_zoom,box_zoom,reset,save"]
        )
        p_test.add_tools(HoverTool(tooltips=test_tooltips))
        
        # Enhanced scatter plot aesthetics
        p_test.circle(
            x='X (test func)',
            y='Y (test func)',
            source=test_source,
            fill_color="green",     
            line_color="black",     
            line_width=0.5,         
            alpha=0.7,             
            size=8,
            legend_label="Test Points"
        )
        p_test.title.text_font_size = "14pt"
        p_test.legend.location = "top_left"

        # Create the second tab
        tab2 = TabPanel(child=p_test, title="2. Mapped Test Data Results")
        
        # --- Combine tabs into a single layout ---
        layout = Tabs(tabs=[tab1, tab2])
        
        # Save and show the final layout
        show(layout)
        print(f"✅ Enhanced visualizations saved to 'assignment_results.html'.")

    except Exception as e:
        print(f"❌ Error during visualization: {e}")
        import traceback
        traceback.print_exc()

def _create_train_plot(train_df, ideal_df, train_col, ideal_col, color, x_range=None):
    """Helper function to create a single training vs. ideal plot."""
    
    source = ColumnDataSource(pd.DataFrame({
        'x': train_df['x'],
        'train_y': train_df[train_col],
        'ideal_y': ideal_df[ideal_col]
    }))
    
    # Format tooltips to show 3 decimal places
    tooltips = [
        ("X", "@x{0.00}"),
        (f"Train ({train_col})", "@train_y{0.000}"),
        (f"Ideal ({ideal_col})", "@ideal_y{0.000}")
    ]
    # Create a dictionary of arguments
    plot_args = {
        "title": f"Training Function '{train_col}' vs. Ideal Fit '{ideal_col}'",
        "width": 600, "height": 350,
        "tools": ["pan,wheel_zoom,box_zoom,reset,save"]
    }
    
    # Only add the x_range argument IF it is not None
    if x_range:
        plot_args["x_range"] = x_range
        
    # Create the figure using the arguments dictionary
    p = figure(**plot_args)
    
    p.add_tools(HoverTool(tooltips=tooltips))
    
    # Plot training line
    p.line(x='x', y='train_y', source=source, color=color, 
           legend_label=f"{train_col} (Train)", line_width=2)
    
    # Plot ideal line
    p.line(x='x', y='ideal_y', source=source, color="gray", 
           line_dash="dashed", legend_label=f"{ideal_col} (Ideal)", line_width=2)
    
    p.title.text_font_size = "14pt"
    p.legend.location = "top_left"
    #p.legend.click_policy = "hide"
    
    return p