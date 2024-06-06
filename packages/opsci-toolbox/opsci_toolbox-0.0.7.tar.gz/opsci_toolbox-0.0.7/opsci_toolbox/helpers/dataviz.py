from plotly.subplots import make_subplots
import plotly.graph_objects as go
import textwrap
import numpy as np
from scipy import interpolate
from scipy.spatial import ConvexHull
import random
from sklearn.metrics.pairwise import cosine_similarity
import plotly.express as px
import chart_studio.tools as tls
import chart_studio.plotly as py
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import math
import pandas as pd
from opsci_toolbox.helpers.nlp import sample_most_engaging_posts, create_frequency_table
from matplotlib.colors import to_hex
import networkx as nx



def upload_chart_studio(
    username: str, 
    api_key: str, 
    fig, 
    title: str
) -> tuple:
    """
    Upload a Plotly visualization to Chart Studio.

    Args:
        username (str): The Chart Studio username.
        api_key (str): The Chart Studio API key.
        fig: The Plotly figure object to be uploaded.
        title (str): The title for the uploaded visualization.

    Returns:
        tuple: A tuple containing the URL of the uploaded visualization and the embed code.
    """
    URL = ""
    EMBED = ""

    try:
        # Set Chart Studio credentials
        tls.set_credentials_file(username=username, api_key=api_key)
        
        # Upload the figure to Chart Studio
        URL = py.plot(fig, filename=title, auto_open=True)
        
        # Get the embed code for the uploaded figure
        EMBED = tls.get_embed(URL)
        
        # Print the URL and embed code
        print("* URL DE LA VIZ >> ", URL)
        print("\n*CODE EMBED A COLLER \n", EMBED)
        
    except Exception as e:
        # Print the exception message and a suggestion to reduce the visualization size
        print(e, "try to reduce the dataviz size by printing less data")

    return URL, EMBED

def scale_to_0_10(x: pd.Series) -> pd.Series:
    """
    Scale a pandas Series to the range [0, 10].

    Args:
        x (pd.Series): The input pandas Series to be scaled.

    Returns:
        pd.Series: The scaled pandas Series with values in the range [0, 10].
    """
    return ((x - x.min()) / (x.max() - x.min()) * 10).astype(int)

def normalize_data_size(df: pd.DataFrame, col: str, coef: int = 20, constant: int = 5) -> pd.DataFrame:
    """
    Normalize the sizes of dots based on a specified column in a DataFrame.

    Args:
        df (pd.DataFrame): The input DataFrame.
        col (str): The column name to be normalized.
        coef (int, optional): The coefficient to scale the normalized values. Defaults to 20.
        constant (int, optional): The constant to add to the scaled normalized values. Defaults to 5.

    Returns:
        pd.DataFrame: The DataFrame with an additional column for the normalized sizes.
    """
    df['normalized_' + col] = ((df[col] - df[col].max()) / (df[col] + df[col].max()) + 1) * coef + constant
    return df

def generate_color_palette(lst: list, transparency: float = 1) -> dict:
    """
    Generate a random color palette of RGBA codes.

    Args:
        lst (List[str]): List of color names or identifiers.
        transparency (float, optional): Transparency value for RGBA colors (0 to 1). Defaults to 1.

    Returns:
        dict: Dictionary containing color names or identifiers as keys and corresponding RGBA codes as values.
    """
    color_palette = {
        color: 'rgba({}, {}, {}, {})'.format(
            random.randrange(0, 255),
            random.randrange(0, 255),
            random.randrange(0, 255),
            transparency
        )
        for color in lst
    }
    return color_palette

def generate_color_palette_with_colormap(lst: list, colormap: str = "viridis") -> dict:
    """
    Generate a color palette with hexadecimal codes using a specified colormap.

    Args:
        lst (List[str]): List of color names or identifiers.
        colormap (str, optional): Name of the colormap to use. Defaults to "viridis".

    Returns:
        Dict[str, str]: Dictionary containing color names or identifiers as keys and corresponding hexadecimal codes as values.
    """
    num_colors = len(lst)

    # Generate example data
    data = np.linspace(0, 1, num_colors)

    # Choose the colormap
    cmap = plt.get_cmap(colormap, num_colors)

    # Normalize the data
    norm = plt.Normalize(0, 1)

    # Interpolate colors
    colors = cmap(norm(data))

    # Convert colors to hexadecimal codes
    hex_colors = {item: to_hex(colors[i]) for i, item in enumerate(lst)}

    return hex_colors

def generate_hexadecimal_color_palette(lst: list, add_transparency: bool = False, transparency: float = 0.5) -> dict:
    """
    Generate a random color palette with hexadecimal codes and optional transparency.

    Args:
        lst (List[str]): List of color names or identifiers.
        add_transparency (bool, optional): Whether to add transparency to the colors. Defaults to False.
        transparency (float, optional): Transparency value for the colors (0 to 1). Defaults to 0.5.

    Returns:
        Dict[str, str]: Dictionary containing color names or identifiers as keys and corresponding hexadecimal codes as values.
    """
    if add_transparency:
        alpha_hex = int(transparency * 255)  # Convert transparency to integer (0-255 range)
        color_palette = {
            color: "#{:02x}{:02x}{:02x}{:02x}".format(
                random.randint(0, 255),
                random.randint(0, 255),
                random.randint(0, 255),
                alpha_hex
            )
            for color in lst
        }
    else:
        color_palette = {
            color: "#{:02x}{:02x}{:02x}".format(
                random.randint(0, 255),
                random.randint(0, 255),
                random.randint(0, 255)
            )
            for color in lst
        }
    return color_palette

def generate_random_hexadecimal_color() -> str:
    """
    Generate a random hexadecimal color code.

    Returns:
        str: Hexadecimal color code.
    """
    return "#{:02x}{:02x}{:02x}".format(
        random.randint(0, 255),
        random.randint(0, 255),
        random.randint(0, 255)
    )

def wrap_text(txt: str, length: int = 50) -> str:
    """
    Wrap text to a specified length.

    Args:
        txt (str): The text to wrap.
        length (int, optional): The maximum length of each line. Defaults to 50.

    Returns:
        str: The wrapped text.
    """
    txt = '<br>'.join(textwrap.wrap(str(txt), width=length))
    return txt

def get_convex_hull_coord(points: np.array, interpolate_curve: bool = True) -> tuple:
    """
    Calculate the coordinates of the convex hull for a set of points.

    Args:
        points (np.array): Array of points, where each row is [x, y].
        interpolate_curve (bool): Whether to interpolate the convex hull.

    Returns:
        tuple: Tuple containing interpolated x and y coordinates of the convex hull.
    """
    # Calculate the convex hull of the points
    hull = ConvexHull(points)

    # Get the x and y coordinates of the convex hull vertices
    x_hull = np.append(points[hull.vertices, 0], points[hull.vertices, 0][0])
    y_hull = np.append(points[hull.vertices, 1], points[hull.vertices, 1][0])

    if interpolate_curve:
        # Calculate distances between consecutive points on the convex hull
        dist = np.sqrt(
            (x_hull[:-1] - x_hull[1:]) ** 2 + (y_hull[:-1] - y_hull[1:]) ** 2
        )

        # Calculate the cumulative distance along the convex hull
        dist_along = np.concatenate(([0], dist.cumsum()))

        # Use spline interpolation to generate interpolated points
        spline, u = interpolate.splprep([x_hull, y_hull], u=dist_along, s=0, per=1)
        interp_d = np.linspace(dist_along[0], dist_along[-1], 50)
        interp_x, interp_y = interpolate.splev(interp_d, spline)
    else:
        # If interpolation is not needed, use the original convex hull points
        interp_x = x_hull
        interp_y = y_hull

    return interp_x, interp_y
    
# def create_scatter_plot(df, col_x, col_y, col_category, color_palette, col_color, col_size, col_text, title="Scatter Plot", x_axis_label="X-axis", y_axis_label="Y-axis", width=1000, height=1000, xaxis_range=None, yaxis_range=None, 
#     size_value =4, opacity=0.8, maxdisplayed=0, plot_bgcolor=None, paper_bgcolor=None, color="indianred", line_width=0.5, line_color="white", colorscale='Viridis', showscale=True, template="plotly"):
#     """
#     Create a scatter plot : 
#     - df contains all data : X / Y values, category for colorization, sizes and text for hover.
#     - col_x : name of the column containing X values
#     - col_y : name of the column containing Y values
#     - col_category : name of the column for colorization
#     - color_palette : a dict mapping category with color value
#     - col_color : name of the column for color ==> to be used only for continuous scale
#     - col_size : name of the column for dot sizes
#     - col_text : name of the column containing text for legend on hover
#     - title : graph title
#     - x_axis_label : label for X
#     - y_axis_label : label for Y
#     - width / height : size of the graphe
#     - xaxis_range / y_axis_range : range values for axis. None for auto values.
#     - size_value =  minimun size (or constant) for dots 
#     - opacity : dots transparency
#     - maxdisplayed : maximum number of dots to display. 0 = infinite
#     - plot_bgcolor : background color for plot
#     - paper_bgcolor : background color for the area around the plot 
#     - color : color code for dots if col_category is None
#     - line_width : width of dots contours
#     - line_color : color of dots contours
#     """

#     if line_color is None :
#         line_color=color

#     fig = go.Figure()

#     #col_category is used to colorize dots
#     if col_category is not None:
#         for i, category in enumerate(df[col_category].unique()):
#             color = color_palette.get(category, 'rgb(0, 0, 0)')  # Default to black if category not found
            
#             #hovertemplate generation 
#             hovertemplate='<b>'+col_x+'</b>:'+df[df[col_category]==category][col_x].astype(str)+'<br><b>'+col_y+'</b>:'+df[df[col_category]==category][col_y].astype(str)+'<br><b>'+col_category+'</b>:'+str(category)
#             if col_size is None:
#                 size=size_value
#             else:
#                 size = df[df[col_category] == category][col_size]
#                 hovertemplate += '<br><b>'+col_size+'</b>:'+size.astype(str)

#             if col_text is not None:
#                 hovertemplate +='<br><b>'+col_text+'</b>:'+ df[df[col_category]==category][col_text].apply(wrap_text)

#             fig.add_trace(
#                 go.Scatter(
#                     x=df[df[col_category]==category][col_x], 
#                     y=df[df[col_category]==category][col_y], 
#                     mode='markers', 
#                     marker=dict(color=color,                 #dots color
#                                 size=size,                   #dots size
#                                 opacity=opacity,             #dots opacity
#                                 line_color=line_color,       #line color around dot
#                                 line_width=line_width,       #line width around dot
#                                 sizemode='area',
#                                 sizemin = size_value,        #minimum size of dot
#                                 maxdisplayed=maxdisplayed,   #max number of dots to display (0 = infinite)
#                                 symbol = "circle"            #type of dot
#                                 ), 
#                     name=category,                           # trace name
#                     hovertemplate=hovertemplate+"<extra></extra>"
#                     )
#                 )
#     # if there is no category for color, we create a simpler plot
#     else:
#         hovertemplate='<b>'+col_x+'</b>:'+df[col_x].astype(str)+'<br><b>'+col_y+'</b>:'+df[col_y].astype(str)
#         if col_size is None:
#             size=size_value
#         else:
#             size = df[col_size]
#             hovertemplate += '<br><b>'+col_size+'</b>:'+size.astype(str)
#         if col_color is not None :
#             hovertemplate +='<br><b>'+col_color+'</b>:'+df[col_color].astype(str)
#             color = df[col_color]
#         else :
#             if color is None:
#                 color = generate_random_hexadecimal_color()
#         if col_text is not None:
#             hovertemplate +='<br><b>'+col_text+'</b>:'+ df[col_text].apply(wrap_text)

#         fig = go.Figure( go.Scatter(
#                     x=df[col_x], 
#                     y=df[col_y], 
#                     mode='markers', 
#                     marker=dict(color=color,                #dots color
#                                 size=size,                  #dots size
#                                 opacity=opacity,            #dots opacity
#                                 line_color=line_color,      #line color around dot
#                                 line_width=line_width,      #line width arount dot
#                                 sizemode='area',            # Scale marker sizes
#                                 sizemin = size_value,       #minimum size of dot
#                                 maxdisplayed=maxdisplayed,  #max number of dots to display (0 = infinite)
#                                 symbol = "circle",           #type of dot
#                                 colorscale=colorscale,
#                                 showscale=showscale
#                                 ), 
#                     name="",
#                     hovertemplate=hovertemplate+"<extra></extra>"
#                     ))

#     #we calculate X and Y axis ranges. 
#     if yaxis_range is None :
#         yaxis_range=[df[col_y].min()-0.1,df[col_y].max()+0.1]
#     if xaxis_range is None : 
#         xaxis_range = [df[col_x].min()-0.1,df[col_x].max()+0.1]

#     # Update layout
#     fig.update_layout(
#         title=title,                  #graph title
#         xaxis_title=x_axis_label,     #xaxis title
#         yaxis_title=y_axis_label,     #yaxis title
#         width=width,                  #plot size
#         height=height,                #plot size
#         xaxis_showline=False,         #intermediate lines
#         xaxis_showgrid=False,         #grid
#         xaxis_zeroline=False,         #zeroline
#         yaxis_showline=False,         #intermediate lines
#         yaxis_showgrid=False,         #grid
#         yaxis_zeroline=False,         #zeroline
#         yaxis_range = yaxis_range,    #yaxis range
#         xaxis_range = xaxis_range,    #xaxis range
#         template=template,
#         plot_bgcolor=plot_bgcolor,    #background color (plot)
#         paper_bgcolor=paper_bgcolor,   #background color (around plot)
#         font_family="Segoe UI Semibold",           # font

