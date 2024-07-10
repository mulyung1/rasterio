from dash import html, register_page, dcc
import dash_bootstrap_components as dbc
import rasterio
from rasterio.plot import show, adjust_band
import numpy as np 
import plotly.express as px
#register the page
register_page(
    __name__,
    name='home',
    path='/'
)

body_text='''
Coming soon
'''

# Open the GeoTIFF file
dataset = rasterio.open('sample.tif')

# Extract and print the CRS (Coordinate Reference System)
crs = dataset.crs
print(f'The CRS: {crs}')

# Extract and print the bounds
bounds = dataset.bounds
print(f'The boundaries: {bounds}')

# Extract and print the transform matrix (Affine transformation)
transform = dataset.transform
print(f'{transform}, the transformation matrix')

# Extract and print the number of bands or channels
bands = dataset.indexes
print(f'{bands}, the available bands')

# Read the bands
band_list = [dataset.read(i) for i in (3, 2, 1)]

# Adjust each band
adjusted_bands = [adjust_band(band) for band in band_list]

# Stack the bands into an image
imgdata = np.dstack(adjusted_bands)

# Close the dataset to free resources
dataset.close()

# Create the Plotly figure
fig = px.imshow(imgdata)

#layout
def layout():
    return dbc.Container(
        [
            html.Div(dcc.Markdown(children=body_text)),
            dcc.Graph(figure=fig)  # Display the image
        ],
        fluid=True
    )