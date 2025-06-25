from flask import Flask, render_template
import pandas as pd
import os
import plotly.express as px
import plotly.io as pio
import traceback
from datetime import datetime

app = Flask(__name__)

CSV_FOLDER = "C:/Users/fedem/Documents/PYTHON/TRADING BOT/BINANCE/BOT FINAL/EMA BOT ANALYSIS"  # Adjust folder path accordingly

# Your create_graph_lines function
def create_graph_lines(dataframe, title, height, width, vertical_lines=None, vertical_descriptions=None):
    df = dataframe.copy()

    if 'Time' in df.columns:
        df['Time'] = pd.to_datetime(df['Time'], errors='coerce')
        df['Time_str'] = df['Time'].dt.strftime('%d/%m/%Y %H:%M')
    else:
        df['Time'] = pd.NaT
        df['Time_str'] = ""

    fig = px.scatter(
        df,
        x='Time',
        y='Invest',
        color='Type',
        color_discrete_map={'LONG': 'green', 'SHORT': 'red'},
        custom_data=['Tick', 'Time_str', 'Entry P', 'Act_Price', 'Lev', '%_X', 'Invest'],
        title=title
    )

    fig.add_scatter(
        x=df['Time'],
        y=df['Invest'],
        mode='lines',
        line=dict(color='rgba(0, 0, 255, 0.3)', dash='solid'),
        name='Trend Line'
    )

    if vertical_lines:
        for idx, vline_time in enumerate(vertical_lines):
            vline_time = pd.to_datetime(vline_time).to_pydatetime()
            annotation_text = (
                vertical_descriptions[idx] if vertical_descriptions and idx < len(vertical_descriptions)
                else vline_time.strftime('%d/%m %H:%M')
            )
            fig.add_vline(x=vline_time, line=dict(color='grey', width=1, dash='solid'))
            fig.add_annotation(
                x=vline_time,
                y=1.10,
                xref="x",
                yref="paper",
                showarrow=False,
                text=annotation_text,
                font=dict(color='grey', size=11),
            )

    fig.update_traces(
        hovertemplate=(
            'Tick: %{customdata[0]}<br>' +
            'Time: %{customdata[1]}<br>' +
            'Entr Price: %{customdata[2]}<br>' +
            'Exit  Price: %{customdata[3]}<br>' +
            'Leverage: %{customdata[4]}<br>' +
            'Change (%): %{customdata[5]}<br>' +
            'Balance: %{customdata[6]}<extra></extra>'
        )
    )

    fig.update_layout(
        legend=dict(
            x=0.9,
            y=0.5,
            bgcolor='rgba(255,255,255,0.8)',
            bordercolor='grey',
            borderwidth=2
        ),
        xaxis_title='Time',
        yaxis_title='Investment (%)',
        legend_title='Trade Type',
        hovermode='closest',
        height=height,
        width=None,  # Let it be responsive
        plot_bgcolor='rgba(230, 230, 250)',
        margin=dict(l=40, r=40, t=50, b=40),
        dragmode=False,
        modebar_remove=['zoom', 'zoomIn', 'zoomOut', 'autoScale', 'select', 'lasso2d', 'pan']
    )

    return fig


