This Dash application visualizes automobile sales data for XYZAutomotives, focusing on two main types of analysis:

Yearly Statistics

Shows trends in automobile sales for a selected year.

Includes:

Total monthly sales (seasonally-adjusted)

Average vehicles sold by type

Advertising expenditure share by vehicle type

Yearly average sales across all years

Recession Period Statistics

Focuses on periods of economic recession (binary Recession variable).

Includes:

Average sales during recession years

Average vehicles sold by type during recession

Advertising expenditure share during recession

Effect of unemployment rate on sales, grouped by vehicle type

Features

Interactive Dropdowns

Report Type Dropdown: Select either “Yearly Statistics” or “Recession Period Statistics.”

Year Dropdown: Enabled only when “Yearly Statistics” is selected. Disabled automatically during recession report selection.

2×2 Plot Layout

Four plots displayed in two rows and two columns for easy comparison and screenshots.

Data Preprocessing Included

Canonicalizes vehicle type names (Supperminicar → Superminicar)

Adds Year and Month columns

Computes seasonally-adjusted sales (Adj_Sales)

Computes revenue (Revenue) per vehicle

Dynamic Callbacks

Plots update automatically based on dropdown selections.

Year dropdown is dynamically enabled/disabled based on report type.

Dependencies

Python 3.x

pandas

numpy

dash

plotly

Install dependencies via:

pip install pandas numpy dash plotly

Usage

Place automobile_sales.csv in the same folder as dashboard_final_assignment.py.

Run the app:

python dashboard_final_assignment.py


Open your browser at http://127.0.0.1:8050/ to view the dashboard.

Notes

Dataset covers years 1980–2013.

Recession periods are marked by the Recession binary column.

All plots use seasonally-adjusted sales for consistency.

The dashboard is designed to be submission-ready with screenshots in a 2×2 layout.
