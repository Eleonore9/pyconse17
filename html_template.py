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

custom_template_with_text = """
<!DOCTYPE html>
<head>
  <title>{title}</title>
  <meta charset="utf-8">
  <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0-beta/css/bootstrap.min.css" integrity="sha384-/Y6pD6FV/Vv2HJnA6t+vslU6fwYXjCFtcEpHbNJ0lyAFsXTsjBbfaDjzALeQsN6M" crossorigin="anonymous">
  <script src="{d3_js_url}"></script>
  <script src="{vega_js_url}"></script>
  <script src="{vegalite_js_url}"></script>
  <script src="{vegaembed_js_url}"></script>
  <style media="screen">
    /* Add space between vega-embed links  */
    .vega-actions a {{
      margin-right: 5px;
    }}
    #vis3 {{
      float: left;
    }}
    #vis2 {{
      float: left;
    }}
    .lower {{
      clear: both;
    }}
  </style>
</head>
<body>
  <div class="container">
   <div class="header clearfix">
   <nav>
    <ul class="nav nav-pills float-right">
     <li class="nav-item">{navbar}</li>
    </ul>
   </nav>
   <h3 class="text-muted">Telling stories with data</h3>
   </div>
   <h2>{title}</h2>
   <div class="col"><h5>{paragraph_1}</h5></div>
    <div class="jumbotron">
     <!-- Container for the visualization -->
     <div id="vis2"></div>
     <div id="vis3"></div>
     <div id="vis"></div>
   </div>
   <div class="col lower">
    <div class="row"><h5>{paragraph_2}</h5></div>
    <div class="row">{references}</div>
   </div>
  </div>
  <script>
  var plot = Object.assign({spec}, {fix});
  var plot2 = Object.assign({figure_2}, {fix});
  var plot3 = Object.assign({figure_3}, {fix})

  // Embed the visualization in the container with id `vis`
  vega.embed("#vis", plot);
  vega.embed("#vis2", plot2);
  vega.embed("#vis3", plot3);
  </script>
</body>
</html>
"""