#     )

#     return fig

def create_scatter_plot(df: pd.DataFrame, col_x: str, col_y: str, col_category: str, color_palette: dict, col_color: str, col_size: str, col_text: str, col_legend: list = [], title: str = "Scatter Plot", x_axis_label: str = "X-axis", y_axis_label: str = "Y-axis", width: int = 1000, height: int = 1000, xaxis_range: list =None, yaxis_range: list =None, size_value: int = 4, opacity: float = 0.8, maxdisplayed: int = 0, mode: str = "markers", textposition: str = "bottom center", plot_bgcolor: str = None, paper_bgcolor: str = None, yaxis_showgrid: bool = False, xaxis_showgrid: bool = False, color: str = "indianred", line_width: float = 0.5, line_color: str = "white", colorscale: str = 'Viridis', showscale: bool = True, template: str = "plotly") -> go.Figure:
    """
    Create a scatter plot.

    Args:
        df (pd.DataFrame): DataFrame containing all data.
        col_x (str): Name of the column containing X values.
        col_y (str): Name of the column containing Y values.
        col_category (str): Name of the column for colorization.
        color_palette (dict): A dictionary mapping category with color value.
        col_color (str): Name of the column for color. Only used for continuous scale.
        col_size (str): Name of the column for dot sizes.
        col_text (str): Name of the column containing text for legend on hover.
        col_legend (List[str], optional): List of column names for legend. Defaults to [].
        title (str, optional): Graph title. Defaults to "Scatter Plot".
        x_axis_label (str, optional): Label for X-axis. Defaults to "X-axis".
        y_axis_label (str, optional): Label for Y-axis. Defaults to "Y-axis".
        width (int, optional): Size of the graph. Defaults to 1000.
        height (int, optional): Size of the graph. Defaults to 1000.
        xaxis_range (list, optional): Range values for X-axis. Defaults to None.
        yaxis_range (list, optional): Range values for Y-axis. Defaults to None.
        size_value (int, optional): Minimum size (or constant) for dots. Defaults to 4.
        opacity (float, optional): Dots transparency. Defaults to 0.8.
        maxdisplayed (int, optional): Maximum number of dots to display. 0 = infinite. Defaults to 0.
        mode (str, optional): Mode for the scatter plot. Defaults to "markers".
        textposition (str, optional): Text position for hover. Defaults to "bottom center".
        plot_bgcolor (str, optional): Background color for plot. Defaults to None.
        paper_bgcolor (str, optional): Background color for the area around the plot. Defaults to None.
        yaxis_showgrid (bool, optional): Whether to show grid on Y-axis. Defaults to False.
        xaxis_showgrid (bool, optional): Whether to show grid on X-axis. Defaults to False.
        color (str, optional): Color code for dots if col_category is None. Defaults to "indianred".
        line_width (float, optional): Width of dots contours. Defaults to 0.5.
        line_color (str, optional): Color of dots contours. Defaults to "white".
        colorscale (str, optional): Color scale for continuous color mapping. Defaults to 'Viridis'.
        showscale (bool, optional): Whether to show color scale. Defaults to True.
        template (str, optional): Plotly template. Defaults to "plotly".

    Returns:
        go.Figure: Plotly scatter plot figure.
    """

    if line_color is None :
        line_color=color

    fig = go.Figure()

    #col_category is used to colorize dots
    if col_category is not None:
        for i, category in enumerate(df[col_category].unique()):
            color = color_palette.get(category, 'rgb(0, 0, 0)')  # Default to black if category not found
            
            #hovertemplate generation 
            hovertemplate='<b>'+col_x+'</b>:'+df[df[col_category]==category][col_x].astype(str)+'<br><b>'+col_y+'</b>:'+df[df[col_category]==category][col_y].astype(str)+'<br><b>'+col_category+'</b>:'+str(category)
            if col_size is None:
                size=size_value
            else:
                size = df[df[col_category] == category][col_size]
                hovertemplate += '<br><b>'+col_size+'</b>:'+size.astype(str)

            if len(col_legend)>0:
                for c in col_legend:
                    hovertemplate +='<br><b>'+str(c)+'</b>:'+ df[df[col_category]==category][c].astype(str).apply(wrap_text)

            fig.add_trace(
                go.Scatter(
                    x=df[df[col_category]==category][col_x], 
                    y=df[df[col_category]==category][col_y], 
                    mode=mode, 
                    text = df[df[col_category]==category][col_text],
                    textposition=textposition,
                    marker=dict(color=color,                 #dots color
                                size=size,                   #dots size
                                opacity=opacity,             #dots opacity
                                line_color=line_color,       #line color around dot
                                line_width=line_width,       #line width around dot
                                sizemode='area',
                                sizemin = size_value,        #minimum size of dot
                                maxdisplayed=maxdisplayed,   #max number of dots to display (0 = infinite)
                                symbol = "circle"            #type of dot
                                ), 
                    name=category,                           # trace name
                    hovertemplate=hovertemplate+"<extra></extra>"
                    )
                )
    # if there is no category for color, we create a simpler plot
    else:
        hovertemplate='<b>'+col_x+'</b>:'+df[col_x].astype(str)+'<br><b>'+col_y+'</b>:'+df[col_y].astype(str)
        if col_size is None:
            size=size_value
        else:
            size = df[col_size]
            hovertemplate += '<br><b>'+col_size+'</b>:'+size.astype(str)
        if col_color is not None :
            hovertemplate +='<br><b>'+col_color+'</b>:'+df[col_color].astype(str)
            color = df[col_color]
        else :
            if color is None:
                color = generate_random_hexadecimal_color()
        if len(col_legend)>0:
            for c in col_legend:
                hovertemplate +='<br><b>'+str(c)+'</b>:'+ df[c].astype(str).apply(wrap_text)

        fig = go.Figure( go.Scatter(
                    x=df[col_x], 
                    y=df[col_y], 
                    mode=mode, 
                    text = df[col_text],
                    textposition=textposition,
                    marker=dict(color=color,                #dots color
                                size=size,                  #dots size
                                opacity=opacity,            #dots opacity
                                line_color=line_color,      #line color around dot
                                line_width=line_width,      #line width arount dot
                                sizemode='area',            # Scale marker sizes
                                sizemin = size_value,       #minimum size of dot
                                maxdisplayed=maxdisplayed,  #max number of dots to display (0 = infinite)
                                symbol = "circle",           #type of dot
                                colorscale=colorscale,
                                showscale=showscale
                                ), 
                    name="",
                    hovertemplate=hovertemplate+"<extra></extra>"
                    ))

    #we calculate X and Y axis ranges. 
    if yaxis_range is None :
        yaxis_range=[df[col_y].min()- 0.1,df[col_y].max() +  0.1]
    if yaxis_range == "auto":
        yaxis_range=None
    
    if xaxis_range is None : 
        xaxis_range = [df[col_x].min()- 0.1,df[col_x].max()+ 0.1]
    if xaxis_range =="auto":
        xaxis_range=None

    # Update layout
    fig.update_layout(
        title=title,                  #graph title
        xaxis_title=x_axis_label,     #xaxis title
        yaxis_title=y_axis_label,     #yaxis title
        width=width,                  #plot size
        height=height,                #plot size
        xaxis_showgrid=xaxis_showgrid,         #grid
        yaxis_showgrid=yaxis_showgrid,         #grid
        yaxis_range = yaxis_range,    #yaxis range
        xaxis_range = xaxis_range,    #xaxis range
        template=template,
        plot_bgcolor=plot_bgcolor,    #background color (plot)
        paper_bgcolor=paper_bgcolor,   #background color (around plot)
        font_family="Segoe UI Semibold",           # font

    )
    return fig

def add_annotations(fig: go.Figure, df: pd.DataFrame, col_x: str, col_y: str, col_txt: str, width: int = 1000, label_size_ratio: int = 100, bordercolor: str = "#C7C7C7", arrowcolor: str = "SlateGray", bgcolor: str = "#FFFFFF", font_color: str = "SlateGray") -> go.Figure:
    """
    Add annotations to a Plotly figure.

    Args:
        fig (go.Figure): Plotly figure object.
        df (pd.DataFrame): DataFrame containing annotation data.
        col_x (str): Name of the column containing X values.
        col_y (str): Name of the column containing Y values.
        col_txt (str): Name of the column containing text for annotations.
        width (int, optional): Width of the figure. Defaults to 1000.
        label_size_ratio (int, optional): Ratio of label size to figure width. Defaults to 100.
        bordercolor (str, optional): Color of annotation borders. Defaults to "#C7C7C7".
        arrowcolor (str, optional): Color of annotation arrows. Defaults to "SlateGray".
        bgcolor (str, optional): Background color of annotations. Defaults to "#FFFFFF".
        font_color (str, optional): Color of annotation text. Defaults to "SlateGray".

    Returns:
        go.Figure: Plotly figure object with annotations added.
    """
    df[col_txt] = df[col_txt].fillna("").astype(str)

    for i, row in df.iterrows():
        fig.add_annotation(
            x=row[col_x],
            y=row[col_y],
            text='<b>'+wrap_text(row[col_txt])+'</b>',
            showarrow=True,
            arrowhead=1,
            font=dict(
                family="Helvetica, Sans-serif",
                size=width / label_size_ratio,
                color=font_color
            ),
            bordercolor=bordercolor,
            borderwidth=width / 1000,
            borderpad=width / 500,
            bgcolor=bgcolor,
            opacity=1,
            arrowcolor=arrowcolor
        )

    return fig

def scatter3D(df: pd.DataFrame, col_x: str, col_y: str, col_z: str, col_category: str, color_palette: dict, col_size: str, col_text: str, title: str = "3D Scatter Plot", x_axis_label: str = "X-axis", y_axis_label: str = "Y-axis", z_axis_label: str = "Z-axis", width: int = 1000, height: int = 1000, xaxis_range: list = None, yaxis_range: list = None, zaxis_range: list = None, size_value: int = 4, opacity: float = 0.8, plot_bgcolor: str = None, paper_bgcolor: str = None, color: str = "indianred", line_width: float = 0.5, line_color: str = "white", template: str = "plotly") -> go.Figure:
    """
    Create a 3D scatter plot.

    Args:
        df (pd.DataFrame): DataFrame containing all data.
        col_x (str): Name of the column containing X values.
        col_y (str): Name of the column containing Y values.
        col_z (str): Name of the column containing Z values.
        col_category (str): Name of the column for colorization.
        color_palette (dict): A dictionary mapping categories with color values.
        col_size (str): Name of the column for dot sizes.
        col_text (str): Name of the column containing text for legend on hover.
        title (str, optional): Graph title. Defaults to "3D Scatter Plot".
        x_axis_label (str, optional): Label for X-axis. Defaults to "X-axis".
        y_axis_label (str, optional): Label for Y-axis. Defaults to "Y-axis".
        z_axis_label (str, optional): Label for Z-axis. Defaults to "Z-axis".
        width (int, optional): Width of the graph. Defaults to 1000.
        height (int, optional): Height of the graph. Defaults to 1000.
        xaxis_range (list, optional): Range values for the X-axis. Defaults to None.
        yaxis_range (list, optional): Range values for the Y-axis. Defaults to None.
        zaxis_range (list, optional): Range values for the Z-axis. Defaults to None.
        size_value (int, optional): Minimum size (or constant) for dots. Defaults to 4.
        opacity (float, optional): Dots transparency. Defaults to 0.8.
        plot_bgcolor (str, optional): Background color for the plot. Defaults to None.
        paper_bgcolor (str, optional): Background color for the area around the plot. Defaults to None.
        color (str, optional): Color code for dots if col_category is None. Defaults to "indianred".
        line_width (float, optional): Width of dots contours. Defaults to 0.5.
        line_color (str, optional): Color of dots contours. Defaults to "white".
        template (str, optional): Plotly template. Defaults to "plotly".

    Returns:
        go.Figure: Plotly figure object.
    """
    fig=go.Figure()
    if col_category is not None:
        for i, category in enumerate(df[col_category].unique()):
            color = color_palette.get(category, 'rgb(0, 0, 0)')  # Default to black if category not found

            #hovertemplate generation 
            hovertemplate='<b>X</b>:'+df[df[col_category]==category][col_x].astype(str)+'<br><b>Y</b>:'+df[df[col_category]==category][col_y].astype(str)+'<br><b>Z</b>:'+df[df[col_category]==category][col_z].astype(str)+'<br><b>'+col_category+'</b>:'+str(category)
            if col_size is None:
                size=size_value
            else:
                size = df[df[col_category] == category][col_size]
                hovertemplate += '<br><b>'+col_size+'</b>:'+size.astype(str)

            if col_text is not None:
                hovertemplate +='<br><b>'+col_text+'</b>:'+ df[df[col_category]==category][col_text].apply(wrap_text)

            fig.add_trace(
                go.Scatter3d(
                    x=df[df[col_category]==category][col_x], 
                    y=df[df[col_category]==category][col_y], 
                    z=df[df[col_category]==category][col_z], 
                    mode='markers', 
                    marker=dict(color=color,                 #dots color
                                size=size,                   #dots size
                                opacity=opacity,             #dots opacity
                                line_color=line_color,          #line color around dot
                                line_width=line_width,              #line width around dot
                                sizemin = size_value,        #minimum size of dot
                                symbol = "circle"            #type of dot
                                ), 
                    name=category,                           # trace name
                    hovertemplate=hovertemplate+"<extra></extra>"
                    )
                )
    else:
        #hovertemplate creation
        hovertemplate='<b>X</b>:'+df[col_x].astype(str)+'<br><b>Y</b>:'+df[col_y].astype(str)+'<br><b>Z</b>:'+df[col_z].astype(str)
        if col_size is None:
            size=size_value
        else:
            size = df[col_size]
            hovertemplate += '<br><b>'+col_size+'</b>:'+size.astype(str)
        if col_text is not None:
            hovertemplate +='<br><b>'+col_text+'</b>:'+ df[col_text].apply(wrap_text)

        fig = go.Figure( go.Scatter3d(
                    x=df[col_x], 
                    y=df[col_y],
                    z=df[col_z], 
                    mode='markers', 
                    marker=dict(color=color,                #dots color
                                size=size,                  #dots size
                                opacity=opacity,            #dots opacity
                                line_color=line_color,         #line color around dot
                                line_width=line_width,             #line width arount dot
                                sizemin = size_value,       #minimum size of dot
                                symbol = "circle"           #type of dot
                                ), 
                    name="",
                    hovertemplate=hovertemplate+"<extra></extra>"
                    ))


    #we calculate X and Y axis ranges. 
    if yaxis_range is None :
        yaxis_range=[df[col_y].min()-0.1,df[col_y].max()+0.1]
    if xaxis_range is None : 
        xaxis_range = [df[col_x].min()-0.1,df[col_x].max()+0.1]
    if zaxis_range is None : 
        zaxis_range = [df[col_z].min()-0.1,df[col_z].max()+0.1]
    fig.update_layout(
        
        font_family="Segoe UI Semibold",           # font
        title=title,                  #graph title
        xaxis_title=x_axis_label,     #xaxis title
        yaxis_title=y_axis_label,     #yaxis title
        zaxis_title=z_axis_label,     #zaxis title
        width=width,                  #plot size
        height=height,                #plot size
        xaxis_showline=False,         #intermediate lines
        xaxis_showgrid=False,         #grid
        xaxis_zeroline=False,         #zeroline
        yaxis_showline=False,         #intermediate lines
        yaxis_showgrid=False,         #grid
        yaxis_zeroline=False,         #zeroline
        zaxis_showline=False,         #intermediate lines
        zaxis_showgrid=False,         #grid
        zaxis_zeroline=False,         #zeroline
        scene_yaxis_range = yaxis_range,    #yaxis range
        scene_xaxis_range = xaxis_range,    #xaxis range
        scene_zaxis_range = zaxis_range,    #zaxis range
        scene_camera = dict(               #camera orientation at start
            up=dict(x=1, y=0, z=2),        
            center=dict(x=0, y=0, z=0),
            eye=dict(x=2, y=1.25, z=0.5)
        ),
        template=template,
        plot_bgcolor=plot_bgcolor,    #background color (plot)
        paper_bgcolor=paper_bgcolor,   #background color (around plot)
        margin=dict(
                    t=width / 15,
                    b=width / 25,
                    r=width / 25,
                    l=width / 25,
                ),
        legend=dict(   
            orientation="h",
            yanchor="bottom",
            y=-0.12,
            xanchor="right",
            x=1,
            itemsizing= 'constant'
        )
    )

    return fig
    

