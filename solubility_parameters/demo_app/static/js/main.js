
function alert_no_params ()
    {
        alert("No parameters for that compound were found.  \n If this is a common compound, try a synonym.")
    }

function alert_promise_rejected ()
    {
        console.log("Substance query was rejected.")
        alert("Your request could not be processed. \n Please contact the administrator.");
    }

function write_hsp_table_html (info)
    {
        return `<table class="table">
        <thead>
          <tr>
            <th scope="col">Substance</th>
            <th scope="col">Delta d</th>
            <th scope="col">Delta p</th>
            <th scope="col">Delta h</th>
            <th scope="col">Mol. Vol.</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <th scope="row">${info.display_name}</th>
            <td>${+info.delta_d}</td>
            <td>${+info.delta_p}</td>
            <td>${+info.delta_h}</td>
            <td>${+info.mol_vol}</td>
          </tr>
        </tbody>
      </table>`
    }

function process_input ()
    {
        d3.event.preventDefault();
        subst_text = d3.select("#substance_0").node().value;
        query_text = subst_text.replace(/\W/g,'').toLowerCase();
        console.log(`Querying for: ${query_text}`);
        url = "/estimate/" + query_text;
        d3.json(url).then( function (params) {
            console.log(params);
            if (params.valid) {
                console.log("Displaying HSP");
                d3.select("#est_hsp")
                    .html(write_hsp_table_html(params));
                if (+params.src_id == 1) {
                    console.log("HSP are experimental!");
                    d3.select("#est_hsp")
                        .append("p")
                        .text("These values were experimentally determined by Hansen.")
                };
            }
            else {
                alert_no_params();
            }
           
        }, alert_promise_rejected)
    };




console.log("Starting up...");
d3.select("#user_input").on("submit", process_input);


