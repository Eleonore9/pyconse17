custom_urls = {"d3js": "https://d3js.org/d3.v4.min.js",
              "vega": "https://cdnjs.cloudflare.com/ajax/libs/vega/3.0.1/vega.js",
              "vega-lite": "https://cdnjs.cloudflare.com/ajax/libs/vega-lite/2.0.0-beta.15/vega-lite.js",
              "vega-embed": "https://cdnjs.cloudflare.com/ajax/libs/vega-embed/3.0.0-beta.20/vega-embed.js"}

custom_template = """
<!DOCTYPE html>
<head>
  <title>{title}</title>
  <meta charset="utf-8">
  <script src="{d3_js_url}"></script>
  <script src="{vega_js_url}"></script>
  <script src="{vegalite_js_url}"></script>
  <script src="{vegaembed_js_url}"></script>
  <style media="screen">
    /* Add space between vega-embed links  */
    .vega-actions a {{
      margin-right: 5px;
    }}
  </style>
</head>
<body>
  <!-- Container for the visualization -->
  <div id="vis"></div>
  <script>
  var plot = Object.assign({spec}, {fix});

  // Embed the visualization in the container with id `vis`
  vega.embed("#vis", plot);
  </script>
</body>
</html>
"""