def fig_bar_trend(df: pd.DataFrame, col_x: str, bar_measure: str, trend_measure: str, x_name: str = "X", bar_name: str = "metric1", trend_name: str = "metric2", marker_color: str = 'lightpink', line_color: str = 'indianred', title_text: str = "Couverture & Résonance", width: int = 1500, height: int = 700, xaxis_tickangle: int = 0, opacity: float = 0.8, plot_bgcolor: str = None, paper_bgcolor: str = None, template: str = "plotly") -> go.Figure:
    """
    Display a graph that combines bar and trend chart to compare 2 metrics.

    Args:
        df (pd.DataFrame): DataFrame containing all data.
        col_x (str): Name of the column containing X values.
        bar_measure (str): Data represented as bar diagram.
        trend_measure (str): Data represented as trend line.
        x_name (str, optional): Label for X-axis. Defaults to "X".
        bar_name (str, optional): Label for the bar measure. Defaults to "metric1".
        trend_name (str, optional): Label for the trend measure. Defaults to "metric2".
        marker_color (str, optional): Color code for bars. Defaults to 'lightpink'.
        line_color (str, optional): Color code for trend line. Defaults to 'indianred'.
        title_text (str, optional): Graph title. Defaults to "Couverture & Résonance".
        width (int, optional): Width of the graph. Defaults to 1500.
        height (int, optional): Height of the graph. Defaults to 700.
        xaxis_tickangle (int, optional): Angle for x ticks. Defaults to 0.
        opacity (float, optional): Opacity of bars. Defaults to 0.8.
        plot_bgcolor (str, optional): Background color for the plot. Defaults to None.
        paper_bgcolor (str, optional): Background color for the area around the plot. Defaults to None.
        template (str, optional): Plotly template. Defaults to "plotly".

    Returns:
        go.Figure: Plotly figure object.
    """

    # nk = np.empty(shape=(len(x), 3, 1), dtype="object")
    # nk[:, 0] = np.array(x.apply(lambda txt: '<br>'.join(textwrap.wrap(str(txt), width=50)))).reshape(-1, 1)
    # nk[:, 1] = np.array(bar_measure).reshape(-1, 1)
    # nk[:, 2] = np.array(trend_measure).reshape(-1, 1)

    fig = make_subplots(specs=[[{"secondary_y": True}]])

    fig.add_trace(
        go.Scatter(
            x=df[col_x].apply(wrap_text), 
            y=df[trend_measure], 
            name=trend_name,
            mode='lines', 
            line_color=line_color, 
            line_width=4,
            textfont=dict(size=8),
            # customdata=nk,
            hovertemplate=("<br>"+x_name+" :"+df[col_x].astype(str)+"<br>"+bar_name+" - "+df[bar_measure].astype(str)+"<br>"+trend_name+" : "+df[trend_measure].astype(str)+"<extra></extra>"),
        ),
        secondary_y=True,
    )
    # Add traces
    fig.add_trace(
        go.Bar(
            x=df[col_x].apply(wrap_text), 
            y = df[bar_measure], 
            name=bar_name, 
            marker_color=marker_color, 
            opacity=opacity,
            # customdata=nk,
            hovertemplate=("<br>"+x_name+" :"+df[col_x].astype(str)+"<br>"+bar_name+" - "+df[bar_measure].astype(str)+"<br>"+trend_name+" : "+df[trend_measure].astype(str)+"<extra></extra>"),
        ),
        secondary_y=False,

    )
    first_axis_range=[-0.5,df[bar_measure].max()*1.01]
    secondary_axis_range=[-0.5,df[trend_measure].max()*1.01]

    # Add figure title
    fig.update_layout(
        
        title_text=title_text, 
        showlegend=True,
        width = width,
        height= height,
        xaxis_tickangle=xaxis_tickangle,
        xaxis_showline=False,
        xaxis_showgrid=False,
        yaxis_showline=False,
        yaxis_showgrid=False,
        font_family="Segoe UI Semibold",
        template=template,
        plot_bgcolor=plot_bgcolor,    #background color (plot)
        paper_bgcolor=paper_bgcolor,   #background color (around plot)
        margin=dict(
                    t=width / 15,
                    b=width / 20,
                    r=width / 20,
                    l=width / 20,
                ),
    )

    # # Set x-axis title
    fig.update_xaxes(title_text=x_name)

    # Set y-axes titles
    fig.update_yaxes(title_text=bar_name, range = first_axis_range, secondary_y=False)
    fig.update_yaxes(title_text=trend_name, range = secondary_axis_range, secondary_y=True)  
    
    return fig


# def fig_bar_trend(x, bar_measure, trend_measure, x_name="X", bar_name ="metric1", trend_name = "metric2", marker_color='lightpink', line_color='indianred', title_text="Couverture & Résonance", width=1500, height=700, xaxis_tickangle=0, opacity=0.8, plot_bgcolor=None, paper_bgcolor=None, template = "plotly"):
#     """
#     Display a graph that combine bar and trend chart to compare 2 metrics :
#     - x = x axis data
#     - bar_measure = data represented as bar diagram
#     - trend_measure = data represented as trend line
#     - x_name / bar_name / trend_name : axis labels
#     - marker_color = color code for bars
#     - line_color = color code for trend line
#     - title_text = graph title
#     - width / height = size of plot
#     - xaxis_tickangle =  angle for x ticks
#     - opacity = opacity of bars
#     """

#     nk = np.empty(shape=(len(x), 3, 1), dtype="object")
#     nk[:, 0] = np.array(x.apply(lambda txt: '<br>'.join(textwrap.wrap(str(txt), width=50)))).reshape(-1, 1)
#     nk[:, 1] = np.array(bar_measure).reshape(-1, 1)
#     nk[:, 2] = np.array(trend_measure).reshape(-1, 1)

#     fig = make_subplots(specs=[[{"secondary_y": True}]])

#     fig.add_trace(
#         go.Scatter(
#             x=x, 
#             y=trend_measure, 
#             name=trend_name,
#             mode='lines', 
#             line_color=line_color, 
#             line_width=4,
#             textfont=dict(size=8),
#             customdata=nk,
#             hovertemplate=("<br>"+x_name+" :%{customdata[0]}<br>"+bar_name+" - %{customdata[1]}<br>"+trend_name+":%{customdata[2]}"+"<extra></extra>"),
#         ),
#         secondary_y=True,
#     )
#     # Add traces
#     fig.add_trace(
#         go.Bar(
#             x=x, 
#             y = bar_measure, 
#             name=bar_name, 
#             marker_color=marker_color, 
#             opacity=opacity,
#             hovertemplate=("<br>"+x_name+" :%{customdata[0]}<br>"+bar_name+" - %{customdata[1]}<br>"+trend_name+":%{customdata[2]}"+"<extra></extra>"),
#         ),
#         secondary_y=False,

#     )
#     first_axis_range=[-0.5,bar_measure.max()*1.01]
#     secondary_axis_range=[-0.5,trend_measure.max()*1.01]

#     # Add figure title
#     fig.update_layout(
        
#         title_text=title_text, 
#         showlegend=True,
#         width = width,
#         height= height,
#         xaxis_tickangle=xaxis_tickangle,
#         xaxis_showline=False,
#         xaxis_showgrid=False,
#         yaxis_showline=False,
#         yaxis_showgrid=False,
#         font_family="Segoe UI Semibold",
#         template=template,
#         plot_bgcolor=plot_bgcolor,    #background color (plot)
#         paper_bgcolor=paper_bgcolor,   #background color (around plot)
#         margin=dict(
#                     t=width / 15,
#                     b=width / 20,
#                     r=width / 20,
#                     l=width / 20,
#                 ),
#     )

#     # # Set x-axis title
#     fig.update_xaxes(title_text=x_name)

#     # Set y-axes titles
#     fig.update_yaxes(title_text=bar_name, range = first_axis_range, secondary_y=False)
#     fig.update_yaxes(title_text=trend_name, range = secondary_axis_range, secondary_y=True)  
    
#     return fig


