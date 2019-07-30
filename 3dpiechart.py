from flask import Flask, render_template,request
app=Flask(__name__)
@app.route('/')
def index():
    a=[2,4,6,8,2]
    return render_template('3dchart.html',a=a)
if __name__=="__main__":
    app.run()
    
    
   #HTML FILE
   
   <html>
  <head>
    <script type="text/javascript" src="https://www.gstatic.com/charts/loader.js"></script>
    <script type="text/javascript">
      google.charts.load("current", {packages:["corechart"]});
      google.charts.setOnLoadCallback(drawChart);
      function drawChart() {
        var data = google.visualization.arrayToDataTable([
          ['Task', 'Hours per Day'],
          ['Work',     {{ a[0] }}],
          ['Eat',     {{ a[1] }} ],
          ['Commute',  {{ a[2] }}],
          ['Watch TV', {{ a[3] }}],
          ['Sleep',    {{ a[4] }}]
        ]);

        var options = {
          title: 'My Daily Activities',
          is3D: true,
        };

        var chart = new google.visualization.PieChart(document.getElementById('piechart_3d'));
        chart.draw(data, options);
      }
    </script>
  </head>
  <body>
    <div id="piechart_3d" style="width: 900px; height: 500px;"></div>
  </body>
</html>