# Updated HTML template without zip usage
HTML_TEMPLATE = """
<!doctype html>
<html>
<head>
    <title>Live Trading Bot Output</title>
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <style>
        body { font-family: Arial, sans-serif; margin: 10px; padding: 0; }
        h2 { text-align: center; }
        .container { max-width: 100%; margin: auto; padding: 10px; }

        .table-wrapper {
            overflow-x: auto;  /* enable horizontal scroll */
            -webkit-overflow-scrolling: touch;  /* smooth scrolling on iOS */
            width: 100%;       /* don't restrict to viewport width, use container's width */
            max-width: 100%;   /* prevent overflowing parent */
        }

        .table-container {
            min-width: 600px;  /* or whatever minimum table width you want */
        }

        table {
            border-collapse: collapse;
            font-size: 14px;
            min-width: max-content;  /* make sure table can grow horizontally */
            width: auto;
            table-layout: auto;
        }
        th, td {
            border: 1px solid #999;
            padding: 6px 8px;
            text-align: center;
        }
        th {
            background-color: #f2f2f2;
            position: sticky;
            top: 0;
            z-index: 1;
        }
        @media (orientation: landscape) {
            .table-wrapper {
                overflow-x: visible;  /* no scroll, allow full width */
                width: auto;
            }
            .table-container {
                min-width: auto;
            }
            table {
                min-width: auto;
                width: 100%;
            }
        }

    </style>
</head>
<body>
    <div style="text-align:center; margin-bottom: 10px;">
        <a href="/" title="Refresh">
            <img src="{{ url_for('static', filename='refresh_dark.png') }}" alt="Refresh" width="40" style="cursor:pointer;">
        </a>
    </div>
    <div class="container">
        <h2>📈 Live Trading Output</h2>
        <p><strong>File:</strong> {{ filename }}</p>
        <p><strong>Last updated:</strong> {{ timestamp }}</p>
        
        <!-- Plotly chart -->
        <div style="width: 100%; overflow-x: auto;">
            {{ plot_div | safe }}
        </div>
        
        <!-- Data table -->
        <div class="table-wrapper">
            <div class="table-container">
                <table>
                    <thead>
                        <tr>
                            {% for col in df.columns %}
                            <th>{{ col }}</th>
                            {% endfor %}
                        </tr>
                    </thead>
                    <tbody>
                        {% for row in df.itertuples(index=False) %}
                        <tr>
                            {% for i in range(df.columns|length) %}
                            <td data-label="{{ df.columns[i] }}">{{ row[i] }}</td>
                            {% endfor %}
                        </tr>
                        {% endfor %}
                    </tbody>
                </table>
            </div>
        </div>

</body>
</html>
"""

@app.route('/')
def display_table():
    try:
        folder = "C:/Users/fedem/Documents/PYTHON/TRADING BOT/BINANCE/BOT FINAL/EMA BOT ANALYSIS"
        csv_files = [os.path.join(folder, f) for f in os.listdir(folder) if f.endswith('.csv')]
        if not csv_files:
            raise FileNotFoundError("No CSV files found in the folder.")
        latest_file = max(csv_files, key=os.path.getmtime)

        # Read full CSV
        df = pd.read_csv(latest_file)

        # Get the first row separately
        first_row = df.iloc[[0]]

        # Filter the rest of the DataFrame (excluding the first row)
        rest_filtered = df[df['Outcm'].notna()]

        # Combine the first row back with the filtered result
        comb_df = pd.concat([first_row, rest_filtered], ignore_index=True)

        # Add missing year and convert Time
        comb_df['Time'] = comb_df['Time'].apply(lambda t: f'2025/{t}')
        comb_df['Time'] = pd.to_datetime(comb_df['Time'], format='%Y/%m/%d %H:%M', errors='coerce')
        comb_df = comb_df.sort_values(by='Time', ascending=False)

        # Add missing year and convert Time to Table data
        df['Time'] = df['Time'].apply(lambda t: f'2025/{t}')
        df['Time'] = pd.to_datetime(df['Time'], format='%Y/%m/%d %H:%M', errors='coerce')
        df = df.sort_values(by='Time', ascending=False)

        # Prepare plot data (filtered)
        rest_filtered = comb_df
        fig = create_graph_lines(
            rest_filtered,
            title="Trading Bot Performance",
            height=600,
            width=1050
        )
        plot_div = pio.to_html(fig, full_html=False)

        # Prepare table data (full, limited to 200 rows)
        df['Time'] = df['Time'].dt.strftime('%Y-%m-%d %H:%M')
        df_table = df.head(20)

        return render_template(
            "index.html",
            df=df_table,
            plot_div=plot_div,
            filename=os.path.basename(latest_file),
            timestamp=pd.Timestamp.now().strftime('%Y-%m-%d %H:%M:%S')
        )
    except Exception as e:
        return f"Error loading data:<br><pre>{traceback.format_exc()}</pre>"
    
if __name__ == '__main__':
    app.run(debug=False, port=5000)