def density_map(df_posts: pd.DataFrame,
                df_dots: pd.DataFrame,
                df_topics: pd.DataFrame,
                col_topic: str,
                col_engagement: str,
                col_text: str,
                col_text_dots: str,
                colorscale: str = "Portland",
                marker_color: str = "#ff7f0e",
                arrow_color: str = "#ff7f0e",
                width: int = 1000,
                height: int = 1000,
                show_text: bool = True,
                show_topics: bool = True,
                show_halo: bool = False,
                show_histogram: bool = True,
                label_size_ratio: int = 100,
                n_words: int = 3,
                title_text: str = "Clustering",
                max_dots_displayed: int = 0,
                max_topics_displayed: int = 20,
                opacity: float = 0.3,
                plot_bgcolor: str = None,
                paper_bgcolor: str = None,
                template: str = "plotly") -> go.Figure:
    """
    Display a 2D histogram with contours and scattered dots.

    Args:
        df_posts (pd.DataFrame): DataFrame containing all data points to plot (corresponding to contours).
        df_dots (pd.DataFrame): DataFrame containing a sample of points to plot as dots.
        df_topics (pd.DataFrame): DataFrame containing topics representations.
        col_topic (str): Column name corresponding to category.
        col_engagement (str): Column name corresponding to a metric.
        col_text (str): Column name corresponding to a text separated by |.
        col_text_dots (str): Column name corresponding to the text for dots.
        colorscale (str, optional): Possible values are https://plotly.com/python/builtin-colorscales/. Defaults to "Portland".
        marker_color (str, optional): Dots color value. Defaults to "#ff7f0e".
        arrow_color (str, optional): Arrow pointing to topic centroid color value. Defaults to "#ff7f0e".
        width (int, optional): Width of the plot. Defaults to 1000.
        height (int, optional): Height of the plot. Defaults to 1000.
        show_text (bool, optional): Show dots. Defaults to True.
        show_topics (bool, optional): Show topics labels. Defaults to True.
        show_halo (bool, optional): Show circles around topics. Defaults to False.
        show_histogram (bool, optional): Show 2D histogram with contours. Defaults to True.
        label_size_ratio (int, optional): Influence the size of the topics labels. Higher value means smaller topics labels. Defaults to 100.
        n_words (int, optional): Number of words to display. Defaults to 3.
        title_text (str, optional): Graph title. Defaults to "Clustering".
        max_dots_displayed (int, optional): Number of dots to display. Defaults to 0.
        max_topics_displayed (int, optional): Number of topics to display. Defaults to 20.
        opacity (float, optional): Opacity of dots. Defaults to 0.3.
        plot_bgcolor (str, optional): Background color for the plot. Defaults to None.
        paper_bgcolor (str, optional): Background color for the area around the plot. Defaults to None.
        template (str, optional): Plotly template. Defaults to "plotly".

    Returns:
        go.Figure: Plotly figure object.
    """

    # df_topics = df_distrib_sample.copy()
    df_topics= df_topics.dropna(subset=col_text)
    df_topics['text_bunka']= df_topics[col_text].apply(lambda x : "|".join(x.split('|')[:n_words]))
    

    if (max_topics_displayed>0) and (max_topics_displayed < len(df_topics[col_topic].unique())):
        df_topics= df_topics.sample(max_topics_displayed)

    #on  crée l'histogramme principal
    if show_histogram:
        fig_density = go.Figure(
                go.Histogram2dContour(
                    x=df_posts['x'],
                    y=df_posts['y'],
                    colorscale=colorscale,
                    showscale=False,
                    hoverinfo="none"
                )
            )
    else : 
        fig_density = go.Figure()

    #paramètre des contours
    fig_density.update_traces(
        contours_coloring="fill", contours_showlabels=False
    )

    #paramètres cosmetiques
    fig_density.update_layout(
                font_size=25,
                width=width,
                height=height,
                margin=dict(
                    t=width / 15,
                    b=width / 25,
                    r=width / 25,
                    l=width / 25,
                ),
                title=dict(text=title_text, font=dict(size=width / 40)),
                xaxis=dict(showline=False, zeroline=False, showgrid=False, showticklabels=False),
                yaxis=dict(showline=False, zeroline=False, showgrid=False, showticklabels=False),
            )

    # création de la légende de chaque points
    nk = np.empty(shape=(len(df_dots), 3, 1), dtype="object")
    nk[:, 0] = np.array(df_dots[col_topic]).reshape(-1, 1)
    nk[:, 1] = np.array(df_dots[col_text_dots].apply(lambda txt: '<br>'.join(textwrap.wrap(txt, width=50)))).reshape(-1, 1)
    nk[:, 2] = np.array(df_dots[col_engagement]).reshape(-1, 1)

    # ajout des points
    if show_text:
        fig_density.add_trace(
            go.Scatter(
                x=df_dots['x'],
                y=df_dots['y'],
                mode="markers",
                marker=dict(opacity=opacity, 
                            color=marker_color, 
                            maxdisplayed=max_dots_displayed
                            ),
                customdata=nk,
                hovertemplate=("<br>%{customdata[1]}<br>Engagements: %{customdata[2]}"+"<extra></extra>"),
                name="",
                
            )
        )

    if show_topics:
        # Afficher les topics
        for i, row in df_topics.iterrows():
            fig_density.add_annotation(
                x=row['topic_x'],
                y=row['topic_y'],
                # text="|".join(row['top_keywords'].split('|')[:n_words]),
                text=str(row['text_bunka']),
                showarrow=True,
                arrowhead=1,
                font=dict(
                    family="Segoe UI Semibold",
                    size=width / label_size_ratio,
                    color="blue",
                ),
                bordercolor="#c7c7c7",
                borderwidth=width / 1000,
                borderpad=width / 500,
                bgcolor="white",
                opacity=1,
                arrowcolor=arrow_color,
            )
    if show_halo:
        for i, row in df_posts.groupby(col_topic):
            x_hull, y_hull = get_convex_hull_coord(np.array(row[['x','y']]))
                
            # Create a Scatter plot with the convex hull coordinates
            trace = go.Scatter(
                x=x_hull,
                y=y_hull,
                mode="lines",
                name="Convex Hull",
                line=dict(color="grey", dash="dot"),
                hoverinfo="none",
            )
            fig_density.add_trace(trace)

    fig_density.update_layout(showlegend=False, 
                              width=width, 
                              height=height, 
                              template=template,
                              plot_bgcolor=plot_bgcolor,    #background color (plot)
                              paper_bgcolor=paper_bgcolor,   #background color (around plot)
                            )


    return fig_density



def topic_heatmap(df: pd.DataFrame,
                  col_x: str = "topic_x",
                  col_y: str = "topic_y",
                  col_topic: str = "soft_topic",
                  color_continuous_scale: str = 'GnBu',
                  title: str = "Similarity between topics") -> go.Figure:
    """
    Display a heatmap representing the similarity between topics.

    Args:
        df (pd.DataFrame): DataFrame containing the topic data.
        col_x (str, optional): Column name for x-axis coordinates. Defaults to "topic_x".
        col_y (str, optional): Column name for y-axis coordinates. Defaults to "topic_y".
        col_topic (str, optional): Column name for the topic labels. Defaults to "soft_topic".
        color_continuous_scale (str, optional): Plotly color scale. Defaults to 'GnBu'.
        title (str, optional): Title of the heatmap. Defaults to "Similarity between topics".

    Returns:
        go.Figure: Plotly figure object representing the heatmap.
    """

    distance_matrix = cosine_similarity(np.array(df[[col_x,col_y]]))

    fig = px.imshow(distance_matrix,
                        labels=dict(color="Similarity Score"),
                        x=df[col_topic].astype(int).sort_values().astype(str),
                        y=df[col_topic].astype(int).sort_values().astype(str),
                        color_continuous_scale=color_continuous_scale
                        )

    fig.update_layout(
        title={
            'text': title,
            'y': .95,
            'x': 0.55,
            'xanchor': 'center',
            'yanchor': 'top',
            'font': dict(
                size=22,
                color="Black")
        },
        width=1000,
        height=1000,
        hoverlabel=dict(
            bgcolor="white",
            font_size=16,
            font_family="Rockwell"
        ),
    )
    fig.update_layout(showlegend=True)
    fig.update_layout(legend_title_text='Trend')
    return fig

def generate_wordcloud(df: pd.DataFrame,
                       col_word: str,
                       col_metric: str,
                       width: int = 3000,
                       height: int = 1500,
                       dpi: int = 300,
                       background_color: str = 'white',
                       font_path: str = "font/SEGUIEMJ.TTF",
                       colormap: str = "Viridis",
                       show: bool = False) -> WordCloud:
    """
    Generate a word cloud from a DataFrame.

    Args:
        df (pd.DataFrame): DataFrame containing word frequency data.
        col_word (str): Column name containing words.
        col_metric (str): Column name containing frequency metrics for each word.
        width (int, optional): Width of the word cloud image. Defaults to 3000.
        height (int, optional): Height of the word cloud image. Defaults to 1500.
        dpi (int, optional): Dots per inch for image resolution. Defaults to 300.
        background_color (str, optional): Background color of the word cloud image. Defaults to 'white'.
        font_path (str, optional): Path to the font file to be used in the word cloud. Defaults to "font/SEGUIEMJ.TTF".
        colormap (str, optional): Colormap for the word cloud image. Defaults to "Viridis".
        show (bool, optional): Whether to display the word cloud image. Defaults to False.

    Returns:
        WordCloud: WordCloud object representing the generated word cloud.
    """
    
    top_n_words={row[col_word]:row[col_metric] for i,row in df.iterrows()}
    
    # Generate a wordcloud of the top n words
    wordcloud = WordCloud(width=width, height=height, background_color=background_color, font_path = font_path, colormap = colormap, prefer_horizontal=1).generate_from_frequencies(top_n_words)
    if show : 
        plt.figure(figsize=(width/dpi, height/dpi), dpi=dpi)
        plt.imshow(wordcloud, interpolation='bilinear')
        plt.axis('off')
        plt.show()
    return wordcloud

def create_radar(df: pd.DataFrame,
                 col_topic: str,
                 col_metrics: list,
                 title: str = "Radar",
                 opacity: float = 0.6,
                 width: int = 1000,
                 height: int = 1000,
                 template: str = "ggplot2",
                 plot_bgcolor: str = None,
                 paper_bgcolor: str = None) -> go.Figure:
    """
    Create a radar chart.

    Args:
        df (pd.DataFrame): DataFrame containing data for radar chart.
        col_topic (str): Column name containing topics.
        col_metrics (List[str]): List of column names containing metric values.
        title (str, optional): Title of the radar chart. Defaults to "Radar".
        opacity (float, optional): Opacity of radar area. Defaults to 0.6.
        width (int, optional): Width of the radar chart. Defaults to 1000.
        height (int, optional): Height of the radar chart. Defaults to 1000.
        template (str, optional): Plotly template to use. Defaults to "ggplot2".
        plot_bgcolor (Optional[str], optional): Background color of the plot. Defaults to None.
        paper_bgcolor (Optional[str], optional): Background color of the paper. Defaults to None.

    Returns:
        go.Figure: Plotly Figure object representing the radar chart.
    """

    df = df[[col_topic] + col_metrics]
    col_metrics.append(col_metrics[0])

    fig = go.Figure()
    for topic in list(df[col_topic].unique()) :

        data = df[df[col_topic]==topic].drop(columns=[col_topic]).values.tolist()[0]
        data.append(data[0])
        fig.add_trace(
            go.Scatterpolar(
                r=data,
                theta=col_metrics,
                fill="toself",
                fillcolor=None,
                name=topic,
                opacity=opacity            
                )
            )

    fig.update_layout(
        polar=dict(
                    angularaxis_showgrid=False,   # remove the axis
                    radialaxis=dict(
                    gridwidth=0,
                    gridcolor=None,
                    tickmode='array',  # Set tick mode to 'array'
                    tickvals=[0, 2, 4, 6, 8, 10],  # Specify tick values
                    showticklabels=True,  # Show tick labels
                    visible=True,
                    range=[0, 10],
                ),
                gridshape='linear',
                # bgcolor="white",
                ),
        showlegend=True,
        font_family="Segoe UI Semibold",
        font_color="SlateGrey",
        title=title,             
        width=width,                  #plot size
        height=height,                #plot size
        plot_bgcolor=plot_bgcolor,    #background color (plot)
        paper_bgcolor=paper_bgcolor,   #background color (around plot)
        template=template,
        margin=dict(l=100, r=100, t=100, b=100)
    )
    return fig

def bar_subplots(df: pd.DataFrame,
                 col_x: str,
                 col_y: str,
                 col_cat: str,
                 color_palette: dict = None,
                 n_cols: int = 4,
                 n_top_words: int = 20,
                 horizontal_spacing: float = 0.2,
                 vertical_spacing: float = 0.08,
                 textposition: str = None,
                 color: str = None,
                 title: str = "Top words per topic",
                 template: str = "plotly",
                 bargap: float = 0.4,
                 width: int = 500,
                 height: int = 35,
                 plot_bgcolor: str = None,
                 paper_bgcolor: str = None,
                 showlegend: bool = True) -> go.Figure:
    """
    Create subplots of horizontal bar charts.

    Args:
        df (pd.DataFrame): DataFrame containing data for bar charts.
        col_x (str): Name of the column containing x-axis values.
        col_y (str): Name of the column containing y-axis values.
        col_cat (str): Name of the column containing categories.
        color_palette (Optional[Dict[str, str]], optional): Dictionary mapping categories to colors. Defaults to None.
        n_cols (int, optional): Number of columns in the subplot grid. Defaults to 4.
        n_top_words (int, optional): Number of top words to display in each bar chart. Defaults to 20.
        horizontal_spacing (float, optional): Spacing between subplots horizontally. Defaults to 0.2.
        vertical_spacing (float, optional): Spacing between subplots vertically. Defaults to 0.08.
        textposition (Optional[str], optional): Position of the text relative to the bars ('inside', 'outside', or None). Defaults to None.
        color (Optional[str], optional): Color of the bars. Defaults to None.
        title (str, optional): Title of the subplot. Defaults to "Top words per topic".
        template (str, optional): Plotly template to use. Defaults to "plotly".
        bargap (float, optional): Space between bars in the same cluster. Defaults to 0.4.
        width (int, optional): Width of each subplot. Defaults to 500.
        height (int, optional): Height of each bar in the subplot. Defaults to 35.
        plot_bgcolor (Optional[str], optional): Background color of the plot. Defaults to None.
        paper_bgcolor (Optional[str], optional): Background color of the paper. Defaults to None.
        showlegend (bool, optional): Whether to display the legend. Defaults to True.

    Returns:
        go.Figure: Plotly Figure object representing the subplots of horizontal bar charts.
    """
    categories = df[col_cat].unique()

    # user define a number of columns, we compute the number of rows requires
    n_rows =  math.ceil(len(categories) / n_cols)

    # fine tune parameter according to the text position provided
    if textposition == 'inside':
        horizontal_spacing = (horizontal_spacing / n_cols)/2
    else:
        horizontal_spacing = (horizontal_spacing / n_cols)
        
    # create subplots
    fig = make_subplots(
        rows = n_rows,                           # number of rows
        cols = n_cols,                           # number of columns
        subplot_titles = list(categories),       # title for each subplot
        vertical_spacing = vertical_spacing / n_rows,     # space between subplots
        horizontal_spacing = horizontal_spacing  # space between subplots
        )

    # create bar traces for each subplot
    row_id = 0
    col_id = 0
    for i, category in enumerate(categories):
        
        # define bar color or create a random color
        if color_palette:
            color = color_palette.get(category, generate_random_hexadecimal_color())
        else : 
            if color is None:
                color = generate_random_hexadecimal_color()

        # define row and column position
        col_id +=1 
        if i % n_cols == 0:
            row_id += 1
        if col_id > n_cols:
            col_id = 1

        # select data
        current_df = df[df[col_cat]==category].sort_values(by=col_x, ascending = True)
        hovertemplate='<b>'+current_df[current_df[col_cat]==category][col_y].astype(str)+"</b><br>"+current_df[current_df[col_cat]==category][col_x].astype(str)

        if textposition == 'inside':
            showticklabels = False
            text=current_df[col_y].head(n_top_words)
        else:
            showticklabels = True
            textposition="auto"
            text=None

        fig.add_trace(
            go.Bar(
                x=current_df[col_x].tail(n_top_words), 
                y=current_df[col_y].tail(n_top_words),
                orientation='h',                                # horizontal bars
                name=category,                                  # trace name for legend
                text=text,                                      # text to display
                textposition=textposition,                      # text position
                textangle=0,                                    # text angle
                marker_color = color,                           # bar color
                hovertemplate=hovertemplate+"<extra></extra>"   # hover info
                ),
            row=row_id, 
            col=col_id
            )

    fig.update_layout(
        height = n_rows * n_top_words * height,    # height depending on the number of rows and words to display
        width = n_cols * width,                    # width depending on the number of cols
        bargap = bargap,                           # space between bars
        uniformtext_minsize=7,                     # Adjust the minimum size of text to avoid overlap
        margin=dict(l=75, r=75, t=75, b=50),       # margins around the plot
        showlegend=showlegend,                     # legend display
        font_family="Segoe UI Semibold",           # font
        template=template,                         # template, possible values : plotly, plotly_white, plotly_dark, ggplot2, seaborn, simple_white, none
        plot_bgcolor=plot_bgcolor,                 # background color (plot)
        paper_bgcolor=paper_bgcolor,               # background color (around plot)
        title_text=title                           # viz title
        )

    fig.update_yaxes(
        showticklabels = showticklabels,          # show text near the bars
        showline=False,                           #intermediate lines
        showgrid=False,                           #grid
        zeroline=False,
        )
    fig.update_xaxes(
        showline=False,         #intermediate lines
        showgrid=False,         #grid
        zeroline=False,
        )
    return fig

