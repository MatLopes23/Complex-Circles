var svg = d3.select("svg"),
    margin = 20,
    diameter = +svg.attr("width"),
    g = svg.append("g").attr("transform", "translate(" + diameter / 2 + "," + diameter / 2 + ")");

var color = d3.scaleLinear()
    .domain([-1, 5])
    .range(["hsl(152,80%,80%)", "hsl(228,30%,40%)"])
    .interpolate(d3.interpolateHcl);

var pack = d3.pack()
    .size([diameter - margin, diameter - margin])
    .padding(2);

var file = document.getElementById('my_data_json').getAttribute('data-name');

d3.json(file, function (error, root) {
    if (error) throw error;

    root = d3.hierarchy(root)
        .sum(function (d) { return d.size; })
        .sort(function (a, b) { return b.value - a.value; });

    var focus = root,
        nodes = pack(root).descendants(),
        view;

    var circle = g.selectAll("circle")
        .data(nodes)
        .enter().append("circle")
        .attr("class", function (d) { return d.parent ? d.children ? "node" : "node node--leaf" : "node node--root"; })
        .style("fill", function (d) { return d.children ? color(d.depth) : d.data.color; })
        .on("click", function (d) { if (focus !== d) zoom(d), d3.event.stopPropagation(); this.style.display = "inline"; })
        .on("mouseover", function(d) {this.style.display = "inline";});

    var text = g.selectAll("text")
        .data(nodes)
        .enter().append("text")
        .attr("class", "label")
        .style("fill-opacity", function (d) { return d.parent === root ? 1 : 0; })
        .style("display", function (d) { return d.parent === root ? "none" : "none"; })
        .style("font-weight", function (d) { return "bold"; })
        .style("font-size", function (d) { return "12px"; })
        .text(function (d) { return d.children != null ? d.data.name : ''; })
        .append('svg:a')
        .attr('href', function (d) { return d.children == null ? d.data.url : ''; })
        .attr('target', '_blank')
        .attr('fill', '#008CBA')
        .append('svg:tspan')
        .attr('x', 0)
        .attr('dy', 20)
        .text(function (d) { return d.children == null ? 'GitHub' : ''; })
        .style("fill", '#008CBA')
        .style('pointer-events', 'auto')
        .style('text-decoration', 'underline')
        .style("font-weight", function (d) { return "800"; })
        .style("font-size", function (d) { return "13px"; })
        .append('svg:tspan')
        .attr('x', 0)
        .attr('dy', 20)
        .text(function (d) { return d.children == null ? 'Complex: ' + d.data.size : ''; })
        .append('svg:tspan')
        .attr('x', 0)
        .attr('dy', 20)
        .text(function (d) { return d.children == null ? 'Cat: ' + d.data.category : ''; });
        
    var node = g.selectAll("circle,text");

    svg
        .style("background", "none")
        .style("border-radius", "50px")
        .on("click", function () { zoom(root); });

    zoomTo([root.x, root.y, root.r * 2 + margin]);

    function zoom(d) {
        var focus0 = focus; focus = d;

        var transition = d3.transition()
            .duration(d3.event.altKey ? 7500 : 750)
            .tween("zoom", function (d) {
                var i = d3.interpolateZoom(view, [focus.x, focus.y, focus.r * 2 + margin]);
                return function (t) { zoomTo(i(t)); };
            });

        transition.selectAll("text")
            .filter(function (d) { return d.parent === focus || this.style.display === "inline"; })
            .style("fill-opacity", function (d) { return d.parent === focus ? 1 : 0; });
            //.on("start", function (d) { if (d.parent === focus) this.style.display = "inline"; })
            //.on("end", function (d) { if (d.parent !== focus) this.style.display = "none"; });
    }

    function zoomTo(v) {
        var k = diameter / v[2]; view = v;
        node.attr("transform", function (d) { return "translate(" + (d.x - v[0]) * k + "," + (d.y - v[1]) * k + ")"; });
        circle.attr("r", function (d) { return d.r * k; });
    }
});

