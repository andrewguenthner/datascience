function dragmove() 
    {
        d3.select(this)
            .attr("x", d3.event.x);
    }

var dragHandler = d3.drag()
            .on("drag", dragmove);

var barBPRect = d3.select("#input_col").node().getBoundingClientRect();
var barBPWidth = barBPRect.width * 0.75;

var barBP = d3.select("#bp_slider")
              .append("svg")
              .attr("id","bp_bar")
              .attr("width",barBPWidth)
              .attr("height",Math.min(barBPWidth / 4,20));

barBP.append("rect")
    .attr("x",barBPWidth / 16)
    .attr("y",Math.min(barBPWidth / 16, 5))
    .attr("width",barBPWidth * 7 / 8)
    .attr("height",Math.min(barBPWidth / 8, 10))
    .attr("rx",5)
    .attr("ry",5)
    .attr("stroke","black")
    .attr("stroke-width","1px")
    .attr("fill","darkgrey");