def pie_subplots(df: pd.DataFrame,
                 col_x: str,
                 col_y: str,
                 col_cat: str,
                 col_color: str,
                 n_cols: int = 4,
                 horizontal_spacing: float = 0.2,
                 vertical_spacing: float = 0.08,
                 title: str = "Top words per topic",
                 template: str = "plotly",
                 width: int = 500,
                 height: int = 150,
                 plot_bgcolor: str = None,
                 paper_bgcolor: str = None,
                 showlegend: bool = True) -> go.Figure:
    """
    Create subplots of pie charts.

    Args:
        df (pd.DataFrame): DataFrame containing data for pie charts.
        col_x (str): Name of the column containing labels.
        col_y (str): Name of the column containing values.
        col_cat (str): Name of the column containing categories.
        col_color (str): Name of the column containing colors.
        n_cols (int, optional): Number of columns in the subplot grid. Defaults to 4.
        horizontal_spacing (float, optional): Spacing between subplots horizontally. Defaults to 0.2.
        vertical_spacing (float, optional): Spacing between subplots vertically. Defaults to 0.08.
        title (str, optional): Title of the subplot. Defaults to "Top words per topic".
        template (str, optional): Plotly template to use. Defaults to "plotly".
        width (int, optional): Width of each subplot. Defaults to 500.
        height (int, optional): Height of each subplot. Defaults to 150.
        plot_bgcolor (Optional[str], optional): Background color of the plot. Defaults to None.
        paper_bgcolor (Optional[str], optional): Background color of the paper. Defaults to None.
        showlegend (bool, optional): Whether to display the legend. Defaults to True.

    Returns:
        go.Figure: Plotly Figure object representing the subplots of pie charts.
    """    
    categories = df[col_cat].unique()

    # user define a number of columns, we compute the number of rows requires
    n_rows =  math.ceil(len(categories) / n_cols)
        
    specs = [[{'type':'domain'}] * n_cols] * n_rows
    # create subplots
    fig = make_subplots(
        rows=n_rows,
        cols=n_cols,
        subplot_titles=list(categories),
        horizontal_spacing=horizontal_spacing / n_cols,
        vertical_spacing=vertical_spacing / n_rows,
        specs=specs
    )

    # create pie chart subplots
    for i, category in enumerate(categories):
        col_id = i % n_cols + 1
        row_id = i // n_cols + 1 

        current_df = df[df[col_cat] == category]
        hovertemplate = '<b>' + current_df[current_df[col_cat] == category][col_y].astype(str) + "</b><br>" + current_df[current_df[col_cat] == category][col_x].astype(str)

        fig.add_trace(
            go.Pie(
            labels=current_df[col_x],
            values=current_df[col_y],
            name=category,
            hole=.4,
            hovertemplate=hovertemplate+"<extra></extra>",
            marker=dict(colors=list(current_df[col_color])),
            sort=False 
            ),
        row=row_id,
        col=col_id,
        )

    # Update layout and axes
    fig.update_layout(
        height=n_rows * height,
        width=n_cols * width,
        uniformtext_minsize=7,
        margin=dict(l=75, r=75, t=75, b=50),
        showlegend=showlegend,
        font_family="Segoe UI Semibold",
        template=template,
        plot_bgcolor=plot_bgcolor,
        paper_bgcolor=paper_bgcolor,
        title_text=title
    )
    fig.update_yaxes(
        showline=False,
        showgrid=False,
        zeroline=False
    )
    fig.update_xaxes(
        showline=False,
        showgrid=False,
        zeroline=False
    )

    return fig


def horizontal_stacked_bars(df: pd.DataFrame,
                             col_x: str,
                             col_y: str,
                             col_percentage: str,
                             col_cat: str,
                             col_color: str,
                             title_text: str = "Sentiment per topic",
                             width: int = 1200,
                             height: int = 1200,
                             xaxis_tickangle: int = 0,
                             horizontal_spacing: float = 0,
                             vertical_spacing: float = 0.08,
                             plot_bgcolor: str = None,
                             paper_bgcolor: str = None,
                             template: str = "plotly") -> go.Figure:
    """
    Create horizontal stacked bar plots.

    Args:
        df (pd.DataFrame): DataFrame containing data for the bar plots.
        col_x (str): Name of the column containing x-axis values.
        col_y (str): Name of the column containing y-axis values.
        col_percentage (str): Name of the column containing percentage values.
        col_cat (str): Name of the column containing categories.
        col_color (str): Name of the column containing colors.
        title_text (str, optional): Title of the plot. Defaults to "Sentiment per topic".
        width (int, optional): Width of the plot. Defaults to 1200.
        height (int, optional): Height of the plot. Defaults to 1200.
        xaxis_tickangle (int, optional): Angle for x-axis ticks. Defaults to 0.
        horizontal_spacing (float, optional): Spacing between subplots horizontally. Defaults to 0.
        vertical_spacing (float, optional): Spacing between subplots vertically. Defaults to 0.08.
        plot_bgcolor (Optional[str], optional): Background color of the plot. Defaults to None.
        paper_bgcolor (Optional[str], optional): Background color of the paper. Defaults to None.
        template (str, optional): Plotly template to use. Defaults to "plotly".

    Returns:
        go.Figure: Plotly Figure object representing the horizontal stacked bar plots.
    """
    categories = df[col_cat].unique()

    n_cols=2
    fig = make_subplots(
        rows = 1,                           # number of rows
        cols = 2,                           # number of columns
        # subplot_titles = list(categories),       # title for each subplot
        vertical_spacing = vertical_spacing,     # space between subplots
        horizontal_spacing = horizontal_spacing / n_cols # space between subplots
        )
    
    for cat in categories:
        current_df = df[df[col_cat] == cat]
        hovertemplate="Catégorie "+current_df[col_y].astype(str)+"<br><b>"+str(cat)+"</b><br>"+current_df[col_x].astype(str)+" "+str(col_x)+"<br>"+current_df[col_percentage].map("{:.1%}".format).astype(str)

        fig.add_trace(
            go.Bar(
                
                x=current_df[col_x], 
                y=current_df[col_y],
                orientation='h',
                # text = current_df[col_x],
                # textposition="inside",
                name=cat, 
                marker=dict(color=current_df[col_color]),
                hovertemplate=hovertemplate+'<extra></extra>',
                textfont_size=14
                ),
            row=1,
            col=1,
        )

        fig.add_trace(
            go.Bar(
                
                x=current_df[col_percentage], 
                y=current_df[col_y],
                orientation='h',
                text = current_df[col_percentage].map("{:.1%}".format),
                textposition="inside",
                textangle=0,
                name="",
                marker=dict(color=current_df[col_color]),
                hovertemplate=hovertemplate+'<extra></extra>',
                 showlegend = False
                ),
            row=1,
            col=2,
        )

    fig.update_layout(
            barmode='stack',
            title_text=title_text, 
            showlegend=True,
            width = width,
            height= height,
            xaxis_tickangle=xaxis_tickangle,
            xaxis_showline=False,
            xaxis_showgrid=False,
            yaxis_showline=False,
            yaxis_showgrid=False,
            uniformtext_minsize=8,
            uniformtext_mode='hide',
            font_family="Segoe UI Semibold",
            template=template,
            plot_bgcolor=plot_bgcolor,    #background color (plot)
            paper_bgcolor=paper_bgcolor,   #background color (around plot)

        )
    fig.update_xaxes(title_text=col_x)
    fig.update_yaxes(title_text=col_y, row=1,col=1)
    fig.update_xaxes(title_text=col_x, range=[0,1], tickformat=".0%", row=1,col=2)
    fig.update_yaxes(showticklabels = False, row=1,col=2)
    
    return fig

def bar_trend_per_day(df: pd.DataFrame, 
                      col_date: str, 
                      col_metric1: str, 
                      col_metric2: str, 
                      xaxis_title: str = "Date", 
                      y1_axis_title: str = "Verbatims", 
                      y2_axis_title: str = "Engagements", 
                      title_text: str = "Trend - couverture & résonance", 
                      width: int = 1500, 
                      height: int = 700, 
                      marker_color: str = "indianred", 
                      line_color: str = "#273746", 
                      plot_bgcolor: str = None, 
                      paper_bgcolor: str = None, 
                      template: str = "plotly") -> go.Figure:
    """
    Creates a Plotly stacked bar chart with a secondary line plot for two metrics over time.

    Parameters:
    - df (pd.DataFrame): The DataFrame containing the data.
    - col_date (str): The name of the column containing dates.
    - col_metric1 (str): The name of the column containing the first metric values.
    - col_metric2 (str): The name of the column containing the second metric values.
    - xaxis_title (str, optional): The title for the x-axis. Defaults to "Date".
    - y1_axis_title (str, optional): The title for the primary y-axis. Defaults to "Verbatims".
    - y2_axis_title (str, optional): The title for the secondary y-axis. Defaults to "Engagements".
    - title_text (str, optional): The title text for the chart. Defaults to "Trend - couverture & résonance".
    - width (int, optional): The width of the chart. Defaults to 1500.
    - height (int, optional): The height of the chart. Defaults to 700.
    - marker_color (str, optional): The color of the bars. Defaults to "indianred".
    - line_color (str, optional): The color of the line plot. Defaults to "#273746".
    - plot_bgcolor (str, optional): The background color of the plot area. Defaults to None.
    - paper_bgcolor (str, optional): The background color of the paper area. Defaults to None.
    - template (str, optional): The template of the chart. Defaults to "plotly".

    Returns:
    - fig (go.Figure): The Plotly Figure object representing the stacked bar chart with line plot.
    """
    # Plotly Stacked Bar Chart
    fig = make_subplots(specs=[[{"secondary_y": True}]])
    hovertemplate='<b>Date :</b>'+ df[col_date].astype(str) + '<br><b>'+y1_axis_title+'</b>:'+ df[col_metric1].astype(str)+ '<br><b>'+y2_axis_title+'</b>:'+ df[col_metric2].astype(int).astype(str)

    fig.add_trace(
            go.Bar(
                name=y1_axis_title, 
                x=df[col_date], 
                y=df[col_metric1], 
                marker_color=marker_color, 
                opacity=0.8,
                hovertemplate=hovertemplate+"<extra></extra>"
                ),
            secondary_y=False,
        )       
        
    fig.add_trace(
            go.Scatter(
                x=df[col_date], 
                y=df[col_metric2], 
                name=y2_axis_title,
                mode='lines', 
                line_color=line_color, 
                line_width=2,
                hovertemplate=hovertemplate+"<extra></extra>"            
                ),
            secondary_y=True,
        )

    first_axis_range=[-0.5,df[col_metric1].max()*1.01]
    secondary_axis_range=[-0.5,df[col_metric2].max()*1.01]
    # Change the layout if necessary
    fig.update_layout(
        barmode='stack',
        xaxis_title=xaxis_title, 
        width = width,
        height = height,
        title_text=title_text, 
        showlegend=True,
        xaxis_tickangle=0,
        xaxis_showline=False,
        xaxis_showgrid=False,
        yaxis_showline=False,
        yaxis_showgrid=False,
        uniformtext_minsize=8,
        uniformtext_mode='hide',
        font_family="Segoe UI Semibold",
        template=template,
        plot_bgcolor=plot_bgcolor,    #background color (plot)
        paper_bgcolor=paper_bgcolor,   #background color (around plot)
        )

                    
    fig.update_yaxes(title_text=y1_axis_title, range=first_axis_range, secondary_y=False)
    fig.update_yaxes(title_text=y2_axis_title, range = secondary_axis_range, secondary_y=True) 
    fig.update_yaxes(
        showline=False,
        showgrid=False,
        zeroline=False
    )
    fig.update_xaxes(
        showline=False,
        showgrid=False,
        zeroline=False
    ) 

    return fig

def bar_trend_per_day_per_cat(df: pd.DataFrame, 
                              col_date: str, 
                              col_cat: str, 
                              col_metric1: str, 
                              col_metric2: str, 
                              col_color: str, 
                              xaxis_title: str = "Date", 
                              y1_axis_title: str = "Verbatims", 
                              y2_axis_title: str = "Engagements", 
                              title_text: str = "Trend - couverture & résonance", 
                              vertical_spacing: float = 0.1, 
                              width: int = 1500, 
                              height: int = 700, 
                              plot_bgcolor: str = None, 
                              paper_bgcolor: str = None, 
                              template: str = "plotly") -> go.Figure:
    """
    Creates a Plotly stacked bar chart with multiple categories, each represented as a separate subplot.

    Parameters:
    - df (pd.DataFrame): The DataFrame containing the data.
    - col_date (str): The name of the column containing dates.
    - col_cat (str): The name of the column containing categories.
    - col_metric1 (str): The name of the column containing the first metric values.
    - col_metric2 (str): The name of the column containing the second metric values.
    - col_color (str): The name of the column containing the color codes for each category.
    - xaxis_title (str, optional): The title for the x-axis. Defaults to "Date".
    - y1_axis_title (str, optional): The title for the primary y-axis. Defaults to "Verbatims".
    - y2_axis_title (str, optional): The title for the secondary y-axis. Defaults to "Engagements".
    - title_text (str, optional): The title text for the chart. Defaults to "Trend - couverture & résonance".
    - vertical_spacing (float, optional): The space between subplots. Defaults to 0.1.
    - width (int, optional): The width of the chart. Defaults to 1500.
    - height (int, optional): The height of the chart. Defaults to 700.
    - plot_bgcolor (str, optional): The background color of the plot area. Defaults to None.
    - paper_bgcolor (str, optional): The background color of the paper area. Defaults to None.
    - template (str, optional): The template of the chart. Defaults to "plotly".

    Returns:
    - fig (go.Figure): The Plotly Figure object representing the stacked bar chart with subplots for each category.
    """
    fig = make_subplots(
        rows = 2,                           # number of rows
        cols = 1,                           # number of columns
        vertical_spacing = vertical_spacing,     # space between subplots
    )

    categories = df[col_cat].unique()
    for cat in categories:
        current_df = df[df[col_cat] == cat]
    
        hovertemplate='<b>Categorie : </b>'+str(cat)+'<br><b>Date : </b>'+ current_df[col_date].astype(str) + '<br><b>'+y1_axis_title+'</b> : '+ current_df[col_metric1].astype(str)+' ('+current_df["per_"+col_metric1].map("{:.1%}".format).astype(str)+')' +'<br><b>'+y2_axis_title+'</b> : '+ current_df[col_metric2].astype(int).astype(str)+' ('+current_df["per_"+col_metric2].map("{:.1%}".format).astype(str)+')'

        fig.add_trace(
            go.Bar(
                x=current_df[col_date], 
                y=current_df[col_metric1],
                orientation='v',
                name=cat, 
                marker=dict(color=current_df[col_color]),
                hovertemplate=hovertemplate+'<extra></extra>',
                textfont_size=14,
                legendgroup=cat
                ),
            row=1,
            col=1,
        )

        fig.add_trace(
            go.Bar(
                
                x=current_df[col_date], 
                y=current_df[col_metric2],
                orientation='v',
                name="",
                marker=dict(color=current_df[col_color]),
                hovertemplate=hovertemplate+'<extra></extra>',
                showlegend = False,
                legendgroup=cat
                ),
            row=2,
            col=1,
        )

    fig.update_layout(
            barmode='stack',
            title_text=title_text, 
            showlegend=True,
            width = width,
            height= height,
            xaxis_tickangle=0,
            xaxis_showline=False,
            xaxis_showgrid=False,
            yaxis_showline=False,
            yaxis_showgrid=False,
            uniformtext_minsize=8,
            uniformtext_mode='hide',
            font_family="Segoe UI Semibold",
            template=template,
            plot_bgcolor=plot_bgcolor,    #background color (plot)
            paper_bgcolor=paper_bgcolor,   #background color (around plot)
            legend_tracegroupgap=0

        )
    fig.update_xaxes(showticklabels = False, row=1,col=1)
    fig.update_xaxes(title_text=xaxis_title, row=2,col=1)
    fig.update_yaxes(title_text=y1_axis_title, row=1,col=1)
    fig.update_yaxes(title_text=y2_axis_title, row=2,col=1)
    fig.update_yaxes(
        showline=False,
        showgrid=False,
        zeroline=False
    )
    fig.update_xaxes(
        showline=False,
        showgrid=False,
        zeroline=False
    )

    return fig

def pie(df: pd.DataFrame, 
        col_x: str, 
        col_y: str, 
        col_color: str, 
        title: str = "Sentiment", 
        template: str = "plotly",  
        width: int = 1000, 
        height: int = 1000, 
        plot_bgcolor: str = None, 
        paper_bgcolor: str = None, 
        showlegend: bool = True) -> go.Figure:
    """
    Creates a Plotly pie chart.

    Parameters:
    - df (pd.DataFrame): The DataFrame containing the data.
    - col_x (str): The name of the column containing the labels for the pie chart slices.
    - col_y (str): The name of the column containing the values for the pie chart slices.
    - col_color (str): The name of the column containing the colors for the pie chart slices.
    - title (str, optional): The title for the pie chart. Defaults to "Sentiment".
    - template (str, optional): The template of the chart. Defaults to "plotly".
    - width (int, optional): The width of the chart. Defaults to 1000.
    - height (int, optional): The height of the chart. Defaults to 1000.
    - plot_bgcolor (str, optional): The background color of the plot area. Defaults to None.
    - paper_bgcolor (str, optional): The background color of the paper area. Defaults to None.
    - showlegend (bool, optional): Whether to show the legend. Defaults to True.

    Returns:
    - fig (go.Figure): The Plotly Figure object representing the pie chart.
    """    
    fig = go.Figure()
    fig.add_trace(go.Pie(
        labels=df[col_x],
        values=df[col_y],
        name="",
        hole=.4,
        hovertemplate='<b>'+ df[col_x].astype(str) +"</b><br>"+ str(col_y) + " : "+df[col_y].astype(str) + "<extra></extra>",
        marker=dict(colors=list(df[col_color])),
        textfont_size = 18,
        sort=False 
        ),
    )

    # Update layout and axes
    fig.update_layout(
        height=height,
        width=width,
        uniformtext_minsize=7,
        margin=dict(l=75, r=75, t=75, b=50),
        showlegend=showlegend,
        font_family="Segoe UI Semibold",
        template=template,
        plot_bgcolor=plot_bgcolor,
        paper_bgcolor=paper_bgcolor,
        title_text=title
    )
    fig.update_yaxes(
        showline=False,
        showgrid=False,
        zeroline=False
    )
    fig.update_xaxes(
        showline=False,
        showgrid=False,
        zeroline=False
    )
    return fig

def bar(df: pd.DataFrame, 
        x: str, 
        y: str, 
        color: str = "indianred", 
        xaxis_title: str = "x", 
        yaxis_title: str = "y", 
        width: int = 1200, 
        height: int = 700, 
        title_text: str = "", 
        plot_bgcolor: str = None, 
        paper_bgcolor: str = None, 
        template: str = "plotly", 
        showlegend: bool = True) -> go.Figure:
    """
    Creates a Plotly vertical bar chart.

    Parameters:
    - df (pd.DataFrame): The DataFrame containing the data.
    - x (str): The name of the column containing the x-axis values.
    - y (str): The name of the column containing the y-axis values.
    - color (str, optional): The color of the bars. Defaults to "indianred".
    - xaxis_title (str, optional): The title for the x-axis. Defaults to "x".
    - yaxis_title (str, optional): The title for the y-axis. Defaults to "y".
    - width (int, optional): The width of the chart. Defaults to 1200.
    - height (int, optional): The height of the chart. Defaults to 700.
    - title_text (str, optional): The title text for the chart. Defaults to "".
    - plot_bgcolor (str, optional): The background color of the plot area. Defaults to None.
    - paper_bgcolor (str, optional): The background color of the paper area. Defaults to None.
    - template (str, optional): The template of the chart. Defaults to "plotly".
    - showlegend (bool, optional): Whether to show the legend. Defaults to True.

    Returns:
    - fig (go.Figure): The Plotly Figure object representing the vertical bar chart.
    """
    fig = go.Figure()
    fig.add_trace(
        go.Bar(
                x=df[x], 
                y=df[y],
                orientation='v',
                name=yaxis_title, 
                marker=dict(color=color),
                hovertemplate = str(x) +" : "+df[x].astype(str)+"<br>"+str(y)+" : "+df[y].astype(str)+'<extra></extra>'
        )

    )
    fig.update_traces(marker_color=color)
    fig.update_layout(
        title=title_text, 
        xaxis_title=xaxis_title, 
        yaxis_title=yaxis_title,
        title_text=title_text, 
        showlegend=showlegend,
        width = width,
        height= height,
        xaxis_tickangle=0,
        xaxis_showline=False,
        xaxis_showgrid=False,
        yaxis_showline=False,
        yaxis_showgrid=False,
        uniformtext_minsize=8,
        uniformtext_mode='hide',
        font_family="Segoe UI Semibold",
        template=template,
        plot_bgcolor=plot_bgcolor,    #background color (plot)
        paper_bgcolor=paper_bgcolor,   #background color (around plot)
        )
    return fig


def add_horizontal_line(fig: go.Figure, 
                         y: float, 
                         line_color: str = "gray", 
                         line_width: float = 1.5, 
                         line_dash: str = "dash", 
                         annotation_text: str = "Longueur moyenne des textes", 
                         annotation_position: str = "top right") -> go.Figure:
    """
    Adds a horizontal line to a Plotly Figure object.

    Parameters:
    - fig (go.Figure): The Plotly Figure object to which the horizontal line will be added.
    - y (float): The y-coordinate of the horizontal line.
    - line_color (str, optional): The color of the horizontal line. Defaults to "gray".
    - line_width (float, optional): The width of the horizontal line. Defaults to 1.5.
    - line_dash (str, optional): The dash style of the horizontal line. Defaults to "dash".
    - annotation_text (str, optional): The text annotation associated with the horizontal line. Defaults to "Longueur moyenne des textes".
    - annotation_position (str, optional): The position of the annotation relative to the horizontal line. Defaults to "top right".

    Returns:
    - fig (go.Figure): The Plotly Figure object with the horizontal line added.
    """    
    fig.add_hline(
        y=y, 
        line_width=line_width, 
        line_dash=line_dash, 
        line_color=line_color,
        annotation_text=annotation_text, 
        annotation_position=annotation_position
        )
    return fig

def add_vertical_line(fig: go.Figure, 
                      x: float, 
                      line_color: str = "gray", 
                      line_width: float = 1.5, 
                      line_dash: str = "dash", 
                      annotation_text: str = "Longueur moyenne des textes", 
                      annotation_position: str = "top right") -> go.Figure:
    """
    Adds a vertical line to a Plotly Figure object.

    Parameters:
    - fig (go.Figure): The Plotly Figure object to which the vertical line will be added.
    - x (float): The x-coordinate of the vertical line.
    - line_color (str, optional): The color of the vertical line. Defaults to "gray".
    - line_width (float, optional): The width of the vertical line. Defaults to 1.5.
    - line_dash (str, optional): The dash style of the vertical line. Defaults to "dash".
    - annotation_text (str, optional): The text annotation associated with the vertical line. Defaults to "Longueur moyenne des textes".
    - annotation_position (str, optional): The position of the annotation relative to the vertical line. Defaults to "top right".

    Returns:
    - fig (go.Figure): The Plotly Figure object with the vertical line added.
    """
    fig.add_vline(
        x=x, 
        line_width=line_width, 
        line_dash=line_dash, 
        line_color=line_color,
        annotation_text=annotation_text, 
        annotation_position=annotation_position
        )
    return fig

def network_graph(T: nx.Graph, 
                  col_size: str = "scaled_size", 
                  col_color: str = "modularity_color",  
                  title_text: str = "Analyse de similitudes", 
                  sample_nodes: float = 0.15, 
                  show_edges: bool = True, 
                  show_halo: bool = False, 
                  textposition: str = None, 
                  line_color: str = "#B7B7B7", 
                  line_dash: str = "dot", 
                  edge_mode: str = "lines+markers", 
                  node_mode: str = "markers+text", 
                  opacity: float = 0.2, 
                  width: int = 1600, 
                  height: int = 1200, 
                  plot_bgcolor: str = None, 
                  paper_bgcolor: str = None, 
                  template: str = "plotly") -> go.Figure:
    """
    Creates a network graph visualization using Plotly.

    Parameters:
    - T (nx.Graph): The NetworkX graph object.
    - col_size (str, optional): The column name for node size. Defaults to "scaled_size".
    - col_color (str, optional): The column name for node color. Defaults to "modularity_color".
    - title_text (str, optional): The title for the graph. Defaults to "Analyse de similitudes".
    - sample_nodes (float, optional): The proportion of nodes to sample for displaying labels. Defaults to 0.15.
    - show_edges (bool, optional): Whether to display edges. Defaults to True.
    - show_halo (bool, optional): Whether to display halo around nodes. Defaults to False.
    - textposition (str, optional): The position of node labels. Defaults to None.
    - line_color (str, optional): The color of edges. Defaults to "#B7B7B7".
    - line_dash (str, optional): The dash style of edges. Defaults to "dot".
    - edge_mode (str, optional): The mode for displaying edges. Defaults to "lines+markers".
    - node_mode (str, optional): The mode for displaying nodes. Defaults to "markers+text".
    - opacity (float, optional): The opacity of nodes. Defaults to 0.2.
    - width (int, optional): The width of the plot. Defaults to 1600.
    - height (int, optional): The height of the plot. Defaults to 1200.
    - plot_bgcolor (str, optional): The background color of the plot area. Defaults to None.
    - paper_bgcolor (str, optional): The background color of the paper area. Defaults to None.
    - template (str, optional): The template of the plot. Defaults to "plotly".

    Returns:
    - fig (go.Figure): The Plotly Figure object representing the network graph visualization.
    """    
    # on construit un dataframe des noeuds à partir des données du graphe pour plus de simplicité
    df_nodes=pd.DataFrame()
    for node in T.nodes(data=True):
        df_nodes_tmp=pd.json_normalize(node[1])
        df_nodes_tmp['node']=node[0]
        df_nodes=pd.concat([df_nodes, df_nodes_tmp])
    df_nodes[['x','y']]=df_nodes['pos'].apply(pd.Series)
    df_nodes = df_nodes.sort_values(by=col_size, ascending=False).reset_index(drop=True)

    # on conserve les labels pour seulement un échantillon de noeuds
    df_sample = sample_most_engaging_posts(df_nodes, "modularity", col_size, sample_size= sample_nodes, min_size=3)

    for index, row in df_nodes.iterrows():
        if row['node'] in df_sample['node'].values:
            df_nodes.at[index, 'node_label'] = row['node']
        else:
            df_nodes.at[index, 'node_label'] = ''
    
    fig = go.Figure()
    # on crée nos liens
    if show_edges:
        for edge in T.edges(data=True):
            x0, y0 = T.nodes[edge[0]]['pos']
            x1, y1 = T.nodes[edge[1]]['pos']

            fig.add_trace(
                go.Scatter(
                    x = tuple([x0, x1, None]),
                    y = tuple([y0, y1, None]),
                    line_width = edge[2]['scaled_weight'],
                    line_color = line_color,
                    mode=edge_mode,
                    line_dash=line_dash,
                    name="",
                    hoverinfo='skip',
                )
            )

    # on affiche éventuellement les halo
    if show_halo:
        for i, row in df_nodes.groupby("modularity"):
            try:
                x_hull, y_hull = get_convex_hull_coord(np.array(row[['x','y']]))
                hull_color = row[col_color].iloc[0]
                # Create a Scatter plot with the convex hull coordinates
                fig.add_trace( 
                    go.Scatter(
                        x=x_hull,
                        y=y_hull,
                        mode="lines",
                        fill="toself",
                        fillcolor=hull_color,
                        opacity=0.1,
                        name="Convex Hull",
                        line=dict(color="grey", dash="dot"),
                        hoverinfo="none",
                    )
                )
            except:
                pass

    # on affiche nos noeuds
    for i, row in df_nodes.iterrows():
        fig.add_trace(
            go.Scatter(
                x = [row['x']],
                y = [row['y']],
                mode=node_mode,
                marker_opacity=opacity,
                marker_size=row[col_size],
                marker_color= row[col_color],
                marker_sizemode='area',
                marker_sizemin = 8,
                textposition=textposition,
                text = row['node_label'],
                textfont_size=row[col_size],
                textfont_color=row[col_color],
                hovertemplate='<b>'+str(row['node'])+'</b><br>Modularity :'+str(row["modularity"])+'</b><br>Frequency :'+str(row["size"])+'</b><br>Eigenvector Centrality : '+str(round(row["eigenvector_centrality"],3))+'</b><br>Degree Centrality : '+str(round(row["degree_centrality"],3))+'</b><br>Betweenness Centrality : '+str(round(row["betweenness_centrality"],3))+"<extra></extra>"
            )
        )

    fig.update_layout(
            width=width,
            height=height,
            showlegend=False,
            hovermode='closest',
            title=title_text,
            titlefont_size=18,
            font_family="Segoe UI Semibold",
            # font_size = 12,
            # uniformtext_minsize=8,
            template=template,
            plot_bgcolor=plot_bgcolor,
            paper_bgcolor = paper_bgcolor,
            
            xaxis=dict(
                showgrid=False, 
                showline=False,                           #intermediate lines
                zeroline=False,
                showticklabels=False, 
                mirror=False
                ),
            yaxis=dict(
                showgrid=False, 
                showline=False,                           #intermediate lines
                zeroline=False,
                showticklabels=False, 
                mirror=False
                ))
    
    return fig

def richesse_lexicale(df: pd.DataFrame, 
                      title: str = "Richesse lexicale", 
                      width: int = 1200, 
                      height: int = 1000, 
                      template: str = "plotly") -> go.Figure:
    """
    Creates a lexical richness visualization using Plotly.

    Parameters:
    - df (pd.DataFrame): The DataFrame containing word frequency data.
    - title (str, optional): The title for the plot. Defaults to "Richesse lexicale".
    - width (int, optional): The width of the plot. Defaults to 1200.
    - height (int, optional): The height of the plot. Defaults to 1000.
    - template (str, optional): The template of the plot. Defaults to "plotly".

    Returns:
    - fig_richesse (go.Figure): The Plotly Figure object representing the lexical richness visualization.
    """
    df = create_frequency_table(df, "freq")
    fig_richesse = go.Figure()
    fig_richesse.add_trace(
            go.Scatter(
                x=df['rank'],
                y=df['freq'], 
                # marker_color=generate_random_hexadecimal_color(),
                mode='markers', 
                name="",
                hovertemplate = 'rank : '+df["rank"].astype(str)+'<br>'+'<b>word : '+df["word"].astype(str)+'</b><br>'+'count : '+df["freq"].astype(str)+'<br>')
            ) 
    fig_richesse.update_layout(title=title, 
                            xaxis_title="Rank", 
                            width=width, 
                            height=height,
                            template=template)    
    fig_richesse.update_xaxes(tickformat=".0f", title_text="Rank", type="log")
    fig_richesse.update_yaxes(tickformat=".0f", title_text="Freq", type="log")
    return fig_richesse

def richesse_lexicale_per_topic(df: pd.DataFrame, 
                                col_topic: str, 
                                title: str = "Richesse lexicale par topic", 
                                width: int = 1200, 
                                height: int = 1000, 
                                template: str = "plotly") -> go.Figure:
    """
    Creates a lexical richness visualization per topic using Plotly.

    Parameters:
    - df (pd.DataFrame): The DataFrame containing word frequency data.
    - col_topic (str): The name of the column representing topics.
    - title (str, optional): The title for the plot. Defaults to "Richesse lexicale par topic".
    - width (int, optional): The width of the plot. Defaults to 1200.
    - height (int, optional): The height of the plot. Defaults to 1000.
    - template (str, optional): The template of the plot. Defaults to "plotly".

    Returns:
    - fig_richesse (go.Figure): The Plotly Figure object representing the lexical richness visualization per topic.
    """
    fig_richesse = go.Figure()
    for topic in list(df[col_topic].unique()):
        df_tmp = create_frequency_table(df[df[col_topic]==topic], "freq")
        fig_richesse.add_trace(
                go.Scatter(
                    x=df_tmp['rank'],
                    y=df_tmp['freq'], 
                    # marker_color=generate_random_hexadecimal_color(),
                    mode='markers', 
                    name=topic,
                    hovertemplate = col_topic+ ' : '+ str(topic)+'<br> rank : '+df_tmp["rank"].astype(str)+'<br>'+'<b>word : '+df_tmp["word"].astype(str)+'</b><br>'+'count : '+df_tmp["freq"].astype(str)+'<br>')
                ) 
        fig_richesse.update_layout(title=title, 
                                xaxis_title="Rank", 
                                width=width, 
                                height=height,
                                template=template)    
        fig_richesse.update_xaxes(tickformat=".0f", title_text="Rank", type="log")
        fig_richesse.update_yaxes(tickformat=".0f", title_text="Freq", type="log")
    return fig_richesse

def subplots_bar_per_day_per_cat(df: pd.DataFrame, 
                                 col_date: str, 
                                 col_cat: str, 
                                 metrics: list, 
                                 col_color: str, 
                                 y_axis_titles: list, 
                                 xaxis_title: str = "Date", 
                                 title_text: str = "Trend - couverture & résonance", 
                                 vertical_spacing: float = 0.1, 
                                 width: int = 1500, 
                                 height: int = 700, 
                                 plot_bgcolor: str = None, 
                                 paper_bgcolor: str = None, 
                                 template: str = "plotly") -> go.Figure:
    """
    Creates subplots of stacked bar charts per day and category using Plotly.

    Parameters:
    - df (pd.DataFrame): The DataFrame containing the data.
    - col_date (str): The name of the column representing dates.
    - col_cat (str): The name of the column representing categories.
    - metrics (List[str]): A list of column names representing metrics to be plotted.
    - col_color (str): The name of the column representing colors for bars.
    - y_axis_titles (List[str]): A list of titles for the y-axes of subplots.
    - xaxis_title (str, optional): The title for the x-axis. Defaults to "Date".
    - title_text (str, optional): The title for the entire plot. Defaults to "Trend - couverture & résonance".
    - vertical_spacing (float, optional): The space between subplots. Defaults to 0.1.
    - width (int, optional): The width of the entire plot. Defaults to 1500.
    - height (int, optional): The height of each subplot. Defaults to 700.
    - plot_bgcolor (str, optional): The background color for the plot area. Defaults to None.
    - paper_bgcolor (str, optional): The background color for the paper area. Defaults to None.
    - template (str, optional): The template of the plot. Defaults to "plotly".

    Returns:
    - fig (go.Figure): The Plotly Figure object representing the subplots of stacked bar charts.
    """
    fig = make_subplots(
        rows = len(metrics),                           # number of rows
        cols = 1,                           # number of columns
        vertical_spacing = vertical_spacing,     # space between subplots
    )

    categories = df[col_cat].unique()
    for cat in categories:
        current_df = df[df[col_cat] == cat]
    
        hovertemplate='<b>Categorie : </b>'+str(cat)+'<br><b>Date : </b>'+ current_df[col_date].astype(str)

        for i, metric in enumerate(metrics):
            hovertemplate +=  '<br><b>'+ metric + " : "+current_df[metric].astype(str) 
            if i==0:
                showlegend = True
            else:
                showlegend = False

            fig.add_trace(
                go.Bar(
                    x=current_df[col_date], 
                    y=current_df[metric],
                    orientation='v',
                    name=cat, 
                    marker=dict(color=current_df[col_color]),
                    hovertemplate=hovertemplate+'<extra></extra>',
                    textfont_size=14,
                    showlegend = showlegend,
                    legendgroup=cat
                    ),
                row = i+1,
                col=1,
            )

    fig.update_layout(
            barmode='stack',
            title_text=title_text, 
            showlegend=True,
            width = width,
            height= height * len(metrics),
            xaxis_tickangle=0,
            xaxis_showline=False,
            xaxis_showgrid=False,
            yaxis_showline=False,
            yaxis_showgrid=False,
            uniformtext_minsize=8,
            uniformtext_mode='hide',
            font_family="Segoe UI Semibold",
            template=template,
            plot_bgcolor=plot_bgcolor,    #background color (plot)
            paper_bgcolor=paper_bgcolor,   #background color (around plot)
            legend_tracegroupgap=0

        )

    for i, title in enumerate(y_axis_titles):
        fig.update_xaxes(title_text=xaxis_title, row=i+1,col=1)

        fig.update_yaxes(title_text=title, row=i+1,col=1)

    fig.update_yaxes(
        showline=False,
        showgrid=False,
        zeroline=False
    )
    fig.update_xaxes(
        showline=False,
        showgrid=False,
        zeroline=False
    )

    return fig

    
def add_shape(fig: go.Figure, 
              shape_type: str = "rect", 
              x0: float = -1, 
              y0: float = -1, 
              x1: float = 0, 
              y1: float = 0, 
              fillcolor: str = 'Silver', 
              opacity: float = 0.1, 
              line_width: float = 0, 
              line_color: str = 'white', 
              dash: str = None, 
              layer: str = "below") -> go.Figure:
    """
    Adds a shape to a Plotly figure.

    Parameters:
    - fig (go.Figure): The Plotly Figure object.
    - shape_type (str, optional): The type of shape to add. Defaults to "rect".
    - x0 (float, optional): The x-coordinate of the lower left corner of the shape. Defaults to -1.
    - y0 (float, optional): The y-coordinate of the lower left corner of the shape. Defaults to -1.
    - x1 (float, optional): The x-coordinate of the upper right corner of the shape. Defaults to 0.
    - y1 (float, optional): The y-coordinate of the upper right corner of the shape. Defaults to 0.
    - fillcolor (str, optional): The fill color of the shape. Defaults to 'Silver'.
    - opacity (float, optional): The opacity of the shape. Defaults to 0.1.
    - line_width (float, optional): The width of the shape's outline. Defaults to 0.
    - line_color (str, optional): The color of the shape's outline. Defaults to 'white'.
    - dash (str, optional): The dash style of the shape's outline. Defaults to None.
    - layer (str, optional): The layer on which the shape is added, either 'below' or 'above' the data. Defaults to "below".

    Returns:
    - fig (go.Figure): The modified Plotly Figure object with the added shape.
    """
    fig.add_shape(
            # Shape for the area between (-1, 0)
            {
                'type': shape_type,
                'x0': x0,
                'y0': y0,
                'x1': x1,
                'y1': y1,
                'fillcolor': fillcolor,
                'opacity': opacity,
                "layer": layer,
                'line': {
                    'width': line_width, 
                    "color": line_color,
                    "dash" : dash,
                    },
                
            }
        )
    return fig

def add_image(fig: go.Figure, 
              xref: str = "paper", 
              yref: str = "paper", 
              x: float = 0, 
              y: float = 0, 
              sizex: float = 0.08, 
              sizey: float = 0.08, 
              xanchor: str = "right", 
              yanchor: str = "bottom", 
              source: str = "data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNDc1IiBoZWlnaHQ9IjM4OCIgdmlld0JveD0iMCAwIDQ3NSAzODgiIGZpbGw9Im5vbmUiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+CjxwYXRoIGQ9Ik0xMDUuNzI3IDI5My4zOTFDMTA1LjcyNyAyNjYuNzc0IDg0LjEyOTMgMjQ1LjE3NyA1Ny42MDEzIDI0NS4xNzdDMzAuOTg0IDI0NS4xNzcgOS4yOTYgMjY2Ljc3NCA5LjI5NiAyOTMuMzkxQzkuMjk2IDMyMC4wMDkgMzAuOTg0IDM0MS42MDcgNTcuNjAxMyAzNDEuNjA3Qzg0LjEyOTMgMzQxLjYwNyAxMDUuNzI3IDMyMC4wMDkgMTA1LjcyNyAyOTMuMzkxWk0wLjg3MDY2NyAyOTMuMzkxQzAuODcwNjY3IDI2Mi4yMDMgMjYuMzI0IDIzNi43NTMgNTcuNjAxMyAyMzYuNzUzQzg4LjY5ODcgMjM2Ljc1MyAxMTQuMTUxIDI2Mi4yMDMgMTE0LjE1MSAyOTMuMzkxQzExNC4xNTEgMzI0LjU3OSA4OC42OTg3IDM1MC4wMyA1Ny42MDEzIDM1MC4wM0MyNi4zMjQgMzUwLjAzIDAuODcwNjY3IDMyNC41NzkgMC44NzA2NjcgMjkzLjM5MVoiIGZpbGw9ImJsYWNrIi8+CjxwYXRoIGQ9Ik0yMzIuNTMxIDI5My40ODFDMjMyLjUzMSAyNjMuNjM3IDIwOS4zMTkgMjQ1LjI2NSAxODYuMjg2IDI0NS4yNjVDMTY2LjU3IDI0NS4yNjUgMTQ3LjQ4MiAyNTguNjIgMTQ1LjI0MSAyODAuMDM4VjMwNi42NTZDMTQ3LjM5MyAzMjguOTcgMTY2LjM5MSAzNDEuNjk2IDE4Ni4yODYgMzQxLjY5NkMyMDkuMzE5IDM0MS42OTYgMjMyLjUzMSAzMjMuMzI1IDIzMi41MzEgMjkzLjQ4MVpNMjQwLjg2NiAyOTMuNDgxQzI0MC44NjYgMzI4LjA3NCAyMTQuNjk3IDM1MC4xMiAxODcuMTgzIDM1MC4xMkMxNjkuOTc3IDM1MC4xMiAxNTMuNTc1IDM0Mi4zMjQgMTQ1LjI0MSAzMjcuNjI1VjM4Ny40OTNIMTM2Ljk5N1YyMzkuNjJIMTQ0Ljg4M0wxNDUuMjQxIDI1Ny41NDRWMjYwLjE0MkMxNTMuNjY2IDI0NS42MjQgMTcwLjE1NSAyMzYuODQyIDE4Ny4yNzMgMjM2Ljg0MkMyMTQuNjA3IDIzNi44NDIgMjQwLjg2NiAyNTguODg4IDI0MC44NjYgMjkzLjQ4MVoiIGZpbGw9ImJsYWNrIi8+CjxwYXRoIGQ9Ik0yNTUuNjQyIDMyOC40MzNMMjYwLjc1MSAzMjIuNzg4QzI2OC4xMDEgMzM1LjUxMyAyODEuMDk1IDM0MS45NjUgMjk0LjE3OCAzNDEuOTY1QzMwOC41MTggMzQxLjk2NSAzMjMuMTI2IDMzMy42MyAzMjMuMTI2IDMxOS41NjFDMzIzLjEyNiAzMDUuNDkgMzA0LjkzNCAyOTkuNjY1IDI4OS43ODcgMjkzLjc0OUMyODAuMzc4IDI4OS45ODYgMjYwLjc1MSAyODMuMzUzIDI2MC43NTEgMjY0LjYyNEMyNjAuNzUxIDI0OS41NjggMjc0LjI4MyAyMzYuNjYyIDI5NC4yNjkgMjM2LjY2MkMzMDkuODYyIDIzNi42NjIgMzIzLjEyNiAyNDUuMzU0IDMyNy41MTggMjU2LjM3OEwzMjEuNjAzIDI2MS4wMzhDMzE2LjMxNSAyNDkuODM3IDMwNC4yMTcgMjQ0LjkwNiAyOTQuMDAxIDI0NC45MDZDMjc5LjEyMiAyNDQuOTA2IDI2OS4xNzQgMjU0LjEzNyAyNjkuMTc0IDI2NC4yNjVDMjY5LjE3NCAyNzcuNDQgMjg0LjIzMSAyODIuOTA1IDI5OS4xMDkgMjg4LjU1MkMzMTEuMDI3IDI5My4yMTIgMzMxLjU1MSAzMDAuNjUgMzMxLjU1MSAzMTkuMDIyQzMzMS41NTEgMzM4LjExMiAzMTMuMjY5IDM1MC4yMSAyOTQuMDAxIDM1MC4yMUMyNzYuNzAzIDM1MC4yMSAyNjEuODI3IDM0MC40NDIgMjU1LjY0MiAzMjguNDMzWiIgZmlsbD0iYmxhY2siLz4KPHBhdGggZD0iTTM0Ni43OCAyOTMuMzkxQzM0Ni43OCAyNTguNTMgMzc1LjAxMSAyMzYuMDM0IDQwMy4yNDEgMjM2LjAzNEM0MTUuNzg4IDIzNi4wMzQgNDMwLjMwNyAyNDAuNTE3IDQzOS45ODUgMjQ4LjU4Mkw0MzUuMzI1IDI1NS40ODJDNDI4Ljc4MyAyNDkuMjk5IDQxNS41MiAyNDQuNDU5IDQwMy4zMzEgMjQ0LjQ1OUMzNzkuMTMzIDI0NC40NTkgMzU1LjIwNCAyNjMuNDU5IDM1NS4yMDQgMjkzLjM5MUMzNTUuMjA0IDMyMy41OTMgMzc5LjQwMyAzNDIuMzIzIDQwMy4yNDEgMzQyLjMyM0M0MTUuNjA4IDM0Mi4zMjMgNDI5LjIzMSAzMzcuMTI2IDQzNi4yMjEgMzMwLjQ5NEw0NDEuMzI5IDMzNy4xMjZDNDMxLjQ3MiAzNDYuMTc4IDQxNi40MTYgMzUwLjc0OSA0MDMuNDIgMzUwLjc0OUMzNzUuMSAzNTAuNzQ5IDM0Ni43OCAzMjguNDMzIDM0Ni43OCAyOTMuMzkxWiIgZmlsbD0iYmxhY2siLz4KPHBhdGggZD0iTTQ2My42MzcgMjM5LjYxOUg0NzIuMDYxVjM0Ny4xNjNINDYzLjYzN1YyMzkuNjE5Wk00NjEuMTI4IDIxMi40NjRDNDYxLjEyOCAyMDguNzAxIDQ2NC4wODUgMjA1Ljc0MyA0NjcuODQ5IDIwNS43NDNDNDcxLjUyNCAyMDUuNzQzIDQ3NC41NzEgMjA4LjcwMSA0NzQuNTcxIDIxMi40NjRDNDc0LjU3MSAyMTYuMjI4IDQ3MS41MjQgMjE5LjE4NSA0NjcuODQ5IDIxOS4xODVDNDY0LjA4NSAyMTkuMTg1IDQ2MS4xMjggMjE2LjIyOCA0NjEuMTI4IDIxMi40NjRaIiBmaWxsPSJibGFjayIvPgo8cGF0aCBkPSJNMjE3Ljg1MyAzMS4zOTE0TDIzNy43MjEgNTEuMjU4TDI1Ny41ODggMzEuMzkxNEwyMzcuNzIxIDExLjUyNDdMMjE3Ljg1MyAzMS4zOTE0Wk0yMzcuNzIxIDYyLjU3MjdMMjA2LjU0IDMxLjM5MTRMMjM3LjcyMSAwLjIxMDAxNkwyNjguOTAxIDMxLjM5MTRMMjM3LjcyMSA2Mi41NzI3Wk0xNTQuMTAxIDU5Ljc1OTRMMTYxLjQzOSA4Ni45NjQ3TDE4OC42NiA3OS42MjJMMTgxLjMyMyA1Mi41OTU0TDE1NC4xMDEgNTkuNzU5NFpNMTU1Ljc5NyA5Ni43NzE0TDE0NC4yOCA1NC4wNzE0TDE4Ni45NjMgNDIuODM5NEwxOTguNDgxIDg1LjI1OEwxNTUuNzk3IDk2Ljc3MTRaTTI4Ni43ODEgNzkuNjIyTDMxNC4wMDMgODYuOTY0N0wzMjEuMzQxIDU5Ljc1OTRMMjk0LjEyIDUyLjU5NTRMMjg2Ljc4MSA3OS42MjJaTTMxOS42NDMgOTYuNzcxNEwyNzYuOTYxIDg1LjI1OEwyODguNDc5IDQyLjgzOTRMMzMxLjE2MiA1NC4wNzE0TDMxOS42NDMgOTYuNzcxNFpNMTU0LjEwMSAxNTYuMTY5TDE4MS4zMjMgMTYzLjMzM0wxODguNjYgMTM2LjMwN0wxNjEuNDM5IDEyOC45NjVMMTU0LjEwMSAxNTYuMTY5Wk0xODYuOTYzIDE3My4wODlMMTQ0LjI4IDE2MS44NTdMMTU1Ljc5NyAxMTkuMTU3TDE5OC40ODEgMTMwLjY3TDE4Ni45NjMgMTczLjA4OVpNMjg2Ljc3NSAxMzYuMzA5TDI5NC4xMiAxNjMuNTM3TDMyMS4zNDggMTU2LjE5M0wzMTQuMDAzIDEyOC45NjVMMjg2Ljc3NSAxMzYuMzA5Wk0yODguNDc5IDE3My4zNDVMMjc2Ljk2NyAxMzAuNjY5TDMxOS42NDMgMTE5LjE1N0wzMzEuMTU1IDE2MS44MzRMMjg4LjQ3OSAxNzMuMzQ1Wk0yMTcuODUzIDE4NC41MzdMMjM3LjcyMSAyMDQuNDA1TDI1Ny41ODggMTg0LjUzN0wyMzcuNzIxIDE2NC42N0wyMTcuODUzIDE4NC41MzdaTTIzNy43MjEgMjE1LjcxOEwyMDYuNTQgMTg0LjUzN0wyMzcuNzIxIDE1My4zNTdMMjY4LjkwMSAxODQuNTM3TDIzNy43MjEgMjE1LjcxOFoiIGZpbGw9ImJsYWNrIi8+Cjwvc3ZnPgo=") -> go.Figure:
    """
    Adds an image to a Plotly figure.

    Parameters:
    - fig (go.Figure): The Plotly Figure object.
    - xref (str, optional): The x-coordinate reference point. Defaults to "paper".
    - yref (str, optional): The y-coordinate reference point. Defaults to "paper".
    - x (float, optional): The x-coordinate of the image position. Defaults to 0.
    - y (float, optional): The y-coordinate of the image position. Defaults to 0.
    - sizex (float, optional): The size of the image in the x-direction. Defaults to 0.08.
    - sizey (float, optional): The size of the image in the y-direction. Defaults to 0.08.
    - xanchor (str, optional): The x-coordinate anchor point. Defaults to "right".
    - yanchor (str, optional): The y-coordinate anchor point. Defaults to "bottom".
    - source (str, optional): The URL source of the image. Defaults to "https://www.example.com/image.jpg".

    Returns:
    - fig (go.Figure): The modified Plotly Figure object with the added image.
    """
    fig.add_layout_image(
    dict(
        source=source,
        xref=xref, 
        yref=yref,
        x=x, y=y,
        sizex=sizex, 
        sizey=sizey,
        xanchor=xanchor,
        yanchor=yanchor
        )
    )
    return fig